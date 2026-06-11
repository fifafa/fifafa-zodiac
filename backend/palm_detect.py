#!/usr/bin/env python3
"""
Palm Line Detection Pipeline
Integrates MediaPipe Hands + U-Net model from yeonsumia/palmistry
"""
import os
import cv2
import numpy as np
import torch
from PIL import Image
import mediapipe as mp
from skimage.morphology import skeletonize

MODEL_PATH = os.path.join(os.path.dirname(__file__), "palm_models", "checkpoint_aug_epoch70.pth")
RESIZE_VALUE = 256

# Lazy-loaded model + cluster centers
_net = None
_centers = None

# Pre-computed K-means cluster centers (from palmistry project, trained on PLSU dataset)
# These distinguish: heart line, head line, life line
_CLUSTER_CENTERS = [
    np.array([5.232849, 4.881592, 6.3223267, 6.64093, 0.8113839,
              0.655735, 0.82874316, 0.74796075, 0.7993417, 0.8345605,
              0.68143266, 0.90320605, 0.5769709, 0.9721149, 0.53258324,
              0.98307294, 0.4804058, 0.9829783, 0.36796156, 0.99141085,
              0.24345541, 0.99082345, 0.30017138, 0.9736235], dtype=np.float32),
    np.array([5.645419, 4.169626, 7.126243, 6.0026045, 0.3532842,
              0.928315, 0.4692493, 0.9680717, 0.578683, 0.9680221,
              0.7227269, 0.9454175, 0.7741767, 0.9495983, 0.7802345,
              0.89685285, 0.8743354, 0.8478447, 0.85625464, 0.82669544,
              0.88459945, 0.8000444, 0.8956431, 0.74734426], dtype=np.float32),
    np.array([5.755994, 3.8910964, 8.680631, 5.3926454, 0.4247846,
              0.93111324, 0.6940754, 0.9203782, 0.8567455, 0.767301,
              0.9177662, 0.6054738, 0.9801044, 0.47111732, 0.9812451,
              0.34593108, 0.97122467, 0.28715244, 0.9036454, 0.26124895,
              0.8069528, 0.25324377, 0.59989274, 0.32016128], dtype=np.float32)
]


def _get_net():
    global _net
    if _net is None:
        from palm_unet import UNet
        _net = UNet(n_channels=3, n_classes=1)
        _net.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
        _net.eval()
    return _net


def _warp_palm(image_bgr: np.ndarray) -> np.ndarray | None:
    """Use MediaPipe Hands to warp palm to a canonical view."""
    pts_index = list(range(21))
    pts_target_normalized = np.float32([
        [1-0.48203104734420776, 0.9063420295715332],
        [1-0.6043621301651001, 0.8119394183158875],
        [1-0.6763232946395874, 0.6790258884429932],
        [1-0.7340714335441589, 0.5716733932495117],
        [1-0.7896472215652466, 0.5098430514335632],
        [1-0.5655680298805237, 0.5117031931877136],
        [1-0.5979393720626831, 0.36575648188591003],
        [1-0.6135331392288208, 0.2713503837585449],
        [1-0.6196483373641968, 0.19251111149787903],
        [1-0.4928809702396393, 0.4982593059539795],
        [1-0.4899863600730896, 0.3213786780834198],
        [1-0.4894656836986542, 0.21283167600631714],
        [1-0.48334982991218567, 0.12900274991989136],
        [1-0.4258815348148346, 0.5180916786193848],
        [1-0.4033462107181549, 0.3581996262073517],
        [1-0.3938145041465759, 0.2616880536079407],
        [1-0.38608720898628235, 0.1775170862674713],
        [1-0.36368662118911743, 0.5642163157463074],
        [1-0.33553171157836914, 0.44737303256988525],
        [1-0.3209102153778076, 0.3749568462371826],
        [1-0.31213682889938354, 0.3026996850967407]
    ])

    image = cv2.flip(image_bgr, 1)
    h, w = image.shape[:2]

    with mp.solutions.hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5) as hands:
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks is None:
            return None
        hand_landmarks = results.multi_hand_landmarks[0]
        pts = np.float32([[hand_landmarks.landmark[i].x * w, hand_landmarks.landmark[i].y * h] for i in pts_index])
        pts_target = np.float32([[x * w, y * h] for x, y in pts_target_normalized])
        M, _ = cv2.findHomography(pts, pts_target, cv2.RANSAC, 5.0)
        warped = cv2.warpPerspective(image, M, (w, h), borderMode=cv2.BORDER_REPLICATE)
        return warped


def _detect_lines(warped_bgr: np.ndarray) -> np.ndarray:
    """Run U-Net on warped palm to detect palm lines mask."""
    pil = Image.fromarray(cv2.cvtColor(warped_bgr, cv2.COLOR_BGR2RGB))
    img = np.asarray(pil.resize((RESIZE_VALUE, RESIZE_VALUE), resample=Image.NEAREST)) / 255.0
    img_t = torch.tensor(img, dtype=torch.float32).unsqueeze(0).permute(0, 3, 1, 2)
    net = _get_net()
    with torch.no_grad():
        pred = net(img_t).squeeze(0)
        # Threshold: > 0.03 → line pixel
        mask = (pred > 0.03).float()
        mask_np = (mask.permute(1, 2, 0).numpy() * 255).astype(np.uint8)
        return mask_np


def _classify_lines(line_mask: np.ndarray) -> list:
    """Classify detected pixels into 3 principal lines using K-means cluster centers."""
    gray = cv2.cvtColor(line_mask, cv2.COLOR_RGB2GRAY) if len(line_mask.shape) == 3 else line_mask
    skel = skeletonize(gray > 0).astype(np.uint8) * 255

    # Build graph from skeleton
    nodes = []
    count = np.zeros(skel.shape)
    for y in range(1, skel.shape[0] - 1):
        for x in range(1, skel.shape[1] - 1):
            if skel[y, x] == 0: continue
            count[y, x] = np.count_nonzero(skel[y-1:y+2, x-1:x+2]) - 1
            if count[y, x] == 1 or count[y, x] >= 3:
                nodes.append((y, x))

    nodes.sort(key=lambda n: n[0] + n[1])

    # Build graph connections
    graph = {n: {} for n in nodes}
    not_visited = np.ones(skel.shape)
    for node in nodes:
        y, x = node
        not_visited[y, x] = 0
        around = np.multiply(count[y-1:y+2, x-1:x+2], not_visited[y-1:y+2, x-1:x+2])
        next_pos = np.transpose(np.nonzero(around))
        if next_pos.shape[0] == 0: continue
        for dy, dx in next_pos:
            ny, nx = y + dy - 1, x + dx - 1
            if dx == 0 or (dy == 0 and dx == 1):
                dy, dx = 2 - dy, 2 - dx
            temp_line = [[y, x, 0, 0], [ny, nx, dy - 1, dx - 1]]
            if count[ny, nx] == 1 or count[ny, nx] >= 3:
                not_visited[ny, nx] = 1
                graph[tuple(temp_line[0][:2])][tuple(temp_line[-1][:2])] = temp_line
                graph[tuple(temp_line[-1][:2])][tuple(temp_line[0][:2])] = list(reversed(temp_line))
                continue
            while True:
                py, px = temp_line[-1][:2]
                not_visited[py, px] = 0
                around2 = np.multiply(count[py-1:py+2, px-1:px+2], not_visited[py-1:py+2, px-1:px+2])
                np2 = np.transpose(np.nonzero(around2))
                if np2.shape[0] == 0: break
                nny, nnx = py + np2[0][0] - 1, px + np2[0][1] - 1
                ddy, ddx = nny - py, nnx - px
                if ddx == -1 or (ddy == -1 and ddx == 0):
                    ddy, ddx = -ddy, -ddx
                temp_line.append([nny, nnx, ddy, ddx])
                not_visited[nny, nnx] = 0
                if count[nny, nnx] == 1 or count[nny, nnx] >= 3:
                    graph[tuple(temp_line[0][:2])][tuple(temp_line[-1][:2])] = temp_line
                    graph[tuple(temp_line[-1][:2])][tuple(temp_line[0][:2])] = list(reversed(temp_line))
                    not_visited[nny, nnx] = 1
                    break
        not_visited[node[0], node[1]] = 1

    # Backtrack to find all possible lines
    lines_node = []
    visited = {n: False for n in nodes}
    finished = {n: False for n in nodes}

    def backtrack(temp, g, vis, fin, nd):
        end_pt = True
        for nxt in g[nd]:
            if not vis[nxt]:
                end_pt = False
                temp.append(nxt)
                vis[nxt] = True
                fin[nxt] = True
                backtrack(temp, g, vis, fin, nxt)
                del temp[-1]
                vis[nxt] = False
        if end_pt:
            lines_node.append(list(temp))

    for node in nodes:
        if not finished[node]:
            temp = [node]
            visited[node] = True
            finished[node] = True
            backtrack(temp, graph, visited, finished, node)

    # Filter lines
    lines = []
    for line_node in lines_node:
        if len(line_node) == 1: continue
        wrong = False
        line = []
        prev, cur = None, line_node[0]
        for i in range(1, len(line_node)):
            nxt = line_node[i]
            if i > 1 and (cur[0] - prev[0]) * (nxt[0] - cur[0]) + (cur[1] - prev[1]) * (nxt[1] - cur[1]) < 0:
                wrong = True
                break
            line.extend(graph[cur][nxt])
            prev, cur = cur, nxt
        if wrong or len(line) < 10: continue
        lines.append(line)

    if len(lines) < 3:
        return [None, None, None]

    # Extract features for each line and classify
    def extract_feature(line, h, w):
        f = np.append(np.min(line, axis=0)[:2] / np.array([h, w], dtype=np.float32),
                      np.max(line, axis=0)[:2] / np.array([h, w], dtype=np.float32)) * 10
        N, step = 10, max(len(line) // 10, 1)
        for i in range(N):
            l = line[i * step:(i + 1) * step]
            f = np.append(f, np.mean(l, axis=0)[2:])
        return f

    features = np.array([extract_feature(l, skel.shape[0], skel.shape[1]) for l in lines])

    classified = [None, None, None]
    nearest = [1e9, 1e9, 1e9]
    chosen_idx = set()
    for i in range(3):
        center = _CLUSTER_CENTERS[i]
        for j, feat in enumerate(features):
            if j in chosen_idx: continue
            d = np.linalg.norm(feat - center)
            if d < nearest[i]:
                nearest[i] = d
                classified[i] = lines[j]
                if i > 0:
                    chosen_idx.add(j)

    return classified  # [heart_line, head_line, life_line]


def _measure_lines(warped_bgr: np.ndarray, lines: list) -> dict:
    """Measure line properties using MediaPipe hand landmarks as thresholds."""
    h, w = warped_bgr.shape[:2]
    image = cv2.flip(warped_bgr, 1)

    heart_thres_x = head_thres_x = life_thres_y = 0
    with mp.solutions.hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5) as hands:
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            lm = results.multi_hand_landmarks[0]
            zero_y = lm.landmark[0].y
            one_y = lm.landmark[1].y
            five_x = lm.landmark[5].x
            nine_x = lm.landmark[9].x
            thirteen_x = lm.landmark[13].x
            heart_thres_x = w * (1 - (nine_x + (five_x - nine_x) * 2 / 5))
            head_thres_x = w * (1 - (thirteen_x + (nine_x - thirteen_x) / 3))
            life_thres_y = h * (one_y + (zero_y - one_y) / 3)

    if None in lines or len([l for l in lines if l is not None]) < 3:
        return {"error": "Could not detect 3 principal lines"}

    heart_line, head_line, life_line = lines[0], lines[1], lines[2]

    result = {
        "heart_line": {
            "length_px": len(heart_line) if heart_line else 0,
            "is_long": (heart_line[0][1] < heart_thres_x) if heart_line else None,
            "description_long": "感情线绵长，情深义重。你重视情感连接，一旦建立关系便会长久维系。",
            "description_short": "感情线较短，社交圈广泛。你一生会遇见形形色色的人，人际关系丰富多元。",
        },
        "head_line": {
            "length_px": len(head_line) if head_line else 0,
            "is_long": (head_line[-1][1] > head_thres_x) if head_line else None,
            "description_long": "智慧线深长，思维广博。你对世界充满好奇，一生探索广泛的知识领域。",
            "description_short": "智慧线集中，专注精深。你倾向于深耕一个领域，成为专家型人才。",
        },
        "life_line": {
            "length_px": len(life_line) if life_line else 0,
            "is_long": (life_line[-1][0] > life_thres_y) if life_line else None,
            "description_long": "生命线深长有力，生命力旺盛。你习惯与他人共同面对挑战，团队协作是你的优势。",
            "description_short": "生命线独立分明，自主性强。你倾向于独立解决问题，个人能力出众。",
        },
    }

    return result


def analyze_palm(image_data: bytes) -> dict:
    """
    Full pipeline: image → warp → U-Net detection → classification → measurement
    
    Returns dict with:
      - success: bool
      - lines_detected: int
      - features: dict with heart_line/head_line/life_line properties
      - error: str (if failed)
    """
    nparr = np.frombuffer(image_data, np.uint8)
    img_bgr = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img_bgr is None:
        return {"success": False, "error": "Invalid image data"}

    # Step 1: Warp palm to canonical view
    warped = _warp_palm(img_bgr)
    if warped is None:
        return {"success": False, "error": "No hand detected in image. Please ensure a clear palm photo."}

    # Step 2: U-Net line detection
    line_mask = _detect_lines(warped)

    # Step 3: Classify lines
    lines = _classify_lines(line_mask)

    # Step 4: Measure
    features = _measure_lines(warped, lines)

    if "error" in features:
        return {"success": False, "error": features["error"], "lines_detected": 0}

    n_lines = len([l for l in lines if l is not None])
    return {
        "success": True,
        "lines_detected": n_lines,
        "heart_line": features["heart_line"],
        "head_line": features["head_line"],
        "life_line": features["life_line"],
    }

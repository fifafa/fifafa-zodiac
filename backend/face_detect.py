#!/usr/bin/env python3
"""
Phase 1 Face Detection — MediaPipe 0.10.x FaceLandmarker-based feature extraction
Extracts: face ratio, forehead/midface/lowerface, eye distance, nose width, jaw angle
"""

import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import Image, ImageFormat
import os

# Model path
_MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "face_landmarker.task")

# Lazy-initialized detector
_detector = None


def _get_detector():
    global _detector
    if _detector is None:
        base_options = python.BaseOptions(model_asset_path=_MODEL_PATH)
        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            num_faces=1,
            min_face_detection_confidence=0.5,
            running_mode=vision.RunningMode.IMAGE,
        )
        _detector = vision.FaceLandmarker.create_from_options(options)
    return _detector


def extract_features(image_path: str) -> dict:
    """
    Extract facial features from a photo.
    Returns dict with normalized ratios, or None if no face detected.
    """
    detector = _get_detector()

    img_bgr = cv2.imread(image_path)
    if img_bgr is None:
        return None

    h, w = img_bgr.shape[:2]
    rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    mp_image = Image(image_format=ImageFormat.SRGB, data=rgb)

    result = detector.detect(mp_image)

    if not result.face_landmarks:
        return None

    lm_list = result.face_landmarks[0]  # first face

    # Helper: get (x, y) for landmark index
    def pt(idx):
        lm = lm_list[idx]
        return (int(lm.x * w), int(lm.y * h))

    def dist(a, b):
        return np.linalg.norm(np.array(a) - np.array(b))

    # Face bounding box
    face_left = pt(234)
    face_right = pt(454)
    face_top = pt(10)
    face_bottom = pt(152)

    face_w = dist(face_left, face_right)
    face_h = dist(face_top, face_bottom)
    face_ratio = round(face_h / face_w, 2) if face_w > 0 else 0

    # Three regions (上庭/中庭/下庭)
    hairline = pt(10)
    brow_top = pt(70)
    nose_bottom = pt(2)
    chin = pt(152)

    total_h = dist(hairline, chin)
    forehead_h = dist(hairline, brow_top)
    midface_h = dist(brow_top, nose_bottom)
    lowerface_h = dist(nose_bottom, chin)

    forehead_ratio = round(forehead_h / total_h, 2) if total_h > 0 else 0
    midface_ratio = round(midface_h / total_h, 2) if total_h > 0 else 0
    lowerface_ratio = round(lowerface_h / total_h, 2) if total_h > 0 else 0

    # Eye distance
    left_eye = pt(33)
    right_eye = pt(263)
    eye_distance = round(dist(left_eye, right_eye) / face_w, 2) if face_w > 0 else 0

    # Nose width
    nose_left = pt(64)
    nose_right = pt(294)
    nose_width = round(dist(nose_left, nose_right) / face_w, 2) if face_w > 0 else 0

    # Jaw angle
    left_jaw = pt(172)
    right_jaw = pt(397)
    jaw_center = pt(152)
    jaw_left_dist = dist(left_jaw, jaw_center)
    jaw_right_dist = dist(right_jaw, jaw_center)
    jaw_width = dist(left_jaw, right_jaw)
    jaw_angle = round(np.degrees(np.arccos(
        (jaw_left_dist**2 + jaw_right_dist**2 - jaw_width**2) /
        (2 * jaw_left_dist * jaw_right_dist + 0.001)
    )))

    # Brow angle
    brow_left = pt(70)
    brow_right = pt(300)
    brow_angle = round(np.degrees(np.arctan2(
        brow_right[1] - brow_left[1],
        brow_right[0] - brow_left[0]
    )))

    return {
        "face_ratio": face_ratio,
        "forehead_ratio": forehead_ratio,
        "midface_ratio": midface_ratio,
        "lowerface_ratio": lowerface_ratio,
        "eye_distance": eye_distance,
        "nose_width": nose_width,
        "jaw_angle": jaw_angle,
        "brow_angle": brow_angle,
    }


if __name__ == "__main__":
    import sys, json
    if len(sys.argv) < 2:
        print("Usage: python face_detect.py <image_path>")
        sys.exit(1)

    features = extract_features(sys.argv[1])
    if features:
        print(json.dumps(features, indent=2))
    else:
        print("No face detected")

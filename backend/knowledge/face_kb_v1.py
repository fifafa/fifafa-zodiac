#!/usr/bin/env python3
"""
Phase 1 Knowledge Base — 面相人格知识库 V1
Target: 300 rules, structured JSON
Sources: 麻衣相法 / 柳庄相法 / 冰鉴 / 神相全编 + MBTI / OCEAN / DISC
"""

FACE_KNOWLEDGE_BASE = [
    # ===== 上庭（额头）=====
    {
        "id": "F001",
        "feature": "额头宽阔饱满",
        "feature_key": "forehead_ratio",
        "condition": ">= 0.35",
        "traditional": "天庭饱满，少年运佳。《麻衣相法》云：'天庭高耸，少年富贵可期'。额头主智慧与早年运势。",
        "modern": "前额叶皮层较活跃区域，通常与抽象思维、规划能力相关。大五人格中通常体现为较高的开放性。",
        "ocean": {"O": "高", "C": "中高", "E": "中", "A": "中", "N": "中低"},
        "mbti_hint": ["INTJ", "INTP", "ENTJ"],
        "strength": "规划能力强，善于前瞻性思考",
        "risk": "容易过度思考，陷入理想化而忽略执行细节",
        "advice": "将长期规划拆解为可执行的周计划，每周复盘执行率。找一个执行力强的合作伙伴互补。",
        "category": "上庭"
    },
    {
        "id": "F002",
        "feature": "额头偏窄",
        "feature_key": "forehead_ratio",
        "condition": "<= 0.28",
        "traditional": "天庭略窄，早年多劳。《冰鉴》言：'额头窄者，早年奔波，中年后渐入佳境'。",
        "modern": "通常与专注力强、实干型思维相关。OCEAN模型中尽责性往往较高，做事踏实。",
        "ocean": {"O": "中", "C": "高", "E": "中低", "A": "中高", "N": "中"},
        "mbti_hint": ["ISTJ", "ISFJ", "ESTJ"],
        "strength": "执行力强，做事专注可靠",
        "risk": "容易陷入细节，缺乏全局视角",
        "advice": "每周留出2小时做战略思考，培养'跳出来看问题'的习惯。尝试不同领域的新鲜事物。",
        "category": "上庭"
    },
    
    # ===== 中庭（鼻子、颧骨）=====
    {
        "id": "F003",
        "feature": "鼻梁高挺端正",
        "feature_key": "nose_width",
        "condition": "<= 0.16",
        "traditional": "鼻为财帛宫，鼻梁高挺者自信果决。《麻衣相法》：'鼻如悬胆，中年得志'。主事业与决断力。",
        "modern": "与自信、领导力相关。外向性通常偏高，情绪稳定性较好。",
        "ocean": {"O": "中高", "C": "高", "E": "高", "A": "中", "N": "低"},
        "mbti_hint": ["ENTJ", "ESTJ", "ENFJ"],
        "strength": "决策果断，有领导气质",
        "risk": "可能过于强势，忽略他人感受",
        "advice": "重大决策前强制征求至少2个不同立场的人的意见。练习倾听，先理解再回应。",
        "category": "中庭"
    },
    {
        "id": "F004",
        "feature": "鼻翼较宽",
        "feature_key": "nose_width",
        "condition": ">= 0.20",
        "traditional": "鼻翼丰厚者待人宽厚。《柳庄相法》论：'鼻头圆大，心地仁慈，乐善好施'。",
        "modern": "与宜人性相关，通常待人温和、善解人意。社交网络中往往扮演调和者角色。",
        "ocean": {"O": "中", "C": "中", "E": "中高", "A": "高", "N": "中"},
        "mbti_hint": ["ENFJ", "ESFJ", "ISFP"],
        "strength": "亲和力强，人际关系融洽",
        "risk": "容易过度迁就他人，忽略自己的边界",
        "advice": "学习设置健康边界。练习说'不'。每月做一次自我需求清单。",
        "category": "中庭"
    },
    
    # ===== 下庭（下巴、嘴）=====
    {
        "id": "F005",
        "feature": "下巴圆润饱满",
        "feature_key": "lowerface_ratio",
        "condition": ">= 0.34",
        "traditional": "下庭饱满，晚年安康。《冰鉴》云：'地阁方圆，晚运亨通'。主人际关系与福泽。",
        "modern": "与情绪稳定性和社会支持系统相关。宜人性通常偏高，容易建立稳定关系。",
        "ocean": {"O": "中", "C": "中高", "E": "中", "A": "高", "N": "低"},
        "mbti_hint": ["ISFJ", "ESFJ", "ENFJ"],
        "strength": "情绪稳定，人际关系持久",
        "risk": "可能安于现状，缺乏突破动力",
        "advice": "每季度设定一个微挑战目标（如公开演讲、学习新技能），突破舒适区。",
        "category": "下庭"
    },
    
    # ===== 眉眼 =====
    {
        "id": "F006",
        "feature": "眉眼间距适中，眉形舒展",
        "feature_key": "brow_angle",
        "condition": ">= 10 & <= 20",
        "traditional": "眉目清秀者心思细腻。《麻衣相法》论眉：'眉为保寿官，清秀者多才艺'。",
        "modern": "通常与情绪感知力、审美能力相关。开放性偏高，对艺术和美有天然敏感。",
        "ocean": {"O": "高", "C": "中", "E": "中", "A": "中高", "N": "中"},
        "mbti_hint": ["INFP", "INFJ", "ISFP"],
        "strength": "感知力敏锐，有创造力",
        "risk": "容易受他人情绪影响，需要独处充电",
        "advice": "将敏感转化为创作输出（写作、绘画、音乐）。保持每日独处时间。",
        "category": "眉眼"
    },
    
    # ===== 眼距 =====
    {
        "id": "F007",
        "feature": "眼距较宽",
        "feature_key": "eye_distance",
        "condition": ">= 0.30",
        "traditional": "眼距宽者眼界开阔，不拘小节。相书称'双瞳分远，志在四方'。",
        "modern": "与发散思维、开放性相关。通常对新事物接纳度高，有创新精神。",
        "ocean": {"O": "高", "C": "中低", "E": "高", "A": "中", "N": "中低"},
        "mbti_hint": ["ENFP", "ENTP", "INFP"],
        "strength": "思维开阔，创意丰富",
        "risk": "容易分心，难以专注于单一目标",
        "advice": "使用番茄工作法聚焦。每周选择1个核心项目深度推进，其余想法记录到'创意冰箱'。",
        "category": "五官"
    },
    
    # ===== 下颌 =====
    {
        "id": "F008",
        "feature": "下颌线条分明",
        "feature_key": "jaw_angle",
        "condition": "<= 115",
        "traditional": "腮骨有力，意志坚定。《冰鉴》：'骨有九起，天庭骨隆起，枕骨强起……'骨骼清奇者意志超人。",
        "modern": "与尽责性、抗压能力正相关。通常做事务实，不轻易放弃。",
        "ocean": {"O": "中低", "C": "高", "E": "中", "A": "中", "N": "低"},
        "mbti_hint": ["ISTJ", "ESTJ", "INTJ"],
        "strength": "意志坚定，抗压能力强",
        "risk": "可能固执己见，不容易接受反馈",
        "advice": "练习'反向思维'：每季度读一本与已有观点完全相反的书。主动寻求不同意见。",
        "category": "下庭"
    },
]

def match_features(features: dict) -> list:
    """Match extracted facial features to knowledge base rules"""
    matches = []
    for rule in FACE_KNOWLEDGE_BASE:
        key = rule["feature_key"]
        if key not in features:
            continue
        val = features[key]
        cond = rule["condition"]
        # Evaluate simple condition
        try:
            if "&" in cond:
                parts = cond.split("&")
                ok = all(eval(f"{val}{p.strip()}") for p in parts)
            else:
                ok = eval(f"{val}{cond}")
            if ok:
                matches.append(rule)
        except:
            continue
    return matches

def get_knowledge_context(features: dict) -> str:
    """Generate knowledge context for LLM prompt"""
    matches = match_features(features)
    if not matches:
        return "（未匹配到特定规则，请基于一般面部特征进行综合分析）"
    
    lines = []
    lines.append(f"【匹配到 {len(matches)} 条知识库规则】\n")
    for i, rule in enumerate(matches, 1):
        lines.append(f"### 规则 {i}：{rule['feature']}")
        lines.append(f"— 传统文化：《{rule['traditional']}》")
        lines.append(f"— 现代心理：{rule['modern']}")
        lines.append(f"— OCEAN倾向：{rule['ocean']}")
        lines.append(f"— 性格优势：{rule['strength']}")
        lines.append(f"— 潜在风险：{rule['risk']}")
        lines.append(f"— 成长建议：{rule['advice']}")
        lines.append("")
    
    return "\n".join(lines)


if __name__ == "__main__":
    test = {
        "forehead_ratio": 0.36,
        "nose_width": 0.15,
        "lowerface_ratio": 0.30,
        "eye_distance": 0.31,
        "jaw_angle": 110,
        "brow_angle": 15,
        "gender": "女",
        "age_range": "25-35"
    }
    ctx = get_knowledge_context(test)
    print(ctx)
    print(f"\n---\nTotal rules in KB: {len(FACE_KNOWLEDGE_BASE)}")
    print("Matched:", len(match_features(test)))

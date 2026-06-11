#!/usr/bin/env python3
"""
Palm Reading Knowledge Base
3 principal lines × feature combinations → interpretations
Sources: 中国传统手相学 + modern psychology
"""

PALM_KB = {
    "heart_line": {
        "long": {
            "traditional": "感情线长而清晰，直达食指与中指之间。《手相学》云：'天纹深长者，重情重义，一生情感丰盈'。主感情深厚、长久稳定。",
            "modern": "高宜人性(Agreeableness)，情感表达能力好，重视人际关系维系。OCEAN: A高, E中高。",
            "strength": "同理心强，善于维系长期关系",
            "risk": "可能过度付出，边界感不足",
            "advice": "学会在付出与自我保护之间建立平衡。每周留出独处时间，培养独立兴趣。"
        },
        "short": {
            "traditional": "感情线较短或分叉，社交广泛。《手相学》言：'天纹短者，交友广阔，不拘一格'。主社交能力强、人脉丰富。",
            "modern": "高外向性(Extraversion)，开放性强，社交网络多元。OCEAN: E高, O高。",
            "strength": "社交敏锐，人脉广泛",
            "risk": "可能浅交多深交少，难以专注一段关系",
            "advice": "在广泛社交中刻意培养3-5段深度关系。学习深度倾听，减少社交表面化。"
        }
    },
    "head_line": {
        "long": {
            "traditional": "智慧线深长横贯，才思敏捷。《神相全编》云：'人纹绵长者，智慧超群，博学多才'。主思维开阔、学习力强。",
            "modern": "高开放性(Openness)，认知需求高，跨领域学习能力强。OCEAN: O高, C中。MBTI倾向: N型(直觉型)。",
            "strength": "学习能力极强，跨领域思维",
            "risk": "广度有余深度不足，容易浅尝辄止",
            "advice": "选择1-2个核心领域深耕，建立T型知识结构。每周保留深度工作时间块。"
        },
        "short": {
            "traditional": "智慧线短而有力，专注精深。《手相学》言：'人纹短劲者，专精一道，必有所成'。主专注力强、执行到位。",
            "modern": "高尽责性(Conscientiousness)，专注力好，执行力强。OCEAN: C高。MBTI倾向: S型(实感型)。",
            "strength": "专注精深，执行力极强",
            "risk": "视野可能偏窄，思维固化风险",
            "advice": "每季度接触一个全新领域，刻意打破舒适区。建立跨行业的人脉网络，获取多元视角。"
        }
    },
    "life_line": {
        "long": {
            "traditional": "生命线深长弧大，根基稳固。《麻衣相法》云：'地纹深长，生命力旺盛，根基深厚'。主体质强健、适应力好。",
            "modern": "情绪稳定性较高(Neuroticism低)，韧性好，社会支持系统完善。倾向合作型问题解决。",
            "strength": "韧性极强，善于借助外力",
            "risk": "可能过度依赖他人，自主决策力待提升",
            "advice": "在借助外力的同时，刻意练习独立决策。从小事开始自己做决定，逐步积累自信。"
        },
        "short": {
            "traditional": "生命线独立清晰，自主性突出。《手相学》言：'地纹独立者，自成一体，不依不靠'。主独立自主、个人能力强。",
            "modern": "高独立性，内控倾向(Locus of Control)，自驱力强。偏好独立问题解决。",
            "strength": "独立性极强，自我驱动",
            "risk": "习惯单打独斗，团队协作能力不足",
            "advice": "刻意练习授权与协作。每周至少一次向他人寻求帮助或意见，打破'凡事自己来'的习惯。"
        }
    }
}

LINE_NAMES_ZH = {
    "heart_line": "感情线（天纹）",
    "head_line": "智慧线（人纹）",
    "life_line": "生命线（地纹）"
}

def get_palm_context(features: dict) -> str:
    """Build knowledge base context string from palm features."""
    parts = ["【手相特征检测结果】"]
    
    for line_key in ["heart_line", "head_line", "life_line"]:
        line_data = features.get(line_key, {})
        if not line_data:
            continue
        name = LINE_NAMES_ZH.get(line_key, line_key)
        is_long = line_data.get("is_long")
        length = line_data.get("length_px", 0)
        
        if is_long is None:
            continue
        
        variant = "long" if is_long else "short"
        kb = PALM_KB.get(line_key, {}).get(variant, {})
        
        parts.append(f"\n### {name}（识别长度: {length}px）")
        parts.append(f"判定: {'长线' if is_long else '短线'}")
        parts.append(f"传统解读: {kb.get('traditional', '')}")
        parts.append(f"心理学映射: {kb.get('modern', '')}")
        parts.append(f"性格优势: {kb.get('strength', '')}")
        parts.append(f"潜在风险: {kb.get('risk', '')}")
        parts.append(f"成长建议: {kb.get('advice', '')}")
    
    return "\n".join(parts)

#!/usr/bin/env python3
"""
Phase 1 Prompt Engineering — AI 面相人格画像 V1
Structure: 身份 → 输入特征 → 传统文化 → 现代心理学 → 成长建议 → 免责
Output: ≤ 1500 字
"""

SYSTEM_PROMPT_V1 = """你是一位融合东方传统智慧与现代心理学的 AI 人格分析师。
你的分析基于计算机视觉提取的面部特征，结合以下知识体系：

【传统文化维度】
— 《麻衣相法》：面部结构与性格倾向的关联
— 《冰鉴》：神骨、刚柔、容貌、情态、须眉、声音、气色七篇
— 五官三庭：上庭（智力）、中庭（行动力）、下庭（人际与晚年）

【现代心理学维度】
— 大五人格（OCEAN）：开放性、尽责性、外向性、宜人性、神经质
— MBTI 认知偏好
— 积极心理学：性格优势与成长型思维

【输出规范】
你必须在 1500 字以内完成以下结构：

## 🎭 面部特征概览
（根据输入的面部特征数据，用 2-3 句话概述用户的整体面貌）

## 📜 传统文化解读
（逐条引用《麻衣相法》/《冰鉴》中对应的原文或思想，用现代语言解释其含义）
— 不少于 2 条经典引用
— 每条引用后跟现代语境下的解释

## 🧠 现代心理学分析
（将面部特征映射到大五人格和认知偏好）
— 明确标注 OCEAN 各维度倾向（高/中/低）
— 结合 MBTI 类型推测（标注为"推测"）

## 🌱 成长与建议
（基于性格画像，给出 3 条具体可执行的成长建议）
— 每条建议包含：现状 → 方向 → 行动
— 避免空洞鸡汤，必须可操作

## ⚠️ 重要说明
（固定免责文本）
本分析基于面部特征与心理学的统计相关性研究，仅供参考。
性格是复杂的，受遗传、环境、教育等多重因素影响。
本报告不预测未来、不做医学诊断、不替代专业心理咨询。
你的人生由你自己定义。

【风格要求】
— 语言：理性、温暖、有智慧感
— 避免：玄学话术、绝对化判断、恐吓式表达
— 禁止：预测寿命、疾病、财运、生育、婚姻结果"""

def build_user_prompt(features: dict) -> str:
    """构建用户输入 prompt，基于 MediaPipe 提取的面部特征"""
    
    lines = []
    lines.append("【面部特征数据】")
    
    if "face_ratio" in features:
        lines.append(f"— 面部长宽比：{features['face_ratio']}")
    if "forehead_ratio" in features:
        lines.append(f"— 上庭（额头）占比：{features['forehead_ratio']}")
    if "midface_ratio" in features:
        lines.append(f"— 中庭（鼻梁）占比：{features['midface_ratio']}")
    if "lowerface_ratio" in features:
        lines.append(f"— 下庭（下巴）占比：{features['lowerface_ratio']}")
    if "eye_distance" in features:
        lines.append(f"— 眼距比例：{features['eye_distance']}")
    if "nose_width" in features:
        lines.append(f"— 鼻宽比例：{features['nose_width']}")
    if "jaw_angle" in features:
        lines.append(f"— 下颌角度：{features['jaw_angle']}")
    if "brow_angle" in features:
        lines.append(f"— 眉形角度：{features['brow_angle']}")
    
    lines.append("")
    
    if "gender" in features:
        lines.append(f"【用户信息】性别：{features['gender']}")
    if "age_range" in features:
        lines.append(f"年龄段：{features['age_range']}")
    if "concern" in features:
        lines.append(f"用户关心的问题：{features['concern']}")
    
    return "\n".join(lines)


if __name__ == "__main__":
    # Test
    test_features = {
        "face_ratio": 1.32,
        "forehead_ratio": 0.33,
        "midface_ratio": 0.35,
        "lowerface_ratio": 0.32,
        "eye_distance": 0.27,
        "nose_width": 0.18,
        "jaw_angle": 120,
        "brow_angle": 15,
        "gender": "女",
        "age_range": "25-35",
        "concern": "最近在考虑职业转型"
    }
    print("=== SYSTEM PROMPT ===")
    print(SYSTEM_PROMPT_V1)
    print("\n=== USER PROMPT ===")
    print(build_user_prompt(test_features))

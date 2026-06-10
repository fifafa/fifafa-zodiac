#!/usr/bin/env python3
"""
Phase 1 Knowledge Base — 面相人格知识库 V2
Total: 316 rules
Sources: 麻衣相法 / 柳庄相法 / 冰鉴 / 神相全编 + MBTI / OCEAN / DISC / PERMA
Generated: auto + manual curation
"""

FACE_KNOWLEDGE_BASE = [
    {
            "id": "F001",
            "feature": "额头宽阔饱满",
            "feature_key": "forehead_ratio",
            "condition": ">= 0.35",
            "traditional": "天庭饱满，少年运佳。《麻衣相法》云：'天庭高耸，少年富贵可期'。额头主智慧与早年运势。",
            "modern": "前额叶皮层较活跃区域，通常与抽象思维、规划能力相关。大五人格中通常体现为较高的开放性。",
            "ocean": {
                    "O": "高",
                    "C": "中高",
                    "E": "中",
                    "A": "中",
                    "N": "中低"
            },
            "mbti_hint": [
                    "INTJ",
                    "INTP",
                    "ENTJ"
            ],
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
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中低",
                    "A": "中高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ISFJ",
                    "ESTJ"
            ],
            "strength": "执行力强，做事专注可靠",
            "risk": "容易陷入细节，缺乏全局视角",
            "advice": "每周留出2小时做战略思考，培养'跳出来看问题'的习惯。尝试不同领域的新鲜事物。",
            "category": "上庭"
    },
    {
            "id": "F003",
            "feature": "鼻梁高挺端正",
            "feature_key": "nose_width",
            "condition": "<= 0.16",
            "traditional": "鼻为财帛宫，鼻梁高挺者自信果决。《麻衣相法》：'鼻如悬胆，中年得志'。主事业与决断力。",
            "modern": "与自信、领导力相关。外向性通常偏高，情绪稳定性较好。",
            "ocean": {
                    "O": "中高",
                    "C": "高",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTJ",
                    "ENFJ"
            ],
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
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中高",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFJ",
                    "ESFJ",
                    "ISFP"
            ],
            "strength": "亲和力强，人际关系融洽",
            "risk": "容易过度迁就他人，忽略自己的边界",
            "advice": "学习设置健康边界。练习说'不'。每月做一次自我需求清单。",
            "category": "中庭"
    },
    {
            "id": "F005",
            "feature": "下巴圆润饱满",
            "feature_key": "lowerface_ratio",
            "condition": ">= 0.34",
            "traditional": "下庭饱满，晚年安康。《冰鉴》云：'地阁方圆，晚运亨通'。主人际关系与福泽。",
            "modern": "与情绪稳定性和社会支持系统相关。宜人性通常偏高，容易建立稳定关系。",
            "ocean": {
                    "O": "中",
                    "C": "中高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ",
                    "ENFJ"
            ],
            "strength": "情绪稳定，人际关系持久",
            "risk": "可能安于现状，缺乏突破动力",
            "advice": "每季度设定一个微挑战目标（如公开演讲、学习新技能），突破舒适区。",
            "category": "下庭"
    },
    {
            "id": "F006",
            "feature": "眉眼间距适中，眉形舒展",
            "feature_key": "brow_angle",
            "condition": ">= 10 & <= 20",
            "traditional": "眉目清秀者心思细腻。《麻衣相法》论眉：'眉为保寿官，清秀者多才艺'。",
            "modern": "通常与情绪感知力、审美能力相关。开放性偏高，对艺术和美有天然敏感。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "中高",
                    "N": "中"
            },
            "mbti_hint": [
                    "INFP",
                    "INFJ",
                    "ISFP"
            ],
            "strength": "感知力敏锐，有创造力",
            "risk": "容易受他人情绪影响，需要独处充电",
            "advice": "将敏感转化为创作输出（写作、绘画、音乐）。保持每日独处时间。",
            "category": "眉眼"
    },
    {
            "id": "F007",
            "feature": "眼距较宽",
            "feature_key": "eye_distance",
            "condition": ">= 0.30",
            "traditional": "眼距宽者眼界开阔，不拘小节。相书称'双瞳分远，志在四方'。",
            "modern": "与发散思维、开放性相关。通常对新事物接纳度高，有创新精神。",
            "ocean": {
                    "O": "高",
                    "C": "中低",
                    "E": "高",
                    "A": "中",
                    "N": "中低"
            },
            "mbti_hint": [
                    "ENFP",
                    "ENTP",
                    "INFP"
            ],
            "strength": "思维开阔，创意丰富",
            "risk": "容易分心，难以专注于单一目标",
            "advice": "使用番茄工作法聚焦。每周选择1个核心项目深度推进，其余想法记录到'创意冰箱'。",
            "category": "五官"
    },
    {
            "id": "F008",
            "feature": "下颌线条分明",
            "feature_key": "jaw_angle",
            "condition": "<= 115",
            "traditional": "腮骨有力，意志坚定。《冰鉴》：'骨有九起，天庭骨隆起，枕骨强起……'骨骼清奇者意志超人。",
            "modern": "与尽责性、抗压能力正相关。通常做事务实，不轻易放弃。",
            "ocean": {
                    "O": "中低",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ",
                    "INTJ"
            ],
            "strength": "意志坚定，抗压能力强",
            "risk": "可能固执己见，不容易接受反馈",
            "advice": "练习'反向思维'：每季度读一本与已有观点完全相反的书。主动寻求不同意见。",
            "category": "下庭"
    },
    {
            "feature": "高额头（额高而阔）",
            "feature_key": "forehead_ratio",
            "condition": ">=0.38",
            "traditional": "《麻衣相法》云：额高而阔，主贵寿，聪明豁达。",
            "modern": "高额头与开放性（O）高度相关，代表好奇心强、思维活跃，类似MBTI中的直觉型（N）。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "INTP"
            ],
            "strength": "思维前瞻，善于规划长远目标",
            "risk": "易脱离现实，过度理想化",
            "advice": "制定具体行动计划，将大目标分解为小步骤；定期与务实型朋友讨论想法，获取现实反馈。",
            "category": "上庭",
            "id": "F009"
    },
    {
            "feature": "中等额头（额方而匀）",
            "feature_key": "forehead_ratio",
            "condition": "0.29-0.37",
            "traditional": "《柳庄相法》曰：额方而匀，主中正平和，福禄自至。",
            "modern": "中等额头反映均衡的开放性（O）与尽责性（C），适应力强，类似MBTI中的判断型（J）与感知型（P）平衡。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESFJ"
            ],
            "strength": "稳重务实，能兼顾理想与现实",
            "risk": "缺乏突破性创新，易安于现状",
            "advice": "每月尝试一项新技能或爱好，打破舒适区；在决策时主动寻求不同观点。",
            "category": "上庭",
            "id": "F010"
    },
    {
            "feature": "窄额头（额窄而低）",
            "feature_key": "forehead_ratio",
            "condition": "<=0.28",
            "traditional": "《冰鉴》云：额窄者，性急而近利，难容物。",
            "modern": "窄额头与低开放性（O）相关，注重细节和传统，类似MBTI中的感觉型（S），尽责性（C）可能较高。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "执行力强，注重细节和规则",
            "risk": "思维僵化，易因小事焦虑",
            "advice": "练习正念冥想缓解焦虑，每天记录三件积极小事；主动参与跨部门合作，拓宽视野。",
            "category": "上庭",
            "id": "F011"
    },
    {
            "feature": "上扬眉（眉势上扬）",
            "feature_key": "brow_angle",
            "condition": ">=21",
            "traditional": "《神相全编》曰：眉上扬者，志气高，性刚烈。",
            "modern": "上扬眉与高外向性（E）和低宜人性（A）相关，代表自信和竞争意识，类似MBTI中的ENTJ。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTP"
            ],
            "strength": "领导力强，敢于挑战权威",
            "risk": "易冲动，人际关系紧张",
            "advice": "在表达观点前先倾听三秒，避免打断他人；每周安排一次非竞争性社交活动。",
            "category": "中庭",
            "id": "F012"
    },
    {
            "feature": "平和眉（眉势平缓）",
            "feature_key": "brow_angle",
            "condition": "10-20",
            "traditional": "《麻衣相法》云：眉平而顺，主性情温和，善解人意。",
            "modern": "平和眉与高宜人性（A）和中等外向性（E）相关，情绪稳定，类似MBTI中的ISFJ。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ENFJ"
            ],
            "strength": "团队协作能力强，善于调解矛盾",
            "risk": "易过度妥协，忽视自身需求",
            "advice": "学会说‘不’，每天设定一个个人边界；在会议中主动提出自己的意见。",
            "category": "中庭",
            "id": "F013"
    },
    {
            "feature": "下垂眉（眉势下垂）",
            "feature_key": "brow_angle",
            "condition": "<=9",
            "traditional": "《柳庄相法》曰：眉垂者，性柔而多虑，易生愁苦。",
            "modern": "下垂眉与高神经质（N）和低外向性（E）相关，敏感内敛，类似MBTI中的INFP。",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "低",
                    "A": "高",
                    "N": "高"
            },
            "mbti_hint": [
                    "INFP",
                    "INFJ"
            ],
            "strength": "同理心强，善于深度思考",
            "risk": "易陷入消极情绪，行动力不足",
            "advice": "建立晨间感恩日记，记录三件好事；设定每日最小行动目标（如散步10分钟）。",
            "category": "中庭",
            "id": "F014"
    },
    {
            "feature": "高额头+上扬眉（额阔眉扬）",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38且brow_angle>=21",
            "traditional": "《冰鉴》云：额阔眉扬，龙虎相济，主大贵。",
            "modern": "此组合强化了高开放性（O）和高外向性（E），类似MBTI中的ENTP，兼具创新与魄力。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTP",
                    "ENFP"
            ],
            "strength": "创新与领导力兼备，能快速推动变革",
            "risk": "易刚愎自用，忽视细节风险",
            "advice": "在项目启动前进行SWOT分析，列出潜在风险；聘请一位细节导向的助手互补。",
            "category": "综合",
            "id": "F015"
    },
    {
            "feature": "窄额头+下垂眉（额窄眉垂）",
            "feature_key": "综合",
            "condition": "forehead_ratio<=0.28且brow_angle<=9",
            "traditional": "《神相全编》曰：额窄眉垂，心狭多忧，福薄之相。",
            "modern": "此组合与低开放性（O）、低外向性（E）和高神经质（N）相关，类似MBTI中的ISFP，易自我封闭。",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "低",
                    "A": "高",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISFP",
                    "ISTP"
            ],
            "strength": "专注力强，对细节敏感",
            "risk": "社交回避，易陷入悲观循环",
            "advice": "每天主动与一位同事进行简短交流；加入一个兴趣小组，每周参加一次线下活动。",
            "category": "综合",
            "id": "F016"
    },
    {
            "traditional": "《麻衣相法》鼻为财星，窄细者心机深",
            "modern": "OCEAN尽责性高，MBTI ISTJ",
            "feature_key": "nose_width",
            "category": "中庭",
            "condition": "<=",
            "feature": "鼻梁窄细",
            "id": "F017",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [],
            "strength": "鼻梁窄细",
            "risk": "需结合具体情境综合判断",
            "advice": "建议深入了解自身性格，发挥优势。"
    },
    {
            "traditional": "《冰鉴》鼻宽者志大，然须防刚愎",
            "modern": "OCEAN外向性高，MBTI ESTP",
            "feature_key": "nose_width",
            "category": "中庭",
            "condition": ">=",
            "feature": "鼻梁宽大",
            "id": "F018",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [],
            "strength": "鼻梁宽大",
            "risk": "需结合具体情境综合判断",
            "advice": "建议深入了解自身性格，发挥优势。"
    },
    {
            "traditional": "《神相全编》中庭长者智，然情路多舛",
            "modern": "OCEAN开放性高，MBTI INTJ",
            "feature_key": "midface_ratio",
            "category": "中庭",
            "condition": ">=",
            "feature": "中庭偏长",
            "id": "F019",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [],
            "strength": "中庭偏长",
            "risk": "需结合具体情境综合判断",
            "advice": "建议深入了解自身性格，发挥优势。"
    },
    {
            "traditional": "《柳庄相法》中庭短者性急，宜修心养性",
            "modern": "OCEAN外向性高，MBTI ESFP",
            "feature_key": "midface_ratio",
            "category": "中庭",
            "condition": "<=",
            "feature": "中庭偏短",
            "id": "F020",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [],
            "strength": "中庭偏短",
            "risk": "需结合具体情境综合判断",
            "advice": "建议深入了解自身性格，发挥优势。"
    },
    {
            "traditional": "《冰鉴》鼻狭中庭长，智谋过人，然心机重",
            "modern": "OCEAN尽责性高+开放性高，MBTI INTJ",
            "feature_key": "nose_width",
            "category": "中庭",
            "condition": ">=",
            "feature": "窄鼻配长中庭",
            "id": "F021",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [],
            "strength": "窄鼻配长中庭",
            "risk": "需结合具体情境综合判断",
            "advice": "建议深入了解自身性格，发挥优势。"
    },
    {
            "traditional": "《神相全编》鼻阔中庭短，勇猛有余，智谋不足",
            "modern": "OCEAN外向性高+情绪稳定性低，MBTI ESTP",
            "feature_key": "nose_width",
            "category": "中庭",
            "condition": ">=",
            "feature": "宽鼻配短中庭",
            "id": "F022",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [],
            "strength": "宽鼻配短中庭",
            "risk": "需结合具体情境综合判断",
            "advice": "建议深入了解自身性格，发挥优势。"
    },
    {
            "condition": ">= 0.35",
            "feature_key": "lowerface_ratio",
            "traditional": "下庭长而颏锐，主晚年劳碌，心机深沉，如《麻衣相法》云‘下停长，奔波忙’；颏尖则性刚，易招是非。",
            "modern": "OCEAN中尽责性低（C-），宜忌冲动；MBTI倾向ESTJ，决策果断但缺乏耐心。",
            "category": "下庭",
            "feature": "lowerface_ratio >= 0.35",
            "id": "F023",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [],
            "strength": "lowerface_ratio >= 0.35",
            "risk": "需结合具体情境综合判断",
            "advice": "建议深入了解自身性格，发挥优势。"
    },
    {
            "condition": ">= 0.25 & <= 0.34",
            "feature_key": "lowerface_ratio",
            "traditional": "下庭中等而颏尖，主中年机变，如《神相全编》曰‘中停匀称，颏尖智巧’；但易多疑，需修心。",
            "modern": "OCEAN中神经质高（N+），MBTI为ENTP，思维敏捷但情绪波动大。",
            "category": "下庭",
            "feature": "lowerface_ratio >= 0.25 & <= 0.34",
            "id": "F024",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [],
            "strength": "lowerface_ratio >= 0.25 & <= 0.34",
            "risk": "需结合具体情境综合判断",
            "advice": "建议深入了解自身性格，发挥优势。"
    },
    {
            "condition": "<= 0.24",
            "feature_key": "lowerface_ratio",
            "traditional": "下庭短而颏锐，主早年劳心，如《冰鉴》云‘下停短促，颏尖性急’；易冲动，需防口舌。",
            "modern": "OCEAN中神经质高（N+），MBTI为INTJ，独立但易固执。",
            "category": "下庭",
            "feature": "lowerface_ratio <= 0.24",
            "id": "F025",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [],
            "strength": "lowerface_ratio <= 0.24",
            "risk": "需结合具体情境综合判断",
            "advice": "建议深入了解自身性格，发挥优势。"
    },
    {
            "id": "F026",
            "feature": "高额头+宽眼距",
            "feature_key": "复合",
            "condition": ">=0.38 & >=0.33",
            "traditional": "《麻衣相法》云：额高而阔，主贵寿，聪明豁达；《神相全编》云：两目相距宽阔，主心胸宽广，气度不凡。",
            "modern": "高额头与开放性（O）高度相关，宽眼距与宜人性（A）正相关，组合代表思维开阔且包容性强，类似MBTI中的ENFP或INFP。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP",
                    "INFP"
            ],
            "strength": "创意丰富，善于接纳多元观点，社交中富有感染力",
            "risk": "可能过于理想化，缺乏执行细节，易被他人影响",
            "advice": "建立每日任务清单，将创意转化为具体行动；定期与务实型朋友讨论，平衡理想与现实。",
            "category": "综合"
    },
    {
            "id": "F027",
            "feature": "高额头+窄眼距",
            "feature_key": "复合",
            "condition": ">=0.38 & <0.33",
            "traditional": "《麻衣相法》云：额高而阔，主贵寿；《柳庄相法》云：目距窄者，性急而专，心机深沉。",
            "modern": "高额头与开放性（O）高相关，窄眼距与神经质（N）正相关，组合代表思维活跃但易焦虑，类似MBTI中的INTJ或ENTJ。",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTJ"
            ],
            "strength": "目标明确，执行力强，善于战略规划",
            "risk": "容易固执己见，忽视他人感受，压力下易急躁",
            "advice": "练习主动倾听，每天花10分钟记录他人观点；设置放松时间，如冥想或散步，缓解焦虑。",
            "category": "综合"
    },
    {
            "id": "F028",
            "feature": "窄额头+宽眼距",
            "feature_key": "复合",
            "condition": "<0.38 & >=0.33",
            "traditional": "《冰鉴》云：额窄者，多劳心；《神相全编》云：目距宽者，心性豁达，善与人交。",
            "modern": "窄额头与尽责性（C）低相关，宽眼距与宜人性（A）高相关，组合代表随和但缺乏条理，类似MBTI中的ESFP或ISFP。",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESFP",
                    "ISFP"
            ],
            "strength": "人际关系融洽，适应力强，善于享受当下",
            "risk": "缺乏长远规划，易拖延，对细节不够关注",
            "advice": "使用番茄工作法提升专注力，每25分钟休息5分钟；设定每周目标，并请朋友监督完成进度。",
            "category": "综合"
    },
    {
            "id": "F029",
            "feature": "窄额头+窄眼距",
            "feature_key": "复合",
            "condition": "<0.38 & <0.33",
            "traditional": "《麻衣相法》云：额窄者，主劳碌；《柳庄相法》云：目距窄者，心性急，多疑。",
            "modern": "窄额头与尽责性（C）低相关，窄眼距与神经质（N）高相关，组合代表情绪敏感且易冲动，类似MBTI中的ISTJ或ESTJ。",
            "ocean": {
                    "O": "低",
                    "C": "低",
                    "E": "中",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "务实可靠，注重传统，在稳定环境中表现出色",
            "risk": "容易陷入细节焦虑，抗拒变化，人际关系紧张",
            "advice": "每天练习正念呼吸5分钟，降低焦虑水平；尝试每周学习一项新技能，逐步适应变化。",
            "category": "综合"
    },
    {
            "id": "F030",
            "feature": "中等额头+宽眼距",
            "feature_key": "复合",
            "condition": ">=0.38 & <0.42 & >=0.33",
            "traditional": "《冰鉴》云：额中正者，主中和之性；《神相全编》云：目距宽者，心胸开阔，善解人意。",
            "modern": "中等额头与开放性（O）中等相关，宽眼距与宜人性（A）高相关，组合代表平衡且亲和，类似MBTI中的INFJ或ENFJ。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "INFJ",
                    "ENFJ"
            ],
            "strength": "善于协调团队，富有同理心，能兼顾理想与现实",
            "risk": "可能过度牺牲自我，难以拒绝他人",
            "advice": "设定个人边界，每天留出30分钟独处时间；学习说“不”的技巧，优先处理自己的核心任务。",
            "category": "综合"
    },
    {
            "id": "F031",
            "feature": "中等额头+窄眼距",
            "feature_key": "复合",
            "condition": ">=0.38 & <0.42 & <0.33",
            "traditional": "《麻衣相法》云：额中正者，主福寿；《柳庄相法》云：目距窄者，心细而专，善谋略。",
            "modern": "中等额头与开放性（O）中等相关，窄眼距与神经质（N）高相关，组合代表谨慎且专注，类似MBTI中的ISTP或ESTP。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTP",
                    "ESTP"
            ],
            "strength": "分析能力强，善于解决具体问题，行动力佳",
            "risk": "容易过度批判他人，缺乏耐心，情绪波动大",
            "advice": "练习感恩日记，每天记录三件积极小事；在决策前先深呼吸10秒，避免冲动反应。",
            "category": "综合"
    },
    {
            "id": "F032",
            "feature": "宽眼距+锐利下颌",
            "feature_key": "综合",
            "condition": "eye_distance>=0.35 && jaw_angle<=100",
            "traditional": "《神相全编》云：目距宽而颐颔锐，主心性豁达而志刚，然易有孤高之嫌。",
            "modern": "宽眼距象征开放性（O）高，锐利下颌象征尽责性（C）高，组合体现独立创新与果断执行力，类似MBTI中的ENTJ或INTJ。",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTJ",
                    "INTJ"
            ],
            "strength": "视野开阔，决策果断，善于从宏观角度制定战略并快速推进",
            "risk": "易忽视细节和他人感受，可能显得冷漠或专断",
            "advice": "在决策前主动征求团队成员意见，尤其是关注情感细节；每周安排时间反思人际互动，练习共情表达。",
            "category": "综合"
    },
    {
            "id": "F033",
            "feature": "宽眼距+圆润下颌",
            "feature_key": "综合",
            "condition": "eye_distance>=0.35 && jaw_angle>100",
            "traditional": "《麻衣相法》云：目距宽而颐颔圆，主宽厚仁德，乐善好施，然易失之优柔。",
            "modern": "宽眼距（高O）与圆润下颌（高宜人性A）结合，代表开放包容与温和协作，类似MBTI中的ENFP或INFP。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP",
                    "INFP"
            ],
            "strength": "富有创造力，善于建立和谐关系，能激发团队灵感",
            "risk": "决策时易受情感影响，缺乏坚定立场",
            "advice": "设定明确的目标优先级，使用决策矩阵平衡情感与逻辑；在重要谈判前准备客观数据支持。",
            "category": "综合"
    },
    {
            "id": "F034",
            "feature": "窄眼距+锐利下颌",
            "feature_key": "综合",
            "condition": "eye_distance<0.35 && jaw_angle<=100",
            "traditional": "《柳庄相法》云：目距狭而颐颔锐，主性急志坚，精于算计，然易招是非。",
            "modern": "窄眼距（低O）与锐利下颌（高C）组合，体现专注务实与高度自律，类似MBTI中的ISTJ或ESTJ。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "注重细节，执行力强，善于在复杂环境中保持秩序和效率",
            "risk": "思维僵化，易陷入完美主义，人际关系紧张",
            "advice": "尝试接受不完美，设定弹性目标；每周参与一次非结构化活动（如自由讨论），培养灵活性。",
            "category": "综合"
    },
    {
            "id": "F035",
            "feature": "窄眼距+圆润下颌",
            "feature_key": "综合",
            "condition": "eye_distance<0.35 && jaw_angle>100",
            "traditional": "《冰鉴》云：目距近而颐颔圆，主内敛而善守，外柔内刚，然易多疑。",
            "modern": "窄眼距（低O）与圆润下颌（高A）结合，代表谨慎保守与温和包容，类似MBTI中的ISFJ或INFJ。",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "低",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISFJ",
                    "INFJ"
            ],
            "strength": "忠诚可靠，善于倾听，能营造稳定和谐的环境",
            "risk": "过度保守，抗拒变化，易因过度顾虑而错失机会",
            "advice": "定期接触新领域知识（如跨行业案例），设定小规模试错计划；与冒险型伙伴合作以平衡风险。",
            "category": "综合"
    },
    {
            "id": "F036",
            "feature": "中等眼距+锐利下颌",
            "feature_key": "综合",
            "condition": "eye_distance>=0.35 && eye_distance<0.42 && jaw_angle<=100",
            "traditional": "《神相全编》云：目距适中而颐颔锐，主智勇双全，刚柔并济，然易显锋芒。",
            "modern": "中等眼距（平衡O）与锐利下颌（高C）组合，体现理性与行动力的均衡，类似MBTI中的ENTP或ESTP。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "高",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTP",
                    "ESTP"
            ],
            "strength": "思维敏捷，适应力强，能在变化中快速找到解决方案",
            "risk": "易冲动行事，缺乏持久耐心，可能忽略长期规划",
            "advice": "在行动前强制进行5分钟利弊分析；建立长期目标清单，每周检查进度以保持方向感。",
            "category": "综合"
    },
    {
            "id": "F037",
            "feature": "中等眼距+圆润下颌",
            "feature_key": "综合",
            "condition": "eye_distance>=0.35 && eye_distance<0.42 && jaw_angle>100",
            "traditional": "《麻衣相法》云：目距匀而颐颔圆，主中和之相，福寿双全，然易流于平庸。",
            "modern": "中等眼距（平衡O）与圆润下颌（高A）组合，体现稳定随和与协作精神，类似MBTI中的ESFJ或ENFJ。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ENFJ"
            ],
            "strength": "亲和力强，善于协调团队，能营造积极氛围",
            "risk": "缺乏主见，易被他人影响，可能忽视自我需求",
            "advice": "每天留出30分钟独处时间，记录个人想法和感受；在团队决策中主动提出自己的观点，即使与他人不同。",
            "category": "综合"
    },
    {
            "id": "F038",
            "feature": "窄鼻+长下庭",
            "feature_key": "综合",
            "condition": "nose_width<0.25 & lowerface_ratio>0.33",
            "traditional": "《神相全编》云：鼻窄而狭，下庭长，主心性孤高，多思少行。",
            "modern": "窄鼻与尽责性（C）低相关，长下庭与开放性（O）高相关，组合暗示理想主义但执行力弱，类似MBTI中的INFP。",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "中",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "INFP",
                    "INFJ"
            ],
            "strength": "富有想象力，善于洞察深层意义",
            "risk": "易陷入空想，行动力不足，难以落地",
            "advice": "每天设定一个最小可行目标并完成；加入一个实践型社群，如手工艺或编程小组，强迫自己动手。",
            "category": "综合"
    },
    {
            "id": "F039",
            "feature": "窄鼻+短下庭",
            "feature_key": "综合",
            "condition": "nose_width<0.25 & lowerface_ratio<0.33",
            "traditional": "《麻衣相法》云：鼻狭而短，下庭促，主性急而刚，易怒难容。",
            "modern": "窄鼻与宜人性（A）低相关，短下庭与情绪稳定性（N）高相关，组合暗示急躁且固执，类似MBTI中的ESTJ。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "高",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ESTJ",
                    "ENTJ"
            ],
            "strength": "果断高效，执行力强，目标导向",
            "risk": "缺乏耐心，易与人冲突，忽视细节",
            "advice": "在决策前强制停顿10秒，深呼吸三次；每周安排一次无目的闲聊，练习倾听他人观点。",
            "category": "综合"
    },
    {
            "id": "F040",
            "feature": "宽鼻+长下庭",
            "feature_key": "综合",
            "condition": "nose_width>0.25 & lowerface_ratio>0.33",
            "traditional": "《柳庄相法》云：鼻宽而长，下庭阔，主心广体胖，乐善好施。",
            "modern": "宽鼻与外向性（E）高相关，长下庭与开放性（O）高相关，组合暗示热情且富有创造力，类似MBTI中的ENFP。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP",
                    "ESFP"
            ],
            "strength": "社交能力强，乐观开朗，善于激励他人",
            "risk": "容易分心，缺乏持久性，过度依赖他人认可",
            "advice": "使用番茄工作法（25分钟专注+5分钟休息）提升专注力；定期独处反思，减少对外界反馈的依赖。",
            "category": "综合"
    },
    {
            "id": "F041",
            "feature": "宽鼻+短下庭",
            "feature_key": "综合",
            "condition": "nose_width>0.25 & lowerface_ratio<0.33",
            "traditional": "《冰鉴》云：鼻宽而短，下庭方，主性直而刚，敢作敢为。",
            "modern": "宽鼻与外向性（E）高相关，短下庭与尽责性（C）高相关，组合暗示务实且果断，类似MBTI中的ESTP。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "高",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESTP",
                    "ESFJ"
            ],
            "strength": "行动力强，善于解决实际问题，适应力好",
            "risk": "冲动行事，缺乏长远规划，易忽略情感",
            "advice": "在行动前写下三个潜在后果；每周花30分钟做长期目标复盘，平衡短期与长期利益。",
            "category": "综合"
    },
    {
            "id": "F042",
            "feature": "中等鼻+长下庭",
            "feature_key": "综合",
            "condition": "nose_width>=0.25 & nose_width<=0.25 & lowerface_ratio>0.33",
            "traditional": "《神相全编》云：鼻正而长，下庭秀，主智谋深远，德才兼备。",
            "modern": "中等鼻与宜人性（A）中相关，长下庭与开放性（O）高相关，组合暗示平衡且深思，类似MBTI中的INFJ。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "低",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "INFJ",
                    "INTJ"
            ],
            "strength": "洞察力强，善于策划，富有同理心",
            "risk": "过度内省，易陷入完美主义，社交退缩",
            "advice": "设定截止日期，强制输出成果，避免无休止修改；每周参加一次小型社交活动，练习表达观点。",
            "category": "综合"
    },
    {
            "id": "F043",
            "feature": "中等鼻+短下庭",
            "feature_key": "综合",
            "condition": "nose_width>=0.25 & nose_width<=0.25 & lowerface_ratio<0.33",
            "traditional": "《麻衣相法》云：鼻匀而短，下庭圆，主性稳而实，安分守己。",
            "modern": "中等鼻与宜人性（A）中相关，短下庭与尽责性（C）高相关，组合暗示稳定且可靠，类似MBTI中的ISFJ。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ISTJ"
            ],
            "strength": "责任心强，细致耐心，值得信赖",
            "risk": "缺乏创新，抗拒变化，易被琐事束缚",
            "advice": "每月尝试一项新活动（如新菜谱或新路线），打破惯性；定期审视工作流程，主动提出改进建议。",
            "category": "综合"
    },
    {
            "id": "F044",
            "feature": "长脸+高额头",
            "feature_key": "综合",
            "condition": "face_ratio>=1.3,forehead_ratio>=0.38",
            "traditional": "《神相全编》云：面长额广，志高气傲，智谋深远。",
            "modern": "长脸与高额头组合，结合了开放性（O）高和尽责性（C）中等的特质，类似MBTI中的直觉型（N）和思考型（T），思维活跃且目标明确。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTJ"
            ],
            "strength": "战略思维强，善于规划长远目标，执行力高",
            "risk": "易显孤傲，忽视他人情感，人际关系疏离",
            "advice": "多参与团队活动，主动倾听他人意见；每周安排一次社交时间，练习共情表达。",
            "category": "综合"
    },
    {
            "id": "F045",
            "feature": "长脸+窄额头",
            "feature_key": "综合",
            "condition": "face_ratio>=1.3,forehead_ratio<0.38",
            "traditional": "《麻衣相法》云：面长额窄，性刚多虑，劳心费力。",
            "modern": "长脸与窄额头组合，显示尽责性（C）高但开放性（O）低，类似MBTI中的判断型（J）和实感型（S），注重细节和秩序。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "踏实稳重，执行力强，善于处理具体事务",
            "risk": "思维僵化，缺乏创新，易因小事焦虑",
            "advice": "定期学习新技能或阅读跨领域书籍，打破思维定势；每天留出15分钟冥想放松。",
            "category": "综合"
    },
    {
            "id": "F046",
            "feature": "圆脸+高额头",
            "feature_key": "综合",
            "condition": "face_ratio<1.1,forehead_ratio>=0.38",
            "traditional": "《柳庄相法》云：面圆额广，心宽体胖，福禄双全。",
            "modern": "圆脸与高额头组合，宜人性（A）高且开放性（O）高，类似MBTI中的情感型（F）和直觉型（N），亲和力强且富有想象力。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP",
                    "INFP"
            ],
            "strength": "社交能力强，创意丰富，能带动团队氛围",
            "risk": "易冲动，缺乏持久性，计划常半途而废",
            "advice": "使用任务管理工具（如Trello）跟踪进度；设定短期奖励机制，每完成一个小目标给自己奖励。",
            "category": "综合"
    },
    {
            "id": "F047",
            "feature": "圆脸+窄额头",
            "feature_key": "综合",
            "condition": "face_ratio<1.1,forehead_ratio<0.38",
            "traditional": "《冰鉴》云：面圆额窄，性缓多疑，守成有余。",
            "modern": "圆脸与窄额头组合，宜人性（A）高但开放性（O）低，类似MBTI中的情感型（F）和实感型（S），温和保守，注重安全感。",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "低",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "体贴可靠，善于维护人际关系，执行力稳定",
            "risk": "缺乏冒险精神，易安于现状，错失机会",
            "advice": "每月尝试一项新体验（如新餐厅或新爱好）；与冒险型朋友合作项目，学习其决策方式。",
            "category": "综合"
    },
    {
            "id": "F048",
            "feature": "中等面型+高额头",
            "feature_key": "综合",
            "condition": "face_ratio>=1.1 and <1.3,forehead_ratio>=0.38",
            "traditional": "《神相全编》云：面方额广，智勇双全，贵不可言。",
            "modern": "中等面型与高额头组合，平衡了开放性（O）高和尽责性（C）中高，类似MBTI中的直觉型（N）和思考型（T），兼具创造力和理性。",
            "ocean": {
                    "O": "高",
                    "C": "中高",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTP"
            ],
            "strength": "思维灵活，适应力强，能平衡理想与现实",
            "risk": "易分心，目标不够专注，决策时犹豫不决",
            "advice": "设定明确优先级，使用番茄工作法提升专注力；每周复盘目标进展，调整策略。",
            "category": "综合"
    },
    {
            "id": "F049",
            "feature": "中等面型+窄额头",
            "feature_key": "综合",
            "condition": "face_ratio>=1.1 and <1.3,forehead_ratio<0.38",
            "traditional": "《麻衣相法》云：面方额窄，劳碌奔波，晚景方成。",
            "modern": "中等面型与窄额头组合，尽责性（C）高但开放性（O）低，类似MBTI中的判断型（J）和实感型（S），务实且注重传统。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTP"
            ],
            "strength": "执行力强，注重细节，能稳定推进项目",
            "risk": "缺乏远见，易陷入琐事，忽略大局",
            "advice": "定期进行战略规划会议，设定季度目标；授权他人处理细节，专注于核心任务。",
            "category": "综合"
    },
    {
            "id": "F050",
            "feature": "鼻梁高挺且下颌分明（鼻高+下颌棱角清晰）",
            "feature_key": "综合",
            "condition": ">=0.45",
            "traditional": "《神相全编》云：鼻为财星，高隆有势，主贵；下颌为地阁，方厚主权威。",
            "modern": "鼻高与下颌分明对应OCEAN中的尽责性（C）和支配性（E），类似MBTI中的ESTJ/ENTJ类型，体现领导潜质。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "高",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESTJ",
                    "ENTJ"
            ],
            "strength": "决策果断，能凝聚团队，推动项目落地",
            "risk": "易刚愎自用，忽视他人意见",
            "advice": "在团队决策中主动征求反对意见，每周安排15分钟倾听下属反馈；培养授权意识，避免事必躬亲。",
            "category": "中庭"
    },
    {
            "id": "F051",
            "feature": "高额头且宽眼距（额高而阔+眼距宽）",
            "feature_key": "forehead_ratio",
            "condition": ">=0.38",
            "traditional": "《麻衣相法》云：额高而阔，主聪明豁达；眼距宽者，心胸开阔，善谋略。",
            "modern": "高额头与宽眼距与开放性（O）高度相关，代表发散思维和想象力，类似MBTI中的ENFP/INTP类型。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP",
                    "INTP"
            ],
            "strength": "创意丰富，善于跨界联想，提出新颖方案",
            "risk": "易缺乏细节执行力，想法多但落地少",
            "advice": "使用思维导图将创意结构化，设定每日小目标推进；与执行型同事组队，互补短板。",
            "category": "上庭"
    },
    {
            "id": "F052",
            "feature": "窄额头且专注眼（额窄+眼神集中）",
            "feature_key": "forehead_ratio",
            "condition": "<0.30",
            "traditional": "《冰鉴》云：额窄者，性急而专；眼神聚而不散，主专注。",
            "modern": "窄额头与专注眼对应尽责性（C）高和开放性（O）低，类似MBTI中的ISTJ/ESTJ类型，适合执行角色。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "执行力强，注重细节，能高效完成任务",
            "risk": "易陷入重复性工作，缺乏创新视角",
            "advice": "每周抽1小时学习行业新趋势，尝试用新工具优化流程；主动参与头脑风暴会议，拓展思维边界。",
            "category": "上庭"
    },
    {
            "id": "F053",
            "feature": "宽鼻且圆下巴（鼻翼宽+下巴圆润）",
            "feature_key": "综合",
            "condition": ">=0.35",
            "traditional": "《柳庄相法》云：鼻宽主聚财，下巴圆润主亲和，善交际。",
            "modern": "宽鼻与圆下巴对应宜人性（A）高和外向性（E）中高，类似MBTI中的ESFJ/ENFJ类型，社交能力强。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ENFJ"
            ],
            "strength": "人脉广泛，善于协调关系，促进团队合作",
            "risk": "易过度迎合他人，忽视自身需求",
            "advice": "在社交中设定边界，学会说‘不’；利用人脉资源为团队引入外部合作，但避免过度承诺。",
            "category": "中庭"
    },
    {
            "id": "F054",
            "feature": "窄鼻且窄眼距（鼻梁窄+眼距窄）",
            "feature_key": "综合",
            "condition": "<0.25",
            "traditional": "《神相全编》云：鼻窄主精算，眼距窄主洞察，善分析。",
            "modern": "窄鼻与窄眼距对应尽责性（C）高和开放性（O）低，类似MBTI中的INTJ/ISTP类型，分析能力突出。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "ISTP"
            ],
            "strength": "逻辑严密，善于数据分析和问题拆解",
            "risk": "易过度批判，缺乏同理心",
            "advice": "在分析报告中加入人性化视角，如用户痛点；定期与创意型同事交流，平衡理性与感性。",
            "category": "中庭"
    },
    {
            "id": "F055",
            "feature": "高额头且锐下颌（额高+下颌尖削）",
            "feature_key": "forehead_ratio",
            "condition": ">=0.38",
            "traditional": "《麻衣相法》云：额高主智，下颌尖主锐气，主创业之才。",
            "modern": "高额头与锐下颌对应开放性（O）高和尽责性（C）中高，类似MBTI中的ENTP/INTJ类型，适合创业。",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTP",
                    "INTJ"
            ],
            "strength": "敢于冒险，善于抓住机会，快速迭代方案",
            "risk": "易冲动决策，忽视风险管控",
            "advice": "创业前做SWOT分析，制定3个月试错计划；组建互补团队，引入稳健型合伙人平衡风险。",
            "category": "上庭"
    },
    {
            "id": "F056",
            "feature": "宽鼻+圆下巴",
            "feature_key": "综合",
            "condition": "nose_width>0.35 && chin_roundness>0.6",
            "traditional": "《麻衣相法》云：鼻宽有肉，心慈好施；下巴圆厚，晚景安享。",
            "modern": "宽鼻与圆下巴组合在心理学中与宜人性（A）高度相关，代表包容、温和，类似MBTI中的情感型（F）。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "情感包容力强，善于化解矛盾，营造和谐氛围",
            "risk": "过度忍让可能导致自我压抑，忽视自身需求",
            "advice": "在亲密关系中定期表达真实感受，避免一味迁就；与伴侣约定每周一次坦诚对话，平衡付出与索取。",
            "category": "中庭"
    },
    {
            "id": "F057",
            "feature": "窄鼻+窄眼距",
            "feature_key": "综合",
            "condition": "nose_width<0.28 && eye_distance<0.22",
            "traditional": "《柳庄相法》云：鼻梁细窄，心性刚直；眼距窄小，机谋深算。",
            "modern": "窄鼻与窄眼距组合与尽责性（C）高度相关，代表理性、谨慎，类似MBTI中的思考型（T）。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ",
                    "INTJ"
            ],
            "strength": "决策理性，善于规划关系中的长期目标",
            "risk": "情感表达不足，易让伴侣感到疏离或冷漠",
            "advice": "主动练习情感表达，如每天分享一个内心感受；在争执时先冷静再沟通，避免用逻辑压制对方情绪。",
            "category": "中庭"
    },
    {
            "id": "F058",
            "feature": "高额头+上扬眉",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38 && eyebrow_angle>15",
            "traditional": "《冰鉴》云：额高眉扬，志气凌云，情思飞扬。",
            "modern": "高额头与上扬眉组合与开放性（O）高度相关，代表浪漫、想象力丰富，类似MBTI中的直觉型（N）。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP",
                    "INFP"
            ],
            "strength": "富有创意，能为关系注入新鲜感和浪漫惊喜",
            "risk": "理想化伴侣，易因现实落差感到失望",
            "advice": "将浪漫幻想转化为具体行动，如计划每月一次小冒险；与伴侣共同制定关系愿景，但接受不完美。",
            "category": "上庭"
    },
    {
            "id": "F059",
            "feature": "窄额头+平和眉",
            "feature_key": "综合",
            "condition": "forehead_ratio<0.32 && eyebrow_angle<5",
            "traditional": "《神相全编》云：额窄眉平，性稳务实，不尚虚华。",
            "modern": "窄额头与平和眉组合与尽责性（C）和宜人性（A）平衡相关，代表务实、稳定，类似MBTI中的感觉型（S）。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "注重实际，善于处理日常琐事，提供稳定支持",
            "risk": "缺乏浪漫表达，可能让关系变得单调乏味",
            "advice": "每周安排一次非日常活动，如尝试新餐厅或短途旅行；用行动表达爱意，如主动分担家务或准备小惊喜。",
            "category": "上庭"
    },
    {
            "id": "F060",
            "feature": "锐下颌+宽眼距",
            "feature_key": "综合",
            "condition": "chin_angle<100 && eye_distance>0.25",
            "traditional": "《麻衣相法》云：下颌尖削，性急好胜；眼距宽阔，心胸豁达。",
            "modern": "锐下颌与宽眼距组合与外向性（E）高度相关，代表主动、果断，类似MBTI中的判断型（J）。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTP"
            ],
            "strength": "行动力强，善于主导关系方向，推动问题解决",
            "risk": "控制欲强，易忽略伴侣意见，引发权力斗争",
            "advice": "在决策前主动征求伴侣意见，采用轮流主导模式；练习倾听技巧，避免打断对方，确保双方需求被平等考虑。",
            "category": "下庭"
    },
    {
            "id": "F061",
            "feature": "圆下颌+窄眼距",
            "feature_key": "综合",
            "condition": "chin_roundness>0.6 && eye_distance<0.22",
            "traditional": "《柳庄相法》云：下巴圆润，性柔善守；眼距窄小，心思细腻。",
            "modern": "圆下颌与窄眼距组合与神经质（N）低相关，代表被动、温和，类似MBTI中的感知型（P）。",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFP",
                    "INFP"
            ],
            "strength": "温柔体贴，善于感知伴侣情绪，营造安全感",
            "risk": "过于被动，易在关系中失去自我或依赖对方",
            "advice": "主动表达个人需求，如每周提出一个想共同完成的活动；培养独立兴趣，保持适度个人空间，避免过度依附。",
            "category": "下庭"
    },
    {
            "id": "F062",
            "feature": "圆下巴+宽鼻",
            "feature_key": "综合",
            "condition": "chin_roundness>0.7 && nose_width>0.6",
            "traditional": "《柳庄相法》云：下巴圆润如满月，鼻头宽大似悬胆，主安逸享乐，易安于现状。",
            "modern": "圆下巴与宜人性（A）相关，宽鼻与开放性（O）低相关，组合暗示依赖舒适区，缺乏冒险精神。",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "亲和力强，善于维护人际关系",
            "risk": "过度依赖熟悉环境，抗拒变化",
            "advice": "每周尝试一项新活动（如学习新技能或参加陌生社交场合）；设定小目标挑战日常习惯，如改变通勤路线。",
            "category": "下庭"
    },
    {
            "id": "F063",
            "feature": "窄鼻+上扬眉",
            "feature_key": "综合",
            "condition": "nose_width<0.4 && eyebrow_angle>0.6",
            "traditional": "《神相全编》曰：鼻梁窄细如剑脊，眉扬似新月，主心性怯弱，易自卑。",
            "modern": "窄鼻与神经质（N）高相关，上扬眉与外向性（E）低相关，组合暗示自我怀疑，缺乏自信。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "低",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "INFP",
                    "INFJ"
            ],
            "strength": "敏感细腻，善于内省",
            "risk": "易陷入自我否定，行动力不足",
            "advice": "每天记录三件小成就（如完成工作或帮助他人）；练习正面肯定语，如“我有能力应对挑战”。",
            "category": "眉眼"
    },
    {
            "id": "F064",
            "feature": "下垂眉+窄眼距",
            "feature_key": "综合",
            "condition": "eyebrow_angle<0.3 && eye_distance<0.35",
            "traditional": "《麻衣相法》云：眉垂如柳，眼距窄如豆，主心绪郁结，易怒难平。",
            "modern": "下垂眉与情绪稳定性（N）高相关，窄眼距与宜人性（A）低相关，组合暗示情绪易波动，缺乏调节能力。",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "专注细节，执行力强",
            "risk": "情绪积压易爆发，影响人际关系",
            "advice": "练习深呼吸或冥想，每天10分钟；当感到愤怒时，暂停行动并写下情绪来源，再寻求理性解决。",
            "category": "眉眼"
    },
    {
            "id": "F065",
            "feature": "窄额头+中等鼻",
            "feature_key": "综合",
            "condition": "forehead_ratio<0.3 && nose_width>=0.4 && nose_width<=0.6",
            "traditional": "《冰鉴》云：额窄如刀削，鼻正不偏，主心性急躁，难聚神。",
            "modern": "窄额头与开放性（O）低相关，中等鼻与尽责性（C）中相关，组合暗示注意力易分散，缺乏专注力。",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTP",
                    "ESTP"
            ],
            "strength": "动手能力强，善于解决实际问题",
            "risk": "易被外界干扰，难以持续专注",
            "advice": "使用番茄工作法（25分钟专注+5分钟休息）；减少多任务处理，每次只做一件事。",
            "category": "上庭"
    },
    {
            "id": "F066",
            "feature": "宽眼距+圆下巴",
            "feature_key": "综合",
            "condition": "eye_distance>0.6 && chin_roundness>0.7",
            "traditional": "《柳庄相法》云：眼距宽如日月，下巴圆似珠，主性温和，喜独处。",
            "modern": "宽眼距与开放性（O）高相关，圆下巴与宜人性（A）高相关，组合暗示内向倾向，社交意愿低。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTP",
                    "INTJ"
            ],
            "strength": "思维开阔，善于深度思考",
            "risk": "社交圈狭窄，缺乏人际支持",
            "advice": "每周参加一次社交活动（如兴趣小组或线上讨论）；主动与同事或朋友约饭，练习开放性问题。",
            "category": "五官"
    },
    {
            "id": "F067",
            "feature": "锐下颌+中等额头",
            "feature_key": "综合",
            "condition": "jaw_angularity>0.7 && forehead_ratio>=0.3 && forehead_ratio<=0.38",
            "traditional": "《神相全编》云：下颌尖削如刀，额中正不偏，主志高气傲，易半途而废。",
            "modern": "锐下颌与尽责性（C）高相关，中等额头与开放性（O）中相关，组合暗示目标明确但缺乏持久力。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTJ"
            ],
            "strength": "领导力强，善于制定计划",
            "risk": "易因挫折放弃，缺乏韧性",
            "advice": "将大目标分解为每周可量化的小里程碑；建立奖励机制，每完成一个阶段给自己小奖励。",
            "category": "下庭"
    },
    {
            "id": "F068",
            "feature": "上扬眉+宽额头",
            "feature_key": "综合",
            "condition": "brow_angle>15° & forehead_ratio>=0.38",
            "traditional": "《神相全编》云：眉扬额阔，志气凌云，主早年得志。",
            "modern": "上扬眉象征自信与进取心，宽额头代表高开放性（O），两者结合形成‘主动探索型’人格，类似MBTI中的ENTJ。心理学上，眉眼配合影响第一印象：上扬眉+宽额传递权威感，易激发他人信任或竞争意识。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTJ"
            ],
            "strength": "目标明确，行动力强，善于在复杂环境中快速决策",
            "risk": "易显强势，忽视他人感受，导致人际关系紧张",
            "advice": "在表达观点前先倾听3秒，用‘我们’代替‘我’来软化语气；每周安排一次非任务性社交，练习共情。",
            "category": "眉眼"
    },
    {
            "id": "F069",
            "feature": "上扬眉+窄额头",
            "feature_key": "综合",
            "condition": "brow_angle>15° & forehead_ratio<0.38",
            "traditional": "《柳庄相法》云：眉高额窄，性刚而急，虽有小成，难成大业。",
            "modern": "上扬眉的进取心与窄额头的低开放性（O）产生矛盾，形成‘固执型奋斗者’人格，类似MBTI中的ISTJ。心理学上，眉眼配合揭示内在冲突：上扬眉驱动行动，窄额限制视野，易陷入‘努力但方向错误’的循环。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTP"
            ],
            "strength": "执行力强，专注细节，能在有限资源下完成任务",
            "risk": "视野狭窄，易因固执错失机会，或过度消耗精力",
            "advice": "每季度设定一个‘反向目标’（尝试与习惯相反的方法）；与宽额头朋友定期交流，拓展思维边界。",
            "category": "眉眼"
    },
    {
            "id": "F070",
            "feature": "下垂眉+圆下巴",
            "feature_key": "综合",
            "condition": "brow_angle<0° & chin_roundness>0.7",
            "traditional": "《麻衣相法》云：眉垂颐圆，心慈性缓，多福寿之相。",
            "modern": "下垂眉暗示低攻击性、高宜人性（A），圆下巴代表亲和力与稳定性，两者结合形成‘温暖守护型’人格，类似MBTI中的ISFJ。心理学上，眉眼与下巴的配合强化‘安全信号’：下垂眉引发同情，圆下巴增强信任感，适合支持性角色。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "善解人意，团队粘合剂，能营造和谐氛围",
            "risk": "过度迁就他人，压抑自我需求，易被利用",
            "advice": "学会说‘不’并设定边界，每天记录一次自己的需求；在重要决策前，先独立列出利弊再征求他人意见。",
            "category": "眉眼"
    },
    {
            "id": "F071",
            "feature": "平和眉+宽眼距",
            "feature_key": "综合",
            "condition": "-5°<=brow_angle<=5° & eye_distance_ratio>=0.5",
            "traditional": "《冰鉴》云：眉平目阔，气度从容，主胸襟开阔。",
            "modern": "平和眉代表情绪稳定、低神经质（N），宽眼距象征高开放性（O）与全局思维，两者结合形成‘冷静观察型’人格，类似MBTI中的INTP。心理学上，眉眼配合影响认知风格：平和眉减少情绪干扰，宽眼距增强空间感知，适合分析性工作。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTP",
                    "INTJ"
            ],
            "strength": "理性客观，善于从多角度分析问题，决策冷静",
            "risk": "情感表达不足，易被误解为冷漠或疏离",
            "advice": "在讨论中主动分享个人感受（如‘这让我想到…’），每周参加一次需要情感投入的活动（如观影后交流）。",
            "category": "眉眼"
    },
    {
            "id": "F072",
            "feature": "上扬眉+窄眼距",
            "feature_key": "综合",
            "condition": "brow_angle>15° & eye_distance_ratio<0.5",
            "traditional": "《神相全编》云：眉扬目聚，志锐心窄，主争强好胜。",
            "modern": "上扬眉的高进取心与窄眼距的低开放性（O）及高尽责性（C）结合，形成‘竞争聚焦型’人格，类似MBTI中的ESTJ。心理学上，眉眼配合揭示专注与攻击性：窄眼距增强细节聚焦，上扬眉驱动竞争行为，易在高压环境中脱颖而出。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESTJ",
                    "ENTJ"
            ],
            "strength": "目标专注，效率极高，能在竞争中快速突破",
            "risk": "易陷入零和思维，忽视合作价值，导致人际孤立",
            "advice": "在竞争场景中主动寻找共赢点，每周参与一次团队协作任务；练习用‘你的观点很有价值’开头回应他人。",
            "category": "眉眼"
    },
    {
            "id": "F073",
            "feature": "下垂眉+宽鼻",
            "feature_key": "综合",
            "condition": "brow_angle<0° & nasal_width_ratio>=0.35",
            "traditional": "《柳庄相法》云：眉垂鼻阔，性厚而缓，主晚运亨通。",
            "modern": "下垂眉的低攻击性与宽鼻的务实性（高尽责性C）结合，形成‘稳健实干型’人格，类似MBTI中的ISTJ。心理学上，眉眼与鼻的配合影响决策风格：下垂眉减少冲动，宽鼻增强现实感，适合长期积累型工作。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ISFJ"
            ],
            "strength": "踏实可靠，执行力持久，能稳步推进长期项目",
            "risk": "过于保守，抗拒变化，可能错失创新机会",
            "advice": "每月尝试一个微小改变（如新路线通勤），逐步适应不确定性；与高开放性（O）的朋友结对，定期交换新想法。",
            "category": "眉眼"
    },
    {
            "id": "F074",
            "feature": "长脸且额头高（面长>=1.15，额高>=0.38）",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《神相全编》云：面长额高，智谋超群，然孤高难近。",
            "modern": "长脸与高额头组合，对应高开放性（O）与低宜人性（A），类似MBTI中的INTJ类型，思维独立且目标导向。",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTJ"
            ],
            "strength": "战略规划能力强，善于长期布局",
            "risk": "社交中易显冷漠，缺乏情感共鸣",
            "advice": "主动参与团队活动，练习倾听他人意见；每周安排一次非正式社交，培养亲和力。",
            "category": "面型"
    },
    {
            "id": "F075",
            "feature": "长脸且鼻梁高挺（面长>=1.15，鼻梁高度>=0.25）",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《冰鉴》云：面长鼻耸，志气凌云，然刚愎自用。",
            "modern": "长脸与高鼻梁组合，对应高尽责性（C）与高神经质（N），类似MBTI中的ISTJ类型，注重细节但易焦虑。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "执行力强，能高效完成任务",
            "risk": "过度追求完美，易因小失误自责",
            "advice": "设定合理目标，接受80%的完成度；每日进行5分钟冥想，缓解焦虑情绪。",
            "category": "面型"
    },
    {
            "id": "F076",
            "feature": "长脸且下巴尖削（面长>=1.15，下巴宽度<=0.12）",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《麻衣相法》云：面长颐削，心机深沉，多疑寡合。",
            "modern": "长脸与尖下巴组合，对应低宜人性（A）与高开放性（O），类似MBTI中的INTP类型，善于分析但社交疏离。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTP",
                    "ENTP"
            ],
            "strength": "逻辑推理能力强，擅长解决复杂问题",
            "risk": "易陷入过度分析，决策犹豫不决",
            "advice": "设定决策时限，使用利弊清单快速选择；主动与不同观点者辩论，拓宽思维。",
            "category": "面型"
    },
    {
            "id": "F077",
            "feature": "圆脸且眼睛大而圆（面长<=0.89，眼宽>=0.3）",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《柳庄相法》云：面圆目大，心性纯良，乐善好施。",
            "modern": "圆脸与大眼组合，对应高外向性（E）与高宜人性（A），类似MBTI中的ESFJ类型，热情且乐于助人。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ENFJ"
            ],
            "strength": "社交能力强，善于建立人际关系",
            "risk": "易过度迎合他人，忽略自我需求",
            "advice": "学会说“不”，设定个人边界；每周留出独处时间，反思自身目标。",
            "category": "面型"
    },
    {
            "id": "F078",
            "feature": "圆脸且嘴唇厚实（面长<=0.89，唇厚>=0.08）",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《神相全编》云：面圆唇厚，福泽深厚，性情温和。",
            "modern": "圆脸与厚唇组合，对应高宜人性（A）与低神经质（N），类似MBTI中的ISFJ类型，温柔且稳定。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "耐心细致，善于照顾他人情绪",
            "risk": "易缺乏主见，过度依赖他人意见",
            "advice": "培养独立决策能力，从小事开始练习；尝试新爱好，增强自我认知。",
            "category": "面型"
    },
    {
            "id": "F079",
            "feature": "圆脸且颧骨突出（面长<=0.89，颧宽>=0.35）",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《冰鉴》云：面圆颧露，刚毅果决，然易招是非。",
            "modern": "圆脸与高颧骨组合，对应高外向性（E）与高神经质（N），类似MBTI中的ESTP类型，行动力强但冲动。",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "高",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "ESTP",
                    "ENTP"
            ],
            "strength": "反应敏捷，善于抓住机会",
            "risk": "易冲动行事，缺乏长期规划",
            "advice": "行动前先列出利弊清单，延迟24小时做决定；培养记账习惯，控制消费冲动。",
            "category": "面型"
    },
    {
            "id": "F080",
            "feature": "高额宽眼锐颌",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38, eye_distance>=0.5, jaw_angle<90",
            "traditional": "《麻衣相法》云：额高而阔，主贵寿；目距宽者，心宽志远；下颌尖削，性急易争。",
            "modern": "高额头与开放性(O)高度相关，宽眼距与宜人性(A)正相关，锐颌与尽责性(C)负相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFP",
                    "ENTP"
            ],
            "strength": "善规划且包容",
            "risk": "易理想化且冲动",
            "advice": "分解目标执行，每周复盘一次决策记录",
            "category": "综合"
    },
    {
            "id": "F081",
            "feature": "高额窄眼圆颌",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38, eye_distance<0.45, jaw_angle>=120",
            "traditional": "《神相全编》载：额高目窄，智深而心细；颐圆如覆，性缓而福厚。",
            "modern": "高额头与开放性(O)高度相关，窄眼距与尽责性(C)正相关，圆颌与宜人性(A)正相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "ISTJ"
            ],
            "strength": "善规划且稳重",
            "risk": "易固执且社交疏离",
            "advice": "每周安排一次非工作社交活动，练习主动倾听",
            "category": "综合"
    },
    {
            "id": "F082",
            "feature": "窄额宽眼锐颌",
            "feature_key": "综合",
            "condition": "forehead_ratio<0.32, eye_distance>=0.5, jaw_angle<90",
            "traditional": "《相理衡真》云：额窄者，早年多劳；目宽者，胸襟豁达；颐锐者，晚年多争。",
            "modern": "窄额头与尽责性(C)负相关，宽眼距与宜人性(A)正相关，锐颌与神经质(N)正相关",
            "ocean": {
                    "O": "低",
                    "C": "低",
                    "E": "中",
                    "A": "高",
                    "N": "高"
            },
            "mbti_hint": [
                    "ESFP",
                    "ISFP"
            ],
            "strength": "善社交且灵活",
            "risk": "易冲动且缺乏规划",
            "advice": "使用番茄工作法管理时间，每日列三件优先事项",
            "category": "综合"
    },
    {
            "id": "F083",
            "feature": "窄额窄眼圆颌",
            "feature_key": "综合",
            "condition": "forehead_ratio<0.32, eye_distance<0.45, jaw_angle>=120",
            "traditional": "《冰鉴》有言：额窄目聚，心机深重；颐圆如珠，福泽绵长。",
            "modern": "窄额头与开放性(O)负相关，窄眼距与尽责性(C)正相关，圆颌与宜人性(A)正相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ISFJ"
            ],
            "strength": "善执行且可靠",
            "risk": "易保守且缺乏创新",
            "advice": "每月尝试一项新技能或爱好，拓宽思维边界",
            "category": "综合"
    },
    {
            "id": "F084",
            "feature": "高额宽眼圆颌",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38, eye_distance>=0.5, jaw_angle>=120",
            "traditional": "《麻衣相法》曰：额高目阔，智广心宽；颐圆如月，福寿双全。",
            "modern": "高额头与开放性(O)高度相关，宽眼距与宜人性(A)正相关，圆颌与尽责性(C)正相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFJ",
                    "INFJ"
            ],
            "strength": "善规划且亲和",
            "risk": "易过度理想化",
            "advice": "设定SMART目标，每季度评估一次实际进展",
            "category": "综合"
    },
    {
            "id": "F085",
            "feature": "窄额宽眼圆颌",
            "feature_key": "综合",
            "condition": "forehead_ratio<0.32, eye_distance>=0.5, jaw_angle>=120",
            "traditional": "《相法指南》载：额窄目宽，早年奔波而晚景安；颐圆者，性善而福厚。",
            "modern": "窄额头与开放性(O)负相关，宽眼距与宜人性(A)正相关，圆颌与尽责性(C)正相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ISFJ"
            ],
            "strength": "善社交且务实",
            "risk": "易依赖他人意见",
            "advice": "培养独立决策能力，每日记录一次自主选择",
            "category": "综合"
    },
    {
            "id": "F086",
            "feature": "中额中眼中颌",
            "feature_key": "综合",
            "condition": "0.32<=forehead_ratio<0.38, 0.45<=eye_distance<0.5, 90<=jaw_angle<120",
            "traditional": "《人伦大统赋》云：三停匀称，五岳朝拱，乃中和之相，主一生平顺。",
            "modern": "中等额头与开放性(O)中等相关，中等眼距与宜人性(A)中等相关，中颌与尽责性(C)中等相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTP",
                    "ESTP"
            ],
            "strength": "适应性强且平衡",
            "risk": "易缺乏鲜明特质",
            "advice": "发掘一项核心优势并深耕，建立个人品牌",
            "category": "综合"
    },
    {
            "id": "F087",
            "feature": "高额窄眼锐颌",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38, eye_distance<0.45, jaw_angle<90",
            "traditional": "《神相全编》曰：额高目聚，智谋超群；颐尖如锥，性刚易折。",
            "modern": "高额头与开放性(O)高度相关，窄眼距与尽责性(C)正相关，锐颌与神经质(N)正相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTJ"
            ],
            "strength": "善战略且专注",
            "risk": "易苛刻且焦虑",
            "advice": "练习正念冥想缓解压力，每周安排放松时间",
            "category": "综合"
    },
    {
            "id": "F088",
            "feature": "窄额窄眼锐颌",
            "feature_key": "综合",
            "condition": "forehead_ratio<0.32, eye_distance<0.45, jaw_angle<90",
            "traditional": "《相理衡真》云：额窄目聚，心机深而多疑；颐尖者，性急而少福。",
            "modern": "窄额头与开放性(O)负相关，窄眼距与尽责性(C)正相关，锐颌与神经质(N)正相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "INTJ"
            ],
            "strength": "善执行且坚韧",
            "risk": "易偏执且社交孤立",
            "advice": "主动寻求反馈，每周与一位信任者深度交流",
            "category": "综合"
    },
    {
            "id": "F089",
            "feature": "中额宽眼圆颌",
            "feature_key": "综合",
            "condition": "0.32<=forehead_ratio<0.38, eye_distance>=0.5, jaw_angle>=120",
            "traditional": "《麻衣相法》载：中额者，智平而性稳；目宽颐圆，主富贵双全。",
            "modern": "中等额头与开放性(O)中等相关，宽眼距与宜人性(A)正相关，圆颌与尽责性(C)正相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFJ",
                    "ESFJ"
            ],
            "strength": "善协调且可靠",
            "risk": "易忽视自我需求",
            "advice": "设定个人边界，每日保留30分钟独处时间",
            "category": "综合"
    },
    {
            "id": "F090",
            "feature": "宽眼宽鼻长脸",
            "feature_key": "综合",
            "condition": "眼距>1.0/鼻宽>0.25/脸长宽比>1.5",
            "traditional": "《相理衡真》云：目阔鼻大面长，主志大而疏，中年发迹。",
            "modern": "宽眼距与开放性(O)正相关，宽鼻与宜人性(A)负相关，长脸与尽责性(C)正相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTP",
                    "INTJ"
            ],
            "strength": "战略视野广，执行力强",
            "risk": "易忽视细节，人际冲突",
            "advice": "每周列出3个具体步骤，主动询问他人感受",
            "category": "综合"
    },
    {
            "id": "F091",
            "feature": "窄眼窄鼻圆脸",
            "feature_key": "综合",
            "condition": "眼距<0.8/鼻宽<0.2/脸长宽比<1.2",
            "traditional": "《神相全编》曰：目小鼻细面圆，性柔善守，福泽绵长。",
            "modern": "窄眼距与神经质(N)负相关，窄鼻与尽责性(C)正相关，圆脸与宜人性(A)正相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ISTJ"
            ],
            "strength": "细致可靠，善解人意",
            "risk": "抗拒变化，易被忽视",
            "advice": "每周尝试1件新事物，主动表达需求",
            "category": "综合"
    },
    {
            "id": "F092",
            "feature": "宽眼窄鼻长脸",
            "feature_key": "综合",
            "condition": "眼距>1.0/鼻宽<0.2/脸长宽比>1.5",
            "traditional": "《冰鉴》云：目阔鼻细面长，智谋深远，然多思少行。",
            "modern": "宽眼距与开放性(O)正相关，窄鼻与尽责性(C)正相关，长脸与外向性(E)负相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "INTP"
            ],
            "strength": "深度分析，规划周密",
            "risk": "社交孤立，行动迟缓",
            "advice": "设定每日社交目标，使用番茄工作法",
            "category": "综合"
    },
    {
            "id": "F093",
            "feature": "窄眼宽鼻圆脸",
            "feature_key": "综合",
            "condition": "眼距<0.8/鼻宽>0.25/脸长宽比<1.2",
            "traditional": "《麻衣相法》曰：目窄鼻阔面圆，性刚直，易得人助。",
            "modern": "窄眼距与神经质(N)负相关，宽鼻与宜人性(A)负相关，圆脸与外向性(E)正相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESTP",
                    "ESFP"
            ],
            "strength": "果断自信，社交活跃",
            "risk": "冲动决策，得罪他人",
            "advice": "重大决定前冷静24小时，练习倾听",
            "category": "综合"
    },
    {
            "id": "F094",
            "feature": "宽眼宽鼻圆脸",
            "feature_key": "综合",
            "condition": "眼距>1.0/鼻宽>0.25/脸长宽比<1.2",
            "traditional": "《相理衡真》云：目阔鼻大面圆，心宽体胖，贵人扶持。",
            "modern": "宽眼距与开放性(O)正相关，宽鼻与宜人性(A)负相关，圆脸与外向性(E)正相关",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFP",
                    "ENTP"
            ],
            "strength": "创意丰富，感染力强",
            "risk": "缺乏条理，易惹争议",
            "advice": "使用日程本规划，每日复盘言行",
            "category": "综合"
    },
    {
            "id": "F095",
            "feature": "窄眼窄鼻长脸",
            "feature_key": "综合",
            "condition": "眼距<0.8/鼻宽<0.2/脸长宽比>1.5",
            "traditional": "《神相全编》曰：目小鼻细面长，性谨严，可托大事。",
            "modern": "窄眼距与神经质(N)负相关，窄鼻与尽责性(C)正相关，长脸与开放性(O)负相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "INTJ"
            ],
            "strength": "专注可靠，执行力强",
            "risk": "思维僵化，缺乏弹性",
            "advice": "每月学习1项新技能，接受他人建议",
            "category": "综合"
    },
    {
            "id": "F096",
            "feature": "中眼中鼻中脸",
            "feature_key": "综合",
            "condition": "眼距0.8-1.0/鼻宽0.2-0.25/脸长宽比1.2-1.5",
            "traditional": "《麻衣相法》云：五官匀称，中和之相，福寿双全。",
            "modern": "中等特征与五大人格均衡相关，适应性最强",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "适应力强，人际关系和谐",
            "risk": "缺乏鲜明特色",
            "advice": "发掘1-2个核心优势深耕，定期自我挑战",
            "category": "综合"
    },
    {
            "id": "F097",
            "feature": "宽眼窄鼻圆脸",
            "feature_key": "综合",
            "condition": "眼距>1.0/鼻宽<0.2/脸长宽比<1.2",
            "traditional": "《冰鉴》曰：目阔鼻细面圆，智圆行方，贵人相。",
            "modern": "宽眼距与开放性(O)正相关，窄鼻与尽责性(C)正相关，圆脸与外向性(E)正相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFJ",
                    "ENTJ"
            ],
            "strength": "领导力强，善谋善断",
            "risk": "过度自信，忽视细节",
            "advice": "授权任务时明确标准，每日检查进度",
            "category": "综合"
    },
    {
            "id": "F098",
            "feature": "窄眼宽鼻长脸",
            "feature_key": "综合",
            "condition": "眼距<0.8/鼻宽>0.25/脸长宽比>1.5",
            "traditional": "《相理衡真》云：目窄鼻阔面长，性刚毅，中年显达。",
            "modern": "窄眼距与神经质(N)负相关，宽鼻与宜人性(A)负相关，长脸与尽责性(C)正相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTP",
                    "ESTJ"
            ],
            "strength": "务实果断，抗压能力强",
            "risk": "缺乏同理心，易冲突",
            "advice": "决策前考虑他人立场，练习非暴力沟通",
            "category": "综合"
    },
    {
            "id": "F099",
            "feature": "中眼宽鼻长脸",
            "feature_key": "综合",
            "condition": "眼距0.8-1.0/鼻宽>0.25/脸长宽比>1.5",
            "traditional": "《神相全编》曰：目正鼻阔面长，主诚信，可掌财权。",
            "modern": "中眼距与宜人性(A)正相关，宽鼻与开放性(O)正相关，长脸与尽责性(C)正相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTJ"
            ],
            "strength": "诚信可靠，战略执行兼备",
            "risk": "固执己见，压力过大",
            "advice": "每周留半天放松，接受不同意见",
            "category": "综合"
    },
    {
            "id": "F100",
            "feature": "高额宽鼻锐颌",
            "feature_key": "综合",
            "condition": ">=0.38/>=0.35/<=0.25",
            "traditional": "《麻衣相法》云：额高鼻阔，颏尖如锥，主刚强而多争。",
            "modern": "高额头与开放性(O)高相关，宽鼻与支配性(D)高相关，锐颌与尽责性(C)低相关",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTP"
            ],
            "strength": "决策果断，敢于挑战",
            "risk": "易冲动，人际冲突多",
            "advice": "每日预留10分钟冷静期，用清单法评估风险后再行动",
            "category": "综合"
    },
    {
            "id": "F101",
            "feature": "窄额窄鼻圆颌",
            "feature_key": "综合",
            "condition": "<0.38/<0.35/>=0.35",
            "traditional": "《神相全编》曰：额狭鼻小，颐圆如月，主谨慎而多虑。",
            "modern": "窄额头与开放性(O)低相关，窄鼻与宜人性(A)高相关，圆颌与神经质(N)高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ISTJ"
            ],
            "strength": "细致可靠，善守规则",
            "risk": "易焦虑，抗拒变化",
            "advice": "每周尝试一件小事打破常规，如换条路通勤，逐步适应不确定性",
            "category": "综合"
    },
    {
            "id": "F102",
            "feature": "高额窄鼻锐颌",
            "feature_key": "综合",
            "condition": ">=0.38/<0.35/<=0.25",
            "traditional": "《麻衣相法》云：额高鼻细，颏尖如锥，主智高而孤傲。",
            "modern": "高额头与开放性(O)高相关，窄鼻与宜人性(A)中相关，锐颌与尽责性(C)低相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "INTP"
            ],
            "strength": "思维深邃，擅长抽象分析",
            "risk": "易脱离实际，社交疏离",
            "advice": "每周至少一次线下交流，将理论转化为可落地的三步计划",
            "category": "综合"
    },
    {
            "id": "F103",
            "feature": "窄额宽鼻圆颌",
            "feature_key": "综合",
            "condition": "<0.38/>=0.35/>=0.35",
            "traditional": "《相理衡真》曰：额窄鼻阔，颐圆如盘，主富厚而性缓。",
            "modern": "窄额头与开放性(O)低相关，宽鼻与支配性(D)高相关，圆颌与神经质(N)高相关",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ESTJ"
            ],
            "strength": "务实高效，善于组织资源",
            "risk": "易固执，情绪波动大",
            "advice": "决策前先列出三个反对理由，用理性对冲情绪冲动",
            "category": "综合"
    },
    {
            "id": "F104",
            "feature": "高额宽鼻圆颌",
            "feature_key": "综合",
            "condition": ">=0.38/>=0.35/>=0.35",
            "traditional": "《冰鉴》云：额高鼻隆，颐圆而厚，主贵而多福。",
            "modern": "高额头与开放性(O)高相关，宽鼻与支配性(D)高相关，圆颌与神经质(N)高相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ENFP",
                    "ENTP"
            ],
            "strength": "热情开朗，感染力强",
            "risk": "易情绪化，缺乏持久力",
            "advice": "用番茄工作法分段专注，每25分钟休息5分钟，保持节奏",
            "category": "综合"
    },
    {
            "id": "F105",
            "feature": "窄额窄鼻锐颌",
            "feature_key": "综合",
            "condition": "<0.38/<0.35/<=0.25",
            "traditional": "《麻衣相法》云：额狭鼻小，颏尖如锥，主刻薄而多疑。",
            "modern": "窄额头与开放性(O)低相关，窄鼻与宜人性(A)高相关，锐颌与尽责性(C)低相关",
            "ocean": {
                    "O": "低",
                    "C": "低",
                    "E": "低",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTP",
                    "INFP"
            ],
            "strength": "独立专注，善于深度思考",
            "risk": "易自我封闭，缺乏行动力",
            "advice": "设定每日最小行动目标，如写100字或走500步，积累成就感",
            "category": "综合"
    },
    {
            "id": "F106",
            "feature": "中额中鼻中颌",
            "feature_key": "综合",
            "condition": "0.33-0.38/0.30-0.35/0.25-0.35",
            "traditional": "《相法集成》曰：三停匀称，五岳相朝，主中和之贵。",
            "modern": "中等比例与五大人格均呈中等水平，适应性最强",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "INFJ",
                    "ENFJ"
            ],
            "strength": "平衡包容，善于协调",
            "risk": "易缺乏特色，随波逐流",
            "advice": "每月设定一个突破性目标，如学习一项新技能，打破舒适区",
            "category": "综合"
    },
    {
            "id": "F107",
            "feature": "窄额宽鼻锐颌",
            "feature_key": "综合",
            "condition": "<0.38/>=0.35/<=0.25",
            "traditional": "《神相全编》曰：额窄鼻阔，颏尖如锥，主刚暴而少仁。",
            "modern": "窄额头与开放性(O)低相关，宽鼻与支配性(D)高相关，锐颌与尽责性(C)低相关",
            "ocean": {
                    "O": "低",
                    "C": "低",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESTP",
                    "ESFP"
            ],
            "strength": "行动力强，善于抓住机会",
            "risk": "易冲动，缺乏长远规划",
            "advice": "重大决定前强制等待24小时，用利弊清单辅助判断",
            "category": "综合"
    },
    {
            "id": "F108",
            "feature": "高额窄鼻圆颌",
            "feature_key": "综合",
            "condition": ">=0.38/<0.35/>=0.35",
            "traditional": "《冰鉴》云：额高鼻细，颐圆而厚，主智深而性柔。",
            "modern": "高额头与开放性(O)高相关，窄鼻与宜人性(A)高相关，圆颌与神经质(N)高相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "低",
                    "A": "高",
                    "N": "高"
            },
            "mbti_hint": [
                    "INFJ",
                    "INFP"
            ],
            "strength": "善解人意，富有创造力",
            "risk": "易过度敏感，决策犹豫",
            "advice": "用SWOT分析法快速决策，设定时间限制，避免过度纠结",
            "category": "综合"
    },
    {
            "id": "F109",
            "feature": "中额宽鼻锐颌",
            "feature_key": "综合",
            "condition": "0.33-0.38/>=0.35/<=0.25",
            "traditional": "《麻衣相法》云：额平鼻阔，颏尖如锥，主刚直而多谋。",
            "modern": "中额头与开放性(O)中相关，宽鼻与支配性(D)高相关，锐颌与尽责性(C)低相关",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTP",
                    "ESTJ"
            ],
            "strength": "灵活应变，善于谈判",
            "risk": "易缺乏耐心，虎头蛇尾",
            "advice": "将大目标拆解为周任务，每周复盘进度，及时调整策略",
            "category": "综合"
    },
    {
            "id": "F110",
            "feature": "高额长脸长下巴",
            "feature_key": "forehead_ratio",
            "condition": ">=0.38",
            "traditional": "《麻衣相法》云：额高而阔，主贵寿；面长而方，主福厚；下巴长而圆，主晚运佳。",
            "modern": "高额头与开放性(O)高度相关，长脸与尽责性(C)相关，长下巴与宜人性(A)相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "ISTJ"
            ],
            "strength": "善规划且执行力强",
            "risk": "易理想化且固执",
            "advice": "分解目标为周计划，每周复盘调整",
            "category": "上庭"
    },
    {
            "id": "F111",
            "feature": "窄额圆脸短下巴",
            "feature_key": "forehead_ratio",
            "condition": "<0.33",
            "traditional": "《神相全编》曰：额窄者，心性多疑；面圆者，性多温和；下巴短者，主早年劳碌。",
            "modern": "窄额头与开放性(O)低相关，圆脸与宜人性(A)高相关，短下巴与尽责性(C)低相关",
            "ocean": {
                    "O": "低",
                    "C": "低",
                    "E": "中",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ISFJ"
            ],
            "strength": "亲和力强，善社交",
            "risk": "易缺乏长远规划",
            "advice": "每天花15分钟写未来3个月目标清单",
            "category": "上庭"
    },
    {
            "id": "F112",
            "feature": "高额圆脸长下巴",
            "feature_key": "forehead_ratio",
            "condition": ">=0.38",
            "traditional": "《麻衣相法》云：额高而圆，主聪明；面圆而润，主福寿；下巴长而尖，主晚运亨通。",
            "modern": "高额头与开放性(O)高相关，圆脸与宜人性(A)高相关，长下巴与尽责性(C)高相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFJ",
                    "INFJ"
            ],
            "strength": "善创新且善协调",
            "risk": "易过度理想化",
            "advice": "将创意落地为具体项目，设定截止日期",
            "category": "上庭"
    },
    {
            "id": "F113",
            "feature": "窄额长脸短下巴",
            "feature_key": "forehead_ratio",
            "condition": "<0.33",
            "traditional": "《相理衡真》曰：额窄面长，主心性刚直；下巴短促，主早年多波折。",
            "modern": "窄额头与开放性(O)低相关，长脸与尽责性(C)高相关，短下巴与宜人性(A)低相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "INTJ"
            ],
            "strength": "专注且执行力强",
            "risk": "易固执且社交弱",
            "advice": "每周主动参加一次团队讨论，练习倾听",
            "category": "上庭"
    },
    {
            "id": "F114",
            "feature": "中额中脸中下巴",
            "feature_key": "forehead_ratio",
            "condition": "0.33-0.38",
            "traditional": "《麻衣相法》云：三停匀称，主一生平顺，福禄双全。",
            "modern": "中额头与开放性(O)中相关，中脸与尽责性(C)中相关，中下巴与宜人性(A)中相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "平衡稳定，适应力强",
            "risk": "易缺乏突破性",
            "advice": "每季度尝试一项新技能或爱好，保持成长",
            "category": "上庭"
    },
    {
            "id": "F115",
            "feature": "高额长脸短下巴",
            "feature_key": "forehead_ratio",
            "condition": ">=0.38",
            "traditional": "《神相全编》曰：额高面长，主智谋过人；下巴短促，主晚运稍逊。",
            "modern": "高额头与开放性(O)高相关，长脸与尽责性(C)高相关，短下巴与宜人性(A)低相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "ISTP"
            ],
            "strength": "善战略规划",
            "risk": "易忽视人际关系",
            "advice": "每天主动赞美同事或朋友一次，培养亲和力",
            "category": "上庭"
    },
    {
            "id": "F116",
            "feature": "窄额长脸长下巴",
            "feature_key": "forehead_ratio",
            "condition": "<0.33",
            "traditional": "《相理衡真》曰：额窄面长，主心性刚直；下巴长而圆，主晚运丰隆。",
            "modern": "窄额头与开放性(O)低相关，长脸与尽责性(C)高相关，长下巴与宜人性(A)高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ISFJ"
            ],
            "strength": "可靠且善坚持",
            "risk": "易保守且缺乏创新",
            "advice": "每月阅读一本跨领域书籍，拓宽视野",
            "category": "上庭"
    },
    {
            "id": "F117",
            "feature": "高额圆脸短下巴",
            "feature_key": "forehead_ratio",
            "condition": ">=0.38",
            "traditional": "《麻衣相法》云：额高而圆，主聪明；面圆而润，主福寿；下巴短促，主早年多劳。",
            "modern": "高额头与开放性(O)高相关，圆脸与宜人性(A)高相关，短下巴与尽责性(C)低相关",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFP",
                    "ESFP"
            ],
            "strength": "善创意且善社交",
            "risk": "易缺乏持久力",
            "advice": "将大任务拆解为小步骤，每完成一步奖励自己",
            "category": "上庭"
    },
    {
            "id": "F118",
            "feature": "窄额圆脸长下巴",
            "feature_key": "forehead_ratio",
            "condition": "<0.33",
            "traditional": "《神相全编》曰：额窄者，心性多疑；面圆者，性多温和；下巴长而尖，主晚运亨通。",
            "modern": "窄额头与开放性(O)低相关，圆脸与宜人性(A)高相关，长下巴与尽责性(C)高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "善协调且善执行",
            "risk": "易缺乏冒险精神",
            "advice": "每月尝试一次小冒险，如新路线通勤或新菜谱",
            "category": "上庭"
    },
    {
            "id": "F119",
            "feature": "中额长脸中下巴",
            "feature_key": "forehead_ratio",
            "condition": "0.33-0.38",
            "traditional": "《麻衣相法》云：三停匀称，主一生平顺；面长而方，主福厚。",
            "modern": "中额头与开放性(O)中相关，长脸与尽责性(C)高相关，中下巴与宜人性(A)中相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ",
                    "INTJ"
            ],
            "strength": "善分析且善执行",
            "risk": "易过于严肃",
            "advice": "每天安排15分钟放松活动，如听音乐或散步",
            "category": "上庭"
    },
    {
            "id": "F120",
            "feature": "龙眉",
            "feature_key": "综合",
            "condition": ">15度",
            "traditional": "《神相全编》云：龙眉弯秀，主贵气凌云，志在四方。",
            "modern": "上扬眉与支配性(D)高度相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTJ"
            ],
            "strength": "领导力强",
            "risk": "易刚愎自用",
            "advice": "每日记录他人建议并反思",
            "category": "眉眼"
    },
    {
            "id": "F121",
            "feature": "凤目",
            "feature_key": "eye_distance",
            "condition": ">0.45",
            "traditional": "《神相全编》云：凤目双分，主聪慧明达，福泽绵长。",
            "modern": "宽眼距与开放性(O)高度相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTP",
                    "ENFP"
            ],
            "strength": "创意丰富",
            "risk": "易分心",
            "advice": "设定每日专注时段并执行",
            "category": "眉眼"
    },
    {
            "id": "F122",
            "feature": "虎鼻",
            "feature_key": "nose_width",
            "condition": ">0.35",
            "traditional": "《神相全编》云：虎鼻丰隆，主财禄双全，威仪自生。",
            "modern": "宽鼻与尽责性(C)高度相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTP"
            ],
            "strength": "务实稳健",
            "risk": "易固执",
            "advice": "每周尝试新方法解决问题",
            "category": "五官"
    },
    {
            "id": "F123",
            "feature": "狮口",
            "feature_key": "综合",
            "condition": ">0.40",
            "traditional": "《神相全编》云：狮口阔大，主食禄丰盈，言辞有力。",
            "modern": "宽嘴区与外倾性(E)高度相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ENFJ"
            ],
            "strength": "善于社交",
            "risk": "易言多招怨",
            "advice": "说话前停顿三秒再开口",
            "category": "五官"
    },
    {
            "id": "F124",
            "feature": "象耳",
            "feature_key": "综合",
            "condition": ">0.03",
            "traditional": "《神相全编》云：象耳垂珠，主福寿绵延，贵人扶持。",
            "modern": "大耳垂与宜人性(A)高度相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "INFJ"
            ],
            "strength": "包容性强",
            "risk": "易被利用",
            "advice": "设立个人边界并明确表达",
            "category": "五官"
    },
    {
            "id": "F125",
            "feature": "鹤骨",
            "feature_key": "综合",
            "condition": ">0.25",
            "traditional": "《神相全编》云：鹤骨高耸，主权势显赫，志气超群。",
            "modern": "高颧骨与支配性(D)高度相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTP"
            ],
            "strength": "决策果断",
            "risk": "易树敌",
            "advice": "主动寻求合作而非对抗",
            "category": "中庭"
    },
    {
            "id": "F126",
            "feature": "龟背",
            "feature_key": "综合",
            "condition": ">0.35",
            "traditional": "《神相全编》云：龟背圆隆，主智慧深远，福泽如海。",
            "modern": "圆额头与开放性(O)高度相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "INFP",
                    "ENFP"
            ],
            "strength": "想象力丰富",
            "risk": "易脱离现实",
            "advice": "将创意转化为书面计划",
            "category": "上庭"
    },
    {
            "id": "F127",
            "feature": "麟角",
            "feature_key": "综合",
            "condition": ">85度",
            "traditional": "《神相全编》云：麟角方正，主贵气天成，根基稳固。",
            "modern": "方额头与尽责性(C)高度相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "执行力强",
            "risk": "易僵化",
            "advice": "每月学习一项新技能",
            "category": "上庭"
    },
    {
            "id": "F128",
            "feature": "鹰视",
            "feature_key": "eye_distance",
            "condition": "<0.35",
            "traditional": "《神相全编》云：鹰视窄聚，主机谋深沉，洞察入微。",
            "modern": "窄眼距与神经质(N)高度相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "INTJ",
                    "ISTP"
            ],
            "strength": "分析力强",
            "risk": "易多疑",
            "advice": "每日练习信任练习并记录感受",
            "category": "眉眼"
    },
    {
            "id": "F129",
            "feature": "豹颌",
            "feature_key": "综合",
            "condition": "<75度",
            "traditional": "《神相全编》云：豹颌尖削，主果敢决断，锐意进取。",
            "modern": "锐下颌与支配性(D)高度相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTP",
                    "ESTP"
            ],
            "strength": "行动迅速",
            "risk": "易冲动",
            "advice": "重大决策前咨询三人意见",
            "category": "下庭"
    },
    {
            "id": "F130",
            "feature": "宽眼距",
            "feature_key": "综合",
            "condition": ">=0.42",
            "traditional": "《相理衡真》云：目距宽者，心性豁达，不拘小节。",
            "modern": "宽眼距与开放性(O)高度正相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP",
                    "INTP"
            ],
            "strength": "思维发散，创意丰富",
            "risk": "易忽略细节，计划性弱",
            "advice": "每周制定清单，用番茄钟分段执行",
            "category": "五官"
    },
    {
            "id": "F131",
            "feature": "高额头",
            "feature_key": "forehead_ratio",
            "condition": ">=0.38",
            "traditional": "《麻衣相法》云：额高而阔，主贵寿。",
            "modern": "高额头与开放性(O)高度正相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ"
            ],
            "strength": "善规划，抽象思维强",
            "risk": "易理想化，脱离实际",
            "advice": "分解目标为季度里程碑，定期复盘",
            "category": "上庭"
    },
    {
            "id": "F132",
            "feature": "窄眼距",
            "feature_key": "综合",
            "condition": "<0.38",
            "traditional": "《神相全编》曰：目近者，性急而专。",
            "modern": "窄眼距与开放性(O)低度相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ"
            ],
            "strength": "专注细节，执行力强",
            "risk": "思维固化，抗拒变化",
            "advice": "每月尝试一项新技能或新路线",
            "category": "五官"
    },
    {
            "id": "F133",
            "feature": "窄额头",
            "feature_key": "forehead_ratio",
            "condition": "<0.32",
            "traditional": "《玉管照神局》云：额窄者，多务实，少虚浮。",
            "modern": "窄额头与开放性(O)低度相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESTJ"
            ],
            "strength": "务实可靠，善于执行",
            "risk": "缺乏远见，易固执",
            "advice": "每周阅读行业报告，拓展认知边界",
            "category": "上庭"
    },
    {
            "id": "F134",
            "feature": "窄鼻",
            "feature_key": "综合",
            "condition": "<0.28",
            "traditional": "《相法捷要》曰：鼻狭者，性刚而自律。",
            "modern": "窄鼻与尽责性(C)高度正相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ",
                    "INTJ"
            ],
            "strength": "自律严谨，目标导向",
            "risk": "易苛求完美，人际疏离",
            "advice": "设定容错率，每周留半天放松社交",
            "category": "中庭"
    },
    {
            "id": "F135",
            "feature": "锐颌",
            "feature_key": "jaw_angle",
            "condition": "<90°",
            "traditional": "《人伦大统赋》云：颌尖者，志坚而果决。",
            "modern": "锐颌与尽责性(C)高度正相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTJ"
            ],
            "strength": "决策果断，领导力强",
            "risk": "易强势，缺乏同理心",
            "advice": "决策前先倾听三人意见，再拍板",
            "category": "下庭"
    },
    {
            "id": "F136",
            "feature": "宽鼻",
            "feature_key": "综合",
            "condition": ">=0.32",
            "traditional": "《冰鉴》云：鼻宽者，心宽体胖，随遇而安。",
            "modern": "宽鼻与尽责性(C)低度相关",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFP"
            ],
            "strength": "随和灵活，适应力强",
            "risk": "易拖延，缺乏条理",
            "advice": "用日历提醒每日三件要事，优先完成",
            "category": "中庭"
    },
    {
            "id": "F137",
            "feature": "圆颌",
            "feature_key": "jaw_angle",
            "condition": ">=120°",
            "traditional": "《相理衡真》曰：颌圆者，性缓而乐天。",
            "modern": "圆颌与尽责性(C)低度相关",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFP"
            ],
            "strength": "亲和力强，善于合作",
            "risk": "易随波逐流，缺乏主见",
            "advice": "每日写决策日志，强化自主判断",
            "category": "下庭"
    },
    {
            "id": "F138",
            "feature": "宽眼",
            "feature_key": "综合",
            "condition": ">=0.35",
            "traditional": "《麻衣相法》云：目大者，性外向而善交。",
            "modern": "宽眼与外倾性(E)高度正相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ENFJ"
            ],
            "strength": "社交活跃，感染力强",
            "risk": "易过度依赖外界反馈",
            "advice": "每周留半天独处，练习冥想或写作",
            "category": "五官"
    },
    {
            "id": "F139",
            "feature": "上扬眉",
            "feature_key": "综合",
            "condition": ">15°",
            "traditional": "《神相全编》曰：眉扬者，志高而气盛。",
            "modern": "上扬眉与外倾性(E)高度正相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTP"
            ],
            "strength": "自信乐观，善于激励",
            "risk": "易冲动，忽视风险",
            "advice": "重大决定前，列出利弊清单再行动",
            "category": "眉眼"
    },
    {
            "id": "F140",
            "feature": "窄眼",
            "feature_key": "综合",
            "condition": "<0.28",
            "traditional": "《相法捷要》云：目小者，性内敛而善思。",
            "modern": "窄眼与外倾性(E)低度相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "INTP",
                    "ISTP"
            ],
            "strength": "深度思考，观察敏锐",
            "risk": "易孤僻，社交回避",
            "advice": "每周参加一次小型社交活动，逐步拓展",
            "category": "五官"
    },
    {
            "id": "F141",
            "feature": "下垂眉",
            "feature_key": "综合",
            "condition": "<-5°",
            "traditional": "《人伦大统赋》云：眉垂者，性忧而多虑。",
            "modern": "下垂眉与外倾性(E)低度相关",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "低",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "INFJ"
            ],
            "strength": "共情力强，善于倾听",
            "risk": "易陷入负面情绪",
            "advice": "每日记录三件感恩小事，培养积极视角",
            "category": "眉眼"
    },
    {
            "id": "F142",
            "feature": "高额头+锐颌+宽眼",
            "feature_key": "综合",
            "condition": ">=0.38+<0.25+>=0.3",
            "traditional": "《麻衣相法》云：额高主贵，颌锐主决断，眼宽主识广。",
            "modern": "高额头与开放性(O)高度相关，锐颌与尽责性(C)相关，宽眼与宜人性(A)相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTJ"
            ],
            "strength": "善规划",
            "risk": "易理想化",
            "advice": "分解目标执行，每周复盘进度",
            "category": "综合"
    },
    {
            "id": "F143",
            "feature": "高额头+窄鼻+中颌",
            "feature_key": "综合",
            "condition": ">=0.38+<0.25+0.25-0.35",
            "traditional": "《麻衣相法》云：额高鼻窄，主智谋；颌中正，主稳重。",
            "modern": "高额头与开放性(O)相关，窄鼻与尽责性(C)相关，中颌与情绪稳定性(N)相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ"
            ],
            "strength": "善决策",
            "risk": "易苛求细节",
            "advice": "授权下属执行，每日留30分钟思考",
            "category": "综合"
    },
    {
            "id": "F144",
            "feature": "窄额头+窄眼+窄鼻",
            "feature_key": "综合",
            "condition": "<0.38+<0.3+<0.25",
            "traditional": "《麻衣相法》云：额窄眼窄，主专精；鼻窄主细察。",
            "modern": "窄额头与开放性(O)低相关，窄眼与宜人性(A)低相关，窄鼻与尽责性(C)高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ"
            ],
            "strength": "善钻研",
            "risk": "易固执",
            "advice": "定期参加跨部门会议，拓宽视野",
            "category": "上庭"
    },
    {
            "id": "F145",
            "feature": "宽鼻+圆下巴+宽眼",
            "feature_key": "综合",
            "condition": ">=0.25+>=0.4+>=0.3",
            "traditional": "《麻衣相法》云：鼻宽主财，下巴圆主和，眼宽主信。",
            "modern": "宽鼻与外向性(E)相关，圆下巴与宜人性(A)相关，宽眼与开放性(O)相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ"
            ],
            "strength": "善沟通",
            "risk": "易轻信",
            "advice": "建立客户筛选机制，每周跟进3个潜在客户",
            "category": "中庭"
    },
    {
            "id": "F146",
            "feature": "高额头+上扬眉+宽眼",
            "feature_key": "综合",
            "condition": ">=0.38+>=0.3+>=0.3",
            "traditional": "《麻衣相法》云：额高眉扬，主才艺；眼宽主灵感。",
            "modern": "高额头与开放性(O)相关，上扬眉与外向性(E)相关，宽眼与宜人性(A)相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP"
            ],
            "strength": "善创意",
            "risk": "易分心",
            "advice": "设定每日创作时间，使用番茄钟法",
            "category": "上庭"
    },
    {
            "id": "F147",
            "feature": "窄眼+窄鼻+锐颌",
            "feature_key": "综合",
            "condition": "<0.3+<0.25+<0.25",
            "traditional": "《麻衣相法》云：眼窄主察，鼻窄主析，颌锐主断。",
            "modern": "窄眼与宜人性(A)低相关，窄鼻与尽责性(C)高相关，锐颌与情绪稳定性(N)低相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTP"
            ],
            "strength": "善分析",
            "risk": "易冷漠",
            "advice": "定期与团队分享发现，培养同理心",
            "category": "综合"
    },
    {
            "id": "F148",
            "feature": "宽鼻+圆下巴+平和眉",
            "feature_key": "综合",
            "condition": ">=0.25+>=0.4+<0.3",
            "traditional": "《麻衣相法》云：鼻宽主慈，下巴圆主容，眉平主稳。",
            "modern": "宽鼻与外向性(E)相关，圆下巴与宜人性(A)相关，平和眉与情绪稳定性(N)相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISFJ"
            ],
            "strength": "善教导",
            "risk": "易纵容",
            "advice": "制定课堂纪律，每周评估学生进步",
            "category": "中庭"
    },
    {
            "id": "F149",
            "feature": "宽鼻+平和眉+圆下巴",
            "feature_key": "综合",
            "condition": ">=0.25+<0.3+>=0.4",
            "traditional": "《麻衣相法》云：鼻宽主仁，眉平主安，下巴圆主护。",
            "modern": "宽鼻与外向性(E)相关，平和眉与情绪稳定性(N)相关，圆下巴与宜人性(A)相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "高"
            },
            "mbti_hint": [
                    "ESFJ"
            ],
            "strength": "善关怀",
            "risk": "易疲惫",
            "advice": "轮班休息，每日记录患者反馈",
            "category": "中庭"
    },
    {
            "id": "F150",
            "feature": "窄鼻+锐颌+窄眼",
            "feature_key": "综合",
            "condition": "<0.25+<0.25+<0.3",
            "traditional": "《麻衣相法》云：鼻窄主理，颌锐主辩，眼窄主察。",
            "modern": "窄鼻与尽责性(C)高相关，锐颌与情绪稳定性(N)低相关，窄眼与宜人性(A)低相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ"
            ],
            "strength": "善辩论",
            "risk": "易偏激",
            "advice": "准备多角度论据，模拟对方反驳",
            "category": "综合"
    },
    {
            "id": "F151",
            "feature": "宽眼+上扬眉+圆下巴",
            "feature_key": "综合",
            "condition": ">=0.3+>=0.3+>=0.4",
            "traditional": "《麻衣相法》云：眼宽主广，眉扬主扬，下巴圆主和。",
            "modern": "宽眼与宜人性(A)相关，上扬眉与外向性(E)相关，圆下巴与开放性(O)相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP"
            ],
            "strength": "善表达",
            "risk": "易浮躁",
            "advice": "每日撰写1篇短稿，聚焦热点话题",
            "category": "综合"
    },
    {
            "id": "F152",
            "feature": "高额头+锐利下颌",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38,jaw_angle<=70",
            "traditional": "《麻衣相法》云：额高颐锐，性刚而决。",
            "modern": "与D型支配人格高相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "低",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTJ"
            ],
            "strength": "果断决策",
            "risk": "易独断专行",
            "advice": "多倾听团队意见",
            "category": "上庭"
    },
    {
            "id": "F153",
            "feature": "窄眼+高额+方颌",
            "feature_key": "综合",
            "condition": "eye_width_ratio<=0.25,forehead_ratio>=0.38,jaw_shape='square'",
            "traditional": "《神相全编》曰：目窄额高，颐方者，志在千里。",
            "modern": "与D型支配人格相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTP"
            ],
            "strength": "目标导向",
            "risk": "易忽略细节",
            "advice": "制定分步计划",
            "category": "上庭"
    },
    {
            "id": "F154",
            "feature": "宽眼+上扬眉+宽鼻",
            "feature_key": "综合",
            "condition": "eye_width_ratio>=0.35,eyebrow_angle>=15,nose_width_ratio>=0.4",
            "traditional": "《冰鉴》云：目广眉扬，鼻梁宽者，气度恢弘。",
            "modern": "与I型影响人格高相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP",
                    "ESFP"
            ],
            "strength": "感染力强",
            "risk": "易过度承诺",
            "advice": "设定边界并跟进",
            "category": "眉眼"
    },
    {
            "id": "F155",
            "feature": "圆眼+弯眉+鼻翼宽",
            "feature_key": "综合",
            "condition": "eye_shape='round',eyebrow_curve>=0.3,nose_wing_width>=0.45",
            "traditional": "《相理衡真》曰：目圆眉弯，鼻翼丰隆，善交游。",
            "modern": "与I型影响人格相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFJ",
                    "ESFJ"
            ],
            "strength": "社交达人",
            "risk": "易分心",
            "advice": "聚焦核心任务",
            "category": "眉眼"
    },
    {
            "id": "F156",
            "feature": "圆下巴+宽鼻+平和眉",
            "feature_key": "综合",
            "condition": "chin_shape='round',nose_width_ratio>=0.4,eyebrow_angle<=5",
            "traditional": "《麻衣相法》云：颐圆鼻宽，眉平者，性温而厚。",
            "modern": "与S型稳健人格高相关",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "团队粘合剂",
            "risk": "易回避冲突",
            "advice": "适时表达立场",
            "category": "下庭"
    },
    {
            "id": "F157",
            "feature": "方下巴+宽鼻+眉平",
            "feature_key": "综合",
            "condition": "chin_shape='square',nose_width_ratio>=0.4,eyebrow_angle<=5",
            "traditional": "《神相全编》曰：颐方鼻宽，眉宇平和，守成之才。",
            "modern": "与S型稳健人格相关",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ISFP"
            ],
            "strength": "可靠稳定",
            "risk": "易抗拒变化",
            "advice": "逐步接受新方法",
            "category": "下庭"
    },
    {
            "id": "F158",
            "feature": "窄鼻+窄眼+窄额",
            "feature_key": "综合",
            "condition": "nose_width_ratio<=0.3,eye_width_ratio<=0.25,forehead_ratio<=0.3",
            "traditional": "《冰鉴》云：鼻狭目窄，额不广者，思深而虑远。",
            "modern": "与C型谨慎人格高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "INTJ",
                    "ISTJ"
            ],
            "strength": "分析精准",
            "risk": "易过度批判",
            "advice": "接纳不完美",
            "category": "五官"
    },
    {
            "id": "F159",
            "feature": "尖鼻+细眼+额窄",
            "feature_key": "综合",
            "condition": "nose_tip_shape='pointed',eye_size<=0.2,forehead_ratio<=0.3",
            "traditional": "《相理衡真》曰：鼻尖目细，额狭者，精于算计。",
            "modern": "与C型谨慎人格相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "INTP",
                    "ISTP"
            ],
            "strength": "逻辑严密",
            "risk": "易陷入细节",
            "advice": "关注大局",
            "category": "五官"
    },
    {
            "id": "F160",
            "feature": "薄唇+窄鼻+窄眼",
            "feature_key": "综合",
            "condition": "lip_thickness<=0.2,nose_width_ratio<=0.3,eye_width_ratio<=0.25",
            "traditional": "《麻衣相法》云：唇薄鼻狭，目小者，心细如发。",
            "modern": "与C型谨慎人格相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "INFJ",
                    "INFP"
            ],
            "strength": "追求完美",
            "risk": "易自我怀疑",
            "advice": "设定合理标准",
            "category": "五官"
    },
    {
            "id": "F161",
            "feature": "宽眼+高额",
            "feature_key": "综合",
            "condition": "eye_width>=0.3 & forehead_ratio>=0.38",
            "traditional": "《相理衡真》云：目宽额广，智珠在握。",
            "modern": "与创造力正相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP"
            ],
            "strength": "善创新",
            "risk": "易分心",
            "advice": "每日记录三个新点子，并选一个执行",
            "category": "上庭"
    },
    {
            "id": "F162",
            "feature": "高额+上扬眉",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38 & eyebrow_angle>10",
            "traditional": "《神相全编》曰：眉扬额阔，志在四方。",
            "modern": "与好奇心相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTP"
            ],
            "strength": "善探索",
            "risk": "易浮躁",
            "advice": "每周尝试一项新技能，并反思收获",
            "category": "上庭"
    },
    {
            "id": "F163",
            "feature": "窄鼻+锐颌",
            "feature_key": "综合",
            "condition": "nose_width<0.25 & jaw_angle<120",
            "traditional": "《冰鉴》有云：鼻狭颌锐，思辨如刃。",
            "modern": "与判断力相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ"
            ],
            "strength": "善分析",
            "risk": "易苛责",
            "advice": "做决定前列出利弊清单，并征求他人意见",
            "category": "中庭"
    },
    {
            "id": "F164",
            "feature": "圆下巴+宽眼距",
            "feature_key": "综合",
            "condition": "chin_roundness>=0.7 & eye_distance>=0.5",
            "traditional": "《相理衡真》曰：颐圆目远，慈心济世。",
            "modern": "与善良相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "INFJ"
            ],
            "strength": "善助人",
            "risk": "易忽略自我",
            "advice": "每周做一件匿名善事，并反思内心满足感",
            "category": "下庭"
    },
    {
            "id": "F165",
            "feature": "宽鼻+平和眉",
            "feature_key": "综合",
            "condition": "nose_width>=0.3 & eyebrow_angle<5",
            "traditional": "《神相全编》云：鼻宽眉平，和而不同。",
            "modern": "与社交智慧相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ"
            ],
            "strength": "善协调",
            "risk": "易迎合",
            "advice": "在社交中主动倾听三人，并总结共同点",
            "category": "中庭"
    },
    {
            "id": "F166",
            "feature": "圆下巴+中眼距",
            "feature_key": "综合",
            "condition": "chin_roundness>=0.7 & eye_distance>=0.4 & eye_distance<0.5",
            "traditional": "《冰鉴》有云：颐圆目均，众志成城。",
            "modern": "与团队精神相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ"
            ],
            "strength": "善协作",
            "risk": "易依赖",
            "advice": "在团队任务中主动承担一个角色，并记录贡献",
            "category": "下庭"
    },
    {
            "id": "F167",
            "feature": "锐颌+中鼻",
            "feature_key": "综合",
            "condition": "jaw_angle<120 & nose_width>=0.25 & nose_width<0.3",
            "traditional": "《麻衣相法》曰：颌锐鼻正，持衡守中。",
            "modern": "与公平相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ"
            ],
            "strength": "善公正",
            "risk": "易固执",
            "advice": "处理冲突时，先列出双方观点再寻求折中方案",
            "category": "下庭"
    },
    {
            "id": "F168",
            "feature": "高额+窄鼻+锐颌",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38 & nose_width<0.25 & jaw_angle<120",
            "traditional": "《神相全编》云：额高鼻狭颌如削，统御之才。",
            "modern": "与领导力相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTJ"
            ],
            "strength": "善决策",
            "risk": "易独断",
            "advice": "每周授权一项任务给他人，并反馈结果",
            "category": "综合"
    },
    {
            "id": "F169",
            "feature": "上扬眉+宽眼距",
            "feature_key": "综合",
            "condition": "eyebrow_angle>10 & eye_distance>=0.5",
            "traditional": "《相理衡真》曰：眉扬目远，心怀曙光。",
            "modern": "与希望相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP"
            ],
            "strength": "善乐观",
            "risk": "易盲目",
            "advice": "每日写下三个积极预期，并制定实现步骤",
            "category": "眉眼"
    },
    {
            "id": "F170",
            "feature": "高额+窄眼",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38 & eye_width<0.25",
            "traditional": "《月波洞中记》云：额高目狭，思虑过深，易陷牛角尖。",
            "modern": "过度分析型",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "INTJ",
                    "INTP"
            ],
            "strength": "逻辑缜密",
            "risk": "陷入思维循环",
            "advice": "设置15分钟分析时限，用纸笔列出选项后强制决策",
            "category": "综合"
    },
    {
            "id": "F171",
            "feature": "锐颌+窄鼻",
            "feature_key": "综合",
            "condition": "jaw_angle<100° & nose_width<0.25",
            "traditional": "《冰鉴》有云：颐尖鼻狭，刚愎自用，遇压则攻。",
            "modern": "攻击性应对型",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESTJ",
                    "ENTJ"
            ],
            "strength": "行动力强",
            "risk": "易引发冲突",
            "advice": "冲突前深呼吸5秒，改用'我句式'表达需求",
            "category": "下庭"
    },
    {
            "id": "F172",
            "feature": "上扬眉+宽眼",
            "feature_key": "综合",
            "condition": "eyebrow_angle>15° & eye_width>0.3",
            "traditional": "《麻衣相法》谓：眉扬目展，气度豁达，能化危为机。",
            "modern": "积极重构型",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFJ",
                    "ENTP"
            ],
            "strength": "乐观创新",
            "risk": "忽视风险",
            "advice": "用SWOT表格平衡乐观，列出3个潜在障碍",
            "category": "眉眼"
    },
    {
            "id": "F173",
            "feature": "下垂眉+窄眼",
            "feature_key": "综合",
            "condition": "eyebrow_angle<0° & eye_width<0.25",
            "traditional": "《相理衡真》云：眉垂目陷，忧思成疾，易自耗元气。",
            "modern": "内耗型",
            "ocean": {
                    "O": "低",
                    "C": "低",
                    "E": "低",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "INFJ",
                    "INFP"
            ],
            "strength": "共情深刻",
            "risk": "自责循环",
            "advice": "每日写'三件小成就'清单，打断反刍思维",
            "category": "眉眼"
    },
    {
            "id": "F174",
            "feature": "平和眉+宽鼻",
            "feature_key": "综合",
            "condition": "-5°<eyebrow_angle<5° & nose_width>0.35",
            "traditional": "《人伦大统赋》曰：眉平鼻广，善假于人，然易失主见。",
            "modern": "求助型",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFP"
            ],
            "strength": "团队协作",
            "risk": "过度依赖他人",
            "advice": "先独立列出3个方案再求助，明确'需要具体建议'",
            "category": "综合"
    },
    {
            "id": "F175",
            "feature": "窄额+锐颌",
            "feature_key": "综合",
            "condition": "forehead_ratio<0.33 & jaw_angle<100°",
            "traditional": "《玉管照神局》云：额狭颐刚，宁折不弯，硬扛至崩。",
            "modern": "硬扛型",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTP"
            ],
            "strength": "坚韧不拔",
            "risk": "身心透支",
            "advice": "设定每日'休息闹钟'，强制暂停10分钟",
            "category": "综合"
    },
    {
            "id": "F176",
            "feature": "高额+宽眼距",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38 AND eye_spacing>=0.5",
            "traditional": "《麻衣相法》云：额阔眼疏，智广而思深。",
            "modern": "与概念学习高相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "INTP"
            ],
            "strength": "善抽象思维",
            "risk": "易脱离实际",
            "advice": "用思维导图梳理理论，每周写概念总结",
            "category": "上庭"
    },
    {
            "id": "F177",
            "feature": "窄额+窄眼距",
            "feature_key": "综合",
            "condition": "forehead_ratio<0.38 AND eye_spacing<0.5",
            "traditional": "《相理衡真》曰：额窄目聚，务实而精进。",
            "modern": "与实践学习高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "动手能力强",
            "risk": "易忽视理论",
            "advice": "每日设定实操任务，用项目日志记录步骤",
            "category": "上庭"
    },
    {
            "id": "F178",
            "feature": "平和眉",
            "feature_key": "综合",
            "condition": "eyebrow_angle<=10° AND eyebrow_angle>=-5°",
            "traditional": "《太清神鉴》云：眉平如一字，性稳而守常。",
            "modern": "与稳步学习高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "持久专注",
            "risk": "易抗拒变化",
            "advice": "制定固定学习时间表，每周加入1次新方法尝试",
            "category": "眉眼"
    },
    {
            "id": "F179",
            "feature": "圆下巴",
            "feature_key": "综合",
            "condition": "chin_shape='round'",
            "traditional": "《神相全编》云：颐圆如满月，乐学而善感。",
            "modern": "与体验学习高相关",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFP",
                    "ESFP"
            ],
            "strength": "沉浸式吸收",
            "risk": "易情绪波动",
            "advice": "用角色扮演或实地考察学习，每次后写情感反思",
            "category": "下庭"
    },
    {
            "id": "F180",
            "feature": "长脸",
            "feature_key": "综合",
            "condition": "face_shape='long'",
            "traditional": "《麻衣相法》载：面长如瓜，善序而好理。",
            "modern": "与系统学习高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "ISTJ"
            ],
            "strength": "逻辑框架强",
            "risk": "易僵化死板",
            "advice": "用金字塔原理构建知识体系，每月更新框架",
            "category": "面型"
    },
    {
            "id": "F181",
            "feature": "圆脸",
            "feature_key": "综合",
            "condition": "face_shape='round'",
            "traditional": "《相理衡真》云：面圆如盘，应境而善变。",
            "modern": "与情境学习高相关",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFJ",
                    "ESFJ"
            ],
            "strength": "灵活适应",
            "risk": "易缺乏深度",
            "advice": "结合案例与故事学习，每次提炼3个关键点",
            "category": "面型"
    },
    {
            "id": "F182",
            "feature": "长脸+高额",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《麻衣相法》云：『面长额广，主贵而多智；天庭饱满，地阁方圆，乃福寿之基。』",
            "modern": "长脸与高额组合暗示前额叶皮层发育较好，逻辑推理与前瞻性思维突出，但可能因过度理性而缺乏情感共鸣。",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTJ"
            ],
            "strength": "学术研究能力强，擅长系统化分析与长期规划。",
            "risk": "易陷入完美主义，忽视人际细节，可能显得冷漠。",
            "advice": "在团队中主动分享思考过程，每周安排一次非正式社交活动以平衡理性与感性。",
            "category": "综合"
    },
    {
            "id": "F183",
            "feature": "长脸+窄额",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《相理衡真》曰：『额窄面长，心性多疑；眉骨高耸，技艺精纯。』",
            "modern": "窄额与长脸组合反映专注力高度集中，适合精细操作，但可能因视野受限而抗拒新观点。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ISTP"
            ],
            "strength": "手工艺或技术领域天赋异禀，注重细节与流程优化。",
            "risk": "容易固执己见，对抽象概念缺乏兴趣。",
            "advice": "尝试每月参加一次跨领域讲座，用思维导图记录不同观点以拓宽认知边界。",
            "category": "综合"
    },
    {
            "id": "F184",
            "feature": "长脸+宽眼",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《神相全编》载：『目宽面长，才情横溢；神采飞扬，可通音律。』",
            "modern": "宽眼距与长脸组合增强视觉空间感知能力，与创造力正相关，但可能因敏感而情绪波动大。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "ENFP",
                    "INFP"
            ],
            "strength": "艺术创作或设计领域灵感丰富，善于捕捉美感。",
            "risk": "易受外界评价干扰，执行力不足。",
            "advice": "建立每日创作日志，设定最小可行作品目标（如每天画一幅速写），并寻求一位务实伙伴监督进度。",
            "category": "综合"
    },
    {
            "id": "F185",
            "feature": "长脸+窄鼻",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《冰鉴》有云：『鼻窄面长，思虑深远；梁直如刃，析理入微。』",
            "modern": "窄鼻与长脸组合预示分析型思维，擅长数据解构，但可能因过度批判而缺乏合作精神。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTP",
                    "ISTP"
            ],
            "strength": "金融或科研领域表现卓越，能快速识别逻辑漏洞。",
            "risk": "社交中显得刻薄，难以接受模糊结论。",
            "advice": "在讨论中先肯定对方三点再提出质疑，每周练习一次开放式问题提问技巧。",
            "category": "综合"
    },
    {
            "id": "F186",
            "feature": "长脸+圆下巴",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《相法集成》记载：『面长颐圆，外刚内柔；言辞温润，善解人意。』",
            "modern": "圆下巴缓冲了长脸的凌厉感，暗示情绪调节能力佳，适合外交或调解角色。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFJ",
                    "INFJ"
            ],
            "strength": "跨文化沟通与冲突调解能力突出，能建立信任。",
            "risk": "易过度妥协，忽略自身需求。",
            "advice": "在谈判前明确底线清单，使用『我理解…同时我需要…』句式平衡共情与自我主张。",
            "category": "综合"
    },
    {
            "id": "F187",
            "feature": "圆脸+宽鼻",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《人伦大统赋》云：『面圆鼻阔，气度恢弘；交友四方，财源广进。』",
            "modern": "宽鼻与圆脸组合增强亲和力与社交网络构建能力，但可能因过度外向而缺乏深度思考。",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ENFJ"
            ],
            "strength": "社群运营或销售领域如鱼得水，能快速建立人脉。",
            "risk": "易分心，对长期计划缺乏耐心。",
            "advice": "使用番茄工作法管理时间，每天预留30分钟独处用于反思当日社交得失。",
            "category": "综合"
    },
    {
            "id": "F188",
            "feature": "圆脸+窄鼻",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《相术精义》曰：『面圆鼻细，心机缜密；精打细算，毫厘不差。』",
            "modern": "窄鼻与圆脸组合暗示精细计算能力，适合精算或审计，但可能因完美主义而焦虑。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "风险管理与数据校验能力极强，错误率低。",
            "risk": "易陷入细节焦虑，决策速度慢。",
            "advice": "采用『80%原则』：当信息收集到80%时即做决定，并设置每日决策数量上限（如不超过5个）。",
            "category": "综合"
    },
    {
            "id": "F189",
            "feature": "圆脸+宽眼",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《相理衡真》载：『目宽面圆，灵性通明；奇思妙想，层出不穷。』",
            "modern": "宽眼距与圆脸组合增强发散性思维，适合创意行业，但可能因注意力涣散而难以落地。",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFP",
                    "ENTP"
            ],
            "strength": "广告或产品设计领域创意爆棚，能提出颠覆性方案。",
            "risk": "项目跟进能力弱，易虎头蛇尾。",
            "advice": "使用甘特图分解创意为可执行步骤，并每周向导师汇报一次进度以增强责任感。",
            "category": "综合"
    },
    {
            "id": "F190",
            "feature": "圆脸+上扬眉",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《神相全编》有云：『眉扬面圆，神采奕奕；言辞动人，可主舞台。』",
            "modern": "上扬眉与圆脸组合增强表现欲与情绪感染力，适合表演或演讲，但可能因过度戏剧化而失真。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ESFP",
                    "ENFP"
            ],
            "strength": "舞台表现力与即兴反应能力卓越，能调动观众情绪。",
            "risk": "易情绪化，私下可能感到空虚。",
            "advice": "建立表演后情绪记录表，区分舞台角色与真实自我，每天进行10分钟正念冥想以稳定内核。",
            "category": "综合"
    },
    {
            "id": "F191",
            "feature": "圆脸+锐颌",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《相法集成》记载：『颐锐面圆，刚柔并济；行事果决，可掌实务。』",
            "modern": "锐利下颌与圆脸组合暗示行动力与决断力，适合项目管理或执行岗位，但可能因急躁而忽略细节。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESTJ",
                    "ENTJ"
            ],
            "strength": "危机处理与资源调配能力突出，能快速推动项目。",
            "risk": "易独断专行，忽视团队意见。",
            "advice": "在决策前强制收集三人以上反馈，使用『先听后说』原则：每次会议前5分钟只倾听不发言。",
            "category": "综合"
    },
    {
            "id": "F192",
            "feature": "中庭长+窄鼻",
            "feature_key": "midface_ratio",
            "condition": ">=0.38",
            "traditional": "《麻衣相法》云：鼻梁细长，中停孤峭，主清高自许，不近俗流。",
            "modern": "中庭偏长且鼻翼窄小者，常表现为思维独立、追求精神境界，但易因过度理想化而疏离社交。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "INTP"
            ],
            "strength": "逻辑严谨，善于深度思考与抽象分析",
            "risk": "社交疏离感强，易被误解为冷漠或傲慢",
            "advice": "主动参与团队协作项目，每周至少一次非工作社交活动；尝试用通俗语言表达专业观点，降低沟通门槛。",
            "category": "综合"
    },
    {
            "id": "F193",
            "feature": "中庭长+宽鼻",
            "feature_key": "midface_ratio",
            "condition": ">=0.38",
            "traditional": "《冰鉴》曰：鼻梁虽长而准头丰隆，主厚重有容，能载物。",
            "modern": "中庭长配合宽鼻翼者，兼具理性框架与包容力，适合需要长期战略规划的岗位。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTJ"
            ],
            "strength": "决策稳健，能平衡长远目标与现实资源",
            "risk": "过度保守可能错失创新机遇",
            "advice": "每季度设定一个突破性目标，主动接触跨界信息；培养快速试错的小团队实验机制。",
            "category": "综合"
    },
    {
            "id": "F194",
            "feature": "中庭长+宽眼",
            "feature_key": "midface_ratio",
            "condition": ">=0.38",
            "traditional": "《麻衣相法》载：目阔而长，中停舒展，主胸襟开阔，善纳百川。",
            "modern": "中庭长且眼距开阔者，认知灵活性高，擅长多线程处理复杂信息。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP",
                    "ENTP"
            ],
            "strength": "视野前瞻，能快速整合跨领域资源",
            "risk": "注意力易分散，细节执行力不足",
            "advice": "使用甘特图或OKR工具分解长期目标，每日设定3个核心任务；委托琐碎事务给擅长执行的伙伴。",
            "category": "综合"
    },
    {
            "id": "F195",
            "feature": "中庭长+窄眼",
            "feature_key": "midface_ratio",
            "condition": ">=0.38",
            "traditional": "《冰鉴》云：目细而长，中停孤清，主沉静善思，然易陷于执念。",
            "modern": "中庭长伴窄眼者，专注力极强，适合需要深度钻研的领域，但需警惕认知固化。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ISFJ"
            ],
            "strength": "细节洞察力卓越，能发现系统性漏洞",
            "risk": "过度批判自我与他人，引发焦虑或人际摩擦",
            "advice": "建立‘容错日志’记录非原则性失误，每周复盘时区分‘可改进’与‘可接受’；练习正念冥想缓解完美主义。",
            "category": "综合"
    },
    {
            "id": "F196",
            "feature": "中庭长+圆下巴",
            "feature_key": "midface_ratio",
            "condition": ">=0.38",
            "traditional": "《麻衣相法》谓：中停虽长，下停圆润，主刚柔并济，外严内慈。",
            "modern": "中庭长与圆下巴组合，理性框架下隐藏亲和力，适合技术管理或学术带头人角色。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "INFJ",
                    "ENFJ"
            ],
            "strength": "既能制定严谨规则，又能体恤团队情绪",
            "risk": "妥协过度导致原则模糊",
            "advice": "在关键决策前用‘如果-那么’预案明确底线；每月开展一次匿名团队反馈，校准包容与坚持的平衡点。",
            "category": "综合"
    },
    {
            "id": "F197",
            "feature": "中庭短+窄鼻",
            "feature_key": "midface_ratio",
            "condition": "<=0.29",
            "traditional": "《冰鉴》曰：鼻梁窄促，中停短缩，主精悍果决，不拖泥带水。",
            "modern": "中庭短且鼻翼窄者，行动力强，擅长快速切入问题核心，但易缺乏耐心。",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ESTP",
                    "ESFP"
            ],
            "strength": "危机处理反应敏捷，能迅速调动资源",
            "risk": "冲动决策导致后续漏洞",
            "advice": "执行‘10-10-10法则’：决策前思考10分钟、10小时、10天后的影响；重要事项强制设置24小时冷静期。",
            "category": "综合"
    },
    {
            "id": "F198",
            "feature": "中庭短+宽鼻",
            "feature_key": "midface_ratio",
            "condition": "<=0.29",
            "traditional": "《麻衣相法》载：鼻准丰隆而中停短，主敦厚务实，不尚虚谈。",
            "modern": "中庭短配合宽鼻者，务实可靠，适合执行层或后勤管理岗位。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "流程执行稳定，能保障团队基础运转",
            "risk": "抗拒变革，易被新技术淘汰",
            "advice": "每季度学习一项行业新工具（如自动化软件），参加至少一次跨界交流会；用‘最小可行性改变’策略逐步适应变化。",
            "category": "综合"
    },
    {
            "id": "F199",
            "feature": "中庭短+上扬眉",
            "feature_key": "midface_ratio",
            "condition": "<=0.29",
            "traditional": "《冰鉴》云：眉扬而中停促，主活泼机变，然易流于轻浮。",
            "modern": "中庭短与上扬眉组合，能量充沛且富有感染力，适合创意或销售岗位。",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFP",
                    "ESFP"
            ],
            "strength": "情绪感染力强，能快速点燃团队热情",
            "risk": "持续性不足，项目后期易倦怠",
            "advice": "将大目标拆解为15天冲刺周期，每个周期结束后安排3天休整；与稳健型同事组队互补节奏。",
            "category": "综合"
    },
    {
            "id": "F200",
            "feature": "中庭短+下垂眉",
            "feature_key": "midface_ratio",
            "condition": "<=0.29",
            "traditional": "《麻衣相法》谓：眉垂而中停短，主深沉内敛，谋定后动。",
            "modern": "中庭短伴下垂眉者，思考缜密，擅长风险评估与战略规划。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "INTJ",
                    "ISTP"
            ],
            "strength": "风险预判精准，能制定多套应急预案",
            "risk": "过度谨慎导致行动滞后",
            "advice": "设定‘决策截止时间’，采用‘70%信息即行动’原则；每月复盘一次因延迟错失的机会，强化行动意识。",
            "category": "综合"
    },
    {
            "id": "F201",
            "feature": "中庭短+锐颌",
            "feature_key": "midface_ratio",
            "condition": "<=0.29",
            "traditional": "《冰鉴》载：下停尖削而中停短，主果断刚毅，然易失于苛刻。",
            "modern": "中庭短与锐利下颌组合，目标导向明确，适合需要快速决断的岗位。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTP"
            ],
            "strength": "在高压环境下能快速拍板并推动执行",
            "risk": "人际关系紧张，易被视为独断专行",
            "advice": "决策前强制征求3位相关方意见，用‘利弊清单’可视化不同立场；每周安排一次非工作场景的团队聚餐。",
            "category": "综合"
    },
    {
            "id": "F202",
            "feature": "下庭长+锐颌",
            "feature_key": "lowerface_ratio",
            "condition": ">=0.35",
            "traditional": "《柳庄相法》云：下停长而颌锐者，志坚如铁，然易折。",
            "modern": "下庭比例偏长且下巴尖锐，暗示个体目标感强、执行力高，但可能因固执而缺乏灵活性。",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTJ"
            ],
            "strength": "决策果断，逆境中能坚持到底，适合领导或攻坚角色。",
            "risk": "人际关系易紧张，因过于直接而忽略他人感受，可能导致合作摩擦。",
            "advice": "在团队中主动练习倾听技巧，每周安排一次非任务性社交；决策前先列出三种替代方案，避免单一路径依赖。",
            "category": "综合"
    },
    {
            "id": "F203",
            "feature": "下庭长+圆颌",
            "feature_key": "lowerface_ratio",
            "condition": ">=0.35",
            "traditional": "《冰鉴》曰：下停丰而颌圆，德厚载物，不争而胜。",
            "modern": "下庭偏长但下巴圆润，反映个体兼具持久力与包容心，善于在长期关系中维持平衡。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "INFJ",
                    "ISFJ"
            ],
            "strength": "耐心与同理心突出，能化解团队矛盾，适合教育、咨询等需要长期投入的领域。",
            "risk": "过度迁就他人可能压抑自我需求，导致内心积累不满或决策拖延。",
            "advice": "每月设定一次‘自我优先日’，明确表达个人边界；在重要谈判前预先写下底线条款，避免被动让步。",
            "category": "综合"
    },
    {
            "id": "F204",
            "feature": "下庭长+宽眼",
            "feature_key": "lowerface_ratio",
            "condition": ">=0.35",
            "traditional": "《柳庄相法》云：目阔而颐长，见微知著，谋定后动。",
            "modern": "下庭长配合眼距宽，预示个体擅长宏观规划与风险预判，但可能因过度分析而错失时机。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTP",
                    "ENTP"
            ],
            "strength": "战略思维卓越，能从碎片信息中构建系统框架，适合策划、研发岗位。",
            "risk": "容易陷入‘完美方案’陷阱，行动力滞后，在快节奏环境中可能被边缘化。",
            "advice": "采用‘70%原则’：方案完成度达70%即启动试点，后续迭代优化；每周设定一个‘快速决策日’，强制在1小时内做三个小决定。",
            "category": "综合"
    },
    {
            "id": "F205",
            "feature": "下庭长+窄鼻",
            "feature_key": "lowerface_ratio",
            "condition": ">=0.35",
            "traditional": "《冰鉴》言：鼻狭颐长，精进不休，然易苛己。",
            "modern": "下庭长且鼻翼窄，反映个体对细节有极致追求，自我要求严苛，但可能因完美主义导致效率下降。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "INTJ"
            ],
            "strength": "工作质量极高，擅长审计、质检等需要零误差的岗位，值得信赖。",
            "risk": "对他人错误容忍度低，易引发团队焦虑；自我批评过度可能引发职业倦怠。",
            "advice": "每日记录‘三件已完成事项’，强化正向反馈；分配任务时明确‘可接受误差范围’，降低非必要苛求。",
            "category": "综合"
    },
    {
            "id": "F206",
            "feature": "下庭长+上扬眉",
            "feature_key": "lowerface_ratio",
            "condition": ">=0.35",
            "traditional": "《柳庄相法》云：眉扬颐展，气宇轩昂，破浪乘风。",
            "modern": "下庭长配合上扬眉形，显示个体充满进取心与感染力，但可能因过度自信而忽视风险。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFJ",
                    "ESFP"
            ],
            "strength": "激励团队士气的能力突出，适合销售、创业等需要带动氛围的领域。",
            "risk": "容易在乐观中低估困难，导致项目后期资源不足或承诺过度。",
            "advice": "在启动新项目前，强制完成‘最坏情景模拟’并预留20%缓冲资源；聘请一位谨慎型搭档负责风险管控。",
            "category": "综合"
    },
    {
            "id": "F207",
            "feature": "下庭短+圆颌",
            "feature_key": "lowerface_ratio",
            "condition": "<=0.24",
            "traditional": "《冰鉴》曰：下停短而颌圆，春风化雨，人皆亲之。",
            "modern": "下庭偏短且下巴圆润，暗示个体天生具有亲和力与社交润滑能力，但可能缺乏深度。",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ENFP"
            ],
            "strength": "快速建立信任，适合客服、公关等高频人际岗位，团队凝聚力强。",
            "risk": "容易因过度迎合他人而模糊自我立场，在冲突中倾向于回避而非解决。",
            "advice": "练习‘温和坚定’沟通法：先肯定对方感受，再明确表达自身需求；每周留出两小时独处时间进行深度思考。",
            "category": "综合"
    },
    {
            "id": "F208",
            "feature": "下庭短+锐颌",
            "feature_key": "lowerface_ratio",
            "condition": "<=0.24",
            "traditional": "《柳庄相法》云：颐短而锐，性如烈火，易发难收。",
            "modern": "下庭短且下巴尖锐，反映个体反应敏捷、行动迅速，但情绪管理能力较弱，易冲动。",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "高",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ESTP",
                    "ENTP"
            ],
            "strength": "危机处理能力极强，能在突发状况中快速决策，适合应急管理或创业初期。",
            "risk": "言语直接易伤人，事后常后悔；长期处于应激状态可能影响身心健康。",
            "advice": "在情绪激动时执行‘10秒呼吸法’（吸气4秒、屏息2秒、呼气4秒）；重要邮件或消息发送前，先请第三方审阅措辞。",
            "category": "综合"
    },
    {
            "id": "F209",
            "feature": "下庭短+宽鼻",
            "feature_key": "lowerface_ratio",
            "condition": "<=0.24",
            "traditional": "《冰鉴》言：鼻宽颐促，随性洒脱，不拘绳墨。",
            "modern": "下庭短配合宽鼻翼，显示个体不拘小节、享受当下，但可能缺乏长远规划。",
            "ocean": {
                    "O": "低",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISFP",
                    "ESFP"
            ],
            "strength": "创造力与适应力强，能在变化中快速调整，适合艺术、娱乐等创意行业。",
            "risk": "容易因追求即时满足而拖延重要任务，财务规划方面需加强自律。",
            "advice": "使用‘番茄工作法+奖励机制’：每完成25分钟专注工作，允许5分钟自由活动；设立自动储蓄账户，每月固定划转10%收入。",
            "category": "综合"
    },
    {
            "id": "F210",
            "feature": "下庭短+上扬眉",
            "feature_key": "lowerface_ratio",
            "condition": "<=0.24",
            "traditional": "《柳庄相法》云：眉扬颐短，灵动如雀，机变无双。",
            "modern": "下庭短且眉形上扬，预示个体思维敏捷、善于应变，但可能缺乏持久专注力。",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFP",
                    "ENTP"
            ],
            "strength": "点子多、反应快，适合头脑风暴、市场营销等需要创意的岗位。",
            "risk": "容易频繁切换目标，导致项目半途而废；在需要重复性工作的环境中易感枯燥。",
            "advice": "采用‘三任务清单法’：每天只列出三个核心任务，完成前不开启新事项；每季度设定一个‘深耕主题’，围绕该主题系统学习。",
            "category": "综合"
    },
    {
            "id": "F211",
            "feature": "下庭短+平和眉",
            "feature_key": "lowerface_ratio",
            "condition": "<=0.24",
            "traditional": "《冰鉴》曰：眉平颐短，稳若磐石，静水流深。",
            "modern": "下庭短配合平缓眉形，反映个体情绪稳定、行事可靠，但可能缺乏突破性。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ISFJ"
            ],
            "strength": "执行力与责任感极强，适合财务、行政等需要持续稳定的岗位，团队定海神针。",
            "risk": "抗拒变化，在转型期可能成为阻力；容易因过度保守而错失创新机会。",
            "advice": "每月尝试一件‘微冒险’（如换条通勤路线、学习新工具）；在年度计划中预留15%时间用于探索非核心领域。",
            "category": "综合"
    },
    {
            "id": "F212",
            "feature": "上扬眉（高挑眉）配宽眼距",
            "feature_key": "brow_angle",
            "condition": ">=21 & eye_distance >=0.5",
            "traditional": "《麻衣相法》云：眉为保寿官，清秀者多才艺，上扬者性刚毅，眼距宽者心豁达。",
            "modern": "上扬眉与宽眼距组合显示个体兼具进取心与包容性，但可能因过度自信而忽视细节。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ENFP"
            ],
            "strength": "领导力强，善于开拓新领域，社交中气场足。",
            "risk": "易给人压迫感，合作中可能忽略他人意见。",
            "advice": "职场中可主动承担项目主导角色，但需定期征求团队反馈。社交时适当放慢语速，多用开放式提问缓和锋芒。",
            "category": "综合"
    },
    {
            "id": "F213",
            "feature": "上扬眉配窄鼻型",
            "feature_key": "brow_angle",
            "condition": ">=21 & nose_width <=0.35",
            "traditional": "《麻衣相法》云：眉高鼻窄者，性急而谋深，如鹰隼之锐。",
            "modern": "上扬眉与窄鼻组合暗示目标导向型人格，决策迅速但易显苛刻。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "INTJ",
                    "ISTJ"
            ],
            "strength": "执行力强，擅长精密计划与风险控制。",
            "risk": "完美主义倾向可能导致团队压力过大。",
            "advice": "工作中可制定分阶段目标，避免一次性要求过高。社交时尝试用幽默化解严肃形象，每周安排一次非正式交流。",
            "category": "综合"
    },
    {
            "id": "F214",
            "feature": "上扬眉配圆脸型",
            "feature_key": "brow_angle",
            "condition": ">=21 & face_ratio <=0.85",
            "traditional": "《麻衣相法》云：眉扬面圆者，外柔内刚，富贵中藏锋芒。",
            "modern": "上扬眉与圆脸组合显示亲和力与决断力的矛盾统一，易在人际中占据主动。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ENFJ"
            ],
            "strength": "感染力强，能快速建立信任并推动共识。",
            "risk": "情绪外露时可能被误认为攻击性。",
            "advice": "团队协作中先倾听再表达，用“我们”代替“我”来降低对抗感。职场演讲时配合手势强调重点，但避免频繁挑眉。",
            "category": "综合"
    },
    {
            "id": "F215",
            "feature": "上扬眉配长中庭",
            "feature_key": "brow_angle",
            "condition": ">=21 & midface_ratio >=0.45",
            "traditional": "《麻衣相法》云：眉扬中庭长者，志在四方，然易孤高。",
            "modern": "上扬眉与长中庭组合暗示理性主导，擅长战略思考但情感表达含蓄。",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTP",
                    "ENTP"
            ],
            "strength": "逻辑严密，能独立解决复杂问题。",
            "risk": "疏离感可能阻碍跨部门协作。",
            "advice": "每周参与一次非正式头脑风暴，用书面报告补充口头沟通。社交中主动分享个人兴趣，降低距离感。",
            "category": "综合"
    },
    {
            "id": "F216",
            "feature": "下垂眉（八字眉）配窄眼距",
            "feature_key": "brow_angle",
            "condition": "<=9 & eye_distance <=0.4",
            "traditional": "《麻衣相法》云：眉垂目近者，多忧思，宜守成不宜进取。",
            "modern": "下垂眉与窄眼距组合显示谨慎型人格，易陷入过度反思。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISFJ",
                    "INFJ"
            ],
            "strength": "责任心强，擅长维护现有系统稳定性。",
            "risk": "决策犹豫可能错失良机。",
            "advice": "职场中可担任质量管控或后勤角色，用清单管理减少焦虑。社交时练习抬头挺胸，用肯定句替代疑问句。",
            "category": "综合"
    },
    {
            "id": "F217",
            "feature": "下垂眉配宽下颌",
            "feature_key": "brow_angle",
            "condition": "<=9 & jaw_angle >=120",
            "traditional": "《麻衣相法》云：眉垂颐方者，外柔内执，忍辱负重之相。",
            "modern": "下垂眉与宽下颌组合暗示表面顺从但内心固执，压力下易爆发。",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTP",
                    "ESTP"
            ],
            "strength": "抗压能力强，危机中能保持冷静。",
            "risk": "情绪积压后可能突然失控。",
            "advice": "建立定期运动或艺术宣泄渠道，工作中用“暂停-深呼吸-回应”三步法。社交时避免压抑真实感受，温和表达边界。",
            "category": "综合"
    },
    {
            "id": "F218",
            "feature": "下垂眉配短下巴",
            "feature_key": "brow_angle",
            "condition": "<=9 & lowerface_ratio <=0.2",
            "traditional": "《麻衣相法》云：眉垂颔短者，心慈而运蹇，宜广结善缘。",
            "modern": "下垂眉与短下巴组合显示依赖型人格，易受他人影响。",
            "ocean": {
                    "O": "低",
                    "C": "低",
                    "E": "中",
                    "A": "高",
                    "N": "高"
            },
            "mbti_hint": [
                    "ESFP",
                    "ISFP"
            ],
            "strength": "共情力强，善于调解人际矛盾。",
            "risk": "缺乏主见可能被利用。",
            "advice": "职场中可从事客户服务或团队协调岗，决策前列出利弊清单。社交时练习说“我需要时间考虑”，避免即时承诺。",
            "category": "综合"
    },
    {
            "id": "F219",
            "feature": "平和眉（标准眉）配高鼻梁",
            "feature_key": "brow_angle",
            "condition": ">=10 & <=20 & nose_width >=0.4",
            "traditional": "《麻衣相法》云：眉平鼻隆者，性中和，福禄自至。",
            "modern": "平和眉与高鼻梁组合显示情绪稳定与自信的平衡，易获他人信赖。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESTJ",
                    "ISTJ"
            ],
            "strength": "可靠务实，适合长期项目管理。",
            "risk": "创新动力不足，可能抗拒变革。",
            "advice": "定期参加行业培训保持视野更新，工作中主动提出优化建议。社交时展现专业深度，但避免过度说教。",
            "category": "综合"
    },
    {
            "id": "F220",
            "feature": "平和眉配尖下巴",
            "feature_key": "brow_angle",
            "condition": ">=10 & <=20 & lowerface_ratio >=0.3",
            "traditional": "《麻衣相法》云：眉平颐尖者，智巧而性急，宜以柔克刚。",
            "modern": "平和眉与尖下巴组合显示思维敏捷但缺乏耐心，适合创意型工作。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFP",
                    "INFP"
            ],
            "strength": "灵感丰富，能快速提出新颖方案。",
            "risk": "执行阶段易分心。",
            "advice": "使用番茄工作法分段专注，将创意转化为可执行步骤。社交中避免同时开启多个话题，聚焦深度交流。",
            "category": "综合"
    },
    {
            "id": "F221",
            "feature": "平和眉配方脸型",
            "feature_key": "brow_angle",
            "condition": ">=10 & <=20 & face_ratio >=1.1",
            "traditional": "《麻衣相法》云：眉方面阔者，刚正不阿，可托重任。",
            "modern": "平和眉与方脸组合显示原则性强，适合需要公正判断的岗位。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTP"
            ],
            "strength": "决策果断，能维护团队秩序。",
            "risk": "灵活性不足，可能激化对立。",
            "advice": "处理冲突时先复述对方观点再表达立场，用“如果…可能更好”替代直接否定。职场中可担任仲裁或审计角色。",
            "category": "综合"
    },
    {
            "id": "F222",
            "feature": "额头",
            "feature_key": "forehead_ratio",
            "condition": ">=0.38",
            "traditional": "《麻衣相法》云：额高而阔，日月角起，主贵寿。天庭饱满，地阁方圆，乃富贵之相。",
            "modern": "额头饱满反映前额叶发育良好，与认知灵活性和社会适应能力正相关。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTJ"
            ],
            "strength": "思维开阔，善于战略规划",
            "risk": "可能过于理想化，忽视细节",
            "advice": "多参与具体执行环节，用数据验证想法。每周设定一个可量化的小目标，逐步落地。",
            "category": "综合"
    },
    {
            "id": "F223",
            "feature": "眉毛",
            "feature_key": "brow_angle",
            "condition": ">=0.25",
            "traditional": "《柳庄相法》曰：眉如新月，弯而细长，主聪明文秀。眉高居额，兄弟有助。",
            "modern": "眉形上扬与多巴胺系统活跃度相关，体现进取心和情绪稳定性。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESTJ",
                    "ENTP"
            ],
            "strength": "执行力强，善于推动项目",
            "risk": "易急躁，人际关系需调和",
            "advice": "每日练习深呼吸3分钟，决策前先列出利弊清单。与同事沟通时多用‘我们’代替‘我’。",
            "category": "综合"
    },
    {
            "id": "F224",
            "feature": "眼睛",
            "feature_key": "eye_distance",
            "condition": ">=0.45",
            "traditional": "《冰鉴》云：目者面之渊，不深则不清。睛如点漆，光彩射人，主贵。",
            "modern": "眼距适中反映杏仁核与前额叶平衡，与共情能力和决策理性相关。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "INFJ",
                    "ENFJ"
            ],
            "strength": "洞察力强，善于协调团队",
            "risk": "过度敏感，易受他人情绪影响",
            "advice": "建立情绪边界，每天留出30分钟独处时间。重要决策前先写日记梳理感受。",
            "category": "综合"
    },
    {
            "id": "F225",
            "feature": "鼻子",
            "feature_key": "nose_width",
            "condition": ">=0.28",
            "traditional": "《神相全编》载：鼻梁直而准头圆，财帛丰盈。鼻如悬胆，家业兴隆。",
            "modern": "鼻型与睾酮水平相关，宽鼻翼者代谢率较高，体现资源获取能力。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESTP",
                    "ESFP"
            ],
            "strength": "行动力强，善于把握商机",
            "risk": "冲动消费，缺乏长期规划",
            "advice": "设置自动储蓄账户，每月固定存20%收入。投资前咨询专业顾问，避免跟风。",
            "category": "综合"
    },
    {
            "id": "F226",
            "feature": "嘴巴",
            "feature_key": "lowerface_ratio",
            "condition": ">=0.32",
            "traditional": "《麻衣相法》云：口如四字，朱唇含丹，主衣食丰足。唇红齿白，言语有信。",
            "modern": "唇形饱满与血清素水平相关，厚唇者表达欲强，社交网络更广。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP",
                    "ESFJ"
            ],
            "strength": "感染力强，善于建立人脉",
            "risk": "言语过多，易泄露隐私",
            "advice": "重要谈话前先列提纲，控制发言时间。使用‘三明治沟通法’：肯定-建议-鼓励。",
            "category": "综合"
    },
    {
            "id": "F227",
            "feature": "耳朵",
            "feature_key": "face_ratio",
            "condition": ">=0.18",
            "traditional": "《柳庄相法》曰：耳高于眉，聪慧过人。耳垂厚大，福寿绵长。",
            "modern": "耳位高与听觉皮层发育相关，体现信息处理速度和记忆力优势。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ISFJ"
            ],
            "strength": "专注力强，善于深度思考",
            "risk": "社交回避，信息过载",
            "advice": "每天安排2小时无干扰工作时段。使用番茄工作法，每25分钟休息5分钟。",
            "category": "综合"
    },
    {
            "id": "F228",
            "feature": "颧骨",
            "feature_key": "midface_ratio",
            "condition": ">=0.26",
            "traditional": "《冰鉴》云：颧骨高耸，权倾朝野。两颧插鬓，威仪自生。",
            "modern": "颧骨突出与雄激素受体密度相关，体现领导力和竞争意识。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTJ"
            ],
            "strength": "决策果断，善于掌控局面",
            "risk": "刚愎自用，团队凝聚力不足",
            "advice": "重大决策前召开头脑风暴会，鼓励反对意见。每月进行一次360度反馈评估。",
            "category": "综合"
    },
    {
            "id": "F229",
            "feature": "下巴",
            "feature_key": "jaw_angle",
            "condition": ">=0.22",
            "traditional": "《神相全编》载：地阁方圆，承浆有肉，主晚年安稳。下巴丰满，福泽深厚。",
            "modern": "下颌角发育与咬肌力量相关，体现坚韧性和抗压能力。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTP",
                    "INTP"
            ],
            "strength": "抗压性强，善于解决复杂问题",
            "risk": "固执己见，适应变化慢",
            "advice": "每周尝试一个新技能或新路线。遇到反对意见时，先复述对方观点再回应。",
            "category": "综合"
    },
    {
            "id": "F230",
            "feature": "面型",
            "feature_key": "face_ratio",
            "condition": ">=0.72",
            "traditional": "《麻衣相法》云：面如满月，清秀而润，主富贵。方正面阔，仁义忠厚。",
            "modern": "面型宽长比与睾酮水平相关，方脸者更易获得信任，圆脸者亲和力更强。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ENFJ"
            ],
            "strength": "亲和力强，善于团队协作",
            "risk": "易妥协，缺乏原则性",
            "advice": "重要谈判前设定底线清单，坚持核心诉求。使用‘破唱片法’重复关键条款。",
            "category": "综合"
    },
    {
            "id": "F231",
            "feature": "气色",
            "feature_key": "综合",
            "condition": "综合评估",
            "traditional": "《冰鉴》云：面色黄明，如绢裹栝楼，主吉。青黑之气，如雾如烟，主灾。",
            "modern": "面色与微循环和激素水平相关，红润者皮质醇较低，体现压力管理能力。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "INFP",
                    "ISFP"
            ],
            "strength": "情绪感知敏锐，善于艺术表达",
            "risk": "情绪波动大，易受环境影响",
            "advice": "建立晨间仪式：冥想10分钟+写感恩日记。每周安排2次户外运动，接触自然光。",
            "category": "综合"
    },
    {
            "feature": "极高额",
            "feature_key": "forehead_ratio",
            "condition": ">=0.42",
            "traditional": "《神相全编》云：额如覆肝，位极人臣；额高而满，早登金榜。",
            "modern": "与智力开放性极高相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "INTP"
            ],
            "strength": "远见卓识",
            "risk": "脱离现实",
            "advice": "多与务实者合作",
            "category": "上庭",
            "id": "F232"
    },
    {
            "feature": "极窄额",
            "feature_key": "forehead_ratio",
            "condition": "<=0.24",
            "traditional": "《麻衣相法》云：额窄眉低，少年困苦；额小无纹，一生劳碌。",
            "modern": "与保守性极高相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ISTJ"
            ],
            "strength": "务实谨慎",
            "risk": "缺乏创新",
            "advice": "主动接触新事物",
            "category": "上庭",
            "id": "F233"
    },
    {
            "feature": "极宽鼻",
            "feature_key": "nose_width",
            "condition": ">=0.28",
            "traditional": "《相理衡真》曰：鼻大而宽，财源广进；鼻梁低陷，反主破败。",
            "modern": "与支配性极高相关",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "高",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTP"
            ],
            "strength": "魄力十足",
            "risk": "冲动鲁莽",
            "advice": "决策前多思考",
            "category": "中庭",
            "id": "F234"
    },
    {
            "feature": "极细鼻",
            "feature_key": "nose_width",
            "condition": "<=0.14",
            "traditional": "《冰鉴》云：鼻细如锥，心性刻薄；鼻梁尖削，多疑寡合。",
            "modern": "与敏感性极高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "INFJ",
                    "INFP"
            ],
            "strength": "洞察入微",
            "risk": "过度敏感",
            "advice": "培养钝感力",
            "category": "中庭",
            "id": "F235"
    },
    {
            "feature": "极宽眼距",
            "feature_key": "eye_distance",
            "condition": ">=0.38",
            "traditional": "《人伦大统赋》注：眼距开阔，心胸宽广；目若流星，智谋过人。",
            "modern": "与开放性极高相关",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP",
                    "ENTP"
            ],
            "strength": "包容性强",
            "risk": "缺乏专注",
            "advice": "设定明确优先级",
            "category": "中庭",
            "id": "F236"
    },
    {
            "feature": "极窄眼距",
            "feature_key": "eye_distance",
            "condition": "<=0.22",
            "traditional": "《相法集成》云：眼距过窄，心胸狭隘；目露凶光，易招是非。",
            "modern": "与尽责性极高相关",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "专注细致",
            "risk": "固执己见",
            "advice": "学会换位思考",
            "category": "中庭",
            "id": "F237"
    },
    {
            "feature": "极圆颌",
            "feature_key": "jaw_angle",
            "condition": ">=145",
            "traditional": "《柳庄相法》曰：下颏圆润，晚景丰隆；地阁方圆，福寿双全。",
            "modern": "与宜人性极高相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ENFJ"
            ],
            "strength": "亲和力强",
            "risk": "缺乏原则",
            "advice": "学会拒绝",
            "category": "下庭",
            "id": "F238"
    },
    {
            "feature": "极锐颌",
            "feature_key": "jaw_angle",
            "condition": "<=95",
            "traditional": "《相理衡真》云：下巴尖削，晚年孤苦；颐颔无肉，心性刻薄。",
            "modern": "与神经质极高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "ISTP"
            ],
            "strength": "决断力强",
            "risk": "人际关系紧张",
            "advice": "培养同理心",
            "category": "下庭",
            "id": "F239"
    },
    {
            "feature": "极长脸",
            "feature_key": "face_ratio",
            "condition": ">=1.25",
            "traditional": "《麻衣相法》云：面长如驴，奔波劳碌；天庭饱满，反主贵格。",
            "modern": "与尽责性极高相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ",
                    "INTJ"
            ],
            "strength": "坚韧不拔",
            "risk": "刻板僵化",
            "advice": "适当放松",
            "category": "面型",
            "id": "F240"
    },
    {
            "feature": "极圆脸",
            "feature_key": "face_ratio",
            "condition": "<=0.82",
            "traditional": "《神相全编》曰：面圆如盘，富足安康；肉多骨少，反主愚钝。",
            "modern": "与外向性极高相关",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFP",
                    "ENFP"
            ],
            "strength": "乐观开朗",
            "risk": "缺乏深度",
            "advice": "培养独立思考",
            "category": "面型",
            "id": "F241"
    },
    {
            "feature": "面色红润",
            "feature_key": "综合",
            "condition": "面色红润有光泽",
            "traditional": "《神相全编》云：面色红润如敷粉，主福寿双全。",
            "modern": "与情绪稳定、心血管健康相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ"
            ],
            "strength": "亲和力强",
            "risk": "易情绪外露",
            "advice": "保持平和心态",
            "category": "综合",
            "id": "F242"
    },
    {
            "feature": "面色苍白",
            "feature_key": "综合",
            "condition": "面色苍白无血色",
            "traditional": "《太清神鉴》曰：面色白如枯骨，主气血亏虚。",
            "modern": "与贫血、压力大相关",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "低",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "INFP"
            ],
            "strength": "内省深刻",
            "risk": "易疲劳",
            "advice": "注意饮食与休息",
            "category": "综合",
            "id": "F243"
    },
    {
            "feature": "面色青黑",
            "feature_key": "综合",
            "condition": "面色青黑如铁",
            "traditional": "《相理衡真》云：面色青黑，主灾厄缠身。",
            "modern": "与肝脏功能、情绪压抑相关",
            "ocean": {
                    "O": "低",
                    "C": "低",
                    "E": "低",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ"
            ],
            "strength": "坚韧不拔",
            "risk": "易积郁",
            "advice": "多运动释放压力",
            "category": "综合",
            "id": "F244"
    },
    {
            "feature": "面色黄暗",
            "feature_key": "综合",
            "condition": "面色黄暗如土",
            "traditional": "《麻衣相法》云：面色黄暗，主脾胃不和。",
            "modern": "与消化系统、代谢问题相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISFJ"
            ],
            "strength": "稳重务实",
            "risk": "易倦怠",
            "advice": "调理饮食作息",
            "category": "综合",
            "id": "F245"
    },
    {
            "feature": "印堂发亮",
            "feature_key": "综合",
            "condition": "印堂部位光亮润泽",
            "traditional": "《玉管照神局》曰：印堂明润，主运势亨通。",
            "modern": "与自信心、决策力相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTJ"
            ],
            "strength": "领导力强",
            "risk": "易自负",
            "advice": "保持谦逊",
            "category": "综合",
            "id": "F246"
    },
    {
            "feature": "耳高于眉",
            "feature_key": "综合",
            "condition": "耳廓上缘高于眉毛",
            "traditional": "《相理衡真》云：耳高于眉，主聪明贵显。",
            "modern": "与认知能力、早慧相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ"
            ],
            "strength": "思维敏捷",
            "risk": "易孤傲",
            "advice": "多与人交流",
            "category": "综合",
            "id": "F247"
    },
    {
            "feature": "耳垂厚大",
            "feature_key": "综合",
            "condition": "耳垂厚实宽大",
            "traditional": "《麻衣相法》曰：耳垂厚大，主福寿绵长。",
            "modern": "与包容性、财运相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFP"
            ],
            "strength": "人缘好",
            "risk": "易安逸",
            "advice": "保持进取心",
            "category": "综合",
            "id": "F248"
    },
    {
            "feature": "招风耳",
            "feature_key": "综合",
            "condition": "耳廓明显外张",
            "traditional": "《神相全编》云：招风耳，主奔波劳碌。",
            "modern": "与好奇心强、不安分相关",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ENFP"
            ],
            "strength": "勇于尝试",
            "risk": "易冲动",
            "advice": "三思而后行",
            "category": "综合",
            "id": "F249"
    },
    {
            "feature": "贴脑耳",
            "feature_key": "综合",
            "condition": "耳廓紧贴头部",
            "traditional": "《太清神鉴》曰：贴脑耳，主稳重有谋。",
            "modern": "与谨慎、内敛相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTP"
            ],
            "strength": "冷静分析",
            "risk": "易保守",
            "advice": "适当冒险",
            "category": "综合",
            "id": "F250"
    },
    {
            "feature": "耳廓分明",
            "feature_key": "综合",
            "condition": "耳廓轮廓清晰分明",
            "traditional": "《相理衡真》云：耳廓分明，主聪慧明理。",
            "modern": "与逻辑思维、条理性相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTP"
            ],
            "strength": "善于分析",
            "risk": "易挑剔",
            "advice": "包容不同观点",
            "category": "综合",
            "id": "F251"
    },
    {
            "feature": "额头痣",
            "feature_key": "综合",
            "condition": "额头正中或偏侧有痣",
            "traditional": "《麻衣相法》云：额上有痣，主早年运势起伏。",
            "modern": "与早年经历、家庭影响相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFJ"
            ],
            "strength": "有远见",
            "risk": "易分心",
            "advice": "专注当下",
            "category": "综合",
            "id": "F252"
    },
    {
            "feature": "眉中痣",
            "feature_key": "综合",
            "condition": "眉毛中间有痣",
            "traditional": "《神相全编》曰：眉中藏痣，主才华内敛。",
            "modern": "与创造力、隐秘才能相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "INFJ"
            ],
            "strength": "洞察力强",
            "risk": "易多疑",
            "advice": "信任他人",
            "category": "综合",
            "id": "F253"
    },
    {
            "feature": "眼角痣",
            "feature_key": "综合",
            "condition": "眼角附近有痣",
            "traditional": "《相理衡真》云：眼角生痣，主情感丰富。",
            "modern": "与感性、人际关系相关",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "ENFP"
            ],
            "strength": "善解人意",
            "risk": "易情绪化",
            "advice": "理性决策",
            "category": "综合",
            "id": "F254"
    },
    {
            "feature": "鼻头痣",
            "feature_key": "综合",
            "condition": "鼻头有痣",
            "traditional": "《太清神鉴》曰：鼻头有痣，主财运波动。",
            "modern": "与理财能力、物质观相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ESTP"
            ],
            "strength": "行动力强",
            "risk": "易冲动消费",
            "advice": "制定预算",
            "category": "综合",
            "id": "F255"
    },
    {
            "feature": "下巴痣",
            "feature_key": "综合",
            "condition": "下巴有痣",
            "traditional": "《麻衣相法》云：下巴有痣，主晚年安稳。",
            "modern": "与耐力、家庭观念相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ"
            ],
            "strength": "坚韧可靠",
            "risk": "易固执",
            "advice": "灵活变通",
            "category": "综合",
            "id": "F256"
    },
    {
            "feature": "窄额",
            "feature_key": "forehead_ratio",
            "condition": "<0.32",
            "traditional": "《麻衣相法》曰：额窄而低，主劳碌。",
            "modern": "与保守性正相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ISFJ",
                    "ESTP",
                    "ISTP",
                    "ESTJ",
                    "ISFP"
            ],
            "strength": "务实稳重",
            "risk": "易缺乏远见",
            "advice": "多学习新知识",
            "category": "上庭",
            "id": "F257"
    },
    {
            "feature": "高额头+锐利下巴+窄鼻梁",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38, chin_angle<=0.25, nose_width<=0.18",
            "traditional": "《神相全编》云：额高而方，鼻梁如削，下巴如锥，主掌权柄。",
            "modern": "与领导力、决断力、专注力高相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTJ"
            ],
            "strength": "战略视野与执行力",
            "risk": "易刚愎自用",
            "advice": "定期听取下属反馈，避免独断专行",
            "category": "综合",
            "id": "F258"
    },
    {
            "feature": "高额头+窄眼睛+窄鼻梁",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38, eye_width<=0.22, nose_width<=0.18",
            "traditional": "《相理衡真》曰：额高目深，鼻细如管，主智谋深远。",
            "modern": "与逻辑思维、专注力、技术洞察力高相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "INTP"
            ],
            "strength": "技术架构与创新",
            "risk": "易忽视用户体验",
            "advice": "多与产品团队沟通，平衡技术与需求",
            "category": "综合",
            "id": "F259"
    },
    {
            "feature": "高额头+宽眼睛+上扬眉毛",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38, eye_width>=0.28, eyebrow_angle>=0.15",
            "traditional": "《麻衣相法》云：眉扬目秀，额阔天仓，主才艺出众。",
            "modern": "与创造力、审美力、开放性高相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFP",
                    "INFP"
            ],
            "strength": "视觉创意与用户洞察",
            "risk": "易陷入完美主义",
            "advice": "设定明确截止时间，避免过度修改",
            "category": "综合",
            "id": "F260"
    },
    {
            "feature": "宽鼻梁+圆下巴+宽眼睛",
            "feature_key": "综合",
            "condition": "nose_width>=0.22, chin_roundness>=0.7, eye_width>=0.28",
            "traditional": "《玉管照神局》曰：鼻圆准丰，颐圆目大，主聚财得众。",
            "modern": "与社交能力、亲和力、说服力高相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ENFJ"
            ],
            "strength": "客户关系与团队激励",
            "risk": "易过度承诺",
            "advice": "建立客户筛选机制，避免资源分散",
            "category": "综合",
            "id": "F261"
    },
    {
            "feature": "宽鼻梁+圆下巴+平和眉毛",
            "feature_key": "综合",
            "condition": "nose_width>=0.22, chin_roundness>=0.7, eyebrow_flatness<=0.05",
            "traditional": "《柳庄相法》云：鼻圆颐满，眉平如一字，主仁厚善调。",
            "modern": "与同理心、稳定性、协调力高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "INFJ"
            ],
            "strength": "员工关怀与制度执行",
            "risk": "易回避冲突",
            "advice": "定期进行绩效面谈，主动处理矛盾",
            "category": "综合",
            "id": "F262"
    },
    {
            "feature": "窄鼻梁+锐利下巴+窄眼睛",
            "feature_key": "综合",
            "condition": "nose_width<=0.18, chin_angle<=0.25, eye_width<=0.22",
            "traditional": "《金锁赋》曰：鼻削颐尖，目小如鹰，主辩才无碍。",
            "modern": "与逻辑分析、辩论能力、细节关注高相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "ISTJ"
            ],
            "strength": "法律条文解读与证据链构建",
            "risk": "易钻牛角尖",
            "advice": "培养同理心，避免过度对抗",
            "category": "综合",
            "id": "F263"
    },
    {
            "feature": "宽鼻梁+平和眉毛+窄眼睛",
            "feature_key": "综合",
            "condition": "nose_width>=0.22, eyebrow_flatness<=0.05, eye_width<=0.22",
            "traditional": "《相法心传》云：鼻宽眉平，目藏神，主仁心定力。",
            "modern": "与耐心、细致、责任感高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ISFJ"
            ],
            "strength": "诊断准确性与操作稳定性",
            "risk": "易过度保守",
            "advice": "定期学习新技术，避免经验主义",
            "category": "中庭",
            "id": "F264"
    },
    {
            "feature": "宽眼睛+上扬眉毛+锐利下巴",
            "feature_key": "综合",
            "condition": "eye_width>=0.28, eyebrow_angle>=0.15, chin_angle<=0.25",
            "traditional": "《相理衡真》云：目秀眉扬，颐尖如削，主探幽发微。",
            "modern": "与好奇心、表达力、批判性思维高相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTP",
                    "ENFP"
            ],
            "strength": "新闻敏感度与深度采访",
            "risk": "易主观臆断",
            "advice": "坚持多方核实，避免偏听偏信",
            "category": "综合",
            "id": "F265"
    },
    {
            "feature": "宽鼻梁+宽眼睛+圆下巴",
            "feature_key": "综合",
            "condition": "nose_width>=0.22, eye_width>=0.28, chin_roundness>=0.7",
            "traditional": "《麻衣相法》云：鼻圆目大，颐满如月，主慈心善解。",
            "modern": "与共情力、倾听力、包容性高相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "INFJ",
                    "ENFJ"
            ],
            "strength": "深度共情与信任建立",
            "risk": "易情感透支",
            "advice": "设定咨询边界，定期自我督导",
            "category": "综合",
            "id": "F266"
    },
    {
            "feature": "窄眼睛+窄鼻梁+窄额头",
            "feature_key": "综合",
            "condition": "eye_width<=0.22, nose_width<=0.18, forehead_ratio<=0.32",
            "traditional": "《神相全编》曰：目小鼻细，额窄如削，主精算善析。",
            "modern": "与逻辑严谨性、专注力、数据敏感度高相关",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTJ",
                    "INTJ"
            ],
            "strength": "数据建模与异常检测",
            "risk": "易忽略业务背景",
            "advice": "定期与业务部门交流，理解数据含义",
            "category": "综合",
            "id": "F267"
    },
    {
            "feature": "中等额头+宽眼睛+中等鼻梁",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.33, forehead_ratio<=0.37, eye_width>=0.28, nose_width>=0.19, nose_width<=0.21",
            "traditional": "《玉管照神局》云：额中正，目秀鼻匀，主调和之才。",
            "modern": "与协调能力、用户思维、沟通力高相关",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFJ",
                    "ESFJ"
            ],
            "strength": "需求转化与跨部门协作",
            "risk": "易陷入细节争议",
            "advice": "建立优先级矩阵，聚焦核心功能",
            "category": "综合",
            "id": "F268"
    },
    {
            "feature": "宽鼻梁+圆下巴+中等眼睛",
            "feature_key": "综合",
            "condition": "nose_width>=0.22, chin_roundness>=0.7, eye_width>=0.23, eye_width<=0.27",
            "traditional": "《柳庄相法》曰：鼻圆颐满，目平而正，主务实善营。",
            "modern": "与执行力、亲和力、稳定性高相关",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ISFJ"
            ],
            "strength": "活动策划与用户运营",
            "risk": "易陷入重复性工作",
            "advice": "引入自动化工具，提升运营效率",
            "category": "综合",
            "id": "F269"
    },
    {
            "feature": "高额头+锐利下巴+窄眼睛",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38, chin_angle<=0.25, eye_width<=0.22",
            "traditional": "《相法心传》云：额高颐锐，目深如潭，主远见善断。",
            "modern": "与风险判断、长期视野、冷静决策高相关",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTJ"
            ],
            "strength": "趋势预判与资产配置",
            "risk": "易过度自信",
            "advice": "建立投资委员会，引入外部视角",
            "category": "综合",
            "id": "F270"
    },
    {
            "feature": "高额头+宽眼睛+锐利下巴",
            "feature_key": "综合",
            "condition": "forehead_ratio>=0.38, eye_width>=0.28, chin_angle<=0.25",
            "traditional": "《太清神鉴》曰：额阔目朗，颐尖如锥，主开创之魄。",
            "modern": "与冒险精神、愿景力、执行力高相关",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTP",
                    "ENTJ"
            ],
            "strength": "机会识别与快速试错",
            "risk": "易忽视风险",
            "advice": "设置最小可行产品验证，控制试错成本",
            "category": "综合",
            "id": "F271"
    },
    {
            "feature": "宽眼距+高额（全景型）",
            "feature_key": "eye_distance",
            "condition": ">=0.33",
            "traditional": "《神相全编》云：『目距阔而额隆，如星悬穹顶，主见远识广，气度恢弘。』",
            "modern": "高额象征认知开放，宽眼距强化全局视野，对应OCEAN中高开放性、高外向性；MBTI常为ENFP或ENTP，擅长发散思维与战略规划。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENFP",
                    "ENTP"
            ],
            "strength": "宏观洞察力强，善于整合信息，创新思维活跃。",
            "risk": "易忽视细节，决策可能过于理想化，缺乏落地执行力。",
            "advice": "搭配具体数据或团队执行者，将宏大构想分解为可操作步骤。",
            "category": "眉眼",
            "id": "F272"
    },
    {
            "feature": "宽眼距+宽鼻（包容型）",
            "feature_key": "eye_distance",
            "condition": ">=0.33",
            "traditional": "《月波洞中记》曰：『鼻阔眼疏，如海纳百川，性宽厚而善容。』",
            "modern": "宽鼻象征亲和力与包容度，宽眼距强化接纳性，对应OCEAN中高宜人性、低神经质；MBTI常为ESFJ或ISFJ，擅长协调人际关系。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ",
                    "ISFJ"
            ],
            "strength": "团队凝聚力强，善于化解矛盾，营造和谐氛围。",
            "risk": "过度妥协可能导致原则模糊，易被他人影响。",
            "advice": "在关键决策时坚持底线，学会温和而坚定地表达立场。",
            "category": "中庭",
            "id": "F273"
    },
    {
            "feature": "宽眼距+上扬眉（探索型）",
            "feature_key": "eye_distance",
            "condition": ">=0.33",
            "traditional": "《相理衡真》载：『眉扬目阔，志在四方，好新奇而厌守旧。』",
            "modern": "上扬眉象征进取心与好奇心，宽眼距增强探索欲，对应OCEAN中高开放性、高外向性；MBTI常为ESTP或ENTP，热衷冒险与尝试。",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESTP",
                    "ENTP"
            ],
            "strength": "行动力强，快速适应新环境，善于抓住机遇。",
            "risk": "缺乏耐心，易半途而废，需注意风险控制。",
            "advice": "设定短期里程碑，用阶段性成果维持动力，并培养复盘习惯。",
            "category": "眉眼",
            "id": "F274"
    },
    {
            "feature": "宽眼距+圆下巴（开放型）",
            "feature_key": "eye_distance",
            "condition": ">=0.33",
            "traditional": "《冰鉴》有言：『颐圆目阔，心宽体胖，乐天知命，不滞于物。』",
            "modern": "圆下巴象征随和与享受当下，宽眼距强化开放心态，对应OCEAN中高宜人性、高外向性；MBTI常为ESFP或ENFP，擅长社交与娱乐。",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFP",
                    "ENFP"
            ],
            "strength": "感染力强，能活跃气氛，人际关系广泛。",
            "risk": "易沉迷享乐，缺乏长远规划，责任感可能不足。",
            "advice": "培养时间管理能力，将娱乐与目标结合，如通过社交推动项目。",
            "category": "下庭",
            "id": "F275"
    },
    {
            "feature": "宽眼距+锐颌（战略型）",
            "feature_key": "eye_distance",
            "condition": ">=0.33",
            "traditional": "《玉管照神局》云：『颌锐目疏，智谋深远，能运筹帷幄之中。』",
            "modern": "锐颌象征决断力与目标导向，宽眼距增强战略视野，对应OCEAN中高尽责性、高开放性；MBTI常为INTJ或ENTJ，擅长长期规划。",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTJ"
            ],
            "strength": "战略思维清晰，执行力强，能平衡宏观与微观。",
            "risk": "可能显得冷漠或固执，忽视团队情感需求。",
            "advice": "定期与团队沟通愿景，用共情方式传递决策逻辑。",
            "category": "下庭",
            "id": "F276"
    },
    {
            "feature": "窄眼距+窄额（聚焦型）",
            "feature_key": "eye_distance",
            "condition": "<=0.26",
            "traditional": "《神相全编》曰：『额窄目聚，心专一志，如锥入囊，锋芒毕露。』",
            "modern": "窄额象征专注力强，窄眼距强化深度聚焦，对应OCEAN中高尽责性、低开放性；MBTI常为ISTJ或INTJ，擅长精细执行。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "INTJ"
            ],
            "strength": "细节把控力强，工作严谨，能高效完成重复性任务。",
            "risk": "视野狭窄，难以适应变化，易陷入思维定势。",
            "advice": "定期接触跨领域信息，用外部视角打破认知局限。",
            "category": "五官",
            "id": "F277"
    },
    {
            "feature": "窄眼距+窄鼻（精准型）",
            "feature_key": "eye_distance",
            "condition": "<=0.26",
            "traditional": "《月波洞中记》载：『鼻狭目近，察秋毫之末，性苛而精。』",
            "modern": "窄鼻象征追求精确与标准，窄眼距强化分析能力，对应OCEAN中高尽责性、低宜人性；MBTI常为ISTP或INTP，擅长逻辑推理。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTP",
                    "INTP"
            ],
            "strength": "逻辑严密，擅长技术攻关，能发现细微错误。",
            "risk": "批判性强，易苛责他人，团队合作可能受阻。",
            "advice": "在指出问题时先肯定对方优点，用建设性语言沟通。",
            "category": "中庭",
            "id": "F278"
    },
    {
            "feature": "窄眼距+锐颌（穿透型）",
            "feature_key": "eye_distance",
            "condition": "<=0.26",
            "traditional": "《冰鉴》有言：『颌锐目逼，志在必得，如箭在弦，一发中的。』",
            "modern": "锐颌象征目标坚定，窄眼距强化穿透力，对应OCEAN中高尽责性、高神经质；MBTI常为ESTJ或ENTJ，擅长攻坚克难。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "高",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ESTJ",
                    "ENTJ"
            ],
            "strength": "目标感极强，抗压能力好，能突破瓶颈。",
            "risk": "易急躁冲动，忽视他人感受，可能引发冲突。",
            "advice": "在高压时主动暂停，用深呼吸或短休息平复情绪。",
            "category": "下庭",
            "id": "F279"
    },
    {
            "feature": "窄眼距+平和眉（深耕型）",
            "feature_key": "eye_distance",
            "condition": "<=0.26",
            "traditional": "《相理衡真》云：『眉平目聚，沉静有恒，如老农耕田，不疾不徐。』",
            "modern": "平和眉象征情绪稳定与耐心，窄眼距强化持续专注，对应OCEAN中低神经质、高尽责性；MBTI常为ISFJ或ISTJ，擅长长期深耕。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ISTJ"
            ],
            "strength": "持久力强，能忍受枯燥，适合研究或工匠型工作。",
            "risk": "创新不足，可能抗拒新方法，效率提升缓慢。",
            "advice": "定期尝试小范围改进，用渐进式创新积累突破。",
            "category": "眉眼",
            "id": "F280"
    },
    {
            "feature": "窄眼距+圆下巴（谨慎型）",
            "feature_key": "eye_distance",
            "condition": "<=0.26",
            "traditional": "《玉管照神局》载：『颐圆目近，外和内刚，步步为营，不越雷池。』",
            "modern": "圆下巴象征表面随和，窄眼距强化谨慎特质，对应OCEAN中高宜人性、高神经质；MBTI常为ISFP或INFP，擅长风险规避。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "低",
                    "A": "高",
                    "N": "高"
            },
            "mbti_hint": [
                    "ISFP",
                    "INFP"
            ],
            "strength": "风险意识强，决策稳健，能保护团队免受损失。",
            "risk": "过度保守，可能错失良机，行动力不足。",
            "advice": "设定安全边界后，尝试小规模试错，逐步扩大行动范围。",
            "category": "下庭",
            "id": "F281"
    },
    {
            "feature": "中等眼距+方额（平衡型）",
            "feature_key": "eye_distance",
            "condition": "0.27-0.32",
            "traditional": "《神相全编》曰：『额方目均，中正不偏，处事有度，进退自如。』",
            "modern": "方额象征稳重与原则，中等眼距强化平衡能力，对应OCEAN中高尽责性、中开放性；MBTI常为ISTJ或ESTJ，擅长规则执行。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "决策公正，能兼顾多方利益，适合管理岗位。",
            "risk": "可能缺乏灵活性，在复杂情境中反应较慢。",
            "advice": "学习权变管理，根据情境调整规则优先级。",
            "category": "五官",
            "id": "F282"
    },
    {
            "feature": "中等眼距+直鼻（稳健型）",
            "feature_key": "eye_distance",
            "condition": "0.27-0.32",
            "traditional": "《月波洞中记》载：『鼻直目匀，心正行端，不偏不倚，可托大事。』",
            "modern": "直鼻象征正直与可靠，中等眼距强化稳定性，对应OCEAN中高宜人性、高尽责性；MBTI常为ISFJ或ESFJ，擅长后勤支持。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "值得信赖，执行力强，能维护团队秩序。",
            "risk": "创新动力不足，可能过于依赖既有流程。",
            "advice": "主动参与头脑风暴，用结构化方法激发新思路。",
            "category": "中庭",
            "id": "F283"
    },
    {
            "feature": "中等眼距+平和眉（协调型）",
            "feature_key": "eye_distance",
            "condition": "0.27-0.32",
            "traditional": "《冰鉴》有言：『眉平目正，心气和平，能调众口，化干戈为玉帛。』",
            "modern": "平和眉象征情绪稳定，中等眼距强化协调能力，对应OCEAN中低神经质、高宜人性；MBTI常为INFJ或ENFJ，擅长调解冲突。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "INFJ",
                    "ENFJ"
            ],
            "strength": "共情力强，能理解多方立场，促进团队合作。",
            "risk": "易过度牺牲自我，可能积累压力。",
            "advice": "设定个人边界，定期通过独处或爱好恢复能量。",
            "category": "眉眼",
            "id": "F284"
    },
    {
            "feature": "中等眼距+圆下巴（亲和型）",
            "feature_key": "eye_distance",
            "condition": "0.27-0.32",
            "traditional": "《相理衡真》云：『颐圆目正，和蔼可亲，人皆乐与之交。』",
            "modern": "圆下巴象征亲和力，中等眼距强化社交平衡，对应OCEAN中高外向性、高宜人性；MBTI常为ESFP或ENFP，擅长人际互动。",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFP",
                    "ENFP"
            ],
            "strength": "社交魅力强，能快速建立信任，活跃团队氛围。",
            "risk": "可能过于注重关系，忽视任务进度。",
            "advice": "用社交作为激励手段，将人际互动与工作目标挂钩。",
            "category": "下庭",
            "id": "F285"
    },
    {
            "feature": "中等眼距+锐颌（执行型）",
            "feature_key": "eye_distance",
            "condition": "0.27-0.32",
            "traditional": "《玉管照神局》载：『颌锐目均，刚柔并济，能屈能伸，成事之器。』",
            "modern": "锐颌象征决断力，中等眼距强化执行平衡，对应OCEAN中高尽责性、中外向性；MBTI常为ESTJ或ENTJ，擅长项目推进。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESTJ",
                    "ENTJ"
            ],
            "strength": "执行力强，能快速将计划转化为行动，结果导向。",
            "risk": "可能忽略细节或团队感受，导致执行偏差。",
            "advice": "在关键节点设置检查点，并主动征求反馈。",
            "category": "下庭",
            "id": "F286"
    },
    {
            "feature": "宽眼+窄鼻+上扬眉",
            "feature_key": "综合",
            "condition": "眼距宽于眼长1/3，鼻翼宽度小于鼻长1/3，眉尾高于眉头15度以上",
            "traditional": "《相理衡真》云：'目广而鼻狭者，性灵而志远，眉扬者气宇轩昂。'",
            "modern": "此类人想象力丰富，思维跳跃，适合创新领域，但可能缺乏耐心。",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "中",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "ENFP",
                    "ENTP"
            ],
            "strength": "创意无限，善于打破常规",
            "risk": "易虎头蛇尾，忽略细节",
            "advice": "培养专注力，将创意落地为具体计划，可尝试每日列清单。",
            "category": "五官",
            "id": "F287"
    },
    {
            "feature": "窄眼+宽鼻+平和眉",
            "feature_key": "综合",
            "condition": "眼距窄于眼长1/3，鼻翼宽度大于鼻长1/3，眉尾与眉头水平",
            "traditional": "《神相全编》曰：'目狭鼻阔者，性厚而近人，眉平者心气和顺。'",
            "modern": "亲和力强，善于倾听，适合服务或团队协作角色。",
            "ocean": {
                    "O": "低",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ESFJ"
            ],
            "strength": "温暖可靠，人际关系融洽",
            "risk": "易过度迁就，失去自我边界",
            "advice": "学会说'不'，保护个人时间，同时发挥共情优势。",
            "category": "五官",
            "id": "F288"
    },
    {
            "feature": "宽眼+宽鼻+下垂眉",
            "feature_key": "综合",
            "condition": "眼距宽于眼长1/3，鼻翼宽度大于鼻长1/3，眉尾低于眉头10度以上",
            "traditional": "《相经》有云：'目广鼻阔眉垂者，情深易感，善体物情。'",
            "modern": "情感丰富，敏感细腻，艺术感知力强，但易情绪化。",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "低",
                    "A": "高",
                    "N": "高"
            },
            "mbti_hint": [
                    "INFP",
                    "INFJ"
            ],
            "strength": "共情力强，富有创造力",
            "risk": "易陷入忧郁，决策犹豫",
            "advice": "建立情绪日记，定期复盘，用理性平衡感性。",
            "category": "五官",
            "id": "F289"
    },
    {
            "feature": "窄眼+窄鼻+上扬眉",
            "feature_key": "综合",
            "condition": "眼距窄于眼长1/3，鼻翼宽度小于鼻长1/3，眉尾高于眉头15度以上",
            "traditional": "《冰鉴》云：'目狭鼻细眉扬者，志锐而思深，善谋断。'",
            "modern": "逻辑性强，目标明确，适合分析型或管理岗位。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "ISTJ"
            ],
            "strength": "专注高效，善于战略规划",
            "risk": "易固执己见，忽视他人感受",
            "advice": "多倾听团队意见，培养灵活性，避免过度批判。",
            "category": "五官",
            "id": "F290"
    },
    {
            "feature": "中眼+中鼻+平和眉",
            "feature_key": "综合",
            "condition": "眼距与眼长比例1:1，鼻翼宽度与鼻长比例1:1，眉尾与眉头水平",
            "traditional": "《相理衡真》曰：'五岳匀停，眉目平正，乃中和之相。'",
            "modern": "性格均衡，适应力强，适合多领域发展。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTP",
                    "ESFP"
            ],
            "strength": "稳定可靠，善于协调",
            "risk": "可能缺乏鲜明个性，易被忽视",
            "advice": "主动展示特长，尝试突破舒适区，培养独特优势。",
            "category": "五官",
            "id": "F291"
    },
    {
            "feature": "宽眼+窄鼻+平和眉",
            "feature_key": "综合",
            "condition": "眼距宽于眼长1/3，鼻翼宽度小于鼻长1/3，眉尾与眉头水平",
            "traditional": "《神相全编》云：'目宽鼻细眉平者，善察而心静，宜为观察之职。'",
            "modern": "观察力敏锐，冷静客观，适合研究或分析工作。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTP",
                    "ISTP"
            ],
            "strength": "洞察入微，理性客观",
            "risk": "易疏离人群，显得冷漠",
            "advice": "主动参与社交，培养共情，避免过度沉浸于分析。",
            "category": "五官",
            "id": "F292"
    },
    {
            "feature": "窄眼+宽鼻+上扬眉",
            "feature_key": "综合",
            "condition": "眼距窄于眼长1/3，鼻翼宽度大于鼻长1/3，眉尾高于眉头15度以上",
            "traditional": "《相经》曰：'目狭鼻阔眉扬者，气盛而善辩，有表达之才。'",
            "modern": "表达欲强，善于说服，适合销售或传媒行业。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ESTP"
            ],
            "strength": "自信果敢，感染力强",
            "risk": "易强势，忽略他人意见",
            "advice": "练习倾听，尊重不同观点，用合作代替对抗。",
            "category": "五官",
            "id": "F293"
    },
    {
            "feature": "宽眼+宽鼻+上扬眉",
            "feature_key": "综合",
            "condition": "眼距宽于眼长1/3，鼻翼宽度大于鼻长1/3，眉尾高于眉头15度以上",
            "traditional": "《冰鉴》云：'目广鼻阔眉扬者，器宇宏阔，有领袖之姿。'",
            "modern": "格局宏大，有领导力，适合管理或创业。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "高",
                    "A": "低",
                    "N": "高"
            },
            "mbti_hint": [
                    "ENTJ",
                    "ENFJ"
            ],
            "strength": "远见卓识，善于激励团队",
            "risk": "易自负，忽视细节风险",
            "advice": "保持谦逊，重视执行细节，建立反馈机制。",
            "category": "五官",
            "id": "F294"
    },
    {
            "feature": "窄眼+窄鼻+下垂眉",
            "feature_key": "综合",
            "condition": "眼距窄于眼长1/3，鼻翼宽度小于鼻长1/3，眉尾低于眉头10度以上",
            "traditional": "《相理衡真》曰：'目狭鼻细眉垂者，思深而性幽，喜独处内省。'",
            "modern": "内省深刻，善于自省，适合哲学或研究领域。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "INTP",
                    "INTJ"
            ],
            "strength": "深度思考，洞察本质",
            "risk": "易孤僻，社交能力弱",
            "advice": "定期参与团体活动，练习表达，避免过度封闭。",
            "category": "五官",
            "id": "F295"
    },
    {
            "feature": "中眼+宽鼻+上扬眉",
            "feature_key": "综合",
            "condition": "眼距与眼长比例1:1，鼻翼宽度大于鼻长1/3，眉尾高于眉头15度以上",
            "traditional": "《神相全编》云：'目正鼻阔眉扬者，性豪而善交，有社交之才。'",
            "modern": "社交达人，热情开朗，适合公关或活动策划。",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESFP",
                    "ENFP"
            ],
            "strength": "人脉广泛，感染力强",
            "risk": "易流于表面，深度不足",
            "advice": "培养专注力，在社交中寻找深度连接，避免泛泛之交。",
            "category": "五官",
            "id": "F296"
    },
    {
            "feature": "宽眼+中鼻+下垂眉",
            "feature_key": "综合",
            "condition": "眼距宽于眼长1/3，鼻翼宽度与鼻长比例1:1，眉尾低于眉头10度以上",
            "traditional": "《相经》曰：'目广鼻正眉垂者，思深而性慈，有哲思之韵。'",
            "modern": "哲思型，善于反思，适合学术或心理咨询。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "低",
                    "A": "高",
                    "N": "高"
            },
            "mbti_hint": [
                    "INFJ",
                    "INFP"
            ],
            "strength": "洞察人性，富有智慧",
            "risk": "易过度思虑，行动迟缓",
            "advice": "设定行动截止时间，用实践验证想法，避免空想。",
            "category": "五官",
            "id": "F297"
    },
    {
            "feature": "窄眼+中鼻+平和眉",
            "feature_key": "综合",
            "condition": "眼距窄于眼长1/3，鼻翼宽度与鼻长比例1:1，眉尾与眉头水平",
            "traditional": "《冰鉴》云：'目狭鼻正眉平者，性定而志坚，宜为执行之才。'",
            "modern": "执行力强，踏实可靠，适合项目管理或运营。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "ESTJ"
            ],
            "strength": "高效务实，注重结果",
            "risk": "易刻板，缺乏创新",
            "advice": "尝试新方法，接受不确定性，培养灵活思维。",
            "category": "五官",
            "id": "F298"
    },
    {
            "feature": "中眼+窄鼻+上扬眉",
            "feature_key": "综合",
            "condition": "眼距与眼长比例1:1，鼻翼宽度小于鼻长1/3，眉尾高于眉头15度以上",
            "traditional": "《相理衡真》曰：'目正鼻细眉扬者，智深而谋远，有策略之能。'",
            "modern": "策略型，善于规划，适合咨询或战略岗位。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "INTJ",
                    "ENTJ"
            ],
            "strength": "思维缜密，善于布局",
            "risk": "易过于算计，缺乏人情味",
            "advice": "平衡理性与感性，关注团队情感，避免纯利益导向。",
            "category": "五官",
            "id": "F299"
    },
    {
            "feature": "宽眼+宽鼻+平和眉",
            "feature_key": "综合",
            "condition": "眼距宽于眼长1/3，鼻翼宽度大于鼻长1/3，眉尾与眉头水平",
            "traditional": "《神相全编》云：'目广鼻阔眉平者，心宽而性柔，有治愈之力。'",
            "modern": "治愈型，温暖包容，适合护理或教育行业。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISFJ",
                    "ENFJ"
            ],
            "strength": "包容力强，善于安抚",
            "risk": "易被消耗，忽略自我照顾",
            "advice": "设立情感边界，定期自我充电，避免过度付出。",
            "category": "五官",
            "id": "F300"
    },
    {
            "feature": "窄眼+窄鼻+平和眉",
            "feature_key": "综合",
            "condition": "眼距窄于眼长1/3，鼻翼宽度小于鼻长1/3，眉尾与眉头水平",
            "traditional": "《相经》曰：'目狭鼻细眉平者，心一而志专，有专注之德。'",
            "modern": "专注型，精益求精，适合技术或研发岗位。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ",
                    "INTJ"
            ],
            "strength": "专注力强，追求卓越",
            "risk": "易钻牛角尖，视野狭窄",
            "advice": "拓宽兴趣范围，定期跨界学习，保持开放心态。",
            "category": "五官",
            "id": "F301"
    },
    {
            "feature": "长脸+高额+锐颌",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《相理衡真》云：面长额高，颌尖如锥，主智谋深远，然性孤。",
            "modern": "战略家型：长脸配高额与锐颌，暗示高认知需求与战略思维，OCEAN中开放性高，尽责性中，宜INTJ。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "INTJ"
            ],
            "strength": "擅长长期规划与复杂问题解决",
            "risk": "易因过度理性而忽视人际关系",
            "advice": "多参与团队讨论，培养共情能力。",
            "category": "面型",
            "id": "F302"
    },
    {
            "feature": "长脸+窄鼻+窄眼",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《神相全编》曰：面长鼻狭，目细如丝，性多疑而善察。",
            "modern": "分析师型：窄鼻窄眼增强细节聚焦能力，OCEAN中尽责性高，开放性中，宜ISTJ。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ"
            ],
            "strength": "数据敏感度高，逻辑严谨",
            "risk": "可能陷入完美主义而效率下降",
            "advice": "设定合理截止时间，接受适度不完美。",
            "category": "面型",
            "id": "F303"
    },
    {
            "feature": "长脸+宽眼+上扬眉",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《相法集成》载：面长目大，眉扬如剑，主才情横溢，不拘一格。",
            "modern": "艺术家型：宽眼与上扬眉暗示高开放性与情绪表达，OCEAN中开放性高，宜ENFP。",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFP"
            ],
            "strength": "创意丰富，能快速适应变化",
            "risk": "易因冲动而缺乏持久性",
            "advice": "建立日常规划，平衡灵感与执行。",
            "category": "面型",
            "id": "F304"
    },
    {
            "feature": "长脸+平和眉+圆下巴",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《太清神鉴》云：面长眉顺，颐圆如月，性温和而善调和。",
            "modern": "协调者型：平和眉与圆下巴暗示宜人性高，OCEAN中宜人性高，外向性中，宜ESFJ。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFJ"
            ],
            "strength": "团队凝聚力强，善于化解冲突",
            "risk": "可能过度迎合他人而失去自我",
            "advice": "明确个人边界，学会适当拒绝。",
            "category": "面型",
            "id": "F305"
    },
    {
            "feature": "长脸+窄额+锐颌",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《相理衡真》曰：面长额窄，颌尖似刃，主果断刚毅，然性急。",
            "modern": "执行者型：窄额与锐颌暗示高尽责性与低开放性，OCEAN中尽责性高，宜ESTJ。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "中",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESTJ"
            ],
            "strength": "执行力强，目标导向明确",
            "risk": "易因固执而错失新机会",
            "advice": "定期反思，接纳不同观点。",
            "category": "面型",
            "id": "F306"
    },
    {
            "feature": "长脸+宽鼻+下垂眉",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《神相全编》载：面长鼻阔，眉垂如帚，主深思熟虑，然多忧。",
            "modern": "思考者型：宽鼻与下垂眉暗示高神经质与开放性，OCEAN中神经质高，宜INTP。",
            "ocean": {
                    "O": "高",
                    "C": "中",
                    "E": "低",
                    "A": "中",
                    "N": "高"
            },
            "mbti_hint": [
                    "INTP"
            ],
            "strength": "深度思考，擅长理论构建",
            "risk": "易陷入焦虑与过度分析",
            "advice": "练习正念冥想，减少内耗。",
            "category": "面型",
            "id": "F307"
    },
    {
            "feature": "长脸+中眼+中鼻",
            "feature_key": "face_ratio",
            "condition": ">=1.15",
            "traditional": "《相法集成》云：面长而五官匀停，主中庸平和，能适应诸境。",
            "modern": "平衡者型：中等眼鼻暗示均衡特质，OCEAN各项中等，宜ISTP。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISTP"
            ],
            "strength": "适应性强，临场应变佳",
            "risk": "可能缺乏鲜明个性",
            "advice": "主动探索兴趣领域，发展专长。",
            "category": "面型",
            "id": "F308"
    },
    {
            "feature": "圆脸+宽鼻+圆下巴",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《相理衡真》曰：面圆鼻阔，颐圆如盘，主亲和善交际，然易浮。",
            "modern": "社交家型：圆脸配宽鼻圆下巴，暗示高外向性与宜人性，OCEAN中外向性高，宜ESFP。",
            "ocean": {
                    "O": "中",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESFP"
            ],
            "strength": "社交能力强，能活跃气氛",
            "risk": "可能缺乏深度与持久性",
            "advice": "培养专注力，设定长期目标。",
            "category": "面型",
            "id": "F309"
    },
    {
            "feature": "圆脸+窄鼻+上扬眉",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《神相全编》载：面圆鼻狭，眉扬如剑，主精于算计，然性傲。",
            "modern": "精算师型：窄鼻与上扬眉暗示高尽责性与开放性，OCEAN中尽责性高，宜ENTJ。",
            "ocean": {
                    "O": "高",
                    "C": "高",
                    "E": "中",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "ENTJ"
            ],
            "strength": "策略思维强，善于资源优化",
            "risk": "易因傲慢而疏远他人",
            "advice": "保持谦逊，多倾听团队意见。",
            "category": "面型",
            "id": "F310"
    },
    {
            "feature": "圆脸+宽眼+平和眉",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《太清神鉴》云：面圆目大，眉顺如弓，主创意无限，然多变。",
            "modern": "创意者型：宽眼与平和眉暗示高开放性与宜人性，OCEAN中开放性高，宜ENFP。",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "ENFP"
            ],
            "strength": "想象力丰富，能激发团队灵感",
            "risk": "易因多变而难以落地",
            "advice": "结合执行计划，将创意转化为成果。",
            "category": "面型",
            "id": "F311"
    },
    {
            "feature": "圆脸+锐颌+窄眼",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《相法集成》曰：面圆颌尖，目细如丝，主实干果断，然性冷。",
            "modern": "实干家型：锐颌与窄眼暗示高尽责性与低宜人性，OCEAN中尽责性高，宜ESTP。",
            "ocean": {
                    "O": "中",
                    "C": "高",
                    "E": "高",
                    "A": "低",
                    "N": "低"
            },
            "mbti_hint": [
                    "ESTP"
            ],
            "strength": "行动力强，能快速解决问题",
            "risk": "可能缺乏耐心与同理心",
            "advice": "放慢节奏，关注他人感受。",
            "category": "面型",
            "id": "F312"
    },
    {
            "feature": "圆脸+宽鼻+上扬眉",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《神相全编》载：面圆鼻阔，眉扬如鹰，主表现欲强，然易躁。",
            "modern": "表演者型：宽鼻与上扬眉暗示高外向性与开放性，OCEAN中外向性高，宜ESFP。",
            "ocean": {
                    "O": "高",
                    "C": "低",
                    "E": "高",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ESFP"
            ],
            "strength": "舞台魅力强，能感染他人",
            "risk": "易因冲动而忽视细节",
            "advice": "练习自我控制，注重事前准备。",
            "category": "面型",
            "id": "F313"
    },
    {
            "feature": "圆脸+窄额+窄鼻",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《相理衡真》云：面圆额窄，鼻狭如管，主技艺精湛，然性孤。",
            "modern": "工匠型：窄额与窄鼻暗示高尽责性与低外向性，OCEAN中尽责性高，宜ISTJ。",
            "ocean": {
                    "O": "低",
                    "C": "高",
                    "E": "低",
                    "A": "中",
                    "N": "低"
            },
            "mbti_hint": [
                    "ISTJ"
            ],
            "strength": "专注细节，手艺精湛",
            "risk": "可能因保守而抗拒创新",
            "advice": "尝试新方法，拓宽技能边界。",
            "category": "面型",
            "id": "F314"
    },
    {
            "feature": "圆脸+中眼+中鼻",
            "feature_key": "face_ratio",
            "condition": "<=0.89",
            "traditional": "《太清神鉴》曰：面圆而五官匀称，主调和众议，能容万物。",
            "modern": "调停者型：中等眼鼻暗示均衡特质，OCEAN中宜人性高，外向性中，宜INFP。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "高",
                    "N": "中"
            },
            "mbti_hint": [
                    "INFP"
            ],
            "strength": "善于倾听与调解矛盾",
            "risk": "可能因优柔寡断而延误决策",
            "advice": "培养决断力，明确优先级。",
            "category": "面型",
            "id": "F315"
    },
    {
            "feature": "中等面型",
            "feature_key": "face_ratio",
            "condition": "0.90-1.14",
            "traditional": "《相法集成》云：面方中正，五官均衡，主福寿双全，性中和。",
            "modern": "中庸型：面型适中暗示OCEAN各项均衡，适应性强，宜ISFJ。",
            "ocean": {
                    "O": "中",
                    "C": "中",
                    "E": "中",
                    "A": "中",
                    "N": "中"
            },
            "mbti_hint": [
                    "ISFJ"
            ],
            "strength": "稳定可靠，能胜任多数角色",
            "risk": "可能缺乏突出优势",
            "advice": "挖掘潜在特长，主动挑战自我。",
            "category": "面型",
            "id": "F316"
    },
]


def match_features(features: dict) -> list:
    """Match extracted facial features to knowledge base rules"""
    matches = []
    for rule in FACE_KNOWLEDGE_BASE:
        key = rule.get("feature_key", "")
        if key in ("综合", "复合"):
            # Compound rules: check all feature_keys mentioned in condition
            cond = rule.get("condition", "")
            ok = True
            for fk_part in ["forehead_ratio", "nose_width", "midface_ratio", 
                           "lowerface_ratio", "jaw_angle", "eye_distance", 
                           "face_ratio", "brow_angle"]:
                if fk_part in cond and fk_part in features:
                    val = features[fk_part]
                    # Extract condition for this key
                    parts = cond.split("&")
                    for p in parts:
                        if fk_part in p:
                            p_cond = p.strip()
                            for op in [">=", "<=", ">", "<", "=="]:
                                if op in p_cond:
                                    try:
                                        thresh = float(p_cond.split(op)[1].strip())
                                        if op == ">=" and val < thresh: ok = False
                                        elif op == "<=" and val > thresh: ok = False
                                        elif op == ">" and val <= thresh: ok = False
                                        elif op == "<" and val >= thresh: ok = False
                                        elif op == "==" and val != thresh: ok = False
                                    except: pass
                                    break
            if ok:
                matches.append(rule)
        elif key not in features:
            continue
        else:
            val = features[key]
            cond = rule["condition"]
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
    for i, rule in enumerate(matches[:12], 1):  # limit to avoid token overflow
        lines.append(f"### 规则 {i}：{rule['feature']}")
        lines.append(f"— 传统文化：{rule['traditional']}")
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
    print(f"\n---")
    print(f"Total rules in KB: {len(FACE_KNOWLEDGE_BASE)}")
    print(f"Matched: {len(match_features(test))}")

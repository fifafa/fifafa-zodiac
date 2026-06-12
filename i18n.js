/**
 * lalalin.xyz i18n — 三语词条库 (zh-CN / en / ja)
 * Auto-detects browser language, supports zh ↔ en ↔ ja toggle
 * Modules: 八字 (Bazi) · 面相 (Face Reading) · 手相 (Palm Reading)
 */
(function() {
  'use strict';

  // ====== Dictionary ======
  var I18N = {
    // Site identity
    'site-name':      { zh:'拉拉林',           en:'Lalalin',             ja:'ララリン' },
    'site-title':     { zh:'拉拉林 · 星之密语 | 东方命理 · 八字 · 面相 · 手相',
                        en:'Lalalin · Star Whispers | Eastern Fortune · Bazi · Face Reading · Palm Reading',
                        ja:'ララリン · 星のささやき | 東洋占い · 八字 · 人相 · 手相' },
    'site-desc':      { zh:'拉拉林——你的东方命理师。八字命盘、面相分析、手相解读。探索你的星图。',
                        en:'Lalalin — your Eastern fortune teller. Bazi chart, face reading, palm reading. Explore your star map.',
                        ja:'ララリン——あなたの東洋占い師。八字命盤、人相鑑定、手相鑑定。あなたの星図を探索。' },
    'og-title':       { zh:'拉拉林 · 星之密语',  en:'Lalalin · Star Whispers',   ja:'ララリン · 星のささやき' },
    'og-desc':        { zh:'东方命理师。八字·面相·手相',  en:'Eastern Fortune Teller. Bazi · Face · Palm',  ja:'東洋占い師。八字·人相·手相' },

    // Hero
    'hero-title':     { zh:'星之密语',           en:'Star Whispers',       ja:'星のささやき' },
    'hero-subtitle':  { zh:'探索你的命运星图',    en:'Explore your destiny chart',  ja:'あなたの運命図を探索' },

    // Tags
    'tag-bazi':       { zh:'八字命理',           en:'Bazi Destiny',        ja:'八字命理' },
    'tag-face':       { zh:'面相十二宫',          en:'Face Reading 12 Palaces',  ja:'人相十二宮' },
    'tag-palm':       { zh:'手相三纹',           en:'Palm Reading 3 Lines',  ja:'手相三紋' },

    // Navigation
    'nav-bazi':       { zh:'八字',               en:'Bazi',                ja:'八字' },
    'nav-mianxiang':  { zh:'面相',               en:'Face',                ja:'人相' },
    'nav-shouxiang':  { zh:'手相',               en:'Palm',                ja:'手相' },

    // Service cards
    'svc-bazi':       { zh:'八字命盘',           en:'Bazi Chart',          ja:'八字命盤' },
    'svc-bazi-desc':  { zh:'四柱八字深度解析',    en:'Four Pillars deep analysis',  ja:'四柱八字の深層解析' },
    'svc-face':       { zh:'面相分析',           en:'Face Reading',        ja:'人相鑑定' },
    'svc-face-desc':  { zh:'五官三庭气色解读',    en:'Five features & three regions',  ja:'五官三停の気色診断' },
    'svc-palm':       { zh:'手相解读',           en:'Palm Reading',        ja:'手相鑑定' },
    'svc-palm-desc':  { zh:'三大主线命运轨迹',    en:'Three major lines analysis',  ja:'三大線の運命鑑定' },

    // Forms
    'form-name':      { zh:'姓名',               en:'Name',                ja:'お名前' },
    'form-gender':    { zh:'性别',               en:'Gender',              ja:'性別' },
    'form-gender-m':  { zh:'男',                 en:'Male',                ja:'男性' },
    'form-gender-f':  { zh:'女',                 en:'Female',              ja:'女性' },
    'form-birth':     { zh:'出生日期',           en:'Birth Date',          ja:'生年月日' },
    'form-birth-time':{ zh:'出生时辰',           en:'Birth Time',          ja:'出生時刻' },
    'form-submit': { zh:'开始解读', en:'Start Reading', ja:'鑑定する' },
    'form-optional': { zh:'（选填）', en:' (Optional)', ja:'（任意）' },
    'btn-retake': { zh:'↺ 重拍', en:'↺ Retake', ja:'↺ 撮り直し' },
    'btn-palm-read': { zh:'✦ 解读手相', en:'✦ Read Palm', ja:'✦ 手相を鑑定' },
    'btn-face-read': { zh:'✦ 解读面相', en:'✦ Read Face', ja:'✦ 人相を鑑定' },

    // CTA
    'cta-start':      { zh:'开启你的命盘',       en:'Discover Your Destiny',  ja:'運命の扉を開く' },

    // Results
    'result-loading':   { zh:'正在推演命盘…',          en:'Reading your fortune…',            ja:'運命を読み解いています…' },
    'result-ai-badge':  { zh:'✦ 命理深度解读',         en:'✦ Deep Fortune Reading',            ja:'✦ 深層鑑定' },

    // Footer
    'footer-disclaimer':{ zh:'以上内容仅供传统文化娱乐参考。命运在自己手中，请理性看待。',
                          en:'For entertainment and cultural reference only. Your destiny is in your own hands.',
                          ja:'本内容は伝統文化の娯楽参考です。運命は自分の手にあります。' },

    // Common
    'common-error':   { zh:'请选择完整出生日期',  en:'Please select full birth date',  ja:'生年月日を全て選択してください' },
    'common-copied':  { zh:'已复制！',             en:'Copied!',                        ja:'コピーしました！' },

    // Language codes
    'lang-zh':        { zh:'zh-CN',  en:'zh-CN',  ja:'zh-CN' },
    'lang-en':        { zh:'en',     en:'en',     ja:'en' },
    'lang-ja':        { zh:'ja',     en:'ja',     ja:'ja' },

    // Face upload context
    'ctx-gender':     { zh:'性别',             en:'Gender',              ja:'性別' },
    'ctx-age':        { zh:'年龄段',            en:'Age Range',            ja:'年齢層' },
    'ctx-concern':    { zh:'关注',             en:'Focus',               ja:'関心事' },
    'btn-retake':     { zh:'重拍',             en:'Retake',              ja:'再撮影' },
    'btn-analyze':    { zh:'解读',              en:'Analyze',              ja:'分析' },
    'loading-face':   { zh:'正在分析面相特征…',     en:'Analyzing facial features…',     ja:'顔の特徴を分析中…' },

    // ====== Bazi Results ======
    'bazi-nayin':     { zh:'纳音',        en:'Nayin',           ja:'納音' },
    'bazi-qianzao':   { zh:'乾造',        en:'Qian Zao (Male)',  ja:'乾造（男性）' },
    'bazi-kunzao':    { zh:'坤造',        en:'Kun Zao (Female)', ja:'坤造（女性）' },
    'bazi-dm':        { zh:'日主',        en:'Day Master',      ja:'日主' },
    'bazi-ming':      { zh:'命',          en:'Destiny',         ja:'命' },
    'bazi-p-year':    { zh:'年柱',        en:'Year Pillar',     ja:'年柱' },
    'bazi-p-month':   { zh:'月柱',        en:'Month Pillar',    ja:'月柱' },
    'bazi-p-day':     { zh:'日柱',        en:'Day Pillar',      ja:'日柱' },
    'bazi-p-hour':    { zh:'时柱',        en:'Hour Pillar',     ja:'時柱' },
    'bazi-s-reading': { zh:'命理解读',    en:'Destiny Reading',  ja:'命理解読' },
    'bazi-s-yongji':  { zh:'用神喜忌',    en:'Yong Shen / Ji Shen', ja:'用神喜忌' },
    'bazi-s-wuxing':  { zh:'五行分布',    en:'Five Elements',    ja:'五行分布' },
    'bazi-s-guide':   { zh:'指导意见',    en:'Guidance',         ja:'アドバイス' },
    'bazi-shenwang':  { zh:'身旺',        en:'Strong Constitution', ja:'身旺' },
    'bazi-shenruo':   { zh:'身弱',        en:'Weak Constitution',   ja:'身弱' },
    'bazi-xi':        { zh:'喜',          en:'Favors',          ja:'喜' },
    'bazi-ji':        { zh:'忌',          en:'Avoids',          ja:'忌' },
    'bazi-tonglei':   { zh:'同类',        en:'Same type',       ja:'同類' },
    'bazi-yi':        { zh:'异',          en:'Opposite',        ja:'異' },
    'bazi-guide-1a':  { zh:'✦ 宜接触',    en:'✦ Favorable fields: ', ja:'✦ 適職：' },
    'bazi-guide-1b':  { zh:'属性的行业，补益运势', en:' industries to boost fortune', ja:'の業種が運気を補う' },
    'bazi-guide-2a':  { zh:'✦ 流年遇',    en:'✦ When year meets ', ja:'✦ 流年で' },
    'bazi-guide-2b':  { zh:'旺时宜保守，忌冒险投资', en:' stay conservative, avoid risks', ja:'の年は保守的に、リスク投資を避けて' },
    'bazi-guide-3a':  { zh:'命主「',      en:'✦ Day Master "',   ja:'✦ 日主「' },
    'bazi-guide-3b':  { zh:'」，注意',     en:'", beware of ',    ja:'」、注意：' },
    'bazi-guide-4a':  { zh:'✦ ',          en:'✦ ',              ja:'✦ ' },
    'bazi-guide-4b':  { zh:'运年大有可为',  en:' years bring great potential', ja:'の年は大いに発展' },
    'bazi-guide-4c':  { zh:'年得贵人助缘',  en:' years bring noble helpers', ja:'年、貴人の助けあり' },
    'bazi-guide-5a':  { zh:'✦ 关键运势在20-30岁，月令', en:'✦ Key fortune 20-30s, month order ', ja:'✦ 運勢の鍵は20-30代、月令' },
    'bazi-guide-5b':  { zh:'有力，中年后', en:' is strong, after midlife ', ja:'が強く、中年以降' },
    'bazi-guide-5c':  { zh:'运上升',       en:' fortune rises',   ja:'運が上昇' },
    'bazi-intro-a':   { zh:'你属',        en:'Your zodiac: ',     ja:'あなたの干支：' },
    'bazi-intro-b':   { zh:'，日柱「',     en:', Day Pillar "',   ja:'、日柱「' },
    'bazi-intro-c':   { zh:'」日主',       en:'" Day Master ',    ja:'」日主' },
    'bazi-intro-d':   { zh:'。命格纳音「',  en:'. Nayin: "',      ja:'。納音「' },
    'bazi-intro-e':   { zh:'」，五行 ',     en:'", Five Elements ', ja:'」、五行 ' },
    'bazi-intro-f':   { zh:'。',           en:'. ',               ja:'。' },
    'bazi-intro-g':   { zh:'，喜',         en:', favors ',         ja:'、喜' },
    'bazi-intro-h':   { zh:'，忌',         en:', avoids ',         ja:'、忌' },
    'bazi-intro-j':   { zh:'月令',         en:' month order ',     ja:'月令' },
    'bazi-intro-k':   { zh:'比劫',         en:'Bi Jie',           ja:'比劫' },
    'bazi-intro-l':   { zh:'财官',         en:'Cai Guan',         ja:'財官' },
    'bazi-intro-m':   { zh:'相随。',       en:' follows.',         ja:'が続く。' },

    // ====== Face Reading (Mian Xiang) ======
    'mx-g1':  { zh:'命宫',     en:'Life Palace',       ja:'命宮' },
    'mx-g2':  { zh:'兄弟宫',   en:'Siblings Palace',   ja:'兄弟宮' },
    'mx-g3':  { zh:'夫妻宫',   en:'Spouse Palace',     ja:'夫妻宮' },
    'mx-g4':  { zh:'子女宫',   en:'Children Palace',   ja:'子女宮' },
    'mx-g5':  { zh:'财帛宫',   en:'Wealth Palace',     ja:'財帛宮' },
    'mx-g6':  { zh:'疾厄宫',   en:'Health Palace',     ja:'疾厄宮' },
    'mx-g7':  { zh:'迁移宫',   en:'Travel Palace',     ja:'遷移宮' },
    'mx-g8':  { zh:'交友宫',   en:'Friends Palace',    ja:'交友宮' },
    'mx-g9':  { zh:'官禄宫',   en:'Career Palace',     ja:'官禄宮' },
    'mx-g10': { zh:'田宅宫',   en:'Property Palace',   ja:'田宅宮' },
    'mx-g11': { zh:'福德宫',   en:'Fortune Palace',    ja:'福德宮' },
    'mx-g12': { zh:'父母宫',   en:'Parents Palace',    ja:'父母宮' },
    'mx-tip-g9':  { zh:'额头正中—主事业官运。15-30岁',     en:'Forehead center — career fortune. Age 15-30',     ja:'額中央—キャリア運。15-30歳' },
    'mx-tip-g12': { zh:'额角—主父母缘分。',                en:'Forehead corners — parental bond.',                ja:'額の角—親との縁。' },
    'mx-tip-g7':  { zh:'额侧-主出行变动。',                 en:'Temple — travel & changes.',                      ja:'こめかみ—移動・変化。' },
    'mx-tip-g11': { zh:'眉尾上方-主福气。',                 en:'Above brow tail — blessings.',                    ja:'眉尻の上—福徳。' },
    'mx-tip-g2':  { zh:'眉毛—主兄弟姐妹朋友。',             en:'Eyebrow — siblings & friends.',                   ja:'眉毛—兄弟・友人。' },
    'mx-tip-g1':  { zh:'印堂眉心—主一生运势根基。',         en:'Yin Tang (between brows) — life foundation.',     ja:'印堂—人生の基盤。' },
    'mx-tip-g10': { zh:'眼皮上方—主房产家宅。',             en:'Upper eyelid — property & home.',                 ja:'瞼の上—家屋・不動産。' },
    'mx-tip-g6':  { zh:'鼻梁山根—主健康。31-50岁',          en:'Nose bridge — health. Age 31-50',                 ja:'鼻根—健康運。31-50歳' },
    'mx-tip-g5':  { zh:'鼻子—主一生财运。',                 en:'Nose — lifelong wealth.',                         ja:'鼻—一生の財運。' },
    'mx-tip-g3':  { zh:'眼尾奸门—主婚姻感情。',             en:'Eye corner (Jian Men) — marriage & love.',        ja:'目尻—結婚・愛情。' },
    'mx-tip-g4':  { zh:'眼下卧蚕—主子嗣缘分。',             en:'Under-eye (Wo Can) — children & descendants.',    ja:'目の下—子孫運。' },
    'mx-tip-g8':  { zh:'下巴两侧—主朋友下属。51岁后',        en:'Jaw sides — friends & subordinates. After 51',     ja:'顎の両側—友人・部下。51歳以降' },
    'mx-cancel':  { zh:'取消',       en:'Cancel',            ja:'キャンセル' },
    'mx-mole-on': { zh:'● 痣相已开',  en:'● Moles ON',        ja:'● ほくろ相オン' },
    'mx-mole-off':{ zh:'● 标注痣相',  en:'● Mark Moles',      ja:'● ほくろをマーク' },
    'mx-mole':    { zh:'痣',          en:'Mole',              ja:'ほくろ' },
    'mx-click-mole':{ zh:'点击痣的位置标注', en:'Click to mark mole position', ja:'ほくろの位置をクリック' },

    // Face reading options
    'mxo-g9-0':  { zh:'天庭饱满',   en:'Full forehead',         ja:'額が豊か' },
    'mxo-g9-1':  { zh:'高广明亮',   en:'Broad & bright',        ja:'高く明るい' },
    'mxo-g9-2':  { zh:'略有凹陷',   en:'Slightly indented',     ja:'やや凹み' },
    'mxo-g9-3':  { zh:'有伏犀骨',   en:'Fu Xi bone present',    ja:'伏犀骨あり' },
    'mxo-g12-0': { zh:'额角丰隆',   en:'Full temple corners',   ja:'額角が豊か' },
    'mxo-g12-1': { zh:'日角月角明', en:'Sun & Moon angles clear',ja:'日月角が明確' },
    'mxo-g12-2': { zh:'额角平坦',   en:'Flat temple corners',   ja:'額角が平坦' },
    'mxo-g12-3': { zh:'略有下陷',   en:'Slightly sunken',       ja:'やや陥没' },
    'mxo-g7-0':  { zh:'额角饱满',   en:'Full temple',           ja:'こめかみ豊か' },
    'mxo-g7-1':  { zh:'开阔平实',   en:'Open & steady',         ja:'開放的で安定' },
    'mxo-g7-2':  { zh:'驿马位明',   en:'Travel mark clear',     ja:'旅行線が明確' },
    'mxo-g7-3':  { zh:'略有内收',   en:'Slightly inward',       ja:'やや内側' },
    'mxo-g11-0': { zh:'福德宫满',   en:'Fortune palace full',   ja:'福徳宮が充実' },
    'mxo-g11-1': { zh:'眉尾丰隆',   en:'Brow tail full',        ja:'眉尻が豊か' },
    'mxo-g11-2': { zh:'福德略平',   en:'Fortune slightly flat', ja:'福徳やや平坦' },
    'mxo-g11-3': { zh:'额角丰盈',   en:'Temple abundant',       ja:'こめかみ豊潤' },
    'mxo-g2-0':  { zh:'眉毛清秀',   en:'Elegant brows',         ja:'眉が清秀' },
    'mxo-g2-1':  { zh:'浓密刚强',   en:'Thick & strong',        ja:'濃く力強い' },
    'mxo-g2-2':  { zh:'眉尾稀疏',   en:'Sparse brow tails',     ja:'眉尻が薄い' },
    'mxo-g2-3':  { zh:'眉形朗阔',   en:'Broad brow shape',      ja:'眉が広々' },
    'mxo-g1-0':  { zh:'宽阔明亮',   en:'Wide & bright',         ja:'広く明るい' },
    'mxo-g1-1':  { zh:'有悬针纹',   en:'Vertical line present', ja:'懸針紋あり' },
    'mxo-g1-2':  { zh:'略有凹陷',   en:'Slightly indented',     ja:'やや凹み' },
    'mxo-g1-3':  { zh:'光洁平整',   en:'Smooth & even',         ja:'滑らか' },
    'mxo-g10-0': { zh:'眼皮丰润',   en:'Full eyelids',          ja:'瞼が豊か' },
    'mxo-g10-1': { zh:'田宅宫满',   en:'Property palace full',  ja:'田宅宮充実' },
    'mxo-g10-2': { zh:'略有微陷',   en:'Slightly sunken',       ja:'やや陥没' },
    'mxo-g10-3': { zh:'明润光泽',   en:'Bright & lustrous',     ja:'明るく潤い' },
    'mxo-g6-0':  { zh:'山根高挺',   en:'High nose bridge',      ja:'鼻根が高い' },
    'mxo-g6-1':  { zh:'山根略低',   en:'Slightly low bridge',   ja:'鼻根やや低い' },
    'mxo-g6-2':  { zh:'山根有节',   en:'Bridge has knots',      ja:'鼻根に節' },
    'mxo-g6-3':  { zh:'山根光润',   en:'Bridge smooth & bright',ja:'鼻根が滑らか' },
    'mxo-g5-0':  { zh:'鼻梁挺直',   en:'Straight nose bridge',  ja:'鼻筋が通る' },
    'mxo-g5-1':  { zh:'鼻头圆润',   en:'Round nose tip',        ja:'鼻先が丸い' },
    'mxo-g5-2':  { zh:'鼻翼丰满',   en:'Full nose wings',       ja:'小鼻が豊か' },
    'mxo-g5-3':  { zh:'鼻子端正',   en:'Well-proportioned nose',ja:'端正な鼻' },
    'mxo-g3-0':  { zh:'眼尾饱满',   en:'Full eye corners',      ja:'目尻が豊か' },
    'mxo-g3-1':  { zh:'眼尾略陷',   en:'Slightly sunken corners',ja:'目尻やや陥没' },
    'mxo-g3-2':  { zh:'奸门光洁',   en:'Jian Men smooth',       ja:'奸門が滑らか' },
    'mxo-g3-3':  { zh:'略有细纹',   en:'Slight fine lines',     ja:'やや小じわ' },
    'mxo-g4-0':  { zh:'卧蚕丰满',   en:'Full Wo Can',           ja:'涙袋が豊か' },
    'mxo-g4-1':  { zh:'眼下平实',   en:'Flat under-eyes',       ja:'目の下が平坦' },
    'mxo-g4-2':  { zh:'泪堂微陷',   en:'Slightly sunken',       ja:'涙堂やや陥没' },
    'mxo-g4-3':  { zh:'明润饱满',   en:'Bright & plump',        ja:'明るくふっくら' },
    'mxo-g8-0':  { zh:'下巴圆润',   en:'Round chin',            ja:'丸い顎' },
    'mxo-g8-1':  { zh:'地阁方圆',   en:'Square Di Ge',          ja:'地閣が角張る' },
    'mxo-g8-2':  { zh:'下巴略尖',   en:'Slightly pointed chin', ja:'やや尖った顎' },
    'mxo-g8-3':  { zh:'地库丰满',   en:'Full Di Ku',            ja:'地庫が豊か' },

    // ====== Palm Reading (Shou Xiang) ======
    'palm-life':   { zh:'生命线',  en:'Life Line',        ja:'生命線' },
    'palm-head':   { zh:'智慧线',  en:'Head Line',        ja:'頭脳線' },
    'palm-heart':  { zh:'感情线',  en:'Heart Line',       ja:'感情線' },
    'palm-fate':   { zh:'命运线',  en:'Fate Line',        ja:'運命線' },
    'palm-sun':    { zh:'太阳线',  en:'Sun Line',         ja:'太陽線' },
    'palm-match':  { zh:'匹配度',  en:'Match Score',       ja:'一致度' },
    'palm-result': { zh:'解读：',  en:'Reading: ',         ja:'鑑定：' },
    'palm-extra':  { zh:'✦ 基于掌纹照片分析，主要线条特征与人工选取一致。建议保持手掌自然放松状态下拍摄。',
                     en:'✦ Based on palm photo analysis. Main line features match manual selection. Keep hand relaxed when photographing.',
                     ja:'✦ 掌紋写真に基づく分析。主要線の特徴は手動選択と一致。リラックスした状態で撮影することをお勧めします。' },

    // Palm option descriptions
    'pl-life-0':  { zh:'长而深弧 体质强健',   en:'Long deep arc — robust health',    ja:'長く深い弧—強健' },
    'pl-life-1':  { zh:'中等弧线 生活规律',    en:'Medium arc — regular lifestyle',   ja:'中程度の弧—規則正しい' },
    'pl-life-2':  { zh:'较短连续 精力集中',    en:'Short continuous — focused energy',ja:'短く連続—集中力あり' },
    'pl-life-3':  { zh:'分叉多向 好奇心强',    en:'Forked — strong curiosity',        ja:'分岐あり—好奇心旺盛' },
    'pl-life-4':  { zh:'断续链状 注意身体',    en:'Chained — watch health',            ja:'途切れ鎖状—健康注意' },
    'pl-head-0':  { zh:'长直贯穿 理智力强',    en:'Long straight — strong intellect',  ja:'長く直線的—知性豊か' },
    'pl-head-1':  { zh:'弧线下弯 想象力丰',    en:'Curved down — rich imagination',    ja:'下方に湾曲—想像力豊か' },
    'pl-head-2':  { zh:'短而平直 务实理性',    en:'Short flat — pragmatic & rational', ja:'短く平直—実務的' },
    'pl-head-3':  { zh:'分叉双线 多才多艺',    en:'Forked double — versatile talent',  ja:'分岐二重線—多才' },
    'pl-head-4':  { zh:'波浪起伏 创意思维',    en:'Wavy — creative thinking',          ja:'波状—創造的思考' },
    'pl-heart-0': { zh:'长而清晰 情深义重',    en:'Long clear — deep affection',       ja:'長く鮮明—情が深い' },
    'pl-heart-1': { zh:'短直克制 理性冷静',    en:'Short straight — rational & calm',  ja:'短く直線—理性的' },
    'pl-heart-2': { zh:'链状连绵 敏感多情',    en:'Chained — sensitive & emotional',   ja:'鎖状—感受性豊か' },
    'pl-heart-3': { zh:'分叉上扬 热情浪漫',    en:'Forked up — passionate & romantic', ja:'分岐上向—情熱的' },
    'pl-heart-4': { zh:'弧线上弯 乐观豁达',    en:'Curved up — optimistic & open',     ja:'上方に湾曲—楽観的' },
    'pl-fate-0':  { zh:'深长至中 事业有成',    en:'Deep to center — career success',   ja:'深く中央まで—成功' },
    'pl-fate-1':  { zh:'中等偏斜 自我奋斗',    en:'Medium slanted — self-made',         ja:'中程度斜め—自力で' },
    'pl-fate-2':  { zh:'断续不连 起伏多变',    en:'Broken — ups & downs',               ja:'途切れ—浮き沈み' },
    'pl-fate-3':  { zh:'双命运线 双重机遇',    en:'Double line — dual opportunities',   ja:'二重線—二重の機会' },
    'pl-fate-4':  { zh:'隐约可见 随缘自在',    en:'Faint — easygoing & free',           ja:'かすかに—自然体' },
    'pl-sun-0':   { zh:'清晰深长 名利双收',    en:'Clear deep — fame & fortune',        ja:'鮮明で深い—名利両得' },
    'pl-sun-1':   { zh:'中等明朗 稳步上升',    en:'Medium clear — steady rise',         ja:'中程度—着実に上昇' },
    'pl-sun-2':   { zh:'短而有力 锋芒初露',    en:'Short powerful — emerging talent',   ja:'短く力強い—才能開花' },
    'pl-sun-3':   { zh:'分叉双线 多面发展',    en:'Forked — multi-faceted growth',      ja:'分岐—多面的発展' },
    'pl-sun-4':   { zh:'浅淡隐约 大器晚成',    en:'Faint — late bloomer',               ja:'かすか—大器晩成' },

    // ====== Share ======
    'share-text':    { zh:'拉拉林·星之密语\n八字·面相·手相 → lalalin.xyz',
                       en:'Lalalin · Star Whispers\nBazi · Face · Palm → lalalin.xyz',
                       ja:'ララリン · 星のささやき\\n八字·人相·手相 → lalalin.xyz' },

    // ====== Misc ======
    'misc-photo-or-upload': { zh:'拍照或上传照片',     en:'Take or upload photo',    ja:'写真を撮るかアップロード' },
    'misc-palm-photo':      { zh:'拍照或上传掌纹照片', en:'Take or upload palm photo', ja:'手相写真を撮るかアップロード' },
    'misc-retry':           { zh:'请重试或更换照片',   en:'Please retry or change photo', ja:'再試行または写真を変更' },
    'misc-no-face':         { zh:'未检测到面部，请确保照片清晰正面', en:'No face detected. Use a clear front-facing photo', ja:'顔が検出されません。正面を向いた鮮明な写真を' },
    'misc-analyzing':       { zh:'分析中...',           en:'Analyzing...',            ja:'分析中...' },

    // Palm errors
    'palm-err-nohand':  { zh:'未检测到手掌，请确保照片清晰、手掌平展', en:'No palm detected. Use a clear, flat palm photo', ja:'手のひらが検出されません。鮮明で平らな手のひらの写真を使用してください' },
    'palm-err-server':  { zh:'服务异常',              en:'Service error',           ja:'サービスエラー' },
    'palm-manual-title':{ zh:'✦ 手动选线（可选）',    en:'✦ Manual Selection (Optional)', ja:'✦ 手動選択（任意）' },
    'palm-loading':     { zh:'正在分析掌纹…',          en:'Analyzing palm lines…',    ja:'掌紋を分析中…' },
    'palm-btn-analyzing':{ zh:'分析中…',              en:'Analyzing…',              ja:'分析中…' },
    'misc-ref':             { zh:'以上分析仅供传统文化娱乐参考', en:'Above is for entertainment & cultural reference only', ja:'以上の分析は伝統文化の娯楽参考です' },
    // ====== Payment & Error UI ======
    'err-title':        { zh:'连接失败',               en:'Connection Failed',         ja:'接続失敗' },
    'err-msg':          { zh:'无法连接到服务，请稍后重试', en:'Unable to connect. Please try later', ja:'サービスに接続できません。後ほどお試しください' },
    'err-retry':        { zh:'🔄 重新加载',             en:'🔄 Reload',                  ja:'🔄 リロード' },
    'load-title':       { zh:'正在推演命盘…',           en:'Reading your fortune…',     ja:'運命を読み解いています…' },
    'load-sub':         { zh:'深度分析中，约需 5-10 秒',  en:'Deep analysis, ~5-10 seconds', ja:'詳細分析中、約5-10秒' },
    'pp-title':         { zh:'✨ 解锁无限解读',          en:'✨ Unlock Unlimited',        ja:'✨ 無限解読を解除' },
    'pp-sub':           { zh:'每次深度解读都需要算力支持，感谢理解', en:'Each reading needs computing resources, thanks for your support', ja:'各鑑定にはリソースが必要です。ご支援ありがとうございます' },
    'pp-coffee':        { zh:'☕ 请喝杯咖啡',            en:'☕ Buy me a coffee',         ja:'☕ コーヒーをおごる' },
    'pp-coffee-desc':   { zh:'单次解读',               en:'Single reading',            ja:'1回の鑑定' },
    'pp-monthly':       { zh:'⭐ 月度会员',             en:'⭐ Monthly Member',          ja:'⭐ 月額会員' },
    'pp-monthly-desc':  { zh:'无限解读 · 可随时取消',     en:'Unlimited · Cancel anytime', ja:'無制限 · いつでも解約可能' },
    'pp-best-badge':    { zh:'最受欢迎',               en:'Most Popular',              ja:'一番人気' },
    'pw-title':         { zh:'免费次数已用完',           en:'Free readings used up',     ja:'無料回数終了' },
    'pw-desc':          { zh:'每次深度解读都需要算力支持，感谢理解与支持', en:'Each reading requires resources. Thanks for understanding!', ja:'各鑑定にリソースが必要です。ご理解とご支援に感謝します' },
    'pw-coffee':        { zh:'请喝杯咖啡',              en:'Buy me a coffee',           ja:'コーヒーをおごる' },
    'pw-monthly':       { zh:'无限解读 ⭐',             en:'Unlimited ⭐',              ja:'無制限 ⭐' },
    'pw-alt':           { zh:'或试试其他模块：',         en:'Or try other modules: ',    ja:'他のモジュール：' },
    // ====== Date selects ======
    'bazi-year':       { zh:'年',               en:'Year',              ja:'年' },
    'bazi-month':      { zh:'月',               en:'Month',             ja:'月' },
    'bazi-day':        { zh:'日',               en:'Day',               ja:'日' },
    'bazi-month-short':{ zh:'月',               en:'',                  ja:'月' },

    // ====== Vice names ======
    'vice-indecisive': { zh:'优柔寡断',         en:'indecisive',        ja:'優柔不断' },
    'vice-impatient':  { zh:'急躁冲动',         en:'impatient',         ja:'短気' },
    'vice-stubborn':   { zh:'固执己见',         en:'stubborn',          ja:'頑固' },
    'vice-rigid':      { zh:'刚愎自用',         en:'rigid',             ja:'独善的' },
    'vice-emotional':  { zh:'感情用事',         en:'emotional',         ja:'感情的' },
  };

  // ====== Runtime ======
  var CURRENT_LANG = 'zh';

  function detectLang() {
    var saved = localStorage.getItem('lalalin-lang');
    if (saved && I18N['site-name'][saved]) return saved;

    var navLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
    if (navLang.startsWith('zh')) return 'zh';
    if (navLang.startsWith('ja')) return 'ja';
    if (navLang.startsWith('en')) return 'en';
    return 'zh';
  }

  window.t = function(key) {
    if (!I18N[key]) {
      console.warn('[i18n] missing key:', key);
      return key;
    }
    return I18N[key][CURRENT_LANG] || I18N[key]['zh'] || key;
  };

  window.getLang = function() { return CURRENT_LANG; };

  function applyLang() {
    // Update all [data-i18n] elements
    document.querySelectorAll('[data-i18n]').forEach(function(el) {
      var key = el.getAttribute('data-i18n');
      if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
        el.placeholder = window.t(key);
      } else if (el.tagName === 'OPTION' && el.value === '' && el.parentElement) {
        // Update select placeholders
        el.textContent = window.t(key);
      } else {
        el.textContent = window.t(key);
      }
    });
    // Re-populate date selects with current language
    if (window._repopulateDateSelects) window._repopulateDateSelects();
    // Update meta
    document.title = window.t('site-title');
    var d = document.querySelector('meta[name="description"]');
    if (d) d.content = window.t('site-desc');
    var ot = document.querySelector('meta[property="og:title"]');
    if (ot) ot.content = window.t('og-title');
    var od = document.querySelector('meta[property="og:description"]');
    if (od) od.content = window.t('og-desc');
    document.documentElement.lang = {zh:'zh-CN', en:'en', ja:'ja'}[CURRENT_LANG];
  }

  window.toggleLang = function() {
    var langs = ['zh', 'en', 'ja'];
    var idx = langs.indexOf(CURRENT_LANG);
    CURRENT_LANG = langs[(idx + 1) % 3];
    localStorage.setItem('lalalin-lang', CURRENT_LANG);
    var btn = document.getElementById('langBtn');
    if (btn) btn.textContent = {zh:'中', en:'EN', ja:'日'}[CURRENT_LANG];
    applyLang();
  };

  // ====== Init ======
  CURRENT_LANG = detectLang();
  var btn = document.getElementById('langBtn');
  if (btn) btn.textContent = {zh:'中', en:'EN', ja:'日'}[CURRENT_LANG];

  // Apply on DOM ready (belt-and-suspenders for inline scripts that manipulate DOM)
  function doApply() { applyLang(); if (window.buildPalmOpts) window.buildPalmOpts(); }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', doApply);
  } else {
    doApply();
  }

  console.log('[lalalin] 🌐 i18n loaded, lang:', CURRENT_LANG);
})();

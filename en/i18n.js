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
    'site-name':      { zh:'TaoPulse',          en:'TaoPulse',            ja:'TaoPulse' },
    'site-title':     { zh:'TaoPulse · 东方三脉 | 八字 · 面相 · 手相',
                        en:'TaoPulse · Oriental Astrology & Face Reading | Bazi · Face · Palm',
                        ja:'TaoPulse · 東方命理の三脈 | 八字 · 人相 · 手相' },
    'site-desc':      { zh:'TaoPulse——东方命理三脉。八字命盘、面相分析、手相解读。探索你的星图。',
                        en:'TaoPulse — Oriental Astrology & Face Reading. Bazi chart, face reading, palm reading. Explore your star map.',
                        ja:'TaoPulse——東方命理の三脈。八字命盤、人相鑑定、手相鑑定。あなたの星図を探索。' },
    'og-title':       { zh:'TaoPulse · 东方三脉',  en:'TaoPulse · Oriental Astrology & Face Reading',  ja:'TaoPulse · 東方命理の三脈' },
    'og-desc':        { zh:'东方命理三脉。八字·面相·手相', en:'Oriental Astrology & Face Reading. Bazi · Face · Palm', ja:'東方命理の三脈。八字·人相·手相' },

    // Hero
    'hero-title':     { zh:'TaoPulse · 东方三脉', en:'TaoPulse',           ja:'TaoPulse' },
    'hero-subtitle':  { zh:'解读你的命理之脉',    en:'Oriental Astrology & Face Reading', ja:'東方命理の三脈' },

    // Intro splash
    'intro-title':    { zh:'TaoPulse',           en:'TaoPulse',             ja:'TaoPulse' },
    'intro-subtitle': { zh:'八字 · 面相 · 手相',  en:'Oriental Astrology & Face Reading', ja:'東方命理の三脈' },
    'intro-bazi-name':{ zh:'八字命盘',           en:'Bazi — The Eight Characters', ja:'八字 — 八つの文字' },
    'intro-bazi-body':{ zh:'八字源于《周易》阴阳五行学说。出生时刻的年月日时，化作天干地支四柱八字——这八个字承载天地之气的流转，映照先天命格、五行盛衰、大运起伏。',
                        en:'Bazi originates from the I Ching\'s Yin-Yang and Five Elements theory. Your birth moment — year, month, day, and hour — forms four pillars of Heavenly Stems and Earthly Branches. These eight characters embody cosmic energy flow, revealing innate destiny, elemental balance, and life cycles.',
                        ja:'八字は『易経』の陰陽五行説に由来します。生まれた瞬間の年月日時が天干地支による四柱八字となり、天地の気の流れを宿し、先天の命格、五行の盛衰、大運の起伏を映し出します。' },
    'intro-bazi-note':{ zh:'《珞琭子》云：「元命胜负，三元者干禄、支命、纳音身，各分衰旺之地。」——《李虚中命书》',
                        en:'"The Three Origins — Stem Fortune, Branch Fate, and Nayin Body — each find their waxing and waning ground." — Li Xuzhong\'s Book of Destiny (Tang Dynasty)',
                        ja:'「三元とは干禄・支命・納音身、各々衰旺の地を分かつ。」——『李虚中命書』（唐代）' },
    'intro-face-name':{ zh:'面相十二宫',          en:'Face Reading — The Twelve Palaces', ja:'人相学 — 十二宮' },
    'intro-face-body':{ zh:'面相源自《麻衣神相》。人面应天象，五官各主其位：天庭主事业，鼻准主财帛，双眉主兄弟，双眼主心性。气色明暗、骨相起伏，皆是命运外显。',
                        en:'Face reading traces to Master Ma\'s Physiognomy. The human face mirrors the cosmos: the forehead governs career, the nose governs wealth, the brows govern fraternity, the eyes govern the heart. Complexion and bone structure reveal one\'s fortune.',
                        ja:'人相学は『麻衣神相』に起源を持ちます。人の顔は天象に応じ、五官それぞれが役割を持ちます。額は官禄を、鼻は財帛を、眉は兄弟を、目は心性を司ります。気色の明暗、骨相の高低、すべてが運命の顕れです。' },
    'intro-face-note':{ zh:'「列百部之灵居，通五脏之神路，惟三才之成象，定一生之失得。」——《麻衣神相·相法总论》',
                        en:'"Arranged are the hundred spirit dwellings, connected to the five organ pathways. Only through the image of the Three Powers can one\'s life be determined." — Ma Yi Shen Xiang · General Treatise',
                        ja:'「百部の霊居を列ね、五臓の神路に通ず。三才の成象により、一生の失得を定む。」——『麻衣神相・相法総論』' },
    'intro-palm-name':{ zh:'手相三纹',           en:'Palm Reading — The Three Lines', ja:'手相 — 三大線' },
    'intro-palm-body':{ zh:'手相可溯至《黄帝内经》。天之纹为感情线、地之纹为智慧线、人之纹为生命线，三才并立。掌中八卦九宫，纹路深浅曲直，映射人生际遇与心性变化。',
                        en:'Palmistry traces to the Yellow Emperor\'s Inner Canon. The Heaven Line (heart), Earth Line (mind), and Human Line (life) form the tripartite order. Alongside the palm\'s Eight Trigrams and Nine Palaces, every line\'s depth, curve, and break reflects life\'s journey.',
                        ja:'手相は『黄帝内経』にまで遡ります。天の紋（感情線）、地の紋（知能線）、人の紋（生命線）の三才が並び立ち、掌中の八卦九宮と紋路の深浅が人生の機縁と心性の変化を映します。' },
    'intro-palm-note':{ zh:'「掌中八卦，定乾坤贵贱。三才纹路，分天地人之气数。」——《玉掌记》',
                        en:'"The palm\'s Eight Trigrams determine nobility and humility. The Three Lines divide the qi of Heaven, Earth, and Humanity." — Jade Palm Records',
                        ja:'「掌中の八卦、乾坤の貴賤を定む。三才の紋路、天地人の気数を分かつ。」——『玉掌記』' },
    'intro-enter':    { zh:'✦ 开启命盘 ✦',       en:'✦ Begin Your Reading ✦', ja:'✦ 鑑定を始める ✦' },
    'intro-skip':     { zh:'跳过介绍',            en:'Skip intro',            ja:'スキップ' },

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
    'cta-start':      { zh:'开启你的命盘',       en:'Start Free Reading',     ja:'運命の扉を開く' },

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
    'share-text':    { zh:'TaoPulse·东方三脉\n八字·面相·手相 → lalalin.xyz',
                       en:'TaoPulse · Oriental Astrology & Face Reading\nBazi · Face · Palm → lalalin.xyz',
                       ja:'TaoPulse · 東方命理の三脈\\n八字·人相·手相 → lalalin.xyz' },

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
    'palm-left-hand':   { zh:'左手',               en:'Left Hand',             ja:'左手' },
    'palm-right-hand':  { zh:'右手',               en:'Right Hand',            ja:'右手' },
    'palm-reject-hint': { zh:'⚠ 请上传清晰的手掌照片，非手型图片将被拒绝', en:'⚠ Please upload a clear palm photo. Non-palm images will be rejected.', ja:'⚠ 鮮明な手のひらの写真をアップロードしてください。手のひら以外の画像は拒否されます' },
    'palm-confirm-msg': { zh:'确认这是一张清晰的<b>手掌</b>照片？', en:'Confirm this is a clear <b>palm</b> photo?', ja:'これは鮮明な<b>手のひら</b>の写真ですか？' },
    'palm-confirm-no':  { zh:'✕ 不是手掌',           en:'✕ Not a palm',          ja:'✕ 手のひらではない' },
    'palm-confirm-yes': { zh:'✓ 确认解读',           en:'✓ Confirm Reading',     ja:'✓ 鑑定を確認' },
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


    // Intro detail
    'intro-more':        { zh:'了解更多 ↓',        en:'Learn more ↓',         ja:'さらに詳しく ↓' },
    'detail-bazi-text':  { zh:'八字即四柱命理学，以人出生时的年月日时对应天干地支，排成四柱共八字。年柱为根，月柱为苗，日柱为花，时柱为果。天干地支共六十甲子，循环不息。五行（金木水火土）相生相克，通过日主天干的五行属性，配合月令旺衰，参看十神关系，即可推演人一生的富贵贫贱、吉凶祸福。核心概念包括：日主强弱、用神喜忌、大运流年。',
                           en:'Bazi (Four Pillars of Destiny) maps your birth year, month, day, and hour to the Heavenly Stems and Earthly Branches — forming four pillars of eight characters. The Year Pillar is the root, Month the sprout, Day the flower, and Hour the fruit. Through the 60-cycle Jiazi system and Five Elements (Metal, Wood, Water, Fire, Earth) interactions, the Day Master's element strength is analyzed alongside seasonal influence and Ten Gods relationships to reveal life patterns. Key concepts: Day Master strength, Useful God, Favorable/Unfavorable elements, and Luck Pillars.',
                           ja:'八字（四柱推命）は、生まれた年月日時を天干地支に当てはめ、四柱八字を構成します。年柱は根、月柱は苗、日柱は花、時柱は果。六十甲子の循環と五行（木火土金水）の相生相克により、日主の強弱を月令と十神関係から判断し、人生の吉凶禍福を推し量ります。核心概念：日主強弱、用神喜忌、大運流年。' },
    'detail-face-text': { zh:'面相学将人脸分为十二宫，对应人生十二个方面。天庭（额头）为官禄宫，主事业功名；印堂（两眉之间）为命宫，主一生运势；两眼为监察宫，主心性善恶；鼻为财帛宫，主财富运势；口为出纳宫，主食禄口福；耳为采听宫，主寿元根基。三庭（上停、中停、下停）对应少年、中年、晚年运势。气色以黄润为吉，青黑为凶。',
                           en:'Face reading divides the face into Twelve Palaces, each governing a life domain. The forehead (Career Palace) rules achievements; the space between brows (Life Palace) governs overall fortune; the eyes (Inspection Palace) reveal character; the nose (Wealth Palace) governs finances; the mouth (Utterance Palace) rules sustenance; the ears (Listening Palace) govern longevity. The Three Regions (upper, middle, lower) correspond to youth, middle age, and later years. A warm, clear complexion is auspicious; dark, ashen tones are inauspicious.',
                           ja:'人相学では顔を十二宮に分け、人生の各側面を読み解きます。額（官禄宮）は事業、眉間（命宮）は運勢、両眼（監察宮）は心性、鼻（財帛宮）は財運、口（出納宮）は食禄、耳（採聴宮）は寿命を司ります。三停（上停・中停・下停）はそれぞれ少年・中年・晚年の運勢に対応。気色は黄色みのある潤いが吉、青黒い色は凶とされます。' },
    'detail-palm-text': { zh:'手相学以三大主线为核心。天纹（感情线）起于小指下方，横贯手掌，主情感婚姻；人纹（智慧线）起于食指下方，斜穿掌心，主思维学业；地纹（生命线）环绕拇指根部，主健康寿元。此外，玉柱纹（事业线）、太阳纹（成功线）、婚姻线、健康线等辅线亦各有深意。掌分八卦九宫，各方位对应不同人生领域。纹理以清晰深长为佳，断续凌乱为劣。',
                           en:'Palmistry centers on three major lines. The Heaven Line (Heart Line) starts below the little finger and crosses the palm — governing emotions and marriage. The Human Line (Head Line) starts below the index finger and angles across the palm — governing intellect and learning. The Earth Line (Life Line) curves around the thumb — governing health and longevity. Secondary lines include the Fate Line (career), Sun Line (success), Marriage Line, and Health Line. The palm is divided into Eight Trigrams and Nine Palaces, each zone corresponding to a life area. Deep, clear, unbroken lines are favorable.',
                           ja:'手相は三大線を核心とします。天紋（感情線）は小指の下から手のひらを横切り、感情・結婚を司ります。人紋（頭脳線）は人差し指の下から斜めに走り、思考・学業を示します。地紋（生命線）は親指の付け根を囲み、健康・寿命を表します。他に玉柱紋（運命線）、太陽紋（成功線）、結婚線、健康線などの補助線もあります。掌は八卦九宮に分かれ、各方位が異なる人生領域に対応。線紋は明瞭で深く長いものが良く、途切れや乱れは注意が必要です。' },

    // Daily fortune
    'daily-label':    { zh:'✦ 今日运势',        en:'✦ Today\'s Fortune',   ja:'✦ 今日の運勢' },

    // Shichen (12 two-hour periods)
    'shichen-unspec': { zh:'未指定',              en:'Unspecified',          ja:'未指定' },
    'shichen-zi':     { zh:'子时 23:00-01:00',   en:'Zi 23:00-01:00',       ja:'子の刻 23:00-01:00' },
    'shichen-chou':   { zh:'丑时 01:00-03:00',   en:'Chou 01:00-03:00',     ja:'丑の刻 01:00-03:00' },
    'shichen-yin':    { zh:'寅时 03:00-05:00',   en:'Yin 03:00-05:00',      ja:'寅の刻 03:00-05:00' },
    'shichen-mao':    { zh:'卯时 05:00-07:00',   en:'Mao 05:00-07:00',      ja:'卯の刻 05:00-07:00' },
    'shichen-chen':   { zh:'辰时 07:00-09:00',   en:'Chen 07:00-09:00',     ja:'辰の刻 07:00-09:00' },
    'shichen-si':     { zh:'巳时 09:00-11:00',   en:'Si 09:00-11:00',       ja:'巳の刻 09:00-11:00' },
    'shichen-wu':     { zh:'午时 11:00-13:00',   en:'Wu 11:00-13:00',       ja:'午の刻 11:00-13:00' },
    'shichen-wei':    { zh:'未时 13:00-15:00',   en:'Wei 13:00-15:00',      ja:'未の刻 13:00-15:00' },
    'shichen-shen':   { zh:'申时 15:00-17:00',   en:'Shen 15:00-17:00',     ja:'申の刻 15:00-17:00' },
    'shichen-you':    { zh:'酉时 17:00-19:00',   en:'You 17:00-19:00',      ja:'酉の刻 17:00-19:00' },
    'shichen-xu':     { zh:'戌时 19:00-21:00',   en:'Xu 19:00-21:00',       ja:'戌の刻 19:00-21:00' },
    'shichen-hai':    { zh:'亥时 21:00-23:00',   en:'Hai 21:00-23:00',      ja:'亥の刻 21:00-23:00' },

    // Privacy
    'privacy-note':   { zh:'你的照片仅用于面相分析，不会存储或分享。',
                        en:'Your photo is used solely for face reading analysis. Never stored or shared.',
                        ja:'お写真は人相鑑定のみに使用し、保存・共有は一切いたしません。' },

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
  
    'daily-0':{ zh:'宜积极进取', en:'Be proactive today', ja:'積極的に行動を' },
    'daily-1':{ zh:'宜柔韧应变', en:'Stay flexible', ja:'柔軟に対応を' },
    'daily-2':{ zh:'宜热情行动', en:'Act with passion', ja:'情熱を持って' },
    'daily-3':{ zh:'宜稳重踏实', en:'Be steady', ja:'着実に進もう' },
    'daily-4':{ zh:'宜诚信待人', en:'Be sincere', ja:'誠実であれ' },
    'daily-5':{ zh:'宜厚德载物', en:'Nurture virtue', ja:'徳を育もう' },
    'daily-6':{ zh:'宜果断决策', en:'Be decisive', ja:'果断に決断を' },
    'daily-7':{ zh:'宜精益求精', en:'Refine skills', ja:'技を磨こう' },
    'daily-8':{ zh:'宜深思远虑', en:'Think deeply', ja:'深く考えよう' },
    'daily-9':{ zh:'宜灵活变通', en:'Be adaptable', ja:'柔軟に適応を' },
    'dtip-0':{ zh:'诸事顺遂', en:'All favorable', ja:'全て順調' },
    'dtip-1':{ zh:'宜静不宜动', en:'Stillness over action', ja:'静を保て' },
    'dtip-2':{ zh:'贵人相助', en:'Benefactors near', ja:'贵人の助け' },
    'dtip-3':{ zh:'灵感迸发', en:'Inspiration strikes', ja:'ひらめきの日' },
    'dtip-4':{ zh:'稳扎稳打', en:'Steady progress', ja:'着実に進もう' },
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

/**
 * lalalin.xyz i18n — 三语词条库 (zh-CN / en / ja)
 * Auto-detects browser language, supports zh ↔ en ↔ ja toggle
 */
(function() {
  'use strict';

  // ====== Dictionary ======
  var I18N = {
    // Navigation
    'nav-star-curtain': { zh:'星幕', en:'Home', ja:'ホーム' },
    'nav-bazi': { zh:'八字', en:'Bazi', ja:'八字' },
    'nav-zodiac': { zh:'生肖', en:'Zodiac', ja:'干支' },
    'nav-tarot': { zh:'塔罗', en:'Tarot', ja:'タロット' },
    'nav-love': { zh:'缘分', en:'Love', ja:'縁結び' },
    'nav-mianxiang': { zh:'面相', en:'Face', ja:'人相' },
    'nav-shouxiang': { zh:'手相', en:'Palm', ja:'手相' },
    'nav-ziwei': { zh:'紫微', en:'Ziwei', ja:'紫微' },

    // Hero
    'hero-title': { zh:'拉拉林 · 星之密语', en:'Lalalin · Star Whispers', ja:'ララリン · 星のささやき' },
    'hero-subtitle': { zh:'AI东方命理师', en:'AI Eastern Fortune Teller', ja:'AI東洋占い師' },
    'hero-desc': { zh:'八字命盘 · 塔罗占卜 · 生肖运势 · 面相手相 · 缘分配对', en:'Bazi · Tarot · Zodiac · Face & Palm Reading · Love Match', ja:'八字 · タロット · 干支 · 人相手相 · 縁結び' },

    // Trust indicators
    'trust-count-label': { zh:'已完成解读', en:'Readings Done', ja:'鑑定実績' },
    'trust-ai-online': { zh:'AI命理师在线', en:'AI Fortune Teller Online', ja:'AI占い師オンライン' },

    // Steps
    'step-1-title': { zh:'输入生辰', en:'Enter Birth Info', ja:'生年月日を入力' },
    'step-1-desc': { zh:'填写姓名和出生日期', en:'Fill in name and birth date', ja:'名前と生年月日を記入' },
    'step-2-title': { zh:'选择命理', en:'Choose Reading', ja:'占いを選択' },
    'step-2-desc': { zh:'八字/塔罗/生肖/面相手相', en:'Bazi/Tarot/Zodiac/Face/Palm', ja:'八字/タロット/干支/人相手相' },
    'step-3-title': { zh:'获得解读', en:'Get Reading', ja:'鑑定結果を見る' },
    'step-3-desc': { zh:'即时AI命理报告', en:'Instant AI fortune report', ja:'AIによる即時鑑定レポート' },

    // CTA
    'cta-start': { zh:'开启你的命盘', en:'Discover Your Destiny', ja:'運命の扉を開く' },

    // Hooks
    'hook-1': { zh:'Ta是你的正缘吗？', en:'Is this your soulmate?', ja:'この人は運命の人？' },
    'hook-2': { zh:'今年财运如何？', en:'How is your wealth this year?', ja:'今年の金運は？' },
    'hook-3': { zh:'何时遇到对的人？', en:'When will you meet The One?', ja:'運命の人と出会うのはいつ？' },
    'hook-4': { zh:'你的命运星图是什么？', en:'What is your destiny chart?', ja:'あなたの運命図は？' },
    'hook-5': { zh:'宇宙想对你说什么？', en:'What does the universe want to tell you?', ja:'宇宙はあなたに何を伝えたい？' },

    // Testimonials
    'testi-1-text': { zh:'塔罗占卜帮我做了重要决定，免费还这么准，已经推荐给全家人。', en:'The tarot reading helped me make a crucial decision. Free and so accurate — I recommended it to my whole family.', ja:'タロット占いで重要な決断ができました。無料でこんなに当たるなんて、家族全員に勧めました。' },
    'testi-1-author': { zh:'星辰大海 · 已使用2个月', en:'Stardust · 2 months user', ja:'星の海 · 利用2ヶ月' },

    // Service cards
    'svc-bazi': { zh:'八字命盘', en:'Bazi Chart', ja:'八字命盤' },
    'svc-bazi-desc': { zh:'四柱八字深度解析', en:'Four Pillars deep analysis', ja:'四柱八字の深層解析' },
    'svc-tarot': { zh:'塔罗占卜', en:'Tarot Reading', ja:'タロット占い' },
    'svc-tarot-desc': { zh:'22张大阿尔卡纳', en:'22 Major Arcana cards', ja:'22枚の大アルカナ' },
    'svc-zodiac': { zh:'生肖运势', en:'Zodiac Fortune', ja:'干支運勢' },
    'svc-zodiac-desc': { zh:'十二生肖流年运程', en:'12 Zodiac annual forecast', ja:'十二支の年間運勢' },
    'svc-love': { zh:'缘分配对', en:'Love Match', ja:'相性診断' },
    'svc-love-desc': { zh:'八字合婚姻缘分析', en:'Bazi marriage compatibility', ja:'八字でみる結婚相性' },
    'svc-face': { zh:'面相分析', en:'Face Reading', ja:'人相鑑定' },
    'svc-face-desc': { zh:'五官三庭气色解读', en:'Five features & three regions', ja:'五官三停の気色診断' },
    'svc-palm': { zh:'手相解读', en:'Palm Reading', ja:'手相鑑定' },
    'svc-palm-desc': { zh:'三大主线命运轨迹', en:'Three major lines analysis', ja:'三大線の運命鑑定' },

    // Forms
    'form-name': { zh:'姓名', en:'Name', ja:'お名前' },
    'form-gender': { zh:'性别', en:'Gender', ja:'性別' },
    'form-gender-m': { zh:'男', en:'Male', ja:'男性' },
    'form-gender-f': { zh:'女', en:'Female', ja:'女性' },
    'form-birth': { zh:'出生日期', en:'Birth Date', ja:'生年月日' },
    'form-birth-time': { zh:'出生时辰', en:'Birth Time', ja:'出生時刻' },
    'form-question': { zh:'你想问什么？', en:'What do you want to ask?', ja:'何を占いますか？' },
    'form-submit': { zh:'开始解读', en:'Start Reading', ja:'鑑定する' },
    'form-optional': { zh:'（选填）', en:'(Optional)', ja:'（任意）' },

    // Results
    'result-loading': { zh:'AI 正在推演命盘…', en:'AI is reading your fortune…', ja:'AIが運命を読み解いています…' },
    'result-ai-badge': { zh:'🤖 DeepSeek AI 深度解读', en:'🤖 DeepSeek AI Deep Reading', ja:'🤖 DeepSeek AI 深層鑑定' },

    // Share
    'share-text': { zh:'拉拉林·星之密语 ✦ AI东方命理师\n八字·塔罗·生肖·面相手相 → lalalin.xyz', en:'Lalalin · Star Whispers ✦ AI Eastern Fortune Teller\nBazi · Tarot · Zodiac · Face & Palm → lalalin.xyz', ja:'ララリン · 星のささやき ✦ AI東洋占い師\n八字 · タロット · 干支 · 人相手相 → lalalin.xyz' },

    // Common
    'common-copied': { zh:'已复制！', en:'Copied!', ja:'コピーしました！' },
    'common-error': { zh:'请选择完整出生日期', en:'Please select full birth date', ja:'生年月日を全て選択してください' },
    'common-trust-count': { zh:'已完成解读', en:'Readings completed', ja:'鑑定完了' },

    // Footer / meta
    'site-title': { zh:'拉拉林 · 星之密语 | AI东方命理 · 八字 · 塔罗 · 面相', en:'Lalalin · Star Whispers | AI Eastern Fortune · Bazi · Tarot · Face Reading', ja:'ララリン · 星のささやき | AI東洋占い · 八字 · タロット · 人相' },
    'site-desc': { zh:'拉拉林——你的AI东方命理师。八字命盘、塔罗占卜、生肖运势、面相手相、缘分配对。探索你的星图。', en:'Lalalin — your AI Eastern fortune teller. Bazi chart, tarot, zodiac, face & palm reading, love matching. Explore your star map.', ja:'ララリン——あなたのAI東洋占い師。八字命盤、タロット占い、干支運勢、人相手相、縁結び。あなたの星図を探索。' },
    'og-title': { zh:'拉拉林 · 星之密语', en:'Lalalin · Star Whispers', ja:'ララリン · 星のささやき' },
    'og-desc': { zh:'AI东方命理师。八字·塔罗·生肖·面相·手相', en:'AI Eastern Fortune Teller. Bazi·Tarot·Zodiac·Face·Palm', ja:'AI東洋占い師。八字·タロット·干支·人相·手相' },

    // Zodiac names
    'zodiac-rat': { zh:'鼠', en:'Rat', ja:'子' },
    'zodiac-ox': { zh:'牛', en:'Ox', ja:'丑' },
    'zodiac-tiger': { zh:'虎', en:'Tiger', ja:'寅' },
    'zodiac-rabbit': { zh:'兔', en:'Rabbit', ja:'卯' },
    'zodiac-dragon': { zh:'龙', en:'Dragon', ja:'辰' },
    'zodiac-snake': { zh:'蛇', en:'Snake', ja:'巳' },
    'zodiac-horse': { zh:'马', en:'Horse', ja:'午' },
    'zodiac-goat': { zh:'羊', en:'Goat', ja:'未' },
    'zodiac-monkey': { zh:'猴', en:'Monkey', ja:'申' },
    'zodiac-rooster': { zh:'鸡', en:'Rooster', ja:'酉' },
    'zodiac-dog': { zh:'狗', en:'Dog', ja:'戌' },
    'zodiac-pig': { zh:'猪', en:'Pig', ja:'亥' },

    // SEO
    'lang-zh': { zh:'zh-CN', en:'zh-CN', ja:'zh-CN' },
    'lang-en': { zh:'en', en:'en', ja:'en' },
    'lang-ja': { zh:'ja', en:'ja', ja:'ja' },

    // Daily card
    'daily-card-title': { zh:'今日运势', en:'Daily Fortune', ja:'今日の運勢' },
    'daily-card-lucky-color': { zh:'幸运色', en:'Lucky Color', ja:'ラッキーカラー' },
    'daily-card-lucky-number': { zh:'幸运数字', en:'Lucky Number', ja:'ラッキーナンバー' },
    'daily-card-advice': { zh:'今日建议', en:'Today\'s Advice', ja:'今日のアドバイス' },

    // AI analysis
    'ai-fortune': { zh:'AI 命理解读', en:'AI Fortune Reading', ja:'AI運命鑑定' },
    'ai-thinking': { zh:'DeepSeek 正在推演…', en:'DeepSeek is reading…', ja:'DeepSeekが解析中…' },
  };

  // ====== Runtime ======
  var CURRENT_LANG = 'zh';

  function detectLang() {
    var saved = localStorage.getItem('lalalin-lang');
    if (saved && I18N['nav-star-curtain'][saved]) return saved;

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

  window.toggleLang = function() {
    var langs = ['zh', 'en', 'ja'];
    var idx = langs.indexOf(CURRENT_LANG);
    CURRENT_LANG = langs[(idx + 1) % 3];
    localStorage.setItem('lalalin-lang', CURRENT_LANG);

    var btn = document.getElementById('langBtn');
    if (btn) btn.textContent = {zh:'中', en:'EN', ja:'日'}[CURRENT_LANG];

    // Update all [data-i18n] elements
    document.querySelectorAll('[data-i18n]').forEach(function(el) {
      var key = el.getAttribute('data-i18n');
      if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
        el.placeholder = window.t(key);
      } else {
        el.textContent = window.t(key);
      }
    });

    // Update meta tags
    document.title = window.t('site-title');
    var metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) metaDesc.content = window.t('site-desc');
    var ogTitle = document.querySelector('meta[property="og:title"]');
    if (ogTitle) ogTitle.content = window.t('og-title');
    var ogDesc = document.querySelector('meta[property="og:description"]');
    if (ogDesc) ogDesc.content = window.t('og-desc');

    // Update html lang
    document.documentElement.lang = {zh:'zh-CN', en:'en', ja:'ja'}[CURRENT_LANG];

    // Refresh dynamic content
    if (window.renderZodiacs) window.renderZodiacs();
    if (window.dailyCard) window.dailyCard();
  };

  // ====== Init ======
  CURRENT_LANG = detectLang();
  var origToggle = window.toggleLang;
  window.toggleLang = function() {
    var l = window.toggleLang.original || origToggle;
    if (l) l();
  };

  // Also patch existing toggleLang reference
  window._origToggleLang = origToggle;

  console.log('[lalalin] 🌐 i18n loaded, lang:', CURRENT_LANG);
})();

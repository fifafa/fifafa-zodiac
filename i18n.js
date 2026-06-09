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
    'site-title':     { zh:'拉拉林 · 星之密语 | AI东方命理 · 八字 · 面相 · 手相',
                        en:'Lalalin · Star Whispers | AI Eastern Fortune · Bazi · Face Reading · Palm Reading',
                        ja:'ララリン · 星のささやき | AI東洋占い · 八字 · 人相 · 手相' },
    'site-desc':      { zh:'拉拉林——你的AI东方命理师。八字命盘、面相分析、手相解读。探索你的星图。',
                        en:'Lalalin — your AI Eastern fortune teller. Bazi chart, face reading, palm reading. Explore your star map.',
                        ja:'ララリン——あなたのAI東洋占い師。八字命盤、人相鑑定、手相鑑定。あなたの星図を探索。' },
    'og-title':       { zh:'拉拉林 · 星之密语',  en:'Lalalin · Star Whispers',   ja:'ララリン · 星のささやき' },
    'og-desc':        { zh:'AI东方命理师。八字·面相·手相',  en:'AI Eastern Fortune Teller. Bazi · Face Reading · Palm Reading',  ja:'AI東洋占い師。八字·人相·手相' },

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
    'result-loading':   { zh:'AI 正在推演命盘…',        en:'AI is reading your fortune…',       ja:'AIが運命を読み解いています…' },
    'result-ai-badge':  { zh:'🤖 DeepSeek AI 深度解读',  en:'🤖 DeepSeek AI Deep Reading',        ja:'🤖 DeepSeek AI 深層鑑定' },

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
      } else {
        el.textContent = window.t(key);
      }
    });
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
  function doApply() { applyLang(); }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', doApply);
  } else {
    doApply();
  }

  console.log('[lalalin] 🌐 i18n loaded, lang:', CURRENT_LANG);
})();

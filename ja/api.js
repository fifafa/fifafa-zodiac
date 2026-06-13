/**
 * lalalin.xyz Fortune API Integration v2.3
 * Fortune telling API with free trial + paywall
 */
(function() {
  'use strict';

  var API_BASE = (function() {
    if (window.location.hostname === 'lalalin.xyz' && window.location.port === '8443') return '';
    return 'https://lalalin.xyz';
  })();
  var GATEWAY = API_BASE;
  var AI_ENABLED = true;
  var FREE_LIMIT = 3;

  var LOADING_HTML = function() {
    var t = window.t || function(k,d){return d;};
    return '<div class="ai-loading"><div class="ai-spinner"></div><p>'+t('load-title','正在推演命盘…')+'</p><p class="ai-loading-sub">'+t('load-sub','深度分析中，约需 5-10 秒')+'</p></div>';
  };
  function getErrorHTML() {
    var t = window.t || function(k,d){return d;};
    return '<div class="ai-error"><div class="ai-error-icon">⚠️</div><p class="ai-error-title">'+t('err-title','连接失败')+'</p><p class="ai-error-msg" id="aiErrorMsg">'+t('err-msg','无法连接到服务，请稍后重试')+'</p><button class="ai-retry-btn" onclick="location.reload()">'+t('err-retry','🔄 重新加载')+'</button></div>';
  }
  function getPaywallHTML() {
    var t = window.t || function(k,d){return d;};
    return '<div class="ai-paywall"><div class="ai-paywall-icon">🔒</div><h3 class="ai-paywall-title">'+t('pw-title','免费次数已用完')+'</h3><p class="ai-paywall-desc">'+t('pw-desc','每次深度解读都需要算力支持，感谢理解与支持')+'</p><div class="ai-paywall-plans"><div class="ai-paywall-plan" onclick="document.getElementById(\'pp-modal-overlay\')&&document.getElementById(\'pp-modal-overlay\').classList.add(\'show\')"><span class="ai-paywall-price">$1.99</span><span>'+t('pw-coffee','请喝杯咖啡')+'</span></div><div class="ai-paywall-plan ai-paywall-plan-best" onclick="document.getElementById(\'pp-modal-overlay\')&&document.getElementById(\'pp-modal-overlay\').classList.add(\'show\')"><span class="ai-paywall-price">$5.99/月</span><span>'+t('pw-monthly','无限解读 ⭐')+'</span></div></div><p class="ai-paywall-alt">'+t('pw-alt','或试试其他模块：')+'<a onclick="goCh(\'mianxiang\')">☉ '+t('svc-face','Face Reading')+'</a> · <a onclick="goCh(\'shouxiang\')">✋ '+t('svc-palm','Palm Reading')+'</a></p></div>';
  }

  // Free trial / premium
  function getFreeReadings() {
    try { var v = localStorage.getItem('lalalin-free-readings'); return v !== null ? parseInt(v) : FREE_LIMIT; }
    catch(e) { return FREE_LIMIT; }
  }
  function useFreeReading() {
    var n = getFreeReadings();
    if (n > 0) try { localStorage.setItem('lalalin-free-readings', n - 1); } catch(e) {}
    return n - 1;
  }
  function hasPremium() {
    try { return !!localStorage.getItem('lalalin-premium'); } catch(e) { return false; }
  }
  function showPaywall(targetId) {
    clearLoading();
    var el = document.getElementById(targetId);
    if (!el) return;
    var div = document.createElement('div');
    div.className = 'ai-paywall-wrap';
    div.innerHTML = getPaywallHTML();
    el.appendChild(div);
    el.style.display = 'block';
    div.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  // Core API
  async function aiFortune(module, userData, lang) {
    if (!AI_ENABLED) return null;
    try {
      var resp = await fetch(GATEWAY + '/api/fortune', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          module: module, name: userData.name || '', gender: userData.gender || '',
          birth: userData.birth || '', birthplace: userData.birthplace || '',
          question: userData.question || '', language: lang || 'zh'
        })
      });
      if (!resp.ok) { console.warn('[AI] HTTP ' + resp.status); return { error: 'HTTP ' + resp.status }; }
      return await resp.json();
    } catch(e) { console.warn('[AI] unreachable:', e.message); return { error: e.message }; }
  }

  // Loading / Error / Result
  var _loadingTarget = null, _submitBtn = null;

  function showLoading(targetId) {
    var el = document.getElementById(targetId);
    if (!el) return;
    _loadingTarget = targetId;
    el.innerHTML = LOADING_HTML();
    el.style.display = 'block';
    el.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  function clearLoading() {
    if (!_loadingTarget) return;
    var el = document.getElementById(_loadingTarget);
    if (el) { var s = el.querySelector('.ai-loading'); if (s) s.remove(); }
    _loadingTarget = null;
    if (_submitBtn) { _submitBtn.disabled = false; _submitBtn.textContent = (window.t ? window.t('form-submit') : '开始解读'); _submitBtn = null; }
  }

  // Scan overlay — full-screen AI processing visual
  var _scanOverlay = null;
  function showScanOverlay(photoDataUrl, module) {
    hideScanOverlay();
    var t = window.t || function(k,d){return d;};
    var msg = module === 'face' ? t('loading-face', 'Analyzing facial features…') : t('palm-loading', 'Analyzing palm lines…');
    var sub = t('misc-ref', 'Neural analysis in progress');
    var tri = ['☰','☷','☵','☲'];
    var ov = document.createElement('div');
    ov.className = 'scan-overlay';
    ov.id = 'lalalinScanOverlay';
    ov.innerHTML =
      '<div class="scan-wrap">' +
        '<div class="scan-bg" style="background-image:url(' + photoDataUrl + ')"></div>' +
        '<div class="scan-core" style="background-image:url(' + photoDataUrl + ')"></div>' +
        '<div class="scan-ring"></div><div class="scan-ring r2"></div><div class="scan-ring r3"></div>' +
        '<div class="scan-line"></div>' +
        '<div class="scan-node n1"></div><div class="scan-node n2"></div><div class="scan-node n3"></div><div class="scan-node n4"></div>' +
        '<div class="scan-tag t1">' + tri[0] + '</div><div class="scan-tag t2">' + tri[1] + '</div>' +
        '<div class="scan-tag t3">' + tri[2] + '</div><div class="scan-tag t4">' + tri[3] + '</div>' +
      '</div>' +
      '<div class="scan-msg">' + msg + '</div>' +
      '<div class="scan-msg-sub">' + sub + '</div>' +
      '<div class="scan-progress"><div class="scan-progress-bar"></div></div>';
    document.body.appendChild(ov);
    _scanOverlay = ov;
    // Prevent background scroll
    document.body.style.overflow = 'hidden';
  }
  function hideScanOverlay() {
    if (_scanOverlay) { _scanOverlay.remove(); _scanOverlay = null; }
    document.body.style.overflow = '';
  }

  function showError(targetId, msg) {
    hideScanOverlay();
    clearLoading();
    var el = document.getElementById(targetId);
    if (!el) return;
    el.innerHTML = getErrorHTML();
    el.style.display = 'block';
    var m = document.getElementById('aiErrorMsg');
    if (m) m.textContent = msg || '无法连接到服务，请稍后重试';
    el.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  function injectAIResult(containerId, aiHtml) {
    hideScanOverlay();
    clearLoading();
    var container = document.getElementById(containerId);
    if (!container) return;
    var div = document.createElement('div');
    div.className = 'ai-result-section';
    div.innerHTML = '<div class="ai-badge">✦ 命理深度解读</div>'
      + '<div class="ai-content">' + formatAIResponse(aiHtml) + '</div>'
      + '<div class="ai-disclaimer">⚠️ 以上内容仅供传统文化娱乐参考</div>'
      + '<div class="ai-result-footer">'
        + '<button class="ai-share-btn" onclick="shareAIFortune()">✧ 分享结果</button>'
        + '<div class="ai-next-module">'
          + '<span class="ai-next-hint">继续探索 → </span>'
          + '<span class="ai-next-link" onclick="goCh(\'mianxiang\')">☉ 面相分析</span>'
          + '<span class="ai-next-link" onclick="goCh(\'shouxiang\')">✋ 手相解读</span>'
        + '</div>'
      + '</div>';
    container.appendChild(div);
    div.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  window.shareAIFortune = function() {
    var c = document.querySelector('.ai-content');
    var t = c ? c.textContent.trim().substring(0, 200) + '…' : '';
    var s = '🔮 TaoPulse 命理解读\\n' + t + '\\n→ lalalin.xyz';
    if (navigator.share) navigator.share({text: s}).catch(function(){});
    else navigator.clipboard.writeText(s).then(function(){ toast('已复制！') });
  };

  function formatAIResponse(text) {
    return text.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
      .replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>')
      .replace(/\n## (.+)/g,'\n<h4>$1</h4>').replace(/\n# (.+)/g,'\n<h3>$1</h3>')
      .replace(/\n- (.+)/g,'\n<li>$1</li>').replace(/\n/g,'<br>');
  }

  // Module: Bazi — defensive override with free trial gate
  function _patchBazi(){
    var origDoBazi = window.doBazi;
    window.doBazi = async function() {
      if (origDoBazi) origDoBazi();
      var y = document.getElementById('baziYear').value;
      var m = document.getElementById('baziMonth').value;
      var d = document.getElementById('baziDay').value;
      var h = document.getElementById('baziHour').value || '12';
      var g = document.getElementById('baziGender').value;
      if (!y || !m || !d) return;

      if (!hasPremium() && getFreeReadings() <= 0) {
        showPaywall('baziResult');
        if (_submitBtn) { _submitBtn.disabled = false; _submitBtn.textContent = (window.t ? window.t('form-submit') : '开始解读'); _submitBtn = null; }
        return;
      }

      _submitBtn = document.querySelector('#baziForm .btn-primary');
      if (_submitBtn) { _submitBtn.disabled = true; _submitBtn.textContent = '分析中…'; }
      showLoading('baziResult');

      var result = await aiFortune('bazi', {
        name: '', gender: g === '1' ? '男' : '女',
        birth: y + '-' + String(m).padStart(2,'0') + '-' + String(d).padStart(2,'0') + ' ' + String(h).padStart(2,'0') + ':00',
        question: '请详细解读我的八字命盘，包括事业、财运、感情、健康'
      });

      if (result && result.result) { if (!hasPremium()) useFreeReading(); injectAIResult('baziResult', result.result); }
      else if (result && result.error) showError('baziResult', result.error);
    };
  }
  if (typeof window.doBazi === 'function') _patchBazi();
  else { var _r=0,_t=setInterval(function(){if(typeof window.doBazi==='function'){_patchBazi();clearInterval(_t)}else if(++_r>30)clearInterval(_t)},100); }

  // Module: Face Reading
  var origInitMianXiang = window.initMianXiang;
  window.initMianXiang = async function() {
    if (origInitMianXiang) origInitMianXiang();
    window._mxPhotoLoaded = async function() {
      if (window._mxPhotoData) {
        showScanOverlay(window._mxPhotoData, 'face');
        showLoading('mianxiangResult');
        var r = await aiFortune('face', { name: '', question: '请根据面相分析性格与运势' });
        hideScanOverlay();
        if (r && r.result) injectAIResult('mianxiangResult', r.result);
        else if (r && r.error) showError('mianxiangResult', r.error);
      }
    };
  };

  // Module: Palm Reading — real CV pipeline
  var origReadShouXiang = window.readShouXiang;
  window.readShouXiang = async function() {
    if (!window._sxPhotoData || !window._sxPhotoLoaded) {
      if (window.t) toast(window.t('misc-photo-or-upload'));
      return;
    }
    // Button loading state
    var btn = document.querySelector('#palmPhotoWrap .btn-primary');
    var btnOrig = btn ? btn.textContent : '';
    if (btn) { btn.disabled = true; btn.textContent = window.t ? window.t('palm-btn-analyzing') : '分析中…'; }
    showScanOverlay(window._sxPhotoData, 'palm');
    showLoading('sxResult');
    var base64 = window._sxPhotoData.split(',')[1] || window._sxPhotoData;
    try {
      var resp = await fetch(GATEWAY + '/api/palm/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image_base64: base64, language: (window._currentLang || 'zh') })
      });
      if (!resp.ok) {
        var t = window.t || function(k){return k;};
        var errText = resp.status === 400 ? t('palm-err-nohand') : t('palm-err-server') + ' (' + resp.status + ')';
        throw new Error(errText);
      }
      var data = await resp.json();
      if (data.report) injectAIResult('sxResult', data.report);
    } catch(e) { hideScanOverlay(); showError('sxResult', e.message); }
    if (btn) { btn.disabled = false; btn.textContent = btnOrig; }
  };

  // CSS
  function addAIStyles() {
    var s = document.createElement('style');
    s.textContent = [
      '.ai-result-section{margin:20px 0;padding:20px 16px;background:linear-gradient(135deg,rgba(107,91,138,0.15),rgba(61,139,107,0.1));border:1px solid rgba(200,166,74,0.3);border-radius:12px;animation:aiFadeIn .6s ease}',
      '.ai-badge{display:inline-block;padding:4px 12px;background:rgba(200,166,74,0.2);border:1px solid var(--gold);border-radius:20px;font-size:.78em;color:var(--gold);margin-bottom:14px;letter-spacing:.05em}',
      '.ai-content{color:var(--moon);font-size:.92em;line-height:1.8;letter-spacing:.03em}',
      '.ai-content h3{color:var(--gold);font-size:1.1em;margin:16px 0 8px;font-weight:600}',
      '.ai-content h4{color:var(--gold);font-size:1em;margin:12px 0 6px;font-weight:600}',
      '.ai-content strong{color:#ede4d0}',
      '.ai-content li{margin-left:16px;padding:2px 0}',
      '.ai-disclaimer{text-align:center;color:var(--moon3);font-size:.65em;margin:16px 0 4px;opacity:.55;letter-spacing:.04em}',
      '.ai-loading{text-align:center;padding:40px;color:var(--gold)}',
      '.ai-loading-sub{font-size:.78em;opacity:.6;margin-top:8px}',
      '.ai-spinner{width:36px;height:36px;margin:0 auto 16px;border:2px solid rgba(200,166,74,0.2);border-top-color:var(--gold);border-radius:50%;animation:aiSpin 1s linear infinite}',
      '.ai-error{text-align:center;padding:30px 16px;background:rgba(220,38,38,0.08);border:1px solid rgba(220,38,38,0.25);border-radius:12px;margin:20px 0}',
      '.ai-error-icon{font-size:2em;margin-bottom:8px}',
      '.ai-error-title{color:#f87171;font-size:1em;font-weight:600;margin:4px 0}',
      '.ai-error-msg{color:var(--moon);font-size:.85em;opacity:.8;margin:8px 0 16px}',
      '.ai-retry-btn{padding:8px 20px;background:rgba(200,166,74,0.15);border:1px solid var(--gold);border-radius:20px;color:var(--gold);font-size:.88em;cursor:pointer;transition:all .2s}',
      '.ai-retry-btn:hover{background:rgba(200,166,74,0.3);transform:translateY(-1px)}',
      '.ai-result-footer{margin-top:20px;padding-top:16px;border-top:1px solid rgba(200,166,74,0.15);text-align:center}',
      '.ai-share-btn{padding:10px 28px;background:linear-gradient(135deg,rgba(200,166,74,0.15),rgba(158,126,48,0.2));border:1px solid var(--gold);border-radius:22px;color:var(--gold);font-size:.88em;cursor:pointer;transition:all .25s;font-family:inherit;letter-spacing:.04em}',
      '.ai-share-btn:active{background:rgba(200,166,74,0.3);transform:scale(.96)}',
      '.ai-next-module{margin-top:14px;display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap}',
      '.ai-next-hint{color:var(--moon3);font-size:.78em}',
      '.ai-next-link{padding:6px 16px;border:1px solid rgba(200,166,74,0.2);border-radius:16px;color:var(--moon2);font-size:.78em;cursor:pointer;transition:all .2s}',
      '.ai-next-link:active{border-color:var(--gold);background:rgba(200,166,74,0.06);color:var(--gold);transform:scale(.96)}',
      '.ai-paywall-wrap{animation:aiFadeIn .6s ease}',
      '.ai-paywall{text-align:center;padding:32px 20px;background:linear-gradient(135deg,rgba(107,91,138,0.12),rgba(15,11,36,0.9));border:1px solid rgba(200,166,74,0.25);border-radius:16px;margin:20px 0}',
      '.ai-paywall-icon{font-size:3em;margin-bottom:8px}',
      '.ai-paywall-title{color:var(--gold);font-size:1.2em;margin:8px 0;letter-spacing:.06em}',
      '.ai-paywall-desc{color:var(--moon3);font-size:.82em;margin-bottom:20px;line-height:1.6}',
      '.ai-paywall-plans{display:flex;gap:10px;justify-content:center;margin-bottom:16px;flex-wrap:wrap}',
      '.ai-paywall-plan{padding:14px 20px;border:1px solid rgba(200,166,74,0.2);border-radius:12px;background:rgba(21,16,48,0.8);cursor:pointer;transition:all .2s;color:var(--moon);font-size:.82em;min-width:120px}',
      '.ai-paywall-plan:active{border-color:var(--gold);background:rgba(200,166,74,0.08);transform:scale(.96)}',
      '.ai-paywall-plan-best{border-color:var(--gold);background:rgba(200,166,74,0.06)}',
      '.ai-paywall-price{display:block;font-size:1.3em;color:var(--gold);font-weight:700;margin-bottom:4px}',
      '.ai-paywall-alt{color:var(--moon3);font-size:.72em}',
      '.ai-paywall-alt a{color:var(--gold);cursor:pointer;text-decoration:underline}',
      '@keyframes aiFadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}',
      '@keyframes aiSpin{to{transform:rotate(360deg)}}'
    ].join('');
    document.head.appendChild(s);
  }

  addAIStyles();
  console.log('[lalalin] 🤖 v2.2 — free trial + paywall loaded');
})();

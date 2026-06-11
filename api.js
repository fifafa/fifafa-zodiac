/**
 * lalalin.xyz AI Fortune API Integration v2.0
 * DeepSeek-powered fortune telling with robust error handling
 */
(function() {
  'use strict';

  // Auto-detect: try same-origin first, fall back to direct server
  var API_BASE = (function() {
    if (window.location.hostname === 'lalalin.xyz' && window.location.port === '8443') {
      return '';
    }
    return 'https://fifafa.xyz:8443'; // valid Let's Encrypt cert
  })();
  var GATEWAY = API_BASE;
  var AI_ENABLED = true;
  var LOADING_HTML = '<div class="ai-loading"><div class="ai-spinner"></div><p>AI 正在推演命盘…</p><p class="ai-loading-sub">DeepSeek 深度分析中，约需 5-10 秒</p></div>';
  var ERROR_HTML = '<div class="ai-error"><div class="ai-error-icon">⚠️</div><p class="ai-error-title">连接失败</p><p class="ai-error-msg" id="aiErrorMsg">无法连接到 AI 服务，请稍后重试</p><button class="ai-retry-btn" onclick="location.reload()">🔄 重新加载</button></div>';

  // ====== Core API ======
  async function aiFortune(module, userData, lang) {
    if (!AI_ENABLED) return null;
    try {
      var resp = await fetch(GATEWAY + '/api/fortune', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          module: module,
          name: userData.name || '',
          gender: userData.gender || '',
          birth: userData.birth || '',
          birthplace: userData.birthplace || '',
          question: userData.question || '',
          language: lang || 'zh'
        })
      });
      if (!resp.ok) {
        console.warn('[AI Fortune] HTTP ' + resp.status);
        return { error: 'HTTP ' + resp.status };
      }
      var data = await resp.json();
      return data;
    } catch(e) {
      console.warn('[AI Fortune] API unreachable:', e.message);
      return { error: e.message };
    }
  }

  // ====== Loading state manager ======
  function showLoading(targetId) {
    var el = document.getElementById(targetId);
    if (!el) return;
    el.innerHTML = LOADING_HTML;
    el.style.display = 'block';
    el.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  function showError(targetId, msg) {
    var el = document.getElementById(targetId);
    if (!el) return;
    el.innerHTML = ERROR_HTML;
    el.style.display = 'block';
    var msgEl = document.getElementById('aiErrorMsg');
    if (msgEl) msgEl.textContent = msg || '无法连接到 AI 服务，请稍后重试';
    el.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  // ====== Result injection ======
  function injectAIResult(containerId, aiHtml) {
    var container = document.getElementById(containerId);
    if (!container) return;
    var div = document.createElement('div');
    div.className = 'ai-result-section';
    div.innerHTML = '<div class="ai-badge">🤖 DeepSeek AI 深度解读</div>' +
      '<div class="ai-content">' + formatAIResponse(aiHtml) + '</div>' +
      '<div class="ai-result-footer">' +
        '<button class="ai-share-btn" onclick="shareAIFortune()">✧ 分享结果</button>' +
        '<div class="ai-next-module">' +
          '<span class="ai-next-hint">继续探索 → </span>' +
          '<span class="ai-next-link" onclick="goCh(\'mianxiang\')">☉ 面相分析</span>' +
          '<span class="ai-next-link" onclick="goCh(\'shouxiang\')">✋ 手相解读</span>' +
        '</div>' +
      '</div>';
    if (container.firstChild) {
      container.insertBefore(div, container.firstChild.nextSibling);
    } else {
      container.appendChild(div);
    }
    div.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  // Share AI fortune result
  window.shareAIFortune = function() {
    var content = document.querySelector('.ai-content');
    var text = content ? content.textContent.trim().substring(0, 200) + '…' : '';
    var shareText = '🔮 拉拉林 AI 命理解读\n' + text + '\n→ lalalin.xyz';
    if (navigator.share) { navigator.share({text: shareText}).catch(function(){}) }
    else { navigator.clipboard.writeText(shareText).then(function(){ toast('已复制！') }) }
  };

  function formatAIResponse(text) {
    text = text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/\n## (.+)/g, '\n<h4>$1</h4>')
      .replace(/\n# (.+)/g, '\n<h3>$1</h3>')
      .replace(/\n- (.+)/g, '\n<li>$1</li>')
      .replace(/\n/g, '<br>');
    return text;
  }

  // ====== Module: 八字 (Bazi) — defensive override ======
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

      showLoading('baziResult');

      var result = await aiFortune('bazi', {
        name: '',
        gender: g === '1' ? '男' : '女',
        birth: y + '-' + String(m).padStart(2,'0') + '-' + String(d).padStart(2,'0') + ' ' + String(h).padStart(2,'0') + ':00',
        question: '请详细解读我的八字命盘，包括事业、财运、感情、健康'
      });

      if (result && result.result) {
        injectAIResult('baziResult', result.result);
      } else if (result && result.error) {
        showError('baziResult', result.error);
      }
    };
  }
  // Ensure original doBazi exists before patching; retry up to 3s
  if (typeof window.doBazi === 'function') { _patchBazi(); }
  else { var _baziRetry=0,_baziTimer=setInterval(function(){if(typeof window.doBazi==='function'){_patchBazi();clearInterval(_baziTimer)}else if(++_baziRetry>30)clearInterval(_baziTimer)},100); }

  // ====== Module: 面相 (Face Reading) ======
  var origInitMianXiang = window.initMianXiang;
  window.initMianXiang = async function() {
    if (origInitMianXiang) origInitMianXiang();
    var oldOnload = window._mxPhotoLoaded;
    window._mxPhotoLoaded = async function() {
      if (window._mxPhotoData) {
        showLoading('mianxiangResult');
        var result = await aiFortune('face', {
          name: '',
          question: '请根据面相分析性格与运势'
        });
        if (result && result.result) {
          injectAIResult('mianxiangResult', result.result);
        } else if (result && result.error) {
          showError('mianxiangResult', result.error);
        }
      }
    };
  };

  // ====== Module: 手相 (Palm Reading) ======
  var origShowPalmPhoto = window.showPalmPhoto;
  window.showPalmPhoto = async function() {
    if (origShowPalmPhoto) origShowPalmPhoto();
    if (window._sxPhotoLoaded) {
      showLoading('shouxiangResult');
      var result = await aiFortune('palm', {
        name: '',
        question: '请根据手相分析性格与命运走向'
      });
      if (result && result.result) {
        injectAIResult('shouxiangResult', result.result);
      } else if (result && result.error) {
        showError('shouxiangResult', result.error);
      }
    }
  };

  // ====== Add CSS for AI results ======
  function addAIStyles() {
    var style = document.createElement('style');
    style.textContent = `
      .ai-result-section {
        margin: 20px 0;
        padding: 20px 16px;
        background: linear-gradient(135deg, rgba(107,91,138,0.15), rgba(61,139,107,0.1));
        border: 1px solid rgba(200,166,74,0.3);
        border-radius: 12px;
        animation: aiFadeIn 0.6s ease;
      }
      .ai-badge {
        display: inline-block;
        padding: 4px 12px;
        background: rgba(200,166,74,0.2);
        border: 1px solid var(--gold);
        border-radius: 20px;
        font-size: 0.78em;
        color: var(--gold);
        margin-bottom: 14px;
        letter-spacing: 0.05em;
      }
      .ai-content {
        color: var(--moon);
        font-size: 0.92em;
        line-height: 1.8;
        letter-spacing: 0.03em;
      }
      .ai-content h3 { color: var(--gold); font-size: 1.1em; margin: 16px 0 8px; font-weight:600; }
      .ai-content h4 { color: var(--gold); font-size: 1em; margin: 12px 0 6px; font-weight:600; }
      .ai-content strong { color: #ede4d0; }
      .ai-content li { margin-left: 16px; padding: 2px 0; }

      .ai-loading {
        text-align: center;
        padding: 40px;
        color: var(--gold);
      }
      .ai-loading-sub {
        font-size: 0.78em;
        opacity: 0.6;
        margin-top: 8px;
      }
      .ai-spinner {
        width: 36px; height: 36px;
        margin: 0 auto 16px;
        border: 2px solid rgba(200,166,74,0.2);
        border-top-color: var(--gold);
        border-radius: 50%;
        animation: aiSpin 1s linear infinite;
      }

      .ai-error {
        text-align: center;
        padding: 30px 16px;
        background: rgba(220,38,38,0.08);
        border: 1px solid rgba(220,38,38,0.25);
        border-radius: 12px;
        margin: 20px 0;
      }
      .ai-error-icon { font-size: 2em; margin-bottom: 8px; }
      .ai-error-title { color: #f87171; font-size: 1em; font-weight:600; margin: 4px 0; }
      .ai-error-msg { color: var(--moon); font-size: 0.85em; opacity: 0.8; margin: 8px 0 16px; }
      .ai-retry-btn {
        padding: 8px 20px;
        background: rgba(200,166,74,0.15);
        border: 1px solid var(--gold);
        border-radius: 20px;
        color: var(--gold);
        font-size: 0.88em;
        cursor: pointer;
        transition: all 0.2s;
      }
      .ai-retry-btn:hover {
        background: rgba(200,166,74,0.3);
        transform: translateY(-1px);
      }

      .ai-result-footer {
        margin-top: 20px;
        padding-top: 16px;
        border-top: 1px solid rgba(200,166,74,0.15);
        text-align: center;
      }
      .ai-share-btn {
        padding: 10px 28px;
        background: linear-gradient(135deg, rgba(200,166,74,0.15), rgba(158,126,48,0.2));
        border: 1px solid var(--gold);
        border-radius: 22px;
        color: var(--gold);
        font-size: 0.88em;
        cursor: pointer;
        transition: all 0.25s;
        font-family: inherit;
        letter-spacing: 0.04em;
      }
      .ai-share-btn:active {
        background: rgba(200,166,74,0.3);
        transform: scale(0.96);
      }
      .ai-next-module {
        margin-top: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        flex-wrap: wrap;
      }
      .ai-next-hint {
        color: var(--moon3);
        font-size: 0.78em;
      }
      .ai-next-link {
        padding: 6px 16px;
        border: 1px solid rgba(200,166,74,0.2);
        border-radius: 16px;
        color: var(--moon2);
        font-size: 0.78em;
        cursor: pointer;
        transition: all 0.2s;
      }
      .ai-next-link:active {
        border-color: var(--gold);
        background: rgba(200,166,74,0.06);
        color: var(--gold);
        transform: scale(0.96);
      }

      @keyframes aiFadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
      @keyframes aiSpin { to { transform: rotate(360deg); } }
    `;
    document.head.appendChild(style);
  }

  // ====== Init ======
  addAIStyles();
  console.log('[lalalin] 🤖 DeepSeek AI integration v2.0 loaded');
})();

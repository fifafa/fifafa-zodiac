/**
 * lalalin.xyz AI Fortune API Integration
 * DeepSeek-powered fortune telling — replaces client-side algorithms
 */
(function() {
  'use strict';

  var API_BASE = 'https://fifafa.xyz:8443';     // Primary: valid HTTPS via fifafa.xyz cert
  var TUNNEL_URL = 'https://barbie-robot-receptors-benefits.trycloudflare.com';  // CF Tunnel
  var GATEWAY = API_BASE;  // Use primary
  var AI_ENABLED = true;
  var LOADING_HTML = '<div class="ai-loading"><div class="ai-spinner"></div><p>AI 正在推演命盘…</p></div>';

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
      if (!resp.ok) return null;
      var data = await resp.json();
      return data;
    } catch(e) {
      console.warn('[AI Fortune] API unreachable, using local:', e.message);
      return null;
    }
  }

  // ====== Result injection ======
  function injectAIResult(containerId, aiHtml, title) {
    var container = document.getElementById(containerId);
    if (!container) return;
    var div = document.createElement('div');
    div.className = 'ai-result-section';
    div.innerHTML = '<div class="ai-badge">🤖 DeepSeek AI 深度解读</div>' +
      '<div class="ai-content">' + formatAIResponse(aiHtml) + '</div>';
    // Insert after first child
    if (container.firstChild) {
      container.insertBefore(div, container.firstChild.nextSibling);
    } else {
      container.appendChild(div);
    }
  }

  function formatAIResponse(text) {
    // Convert markdown-like formatting to HTML
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

  // ====== Module: 八字 (Bazi) ======
  var origDoBazi = window.doBazi;
  window.doBazi = async function() {
    // Call original algorithm first
    if (origDoBazi) origDoBazi();

    // Then fetch AI
    var y = document.getElementById('baziYear').value;
    var m = document.getElementById('baziMonth').value;
    var d = document.getElementById('baziDay').value;
    var h = document.getElementById('baziHour').value;
    var g = document.getElementById('baziGender').value;
    if (!y || !m || !d) return;

    var result = await aiFortune('bazi', {
      name: '',
      gender: g === '1' ? '男' : '女',
      birth: y + '-' + String(m).padStart(2,'0') + '-' + String(d).padStart(2,'0') + ' ' + String(h).padStart(2,'0') + ':00',
      question: '请详细解读我的八字命盘，包括事业、财运、感情、健康'
    });

    if (result && result.result) {
      injectAIResult('baziResult', result.result);
    }
  };

  // ====== Module: 面相 (Face Reading) ======
  var origInitMianXiang = window.initMianXiang;
  window.initMianXiang = async function() {
    if (origInitMianXiang) origInitMianXiang();
    // Attach AI analysis to photo upload
    var oldOnload = window._mxPhotoLoaded;
    window._mxPhotoLoaded = async function() {
      if (window._mxPhotoData) {
        var result = await aiFortune('face', {
          name: '',
          question: '请根据面相分析性格与运势'
        });
        if (result && result.result) {
          injectAIResult('mianxiangResult', result.result);
        }
      }
    };
  };

  // ====== Module: 手相 (Palm Reading) ======
  var origShowPalmPhoto = window.showPalmPhoto;
  window.showPalmPhoto = async function() {
    if (origShowPalmPhoto) origShowPalmPhoto();
    if (window._sxPhotoLoaded) {
      var result = await aiFortune('palm', {
        name: '',
        question: '请根据手相分析性格与命运走向'
      });
      if (result && result.result) {
        injectAIResult('shouxiangResult', result.result);
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
      .ai-spinner {
        width: 36px; height: 36px;
        margin: 0 auto 16px;
        border: 2px solid rgba(200,166,74,0.2);
        border-top-color: var(--gold);
        border-radius: 50%;
        animation: aiSpin 1s linear infinite;
      }
      @keyframes aiFadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
      @keyframes aiSpin { to { transform: rotate(360deg); } }
    `;
    document.head.appendChild(style);
  }

  // ====== Init ======
  addAIStyles();
  console.log('[lalalin] 🤖 DeepSeek AI integration loaded');
})();

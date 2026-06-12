/**
 * lalalin.xyz PayPal Payment Module
 * Loads PayPal SDK, renders buttons, handles checkout flow
 * Usage: add <div class="paypal-btn-container" data-plan="v5_monthly"></div> to any page
 */
(function() {
  'use strict';

  var GATEWAY = 'https://api.lalalin.xyz';  // Cloudflare tunnel (standard 443)
  var sdkLoaded = false;
  var paypalReady = false;

  // ====== Load PayPal SDK ======
  function loadPayPalSDK(clientId) {
    if (sdkLoaded) return;
    sdkLoaded = true;

    var script = document.createElement('script');
    script.src = 'https://www.paypal.com/sdk/js?client-id=' + encodeURIComponent(clientId) +
      '&currency=USD&intent=capture&locale=' + getPayPalLocale();
    script.onload = function() {
      paypalReady = true;
      console.log('[PayPal] SDK loaded, client-id:', clientId.substring(0,10)+'...');
      renderAllButtons();
    };
    script.onerror = function() {
      console.error('[PayPal] SDK load failed');
      // Fallback: show direct PayPal.me link
      document.querySelectorAll('.paypal-btn-container').forEach(function(el) {
        el.innerHTML = '<a href="https://paypal.me/lalalin" target="_blank" ' +
          'style="display:inline-block;padding:12px 32px;background:var(--gold);' +
          'color:#1a1a2e;border-radius:8px;font-weight:700;text-decoration:none">' +
          '💳 前往 PayPal 支付</a>';
      });
    };
    document.head.appendChild(script);
  }

  function getPayPalLocale() {
    var lang = (localStorage.getItem('lalalin-lang') || navigator.language || 'zh').substring(0,2);
    var map = { zh: 'zh_CN', en: 'en_US', ja: 'ja_JP' };
    return map[lang] || 'en_US';
  }

  // ====== Init: fetch config then load SDK ======
  function init() {
    fetch(GATEWAY + '/api/paypal/config')
      .then(function(r) { return r.json(); })
      .then(function(cfg) {
        console.log('[PayPal] Config:', cfg.mode);
        loadPayPalSDK(cfg.client_id);
      })
      .catch(function(e) {
        console.warn('[PayPal] Config fetch failed:', e.message);
        // Render fallback buttons
        document.querySelectorAll('.paypal-btn-container').forEach(function(el) {
          el.innerHTML = '<div style="color:var(--moon);padding:16px;text-align:center">' +
            '💰 PayPal 支付暂不可用，请稍后重试</div>';
        });
      });
  }

  // ====== Render PayPal buttons ======
  function renderAllButtons() {
    if (!paypalReady || typeof paypal === 'undefined') return;

    document.querySelectorAll('.paypal-btn-container').forEach(function(container) {
      var plan = container.getAttribute('data-plan') || 'coffee';
      renderButton(container, plan);
    });
  }

  function renderButton(container, plan) {
    // Skip if already rendered
    if (container.querySelector('.paypal-buttons')) return;

    var wrapper = document.createElement('div');
    wrapper.className = 'paypal-buttons';
    container.innerHTML = '';
    container.appendChild(wrapper);

    paypal.Buttons({
      style: {
        layout: 'vertical',
        color: 'gold',
        shape: 'rect',
        label: 'paypal',
        tagline: false
      },

      createOrder: function() {
        return fetch(GATEWAY + '/api/paypal/create-order', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ plan: plan })
        })
        .then(function(r) { return r.json(); })
        .then(function(data) {
          if (!data.order_id) throw new Error('Order creation failed');
          console.log('[PayPal] Order created:', data.order_id);
          return data.order_id;
        })
        .catch(function(e) {
          console.error('[PayPal] Create order error:', e);
          alert('订单创建失败，请重试');
          throw e;
        });
      },

      onApprove: function(data) {
        // Show processing state
        wrapper.innerHTML = '<div style="text-align:center;padding:24px;color:var(--gold)">' +
          '<div class="ai-spinner"></div><p>正在确认支付...</p></div>';

        return fetch(GATEWAY + '/api/paypal/capture-order', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ order_id: data.orderID })
        })
        .then(function(r) { return r.json(); })
        .then(function(result) {
          console.log('[PayPal] Capture result:', result);
          if (result.status === 'completed') {
            onPaymentSuccess(container, plan, result);
          } else {
            onPaymentError(container, '支付验证失败');
          }
        })
        .catch(function(e) {
          console.error('[PayPal] Capture error:', e);
          onPaymentError(container, '支付扣款失败，请联系客服');
        });
      },

      onCancel: function() {
        wrapper.innerHTML = '<div style="text-align:center;padding:16px;color:var(--moon)">' +
          '支付已取消</div>';
        // Re-render after 3 seconds
        setTimeout(function() { renderButton(container, plan); }, 3000);
      },

      onError: function(err) {
        console.error('[PayPal] Button error:', err);
        onPaymentError(container, 'PayPal 支付出错');
      }
    }).render(wrapper);
  }

  // ====== Success / Error display ======
  function onPaymentSuccess(container, plan, result) {
    var planNames = {
      'v5_monthly': 'Lite 月度会员', 'v5_yearly': 'Lite 年度会员',
      'v16_monthly': 'Premium 月度会员', 'v16_yearly': 'Premium 年度会员',
      'lifetime': '终身会员', 'coffee': '一杯咖啡'
    };
    container.innerHTML =
      '<div style="text-align:center;padding:24px;animation:aiFadeIn 0.6s ease">' +
      '<div style="font-size:48px;margin-bottom:12px">🎉</div>' +
      '<div style="color:var(--gold);font-size:1.2em;font-weight:700;margin-bottom:8px">' +
      '支付成功！感谢支持 🙏</div>' +
      '<div style="color:var(--moon);font-size:0.9em">' +
      (planNames[plan] || plan) + ' · ' + result.currency + ' ' + result.amount + '</div>' +
      '<div style="color:var(--text3);font-size:0.75em;margin-top:6px">' +
      'Transaction: ' + (result.transaction_id || '').substring(0, 17) + '...</div>' +
      '</div>';

    // Store in localStorage for premium access unlock
    try { localStorage.setItem('lalalin-premium', JSON.stringify({
      plan: plan, date: new Date().toISOString(), tx: result.transaction_id
    })); } catch(e) {}

    // Reload page after 2 seconds to unlock features
    setTimeout(function() { location.reload(); }, 2000);
  }

  function onPaymentError(container, msg) {
    container.innerHTML =
      '<div style="text-align:center;padding:20px;color:var(--red)">' +
      '❌ ' + msg + '</div>' +
      '<div style="text-align:center;margin-top:8px">' +
      '<button onclick="location.reload()" style="' +
      'padding:8px 24px;background:var(--gold);color:#1a1a2e;border:none;' +
      'border-radius:6px;font-weight:700;cursor:pointer">重新加载</button></div>';
  }

  // ====== Floating support button ======
  function injectFloatingButton() {
    // Don't duplicate
    if (document.getElementById('pp-float-btn')) return;

    var plan = document.body.getAttribute('data-paypal-plan') ||
               (window.location.pathname.indexOf('v16') >= 0 ? 'v16_monthly' :
                window.location.pathname.indexOf('v5') >= 0 ? 'v5_monthly' :
                'coffee');

    var style = document.createElement('style');
    style.textContent = `
      .pp-float-btn {
        position: fixed; bottom: 24px; right: 20px; z-index: 9999;
        width: 52px; height: 52px; border-radius: 50%;
        background: linear-gradient(135deg, #0070ba, #003087);
        color: #fff; border: 2px solid rgba(255,255,255,0.2);
        font-size: 22px; cursor: pointer; display: flex;
        align-items: center; justify-content: center;
        box-shadow: 0 4px 16px rgba(0,112,186,0.4);
        transition: transform .2s, box-shadow .2s;
      }
      .pp-float-btn:hover { transform: scale(1.08); box-shadow: 0 6px 24px rgba(0,112,186,0.6); }
      .pp-float-btn:active { transform: scale(0.95); }
    `;
    document.head.appendChild(style);

    // Floating PayPal button — opens the static payment modal
    var btn = document.createElement('div');
    btn.id = 'pp-float-btn';
    btn.className = 'pp-float-btn';
    btn.innerHTML = '💳';
    btn.title = '支持我们';
    btn.onclick = function() {
      var overlay = document.getElementById('pp-modal-overlay');
      if (overlay) overlay.classList.add('show');
    };
    document.body.appendChild(btn);
  }

  // ====== Start ======
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() { injectFloatingButton(); init(); });
  } else {
    injectFloatingButton();
    init();
  }
})();

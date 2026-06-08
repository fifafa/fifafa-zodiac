/**
 * lalalin.xyz PayPal Payment Module
 * Loads PayPal SDK, renders buttons, handles checkout flow
 * Usage: add <div class="paypal-btn-container" data-plan="v5_monthly"></div> to any page
 */
(function() {
  'use strict';

  var GATEWAY = 'https://fifafa.xyz:8443';  // API base: valid Let's Encrypt cert + CORS
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
      .pp-modal-overlay {
        display: none; position: fixed; inset: 0; z-index: 10000;
        background: rgba(0,0,0,0.75); justify-content: center; align-items: center;
      }
      .pp-modal-overlay.show { display: flex; }
      .pp-modal {
        background: var(--bg,#1a1a2e); border: 1px solid var(--bd,rgba(200,166,74,0.2));
        border-radius: 16px; padding: 24px; max-width: 380px; width: 90%;
        color: var(--text,#ede4d0); animation: aiFadeIn .3s ease;
      }
      .pp-modal h3 { text-align: center; color: var(--gold,#c8a64a); margin-bottom: 8px; }
      .pp-modal .pp-sub { text-align: center; color: var(--moon3,#888); font-size: .8em; margin-bottom: 20px; }
      .pp-plan-row {
        display: flex; gap: 8px; margin-bottom: 8px; flex-wrap: wrap;
      }
      .pp-plan-chip {
        flex: 1; min-width: 80px; padding: 10px 8px; text-align: center;
        border: 1px solid var(--bd); border-radius: 10px; cursor: pointer;
        font-size: .75em; color: var(--moon); transition: .2s;
        background: var(--card2);
      }
      .pp-plan-chip:hover, .pp-plan-chip.sel {
        border-color: var(--gold); background: rgba(200,166,74,0.1); color: var(--gold);
      }
      .pp-plan-chip .p { font-weight: 700; font-size: 1.1em; }
      .pp-close {
        text-align: center; margin-top: 16px; color: var(--moon3);
        font-size: .75em; cursor: pointer;
      }
    `;
    document.head.appendChild(style);

    // Floating button
    var btn = document.createElement('div');
    btn.id = 'pp-float-btn';
    btn.className = 'pp-float-btn';
    btn.innerHTML = '💳';
    btn.title = '支持我们';
    btn.onclick = function() { showPaymentModal(plan); };
    document.body.appendChild(btn);

    // Modal
    var overlay = document.createElement('div');
    overlay.id = 'pp-modal-overlay';
    overlay.className = 'pp-modal-overlay';
    overlay.onclick = function(e) { if (e.target === overlay) overlay.classList.remove('show'); };

    var modal = document.createElement('div');
    modal.className = 'pp-modal';
    modal.innerHTML =
      '<h3>💰 支持 lalalin.xyz</h3>' +
      '<div class="pp-sub">AI命理服务需要持续维护，感谢你的支持</div>' +
      '<div class="pp-plan-row">' +
      '<div class="pp-plan-chip sel" data-plan="coffee"><div class="p">$1.99</div>请喝杯咖啡</div>' +
      '<div class="pp-plan-chip" data-plan="v16_monthly"><div class="p">$5.99</div>月度会员</div>' +
      '</div>' +
      '<div class="pp-plan-row">' +
      '<div class="pp-plan-chip" data-plan="v16_yearly"><div class="p">$39.99</div>年度会员</div>' +
      '<div class="pp-plan-chip" data-plan="lifetime"><div class="p">$49.99</div>终身会员</div>' +
      '</div>' +
      '<div id="pp-btn-container" class="paypal-btn-container" data-plan="coffee" style="margin-top:16px;min-height:150px"></div>' +
      '<div class="pp-close" onclick="document.getElementById(\'pp-modal-overlay\').classList.remove(\'show\')">✕ 关闭</div>';

    overlay.appendChild(modal);
    document.body.appendChild(overlay);

    // Plan chip click handler
    modal.querySelectorAll('.pp-plan-chip').forEach(function(chip) {
      chip.onclick = function() {
        modal.querySelectorAll('.pp-plan-chip').forEach(function(c) { c.classList.remove('sel'); });
        this.classList.add('sel');
        var container = document.getElementById('pp-btn-container');
        if (container) {
          container.setAttribute('data-plan', this.getAttribute('data-plan'));
          // Re-render button
          container.innerHTML = '';
          if (paypalReady) renderButton(container, this.getAttribute('data-plan'));
        }
      };
    });
  }

  function showPaymentModal(plan) {
    var overlay = document.getElementById('pp-modal-overlay');
    if (overlay) {
      overlay.classList.add('show');
      var container = document.getElementById('pp-btn-container');
      if (container && paypalReady && !container.querySelector('.paypal-buttons')) {
        renderButton(container, plan);
      }
    }
  }

  // ====== Start ======
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() { injectFloatingButton(); init(); });
  } else {
    injectFloatingButton();
    init();
  }
})();

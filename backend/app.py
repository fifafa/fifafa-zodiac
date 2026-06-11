#!/usr/bin/env python3
"""
lalalin.xyz FastAPI Backend
Replaces OpenClaw Gateway — direct DeepSeek API integration
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
import time
import aiohttp
import urllib.parse
import base64
import tempfile

from face_detect import extract_features
from face_report import FaceReportGenerator
from knowledge.face_kb_v2 import get_knowledge_context, match_features

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))

from deepseek_client import DeepSeekClient
from prompts import PROMPTS
from palm_detect import analyze_palm
from palm_kb import get_palm_context

app = FastAPI(title="lalalin AI Backend", version="1.0.0")

# Admin auth token
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN", "lalalin2026")

# Usage stats (in-memory, resets on restart)
from collections import defaultdict
from datetime import datetime, date
stats = {
    "total_calls": 0,
    "today_calls": 0,
    "today_date": str(date.today()),
    "calls_by_module": defaultdict(int),
    "total_tokens": 0,
    "errors": 0,
    "started_at": datetime.utcnow().isoformat() + "Z",
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://lalalin.xyz",
        "https://www.lalalin.xyz",
        "https://fifafa.xyz",
        "https://fifafa.xyz:8443",
    ],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    max_age=86400,
)

# Init DeepSeek client
deepseek = DeepSeekClient(
    api_key=os.environ.get("DEEPSEEK_API_KEY", ""),
    base_url=os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
)


class FortuneRequest(BaseModel):
    module: str  # bazi, tarot, zodiac, ziwei, face, palm, mole, dream
    name: Optional[str] = ""
    gender: Optional[str] = ""
    birth: Optional[str] = ""  # YYYY-MM-DD HH:MM or YYYY-MM-DD
    birthplace: Optional[str] = ""
    question: Optional[str] = ""
    language: Optional[str] = "zh"


class FortuneResponse(BaseModel):
    module: str
    result: str
    model: str
    tokens_used: int
    elapsed_ms: float


@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "lalalin-backend", "version": "1.0.0"}


@app.post("/api/fortune", response_model=FortuneResponse)
async def fortune(req: FortuneRequest):
    """AI fortune-telling endpoint"""
    module = req.module.lower()

    if module not in PROMPTS:
        raise HTTPException(status_code=400, detail=f"Unknown module: {module}")

    # Track stats
    today = str(date.today())
    if stats["today_date"] != today:
        stats["today_date"] = today
        stats["today_calls"] = 0
    stats["total_calls"] += 1
    stats["today_calls"] += 1
    stats["calls_by_module"][module] += 1

    system_prompt = PROMPTS[module]
    lang = req.language or "zh"
    if lang != "zh":
        system_prompt += f"\n\nYou MUST respond in {lang} language."

    # Build user message
    parts = []
    if req.name:
        parts.append(f"姓名: {req.name}")
    if req.gender:
        g = "男" if req.gender.lower() in ("m", "male", "男") else "女"
        parts.append(f"性别: {g}")
    if req.birth:
        parts.append(f"出生: {req.birth}")
    if req.birthplace:
        parts.append(f"出生地: {req.birthplace}")
    if req.question:
        parts.append(f"问题: {req.question}")

    user_message = "\n".join(parts) if parts else "请为我进行" + module + "解读"

    # Call DeepSeek
    start = time.time()
    result_text, tokens = await deepseek.chat(
        system=system_prompt,
        user=user_message,
        model="deepseek-chat",
        max_tokens=2048,
    )
    elapsed = (time.time() - start) * 1000
    stats["total_tokens"] += tokens

    return FortuneResponse(
        module=module,
        result=result_text,
        model="deepseek-chat",
        tokens_used=tokens,
        elapsed_ms=round(elapsed),
    )


# ====== PayPal Payment Integration ======

PAYPAL_CLIENT_ID = os.environ.get("PAYPAL_CLIENT_ID", "")
PAYPAL_SECRET = os.environ.get("PAYPAL_SECRET", "")
PAYPAL_MODE = os.environ.get("PAYPAL_MODE", "sandbox")
PAYPAL_API = "https://api-m.paypal.com" if PAYPAL_MODE == "live" else "https://api-m.sandbox.paypal.com"

PLANS = {
    "v5_monthly":  {"name": "Lite Monthly",  "name_zh": "Lite 月度会员", "price": "2.99",  "currency": "USD"},
    "v5_yearly":   {"name": "Lite Yearly",   "name_zh": "Lite 年度会员", "price": "19.99", "currency": "USD"},
    "v16_monthly": {"name": "Premium Monthly","name_zh": "Premium 月度会员","price": "5.99",  "currency": "USD"},
    "v16_yearly":  {"name": "Premium Yearly", "name_zh": "Premium 年度会员","price": "39.99", "currency": "USD"},
    "lifetime":    {"name": "Lifetime",       "name_zh": "终身会员",       "price": "49.99", "currency": "USD"},
    "coffee":      {"name": "Buy Me a Coffee","name_zh": "请喝杯咖啡",     "price": "1.99",  "currency": "USD"},
}


async def _paypal_token():
    """Fetch PayPal OAuth2 access token"""
    async with aiohttp.ClientSession() as session:
        auth = aiohttp.BasicAuth(PAYPAL_CLIENT_ID, PAYPAL_SECRET)
        async with session.post(
            f"{PAYPAL_API}/v1/oauth2/token",
            data={"grant_type": "client_credentials"},
            auth=auth,
            headers={"Accept": "application/json", "Accept-Language": "en_US"},
        ) as resp:
            data = await resp.json()
            if resp.status != 200:
                raise HTTPException(status_code=502, detail=f"PayPal auth failed: {data}")
            return data["access_token"]


@app.get("/api/paypal/config")
async def paypal_config():
    """Return PayPal Client ID for frontend SDK init"""
    if not PAYPAL_CLIENT_ID:
        raise HTTPException(status_code=503, detail="PayPal not configured")
    return {"client_id": PAYPAL_CLIENT_ID, "mode": PAYPAL_MODE}


class CreateOrderRequest(BaseModel):
    plan: str  # plan key from PLANS dict

class CaptureOrderRequest(BaseModel):
    order_id: str

@app.post("/api/paypal/create-order")
async def create_paypal_order(req: CreateOrderRequest):
    """Create a PayPal order, return orderID for frontend approval"""
    plan = PLANS.get(req.plan)
    if not plan:
        raise HTTPException(status_code=400, detail=f"Unknown plan: {req.plan}")

    token = await _paypal_token()

    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{PAYPAL_API}/v2/checkout/orders",
            json={
                "intent": "CAPTURE",
                "purchase_units": [{
                    "amount": {
                        "currency_code": plan["currency"],
                        "value": plan["price"]
                    },
                    "description": f"lalalin.xyz — {plan['name_zh']} ({plan['name']})"
                }],
                "application_context": {
                    "brand_name": "lalalin.xyz",
                    "landing_page": "NO_PREFERENCE",
                    "user_action": "PAY_NOW",
                    "shipping_preference": "NO_SHIPPING",
                }
            },
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        ) as resp:
            data = await resp.json()
            if resp.status not in (200, 201):
                raise HTTPException(status_code=502, detail=f"PayPal order creation failed: {data}")
            return {
                "order_id": data["id"],
                "plan": plan["name_zh"],
                "amount": f"{plan['currency']} {plan['price']}",
            }


@app.post("/api/paypal/capture-order")
async def capture_paypal_order(req: CaptureOrderRequest):
    """Capture an approved PayPal order"""
    token = await _paypal_token()

    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{PAYPAL_API}/v2/checkout/orders/{urllib.parse.quote(req.order_id, safe='')}/capture",
            json={},
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        ) as resp:
            data = await resp.json()
            if resp.status not in (200, 201):
                raise HTTPException(status_code=502, detail=f"PayPal capture failed: {data}")
            # Extract relevant info
            capture = data.get("purchase_units", [{}])[0].get("payments", {}).get("captures", [{}])[0]
            return {
                "status": "completed",
                "transaction_id": capture.get("id", ""),
                "amount": capture.get("amount", {}).get("value", ""),
                "currency": capture.get("amount", {}).get("currency_code", "USD"),
                "payer_email": data.get("payer", {}).get("email_address", ""),
            }


# ====== Face Personality Analysis API ======

class FaceAnalyzeRequest(BaseModel):
    image_base64: str  # base64-encoded JPEG/PNG
    gender: Optional[str] = None
    age_range: Optional[str] = None
    concern: Optional[str] = None  # what user wants to know
    language: Optional[str] = "zh"


@app.post("/api/face/analyze")
async def analyze_face(req: FaceAnalyzeRequest):
    """
    Full pipeline: photo → feature extraction → KB match → LLM report
    """
    # 1. Decode image
    try:
        image_data = base64.b64decode(req.image_base64)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid base64 image")

    # 2. Save to temp file and extract features
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        tmp.write(image_data)
        tmp_path = tmp.name

    try:
        features = extract_features(tmp_path)
    finally:
        os.unlink(tmp_path)

    if features is None:
        raise HTTPException(status_code=400, detail="No face detected in image")

    # 3. Add user context
    if req.gender:
        features["gender"] = req.gender
    if req.age_range:
        features["age_range"] = req.age_range
    if req.concern:
        features["concern"] = req.concern

    # 4. Generate report
    generator = FaceReportGenerator()
    result = await generator.generate(features)

    return {
        "features": features,
        "rules_matched": result["rules_matched"],
        "report": result["report"],
        "model": result["model"],
        "tokens_used": result["tokens_used"],
    }


@app.get("/api/face/features")
async def face_features_endpoint():
    """Quick check: is face detection available?"""
    try:
        import mediapipe
        return {"status": "ok", "mediapipe": mediapipe.__version__}
    except ImportError:
        return {"status": "unavailable", "error": "mediapipe not installed"}


# ====== Palm Reading Analysis API ======

class PalmAnalyzeRequest(BaseModel):
    image_base64: str
    language: Optional[str] = "zh"

@app.post("/api/palm/analyze")
async def analyze_palm_endpoint(req: PalmAnalyzeRequest):
    """Full pipeline: photo → MediaPipe warp → U-Net detection → classification → DeepSeek report"""
    try:
        image_data = base64.b64decode(req.image_base64)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid base64 image")

    result = analyze_palm(image_data)
    if not result.get("success"):
        stats["errors"] += 1
        raise HTTPException(status_code=400, detail=result.get("error", "Palm analysis failed"))

    # Build KB context
    kb_context = get_palm_context(result)
    
    # Build prompt
    lang = req.language or "zh"
    system_prompt = PROMPTS.get("palm", """你是一位融合东方传统手相学与现代心理学的 AI 分析师。
你的分析基于计算机视觉提取的手掌纹路特征。

【传统文化维度】
— 《手相学》：三大主线（天纹/人纹/地纹）代表感情、智慧、生命
— 《麻衣相法》手相篇
— 掌纹深浅、长短、分叉的含义

【现代心理学维度】
— 大五人格（OCEAN）
— 依恋理论
— 积极心理学

【输出规范】
在 1200 字以内完成：
## 🖐 掌纹特征概览
## 📜 传统文化解读（不少于 2 条经典引用）
## 🧠 现代心理学分析（OCEAN 维度）
## 🌱 成长建议（3 条可执行建议）
## ⚠️ 免责说明""")

    user_message = kb_context + "\n\n请基于以上手相特征数据，生成一份完整的手相解读报告。" + ("请用中文回复。" if lang == "zh" else f"Please respond in {lang}.")

    start = time.time()
    result_text, tokens = await deepseek.chat(
        system=system_prompt,
        user=user_message,
        model="deepseek-chat",
        max_tokens=2048,
    )
    elapsed = (time.time() - start) * 1000

    # Track stats
    today = str(date.today())
    if stats["today_date"] != today:
        stats["today_date"] = today
        stats["today_calls"] = 0
    stats["total_calls"] += 1
    stats["today_calls"] += 1
    stats["calls_by_module"]["palm"] += 1
    stats["total_tokens"] += tokens

    return {
        "success": True,
        "report": result_text,
        "features": result,
        "model": "deepseek-chat",
        "tokens_used": tokens,
        "elapsed_ms": round(elapsed),
    }


# ====== Admin API ======

from fastapi import Header

def _check_admin(authorization: str = Header(None)):
    if not authorization or authorization != f"Bearer {ADMIN_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True

@app.get("/api/admin/stats")
async def admin_stats(_=Header(None, alias="authorization")):
    """Get usage statistics (admin only)"""
    auth = _.split("Bearer ")[-1] if _ and "Bearer " in _ else ""
    if auth != ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {
        "started_at": stats["started_at"],
        "total_calls": stats["total_calls"],
        "today_calls": stats["today_calls"],
        "today_date": stats["today_date"],
        "calls_by_module": dict(stats["calls_by_module"]),
        "total_tokens": stats["total_tokens"],
        "errors": stats["errors"],
    }

@app.post("/api/admin/reset-stats")
async def admin_reset_stats(authorization: str = Header(None)):
    """Reset usage counters"""
    if not authorization or authorization.split("Bearer ")[-1] != ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    stats["total_calls"] = 0
    stats["today_calls"] = 0
    stats["calls_by_module"] = defaultdict(int)
    stats["total_tokens"] = 0
    stats["errors"] = 0
    return {"status": "ok", "message": "Stats reset"}

@app.get("/admin")
async def admin_panel():
    """Serve admin dashboard HTML"""
    from fastapi.responses import HTMLResponse
    html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>lalalin · 管理面板</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC',sans-serif;background:#0f0b24;color:#ede4d0;min-height:100vh;padding:24px}
h1{color:#c8a64a;margin-bottom:4px;font-size:1.5em}
.sub{color:#7a6e55;font-size:.8em;margin-bottom:24px}
.login-box{max-width:360px;margin:80px auto;padding:32px;background:#151030;border:1px solid rgba(200,166,74,0.15);border-radius:16px;text-align:center}
.login-box input{width:100%;padding:12px;margin:16px 0;border-radius:8px;border:1px solid rgba(200,166,74,0.2);background:#0f0b24;color:#ede4d0;font-size:.9em;outline:none}
.login-box input:focus{border-color:#c8a64a}
.login-box button{padding:12px 32px;background:linear-gradient(135deg,rgba(200,166,74,0.2),rgba(158,126,48,0.3));border:1px solid #c8a64a;border-radius:12px;color:#c8a64a;font-size:.9em;cursor:pointer;font-weight:600}
.login-box button:hover{background:rgba(200,166,74,0.3)}
.error{color:#dc2626;font-size:.8em;margin-top:8px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin-bottom:24px}
.stat-card{background:#151030;border:1px solid rgba(200,166,74,0.12);border-radius:14px;padding:20px}
.stat-card .label{font-size:.7em;color:#7a6e55;margin-bottom:6px;letter-spacing:.06em}
.stat-card .value{font-size:1.8em;color:#c8a64a;font-weight:700}
.stat-card .value.small{font-size:1.2em}
table{width:100%;border-collapse:collapse;margin-top:20px;background:#151030;border-radius:12px;overflow:hidden}
th,td{padding:12px 16px;text-align:left;font-size:.82em}
th{background:rgba(200,166,74,0.08);color:#c8a64a;letter-spacing:.04em}
td{border-top:1px solid rgba(200,166,74,0.06);color:#baae90}
.btn-sm{padding:6px 14px;border-radius:8px;border:1px solid rgba(200,166,74,0.2);background:rgba(200,166,74,0.06);color:#c8a64a;font-size:.75em;cursor:pointer;transition:.2s}
.btn-sm:hover{background:rgba(200,166,74,0.15)}
.actions{display:flex;gap:10px;margin:16px 0;flex-wrap:wrap}
.refresh{color:#7a6e55;font-size:.7em;margin-left:8px}
</style>
</head>
<body>
<div id="loginBox" class="login-box">
  <h1>🔐 管理面板</h1>
  <p class="sub">lalalin.xyz Admin</p>
  <input id="tokenInput" type="password" placeholder="输入管理密码" autofocus>
  <button onclick="login()">登 录</button>
  <p id="loginError" class="error"></p>
</div>
<div id="dashboard" style="display:none">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px">
    <div><h1>📊 lalalin 管理面板</h1><p class="sub">实时用量统计</p></div>
    <button class="btn-sm" onclick="logout()">登出</button>
  </div>
  <div class="grid" id="statsGrid"></div>
  <h3 style="color:#c8a64a;margin:20px 0 12px">📋 模块用量</h3>
  <table><thead><tr><th>模块</th><th>调用次数</th></tr></thead><tbody id="moduleTable"></tbody></table>
  <div class="actions">
    <button class="btn-sm" onclick="loadStats()">🔄 刷新</button>
    <button class="btn-sm" style="border-color:rgba(220,38,38,0.3);color:#dc2626" onclick="resetStats()">⚠️ 重置统计</button>
    <button class="btn-sm" onclick="window.open('https://lalalin.xyz')">🌐 打开网站</button>
  </div>
  <p id="serverInfo" style="color:#7a6e55;font-size:.7em;margin-top:20px"></p>
</div>
<script>
var TOKEN = '';
var API = '';

function login(){
  TOKEN = document.getElementById('tokenInput').value.trim();
  if(!TOKEN) return;
  loadStats();
}

function logout(){ TOKEN = ''; document.getElementById('loginBox').style.display='block'; document.getElementById('dashboard').style.display='none'; document.getElementById('tokenInput').value=''; }

async function loadStats(){
  if(!TOKEN) return;
  try{
    var r = await fetch('/api/admin/stats', {headers:{'Authorization':'Bearer '+TOKEN}});
    if(!r.ok) throw new Error('认证失败');
    var d = await r.json();
    document.getElementById('loginBox').style.display='none';
    document.getElementById('dashboard').style.display='block';
    document.getElementById('statsGrid').innerHTML =
      '<div class="stat-card"><div class="label">📞 总调用</div><div class="value">'+d.total_calls+'</div></div>'+
      '<div class="stat-card"><div class="label">📅 今日调用</div><div class="value">'+d.today_calls+'</div></div>'+
      '<div class="stat-card"><div class="label">🔤 总 Token</div><div class="value small">'+(d.total_tokens||0).toLocaleString()+'</div></div>'+
      '<div class="stat-card"><div class="label">⚠️ 错误数</div><div class="value">'+(d.errors||0)+'</div></div>';
    var tb = '';
    for(var k in (d.calls_by_module||{})) tb += '<tr><td>'+k+'</td><td>'+d.calls_by_module[k]+'</td></tr>';
    document.getElementById('moduleTable').innerHTML = tb || '<tr><td colspan="2" style="color:#7a6e55">暂无数据</td></tr>';
    document.getElementById('serverInfo').textContent = '🟢 服务启动: '+d.started_at+' · 统计日期: '+d.today_date;
  }catch(e){
    document.getElementById('loginError').textContent = e.message;
  }
}

async function resetStats(){
  if(!confirm('确定要重置所有统计数据？')) return;
  try{
    var r = await fetch('/api/admin/reset-stats', {method:'POST',headers:{'Authorization':'Bearer '+TOKEN}});
    if(r.ok){ loadStats(); }
  }catch(e){}
}
</script>
</body>
</html>"""
    return HTMLResponse(content=html)


if __name__ == "__main__":
    import uvicorn
    print("Starting lalalin AI Backend on 0.0.0.0:8790")
    uvicorn.run(app, host="0.0.0.0", port=8790)

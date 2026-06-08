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

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))

from deepseek_client import DeepSeekClient
from prompts import PROMPTS

app = FastAPI(title="lalalin AI Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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


if __name__ == "__main__":
    import uvicorn
    print("Starting lalalin AI Backend on 0.0.0.0:8790")
    uvicorn.run(app, host="0.0.0.0", port=8790)

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


if __name__ == "__main__":
    import uvicorn
    print("Starting lalalin AI Backend on 0.0.0.0:8790")
    uvicorn.run(app, host="0.0.0.0", port=8790)

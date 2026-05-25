#!/usr/bin/env python3
"""
DeepSeek API Client
Supports deepseek-chat (V3) and deepseek-reasoner (R1)
"""
import json
import os
from typing import Tuple

try:
    import aiohttp
except ImportError:
    aiohttp = None


class DeepSeekClient:
    def __init__(self, api_key: str = "", base_url: str = "https://api.deepseek.com"):
        self.api_key = api_key or os.environ.get("DEEPSEEK_API_KEY", "")
        self.base_url = base_url.rstrip("/")

    async def chat(
        self,
        system: str,
        user: str,
        model: str = "deepseek-chat",
        max_tokens: int = 2048,
        temperature: float = 0.7,
    ) -> Tuple[str, int]:
        """Send chat request to DeepSeek, return (text, tokens_used)"""
        if not self.api_key:
            return self._fallback_response(system, user), 0

        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]

        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": False,
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        if aiohttp:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/v1/chat/completions",
                    json=payload,
                    headers=headers,
                    timeout=aiohttp.ClientTimeout(total=60),
                ) as resp:
                    if resp.status != 200:
                        error = await resp.text()
                        return f"[API Error {resp.status}] {error[:200]}", 0
                    data = await resp.json()
                    text = data["choices"][0]["message"]["content"]
                    tokens = data.get("usage", {}).get("total_tokens", 0)
                    return text, tokens
        else:
            return self._fallback_response(system, user), 0

    def chat_sync(self, system: str, user: str, model: str = "deepseek-chat", max_tokens: int = 2048) -> Tuple[str, int]:
        """Synchronous version using requests"""
        import requests
        
        if not self.api_key:
            return self._fallback_response(system, user), 0

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "max_tokens": max_tokens,
            "temperature": 0.7,
            "stream": False,
        }

        try:
            resp = requests.post(
                f"{self.base_url}/v1/chat/completions",
                json=payload,
                headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
                timeout=60,
            )
            if resp.status_code != 200:
                return f"[API Error {resp.status_code}] {resp.text[:200]}", 0
            data = resp.json()
            text = data["choices"][0]["message"]["content"]
            tokens = data.get("usage", {}).get("total_tokens", 0)
            return text, tokens
        except Exception as e:
            return f"[Network Error] {str(e)}", 0

    def _fallback_response(self, system: str, user: str) -> str:
        """Return when API key is not configured"""
        return (
            "🔮 命理系统正在初始化中...\n\n"
            "DeepSeek API 密钥尚未配置。请联系管理员完成设置。\n\n"
            "Fortune system is initializing. DeepSeek API key not configured yet."
        )

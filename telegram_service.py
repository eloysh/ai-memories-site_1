from __future__ import annotations

from typing import Any, Dict, Optional

import httpx

from config import settings


TELEGRAM_API = "https://api.telegram.org/bot"


def bot_api_url(method: str) -> str:
    if not settings.TELEGRAM_BOT_TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")
    return f"{TELEGRAM_API}{settings.TELEGRAM_BOT_TOKEN}/{method}"


async def send_message(chat_id: int | str, text: str) -> Dict[str, Any]:
    payload = {
        "chat_id": chat_id,
        "text": text[:4000],
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(bot_api_url("sendMessage"), json=payload)
        response.raise_for_status()
        return response.json()


async def send_photo(chat_id: int | str, image_path: str, caption: str = "") -> Dict[str, Any]:
    async with httpx.AsyncClient(timeout=180) as client:
        with open(image_path, "rb") as file:
            files = {"photo": file}
            data = {"chat_id": str(chat_id), "caption": caption[:1000]}
            response = await client.post(bot_api_url("sendPhoto"), data=data, files=files)
            response.raise_for_status()
            return response.json()


async def set_webhook() -> Dict[str, Any]:
    if not settings.PUBLIC_BASE_URL:
        raise RuntimeError("PUBLIC_BASE_URL is not set")
    payload = {"url": settings.PUBLIC_BASE_URL.rstrip("/") + "/telegram/webhook"}
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(bot_api_url("setWebhook"), json=payload)
        response.raise_for_status()
        return response.json()


def extract_message(update: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    return update.get("message") or update.get("edited_message")


def get_chat_id(update: Dict[str, Any]) -> Optional[int]:
    message = extract_message(update)
    if not message:
        return None
    chat = message.get("chat") or {}
    return chat.get("id")


def get_text(update: Dict[str, Any]) -> str:
    message = extract_message(update)
    if not message:
        return ""
    return (message.get("text") or "").strip()

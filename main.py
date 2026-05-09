from __future__ import annotations

from typing import Any, Dict, Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from agents import create_episode_pack
from config import settings
from image_generator import generate_nano_image
from telegram_service import get_chat_id, get_text, send_message, send_photo, set_webhook


DEFAULT_TITLE = "Ты её потерял"
DEFAULT_STORY = """
Кристина выходит из подъезда. Её ждёт Артём. Она обнимает его как опору.
Это видит Дима из машины, ревнует, выходит и подходит к Артёму.
Между ними начинается конфликт и драка. Кристина пытается остановить их,
держится за живот. Мама видит происходящее и переживает. В разгар конфликта
приезжает Василий на дорогой машине и забирает Кристину.
""".strip()


app = FastAPI(title=settings.PROJECT_NAME)
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")


class EpisodeRequest(BaseModel):
    title: str = DEFAULT_TITLE
    story: str = DEFAULT_STORY


class ImageRequest(BaseModel):
    scene_id: str = "scene_01"
    title: str = DEFAULT_TITLE
    story: str = DEFAULT_STORY
    custom_prompt: Optional[str] = None


@app.get("/")
def home() -> Dict[str, Any]:
    return {
        "status": "ok",
        "project": settings.PROJECT_NAME,
        "message": "Golden Cage AI Studio is running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health() -> Dict[str, Any]:
    return {
        "status": "ok",
        "project": settings.PROJECT_NAME,
        "telegram_key_loaded": bool(settings.TELEGRAM_BOT_TOKEN),
        "gemini_key_loaded": bool(settings.GEMINI_API_KEY),
        "xai_key_loaded": bool(settings.XAI_API_KEY),
        "public_base_url_loaded": bool(settings.PUBLIC_BASE_URL),
        "nano_model": settings.NANO_MODEL,
        "grok_video_model": settings.GROK_VIDEO_MODEL,
    }


@app.post("/episode/create")
def create_episode(request: EpisodeRequest) -> Dict[str, Any]:
    return create_episode_pack(request.title, request.story)


@app.post("/image/generate")
async def image_generate(request: ImageRequest) -> Dict[str, Any]:
    pack = create_episode_pack(request.title, request.story)
    selected = None
    for scene in pack["scenes"]:
        if scene["id"] == request.scene_id:
            selected = scene
            break

    if request.custom_prompt:
        prompt = request.custom_prompt
        scene_id = request.scene_id or "custom"
    elif selected:
        prompt = selected["nano_prompt"]
        scene_id = selected["id"]
    else:
        return {"status": "error", "message": f"Scene not found: {request.scene_id}"}

    result = await generate_nano_image(prompt=prompt, scene_id=scene_id)
    return {"status": "ok", "image": result, "prompt": prompt}


@app.post("/telegram/set-webhook")
async def telegram_set_webhook() -> Dict[str, Any]:
    return await set_webhook()


@app.post("/telegram/webhook")
async def telegram_webhook(request: Request) -> Dict[str, Any]:
    update = await request.json()
    chat_id = get_chat_id(update)
    text = get_text(update)

    if not chat_id:
        return {"ok": True, "ignored": "no_chat"}

    try:
        if text.startswith("/start"):
            await send_message(
                chat_id,
                "🎬 <b>Golden Cage AI Studio</b> запущен.\n\n"
                "Команды:\n"
                "/episode — собрать пакет серии\n"
                "/scenes — список сцен\n"
                "/prompt scene_01 — получить промпт Nano Banana\n"
                "/grok scene_01 — получить промпт оживления\n"
                "/image scene_01 — сгенерировать кадр Nano Banana\n\n"
                "Начни с: /episode",
            )

        elif text.startswith("/episode"):
            pack = create_episode_pack(DEFAULT_TITLE, DEFAULT_STORY)
            msg = f"✅ <b>{pack['episode_title']}</b>\n\nСцен: {len(pack['scenes'])}\n\n"
            msg += "Готовы агенты:\n— Showrunner\n— Continuity Keeper\n— Nano Prompt Writer\n— Grok Prompt Writer\n— Post Agent\n\n"
            msg += "Напиши /scenes"
            await send_message(chat_id, msg)

        elif text.startswith("/scenes"):
            pack = create_episode_pack(DEFAULT_TITLE, DEFAULT_STORY)
            lines = ["🎞 <b>Список сцен</b>\n"]
            for scene in pack["scenes"]:
                lines.append(f"{scene['id']} — {scene['title']}")
            lines.append("\nПример: /prompt scene_01")
            await send_message(chat_id, "\n".join(lines))

        elif text.startswith("/prompt"):
            parts = text.split(maxsplit=1)
            scene_id = parts[1].strip() if len(parts) > 1 else "scene_01"
            pack = create_episode_pack(DEFAULT_TITLE, DEFAULT_STORY)
            scene = next((s for s in pack["scenes"] if s["id"] == scene_id), None)
            if not scene:
                await send_message(chat_id, f"Не нашла сцену: {scene_id}")
            else:
                await send_message(chat_id, f"🖼 <b>{scene['title']}</b>\n\n<code>{scene['nano_prompt']}</code>")

        elif text.startswith("/grok"):
            parts = text.split(maxsplit=1)
            scene_id = parts[1].strip() if len(parts) > 1 else "scene_01"
            pack = create_episode_pack(DEFAULT_TITLE, DEFAULT_STORY)
            scene = next((s for s in pack["scenes"] if s["id"] == scene_id), None)
            if not scene:
                await send_message(chat_id, f"Не нашла сцену: {scene_id}")
            else:
                await send_message(chat_id, f"🎥 <b>{scene['title']}</b>\n\n<code>{scene['grok_prompt']}</code>")

        elif text.startswith("/image"):
            parts = text.split(maxsplit=1)
            scene_id = parts[1].strip() if len(parts) > 1 else "scene_01"
            pack = create_episode_pack(DEFAULT_TITLE, DEFAULT_STORY)
            scene = next((s for s in pack["scenes"] if s["id"] == scene_id), None)
            if not scene:
                await send_message(chat_id, f"Не нашла сцену: {scene_id}")
            else:
                await send_message(chat_id, f"Генерирую кадр: {scene['title']}…")
                result = await generate_nano_image(scene["nano_prompt"], scene_id=scene_id)
                await send_photo(chat_id, result["local_path"], caption=f"✅ {scene['title']}\n{result['url']}")

        else:
            await send_message(
                chat_id,
                "Я поняла. Пока работаю командами:\n/episode\n/scenes\n/prompt scene_01\n/grok scene_01\n/image scene_01",
            )

    except Exception as exc:
        await send_message(chat_id, f"⚠️ Ошибка: {str(exc)[:1000]}")

    return {"ok": True}

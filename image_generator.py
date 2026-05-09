from __future__ import annotations

import asyncio
import uuid
from pathlib import Path
from typing import Any, Dict, List

from google import genai

from config import settings

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def public_url_for(filename: str) -> str:
    base = settings.PUBLIC_BASE_URL.rstrip("/")
    if not base:
        return f"/outputs/{filename}"
    return f"{base}/outputs/{filename}"


def _response_images(response: Any) -> List[Any]:
    parts: List[Any] = []
    if hasattr(response, "parts") and response.parts:
        parts = list(response.parts)
    elif getattr(response, "candidates", None):
        for candidate in response.candidates:
            content = getattr(candidate, "content", None)
            if content and getattr(content, "parts", None):
                parts.extend(content.parts)

    images = []
    for part in parts:
        if getattr(part, "inline_data", None) is not None:
            try:
                images.append(part.as_image())
            except Exception:
                pass
    return images


async def generate_nano_image(prompt: str, scene_id: str = "scene") -> Dict[str, Any]:
    if not settings.GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not set")

    client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def run() -> Dict[str, Any]:
        response = client.models.generate_content(
            model=settings.NANO_MODEL,
            contents=[prompt],
        )
        images = _response_images(response)
        if not images:
            raise RuntimeError("Gemini returned no image")

        filename = f"{scene_id}_{uuid.uuid4().hex[:8]}.png"
        path = OUTPUT_DIR / filename
        images[0].save(path)
        return {
            "filename": filename,
            "local_path": str(path),
            "url": public_url_for(filename),
            "model": settings.NANO_MODEL,
        }

    return await asyncio.to_thread(run)

from __future__ import annotations

import asyncio
from datetime import timedelta
from typing import Any, Dict, Optional

import xai_sdk

from config import settings


async def generate_grok_video(
    prompt: str,
    image_url: Optional[str] = None,
    duration: Optional[int] = None,
    aspect_ratio: Optional[str] = None,
    resolution: Optional[str] = None,
) -> Dict[str, Any]:
    if not settings.XAI_API_KEY:
        raise RuntimeError("XAI_API_KEY is not set")

    def run() -> Dict[str, Any]:
        client = xai_sdk.Client(api_key=settings.XAI_API_KEY)
        kwargs: Dict[str, Any] = {
            "prompt": prompt,
            "model": settings.GROK_VIDEO_MODEL,
            "duration": duration or settings.DEFAULT_VIDEO_DURATION,
            "aspect_ratio": aspect_ratio or settings.DEFAULT_ASPECT_RATIO,
            "resolution": resolution or settings.DEFAULT_VIDEO_RESOLUTION,
            "timeout": timedelta(seconds=settings.VIDEO_TIMEOUT_SEC),
            "interval": timedelta(seconds=settings.VIDEO_POLL_SEC),
        }
        if image_url:
            kwargs["image_url"] = image_url

        response = client.video.generate(**kwargs)
        return {
            "url": getattr(response, "url", None),
            "duration": getattr(response, "duration", None),
            "model": getattr(response, "model", settings.GROK_VIDEO_MODEL),
            "raw_type": type(response).__name__,
        }

    return await asyncio.to_thread(run)

# Golden Cage AI Studio

Telegram + FastAPI backend for an AI mini-studio that creates scene packs, Nano Banana prompts, Grok animation prompts, image generations, and first-pass video generations for the series «Золотая клетка».

## What is included

- Showrunner agent: breaks the episode into cinematic scenes and transitions.
- Continuity Keeper: keeps character/style rules consistent.
- Nano Prompt Writer: creates image prompts for Gemini / Nano Banana.
- Grok Prompt Writer: creates animation prompts for Grok Imagine.
- Post Agent: prepares caption, pinned comment, hashtags and cover options.
- Telegram bot commands.
- Render deployment config.

## Telegram commands

```text
/start
/episode
/scenes
/prompt scene_01
/grok scene_01
/image scene_01
/animate scene_01 PUBLIC_IMAGE_URL
```

## Render build settings

```text
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
```

## Environment variables

Add these in Render > your service > Environment:

```env
TELEGRAM_BOT_TOKEN=
ADMIN_CHAT_ID=
PUBLIC_BASE_URL=https://your-render-service.onrender.com
GEMINI_API_KEY=
NANO_MODEL=gemini-2.5-flash-image
XAI_API_KEY=
GROK_VIDEO_MODEL=grok-imagine-video
PROJECT_NAME=Golden Cage AI Studio
DEFAULT_ASPECT_RATIO=9:16
DEFAULT_VIDEO_DURATION=10
DEFAULT_VIDEO_RESOLUTION=720p
MAX_IMAGE_VARIANTS=2
MAX_REGENERATIONS=2
VIDEO_POLL_SEC=5
VIDEO_TIMEOUT_SEC=600
```

Do not put real secret values in GitHub. Add them only in Render Environment Variables.

## After deploy

Open:

```text
https://your-render-service.onrender.com/health
```

Then set the Telegram webhook:

```text
https://your-render-service.onrender.com/docs
```

Run POST `/telegram/set-webhook`.

Then open the Telegram bot and send:

```text
/start
```

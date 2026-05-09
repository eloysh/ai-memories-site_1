from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Golden Cage AI Studio"

    TELEGRAM_BOT_TOKEN: str = ""
    ADMIN_CHAT_ID: str = ""
    PUBLIC_BASE_URL: str = ""

    GEMINI_API_KEY: str = ""
    NANO_MODEL: str = "gemini-2.5-flash-image"

    XAI_API_KEY: str = ""
    GROK_VIDEO_MODEL: str = "grok-imagine-video"

    DEFAULT_ASPECT_RATIO: str = "9:16"
    DEFAULT_VIDEO_DURATION: int = 10
    DEFAULT_VIDEO_RESOLUTION: str = "720p"

    MAX_IMAGE_VARIANTS: int = 2
    MAX_REGENERATIONS: int = 2
    HTTP_TIMEOUT_SEC: int = 180
    VIDEO_POLL_SEC: int = 5
    VIDEO_TIMEOUT_SEC: int = 120

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()

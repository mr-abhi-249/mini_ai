"""Configuration helpers loaded from environment variables."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    openai_api_key: str | None
    voice_language: str
    tts_enabled: bool

    @classmethod
    def from_env(cls) -> "Settings":
        tts_flag = os.getenv("MINI_TTS_ENABLED", "1").strip().lower()
        return cls(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            voice_language=os.getenv("MINI_VOICE_LANGUAGE", "en-IN"),
            tts_enabled=tts_flag not in {"0", "false", "no"},
        )

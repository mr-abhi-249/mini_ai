"""Text-to-speech output module."""

try:
    import pyttsx3
except Exception:  # pragma: no cover - optional runtime dependency
    pyttsx3 = None


class Speaker:
    def __init__(self, enabled: bool = True) -> None:
        self.enabled = enabled
        self._engine = None
        if enabled and pyttsx3 is not None:
            try:
                self._engine = pyttsx3.init()
            except Exception:
                self._engine = None

    def say(self, text: str) -> None:
        print("Mini:", text)
        if self._engine is not None:
            self._engine.say(text)
            self._engine.runAndWait()

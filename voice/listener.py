"""Voice input module."""

try:
    import speech_recognition as sr
except Exception:  # pragma: no cover - optional runtime dependency
    sr = None


class VoiceListener:
    def __init__(self, language: str = "en-IN") -> None:
        self.language = language
        self.recognizer = sr.Recognizer() if sr is not None else None
        self.available = self.recognizer is not None

    def _select_microphone_index(self):
        if sr is None:
            return None
        try:
            working_microphones = sr.Microphone.list_working_microphones()
        except Exception as exc:
            print(f"Microphone discovery failed: {exc}")
            return None

        if not working_microphones:
            print("No working microphones reported; using the default input device.")
            return None

        if isinstance(working_microphones, dict):
            microphone_index = next(iter(working_microphones.keys()))
        elif isinstance(working_microphones, (list, tuple, set)):
            microphone_index = next(iter(working_microphones))
        else:
            microphone_index = working_microphones

        print(f"Using microphone {microphone_index}")
        return microphone_index

    def listen_command(self) -> str:
        if sr is None or self.recognizer is None:
            return ""

        microphone_index = self._select_microphone_index()
        try:
            microphone_kwargs = {"device_index": microphone_index} if microphone_index is not None else {}
            with sr.Microphone(**microphone_kwargs) as source:
                print("Listening...")
                self.recognizer.dynamic_energy_threshold = True
                self.recognizer.pause_threshold = 0.8
                self.recognizer.non_speaking_duration = 0.5
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)
        except Exception as exc:
            print(f"Voice input unavailable: {exc}")
            return ""

        for language in (self.language, "en-US", None):
            try:
                if language is None:
                    command = self.recognizer.recognize_google(audio)  # type: ignore[attr-defined]
                else:
                    command = self.recognizer.recognize_google(audio, language=language)  # type: ignore[attr-defined]
                print("You said:", command)
                return command.lower()
            except Exception:
                continue
        return ""

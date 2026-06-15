"""Built-in system command handlers."""

import os
import webbrowser
from dataclasses import dataclass

try:
    import psutil
except Exception:  # pragma: no cover - optional runtime dependency
    psutil = None


@dataclass
class CommandResult:
    handled: bool
    action: str | None = None


class SystemCommandHandler:
    def handle(self, cmd: str, speak) -> CommandResult:
        normalized_cmd = " ".join(cmd.split()).strip().lower()
        if not normalized_cmd:
            return CommandResult(False)

        if any(phrase in normalized_cmd for phrase in ("hey mini", "hello mini", "hi mini")):
            speak("Owner verified. Yes Boss, how can I help you?")
            return CommandResult(True)
        if "what remains in" in normalized_cmd and "mini project" in normalized_cmd:
            speak(
                "Okay Sir. Remaining roadmap: GUI integration, full command modules, "
                "Gemini and Ollama routing, memory and RAG pipelines, and the multi-agent system."
            )
            return CommandResult(True)

        if "open youtube" in normalized_cmd:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            return CommandResult(True)
        if "open google" in normalized_cmd:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            return CommandResult(True)
        if "open chrome" in normalized_cmd:
            speak("Opening Chrome")
            if os.name == "nt":
                os.system("start chrome")
            else:
                webbrowser.open("https://www.google.com")
            return CommandResult(True)
        if "cpu" in normalized_cmd:
            if psutil is None:
                speak("CPU monitoring is not available.")
            else:
                speak(f"CPU usage is {psutil.cpu_percent(interval=1)} percent")
            return CommandResult(True)
        if "ram" in normalized_cmd or "memory" in normalized_cmd:
            if psutil is None:
                speak("Memory monitoring is not available.")
            else:
                mem = psutil.virtual_memory()
                speak(f"RAM usage is {int(mem.percent)} percent")
            return CommandResult(True)
        if "battery" in normalized_cmd:
            if psutil is None:
                speak("Battery monitoring is not available.")
            else:
                battery = psutil.sensors_battery()
                speak("I cannot read battery information on this device." if battery is None else f"Battery is at {battery.percent} percent")
            return CommandResult(True)
        if any(word in normalized_cmd for word in ("exit", "quit", "bye")):
            speak("Goodbye Abhi")
            return CommandResult(True, action="exit")
        if "switch mode" in normalized_cmd:
            return CommandResult(True, action="switch_mode")
        return CommandResult(False)

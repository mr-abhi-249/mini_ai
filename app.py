"""Top-level entry point for Mini AI assistant."""

from commands.ai_chat import AIChatCommand
from commands.system import SystemCommandHandler
from utils.config import Settings
from utils.constants import HELP_TEXT, TITLE
from voice.listener import VoiceListener
from voice.speaker import Speaker


class AssistantApp:
    def __init__(self) -> None:
        self.settings = Settings.from_env()
        self.speaker = Speaker(enabled=self.settings.tts_enabled)
        self.listener = VoiceListener(language=self.settings.voice_language)
        self.system_handler = SystemCommandHandler()
        self.ai_chat = AIChatCommand(api_key=self.settings.openai_api_key)

    def respond(self, text: str) -> None:
        clean_text = " ".join(str(text).split()).strip() if text else ""
        self.speaker.say(clean_text or "Sorry, I could not process that.")

    def show_menu(self) -> bool:
        print("\n" + "=" * 50)
        print(TITLE)
        print("=" * 50)
        print("\nChoose mode:")
        print("  1. Voice Mode (speak commands)")
        print("  2. Text Mode (type commands)")
        choice = self._read_input("\nEnter choice (1 or 2): ")
        if choice is None:
            print("\nNo input detected. Starting in text mode.")
            return False
        return choice.strip() == "1"

    @staticmethod
    def _read_input(prompt: str) -> str | None:
        try:
            return input(prompt)
        except EOFError:
            return None

    def handle_command(self, cmd: str):
        result = self.system_handler.handle(cmd, self.respond)
        if result.action == "exit":
            raise SystemExit
        if result.action == "switch_mode":
            return "switch_mode"
        if result.handled:
            return None

        if cmd:
            ai_response = self.ai_chat.analyze(cmd)
            if ai_response:
                self.respond(ai_response)
            else:
                self.respond("Sorry, I don't know that command yet.")
        return None

    def voice_mode(self) -> bool:
        if not self.listener.available:
            self.respond("Voice mode is not available. Switching to text mode.")
            return False

        self.respond("Mini online in voice mode. Press Enter, then speak your command.")
        if self.ai_chat.enabled:
            self.respond("AI mode enabled.")

        print("\nTip: Say 'switch mode' to change to text mode")
        print("     Say 'exit' to quit\n")

        while True:
            if self._read_input("Press Enter to talk to Mini...") is None:
                raise SystemExit
            command = self.listener.listen_command()
            if command:
                result = self.handle_command(command)
                if result == "switch_mode":
                    self.respond("Switching to text mode")
                    return False

    def text_mode(self) -> bool:
        print("\n" + "=" * 50)
        print("MINI AI ASSISTANT - TEXT MODE")
        print("=" * 50)
        print("\nType 'help' for commands")
        print("Type 'switch mode' to use voice")
        print("Type 'exit' to quit\n")

        while True:
            raw_command = self._read_input("You: ")
            if raw_command is None:
                raise SystemExit
            command = raw_command.strip().lower()
            if command == "help":
                self.respond(HELP_TEXT)
                continue
            if command:
                result = self.handle_command(command)
                if result == "switch_mode":
                    self.respond("Switching to voice mode")
                    return True

    def run(self) -> None:
        try:
            use_voice = self.show_menu()
            while True:
                use_voice = self.voice_mode() if use_voice else self.text_mode()
        except (KeyboardInterrupt, SystemExit):
            self.respond("Mini offline. Goodbye!")


def main() -> None:
    AssistantApp().run()


if __name__ == "__main__":
    main()

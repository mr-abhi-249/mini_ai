"""AI fallback command integration."""

from ai_module import analyze_input, init_ai


class AIChatCommand:
    def __init__(self, api_key: str | None = None) -> None:
        self.enabled = init_ai(api_key=api_key)

    def analyze(self, user_input: str) -> str | None:
        if not self.enabled:
            return None
        return analyze_input(user_input)

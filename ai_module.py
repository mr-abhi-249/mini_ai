import os

try:
    from openai import OpenAI
except Exception:  # pragma: no cover - optional runtime dependency
    OpenAI = None

client = None


def init_ai(api_key=None):
    """Initialize OpenAI client with API key"""
    global client

    if OpenAI is None:
        print("OpenAI package not installed; AI mode disabled")
        return False

    if api_key is None:
        api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("OPENAI_API_KEY not set; AI fallback disabled")
        return False

    try:
        client = OpenAI(api_key=api_key)
        print("✓ OpenAI AI initialized successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to initialize OpenAI: {e}")
        return False


def analyze_input(user_input, context=None):
    """Analyze user input and get AI response."""
    global client

    if client is None:
        print("AI not initialized. Call init_ai() first")
        return None

    try:
        system_prompt = """You are Mini, a helpful voice assistant.
- Answer questions concisely and accurately
- Suggest commands you can execute (like opening websites, checking system info)
- Keep responses brief (1-2 sentences) for voice output
- Be friendly and helpful"""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ]

        if context:
            messages.insert(1, {"role": "assistant", "content": context})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"AI Error: {e}")
        return None


def is_initialized():
    """Check if AI is initialized"""
    return client is not None

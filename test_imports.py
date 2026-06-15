"""Core import smoke test script."""

modules = [
    "app",
    "commands.system",
    "commands.ai_chat",
    "voice.listener",
    "voice.speaker",
    "utils.config",
]

for module_name in modules:
    __import__(module_name)

print("Core modules imported successfully!")

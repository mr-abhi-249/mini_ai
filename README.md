# Mini AI Assistant

Mini AI is a lightweight voice/text assistant with modular folders for voice, commands, AI, memory, automation, dashboard, RAG, and security.

## Run

```bash
python app.py
```

You can still run the legacy entry point:

```bash
python main.py
```

## Core commands

- `open youtube`
- `open google`
- `open chrome`
- `cpu`
- `ram` / `memory`
- `battery`
- `switch mode`
- `exit`

## AI configuration

AI fallback is optional and uses environment variables:

```bash
export OPENAI_API_KEY="your-key"
```

Without `OPENAI_API_KEY`, the assistant runs with built-in commands only.

## Project structure

The repository now includes the planned architecture folders and placeholder modules for future expansion:

- `voice/`, `commands/`, `automation/`, `dashboard/`, `memory/`, `ai/`, `rag/`, `security/`, `utils/`
- `data/`, `screenshots/`, `uploads/`, `docs/`, `tests/`

## Smoke checks

```bash
python test_imports.py
python -m unittest discover -s tests -q
```

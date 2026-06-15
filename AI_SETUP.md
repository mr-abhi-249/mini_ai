# AI Setup Guide for Mini Assistant

## 🤖 AI Features Added

Your Mini assistant now has **ChatGPT AI integration** to analyze any user input and provide intelligent responses!

### Features:
- ✓ Understands natural language questions
- ✓ Provides intelligent answers using ChatGPT
- ✓ Falls back to built-in commands (open youtube, check cpu, etc.)
- ✓ Voice input + AI response

---

## 🔧 Setup Steps

### 1. **Get OpenAI API Key**
   - Go to: https://platform.openai.com/api-keys
   - Sign up or login with your account
   - Click "Create new secret key"
   - Copy the key (starts with `sk-`)

### 2. **Set API Key as Environment Variable**

#### On Windows (Command Prompt):
```bash
setx OPENAI_API_KEY "your-api-key-here"
```
Then restart Command Prompt.

#### On Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY = "your-api-key-here"
```

#### Or create `.env` file:
In `d:\Mini-Ai\`, create `.env` file with:
```
OPENAI_API_KEY=your-api-key-here
```

### 3. **Test AI**
```bash
cd d:\Mini-Ai
python main.py
```

When started, Mini will say:
- "Mini online"
- "AI mode enabled" ✓

---

## 💬 Try These AI Queries

Press Enter and say:
- **"What is the weather?"** → AI answers
- **"How do I cook pasta?"** → AI explains
- **"What is artificial intelligence?"** → AI explains
- **"Tell me a joke"** → AI tells a joke
- **"What time is it?"** → AI answers
- **"Open YouTube"** → System command (built-in)
- **"Check CPU"** → System command (built-in)

---

## 💰 Cost

- ChatGPT API is **pay-as-you-go**
- Current pricing: ~$0.0005 per 1000 tokens (~4 words)
- Average query: ~$0.0001 - $0.001
- **Set spending limits** in your OpenAI account

---

## ⚠️ Without API Key

AI features disabled, but the assistant still works:
- ✓ Open websites
- ✓ Check CPU/RAM/Battery
- ✓ Execute built-in commands
- ✗ No intelligent question answering

---

## 📁 Files Created

- `ai_module.py` - AI integration module
- `main.py` - Enhanced with AI support

---

## 🚀 Run AI Assistant

```bash
cd d:\Mini-Ai
python main.py
```

Enjoy! 🎤🤖

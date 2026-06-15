# Add Mini to Windows PATH - Setup Instructions

## Option 1: Add to PATH (Run Once - Works Forever)

### For Windows 10/11:

1. **Open Environment Variables:**
   - Press `Windows + X`
   - Click "System"
   - Click "Advanced system settings"
   - Click "Environment Variables" button
   - Under "User variables", click "New"

2. **Add Mini Path:**
   - Variable name: `PATH` (or edit existing PATH)
   - Variable value: `D:\Mini-Ai`
   - Click OK

3. **Restart Command Prompt**
   - Close and reopen Command Prompt
   - Type: `mini`
   - Press Enter ✓

---

## Option 2: Quick Add to PATH (Command Prompt - Admin)

```bash
setx PATH "%PATH%;D:\Mini-Ai"
```

Then restart Command Prompt and type: `mini`

---

## Option 3: PowerShell (Admin)

```powershell
$env:Path += ";D:\Mini-Ai"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [EnvironmentVariableTarget]::User)
```

---

## Test It:

After setup, open a **new Command Prompt** and type:
```bash
mini
```

Mini will activate and start! 🤖

---

## Quick Launch Methods:

### From Any Folder:
```bash
mini
```

### From D:\Mini-Ai:
```bash
mini.bat
```

### From Python:
```bash
python app.py
```

---

Done! Now you can launch Mini from anywhere by just typing `mini` ✓

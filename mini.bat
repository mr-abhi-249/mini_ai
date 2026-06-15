@echo off
REM Mini AI Assistant Launcher
REM This batch file activates the virtual environment and runs the assistant

cd /d D:\Mini-Ai
call venv\Scripts\activate.bat
python main.py
pause

import pyttsx3
import os
import webbrowser
import psutil

engine = pyttsx3.init()

def speak(text: str):
    print("Mini:", text)
    engine.say(text)
    engine.runAndWait()

def handle_command(cmd: str):
    cmd = cmd.lower()

    if "open youtube" in cmd:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in cmd:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open chrome" in cmd:
        speak("Opening Chrome")
        os.system("start chrome")
    elif "cpu" in cmd:
        cpu = psutil.cpu_percent(interval=1)
        speak(f"CPU usage is {cpu} percent")
    elif "ram" in cmd or "memory" in cmd:
        mem = psutil.virtual_memory()
        speak(f"RAM usage is {int(mem.percent)} percent")
    elif "battery" in cmd:
        battery = psutil.sensors_battery()
        if battery is None:
            speak("I cannot read battery information on this device.")
        else:
            speak(f"Battery is at {battery.percent} percent")
    elif "exit" in cmd or "quit" in cmd or "bye" in cmd:
        speak("Goodbye Abhi")
        raise SystemExit
    else:
        speak("Sorry, I don't know that command yet.")

if __name__ == "__main__":
    speak("Mini online. Type your command.")
    while True:
        user = input("You: ")
        if not user.strip():
            continue
        handle_command(user)
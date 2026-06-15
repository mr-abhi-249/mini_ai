import pyttsx3
import os
import webbrowser
import psutil
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()
DEFAULT_RECOGNITION_LANGUAGE = os.environ.get("MINI_VOICE_LANGUAGE", "en-IN")

def speak(text: str):
    print("Mini:", text)
    engine.say(text)
    engine.runAndWait()

def _select_microphone_index():
    """Return a working microphone index when one is available."""
    try:
        working_microphones = sr.Microphone.list_working_microphones()
    except Exception as exc:
        print(f"Microphone discovery failed: {exc}")
        return None

    if not working_microphones:
        print("No working microphones reported; using the default input device.")
        return None

    if isinstance(working_microphones, dict):
        microphone_index, microphone_label = next(iter(working_microphones.items()))
    elif isinstance(working_microphones, (list, tuple, set)):
        microphone_index = next(iter(working_microphones))
        microphone_label = None
    else:
        microphone_index = working_microphones
        microphone_label = None

    try:
        microphone_names = sr.Microphone.list_microphone_names()
    except Exception:
        microphone_names = []

    if isinstance(microphone_index, int) and 0 <= microphone_index < len(microphone_names):
        print(f"Using microphone {microphone_index}: {microphone_names[microphone_index]}")
    elif microphone_label:
        print(f"Using microphone {microphone_index}: {microphone_label}")
    else:
        print(f"Using microphone {microphone_index}")

    return microphone_index

def listen_command():
    microphone_index = _select_microphone_index()

    try:
        microphone_kwargs = {}
        if microphone_index is not None:
            microphone_kwargs["device_index"] = microphone_index

        with sr.Microphone(**microphone_kwargs) as source:
            print("Listening...")
            r.dynamic_energy_threshold = True
            r.pause_threshold = 0.8
            r.non_speaking_duration = 0.5
            r.adjust_for_ambient_noise(source, duration=0.5)

            try:
                audio = r.listen(source, timeout=8, phrase_time_limit=8)
            except sr.WaitTimeoutError:
                speak("No speech detected.")
                return ""
    except OSError as exc:
        speak(f"Microphone access failed: {exc}")
        return ""

    try:
        print("Recognizing...")
        for language in (DEFAULT_RECOGNITION_LANGUAGE, "en-US", None):
            try:
                if language is None:
                    command = r.recognize_google(audio)  # type: ignore[attr-defined]
                else:
                    command = r.recognize_google(audio, language=language)  # type: ignore[attr-defined]

                print("You said:", command)
                return command.lower()
            except sr.UnknownValueError:
                continue

        speak("Sorry, I could not understand.")
        return ""
    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        speak("Speech service is not available.")
        return ""
def handle_command(cmd: str):
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
    elif cmd:
        speak("Sorry, I don't know that command yet.")

if __name__ == "__main__":
    speak("Mini online. Press Enter, then speak your command.")
    while True:
        input("Press Enter to talk to Mini...")
        command = listen_command()
        if command:
            handle_command(command)
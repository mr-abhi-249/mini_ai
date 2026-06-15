import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
DEFAULT_RECOGNITION_LANGUAGE = "en-IN"
r.energy_threshold = 500
r.pause_threshold = 0.8


def _select_microphone_index():
    try:
        working_microphones = sr.Microphone.list_working_microphones()
    except Exception as exc:
        print(f"  Could not enumerate microphones: {exc}")
        return None

    if not working_microphones:
        print("  No working microphones reported; using the default input device.")
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
        print(f"  Using microphone {microphone_index}: {microphone_names[microphone_index]}")
    elif microphone_label:
        print(f"  Using microphone {microphone_index}: {microphone_label}")
    else:
        print(f"  Using microphone {microphone_index}")

    return microphone_index

print("Starting speech recognition test...")
print("Available microphones:")
try:
    for index, name in enumerate(sr.Microphone.list_working_microphones()):
        print(f"  {index}: {name}")
except Exception as e:
    print(f"  Could not enumerate microphones: {e}")

microphone_index = _select_microphone_index()

try:
    microphone_kwargs = {}
    if microphone_index is not None:
        microphone_kwargs["device_index"] = microphone_index

    with sr.Microphone(**microphone_kwargs) as source:
        print("\nCalibrating noise...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Speak within 8 seconds...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            print("No speech detected.")
            speak("No speech detected.")
            raise SystemExit
except OSError as exc:
    print(f"Microphone access failed: {exc}")
    speak(f"Microphone access failed: {exc}")
    raise SystemExit

try:
    print("Recognizing...")
    text = ""
    for language in (DEFAULT_RECOGNITION_LANGUAGE, "en-US", None):
        try:
            if language is None:
                text = r.recognize_google(audio)  # type: ignore[attr-defined]
            else:
                text = r.recognize_google(audio, language=language)  # type: ignore[attr-defined]
            break
        except sr.UnknownValueError:
            continue
    if not text:
        raise sr.UnknownValueError()
    print("You said:", text)
    speak("You said " + text)
except sr.UnknownValueError:
    print("Sorry, I could not understand.")
    speak("Sorry, I could not understand.")
except sr.RequestError as e:
    print("API error:", e)
    speak("There was an error with speech recognition.")
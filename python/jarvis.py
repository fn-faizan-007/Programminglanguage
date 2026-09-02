
import speech_recognition as sr
import webbrowser
import pyttsx3
import wikipedia
import urllib.parse

# ==========================
# TEXT TO SPEECH
# ==========================

engine = pyttsx3.init()
engine.setProperty("rate", 180)


def speak(text):
    print("\nJarvis:", text)
    engine.say(text)
    engine.runAndWait()


# ==========================
# SPEECH RECOGNITION
# ==========================

recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.8
recognizer.energy_threshold = 300


def listen():
    try:
        with sr.Microphone() as source:

            print("\nListening...")

            # Microphone noise adjustment
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower().strip()

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return ""

    except sr.UnknownValueError:
        print("Could not understand your voice.")
        return ""

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return ""

    except Exception as e:
        print("Microphone Error:", e)
        return ""


# ==========================
# WIKIPEDIA SEARCH
# ==========================

def search_wikipedia(query):

    try:
        print("\nSearching Wikipedia...")

        result = wikipedia.summary(query, sentences=3)

        print("\n========== ANSWER ==========")
        print(result)
        print("============================\n")

        speak(result)

    except wikipedia.exceptions.DisambiguationError:

        answer = "Multiple results found. Please be more specific."

        print(answer)
        speak(answer)

    except wikipedia.exceptions.PageError:

        answer = "Sorry, I could not find information on that topic."

        print(answer)
        speak(answer)

    except Exception as e:

        print("Wikipedia Error:", e)
        speak("Sorry sir, something went wrong.")


# ==========================
# OPEN WEBSITE
# ==========================

def open_website(command):

    if "google" in command:

        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        return True

    elif "youtube" in command:

        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return True

    elif "facebook" in command:

        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
        return True

    elif "linkedin" in command:

        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
        return True

    elif "github" in command:

        speak("Opening GitHub")
        webbrowser.open("https://github.com")
        return True

    elif "gmail" in command:

        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
        return True

    elif "whatsapp" in command:

        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
        return True

    return False


# ==========================
# WHATSAPP MESSAGE
# ==========================

def whatsapp_message(command):

    if "whatsapp" not in command:
        return False

    if "message" not in command:
        return False

    # Example:
    # "message whatsapp hello brother"

    message = command.split("message", 1)[1]

    message = message.replace("whatsapp", "", 1).strip()

    if not message:
        speak("What message should I send?")
        return True

    encoded_message = urllib.parse.quote(message)

    url = f"https://web.whatsapp.com/send?text={encoded_message}"

    speak("Opening WhatsApp with your message")

    webbrowser.open(url)

    return True


# ==========================
# PROCESS COMMAND
# ==========================

def process_command(command):

    if not command:
        return

    # Exit
    if "exit" in command or "shutdown" in command or "quit" in command:

        speak("Goodbye Sir")
        return "exit"

    # WhatsApp message
    if whatsapp_message(command):

        return

    # Open websites
    if open_website(command):

        return

    # Wikipedia
    search_wikipedia(command)


# ==========================
# MAIN PROGRAM
# ==========================

speak("Initializing Jarvis")

while True:

    text = listen()

    if not text:
        continue

    # --------------------------------
    # CASE 1:
    # "Jarvis open YouTube"
    # --------------------------------

    if "jarvis" in text:

        command = text.replace("jarvis", "", 1).strip()

        # If command is already present
        if command:

            result = process_command(command)

            if result == "exit":
                break

        # --------------------------------
        # CASE 2:
        # "Jarvis"
        # Then wait for next command
        # --------------------------------

        else:

            speak("Yes Sir")

            command = listen()

            if command:

                result = process_command(command)

                if result == "exit":
                    break

import subprocess
import webbrowser
import urllib.parse
import pyttsx3
import time
import re


# ============================================================
# JARVIS - WINDOWS SPEECH VERSION
# No speech_recognition
# No PyAudio
# ============================================================


# ============================================================
# TEXT TO SPEECH
# ============================================================

engine = pyttsx3.init()

engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)


def speak(text):
    print(f"\nJarvis: {text}")

    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS Error:", e)


# ============================================================
# WINDOWS SPEECH RECOGNITION
# ============================================================

def listen():

    powershell_script = r'''
Add-Type -AssemblyName System.Speech

try {

    $recognizer = New-Object System.Speech.Recognition.SpeechRecognitionEngine

    # Use default Windows microphone
    $recognizer.SetInputToDefaultAudioDevice()

    # Create dictation grammar
    $grammar = New-Object System.Speech.Recognition.DictationGrammar
    $grammar.Name = "Dictation"
    $recognizer.LoadGrammar($grammar)

    # Improve recognition settings
    $recognizer.InitialSilenceTimeout = [TimeSpan]::FromSeconds(5)
    $recognizer.BabbleTimeout = [TimeSpan]::FromSeconds(3)
    $recognizer.EndSilenceTimeout = [TimeSpan]::FromSeconds(1)

    Write-Host "LISTENING"

    $result = $recognizer.Recognize()

    if ($result -ne $null) {
        Write-Output $result.Text
    }

    $recognizer.Dispose()

}
catch {
    Write-Error $_.Exception.Message
}
'''

    try:

        print("\nListening...")

        result = subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-Command",
                powershell_script
            ],
            capture_output=True,
            text=True,
            timeout=15
        )

        command = result.stdout.strip()

        # Remove PowerShell extra output if present
        lines = command.splitlines()

        clean_lines = []

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if line.upper() == "LISTENING":
                continue

            clean_lines.append(line)

        command = " ".join(clean_lines)

        if command:

            print(f"You: {command}")

            return command.lower().strip()

        if result.stderr.strip():
            print("Speech Error:", result.stderr.strip())

        print("Nothing heard.")

        return ""

    except subprocess.TimeoutExpired:

        print("Listening timed out.")

        return ""

    except Exception as e:

        print("Speech Error:", e)

        return ""


# ============================================================
# NORMALIZE COMMAND
# ============================================================

def normalize_command(command):

    command = command.lower().strip()

    # Remove punctuation
    command = re.sub(r"[^\w\s]", " ", command)

    # Remove extra spaces
    command = " ".join(command.split())

    return command


# ============================================================
# WEBSITE LIST
# ============================================================

WEBSITES = {

    "youtube": "https://www.youtube.com",

    "instagram": "https://www.instagram.com",

    "insta": "https://www.instagram.com",

    "google": "https://www.google.com",

    "facebook": "https://www.facebook.com",

    "linkedin": "https://www.linkedin.com",

    "github": "https://github.com",

    "gmail": "https://mail.google.com",

    "whatsapp": "https://web.whatsapp.com",

    "chatgpt": "https://chatgpt.com",

    "twitter": "https://x.com",

    "x": "https://x.com"
}


# ============================================================
# OPEN WEBSITE
# ============================================================

def open_website(command):

    command = normalize_command(command)

    # Remove common words
    remove_words = [
        "please",
        "open",
        "launch",
        "start",
        "website",
        "the"
    ]

    cleaned = command

    for word in remove_words:

        cleaned = re.sub(
            rf"\b{re.escape(word)}\b",
            " ",
            cleaned
        )

    cleaned = " ".join(cleaned.split())

    # Exact website match
    if cleaned in WEBSITES:

        url = WEBSITES[cleaned]

        speak(f"Opening {cleaned}")

        webbrowser.open(url)

        return True

    # Website appears inside command
    for name, url in WEBSITES.items():

        if re.search(rf"\b{re.escape(name)}\b", cleaned):

            speak(f"Opening {name}")

            webbrowser.open(url)

            return True

    return False


# ============================================================
# GOOGLE SEARCH
# ============================================================

def google_search(command):

    command = normalize_command(command)

    search_words = [
        "search for",
        "search",
        "google",
        "find"
    ]

    query = command

    for word in search_words:

        if query.startswith(word):

            query = query[len(word):].strip()

            break

    if not query:

        speak("What should I search for?")

        return True

    encoded_query = urllib.parse.quote_plus(query)

    url = f"https://www.google.com/search?q={encoded_query}"

    speak(f"Searching Google for {query}")

    webbrowser.open(url)

    return True


# ============================================================
# YOUTUBE SEARCH
# ============================================================

def youtube_search(command):

    command = normalize_command(command)

    patterns = [

        "search youtube for",
        "search youtube",
        "youtube search",
        "search on youtube",
        "find on youtube"

    ]

    query = ""

    for pattern in patterns:

        if pattern in command:

            query = command.split(
                pattern,
                1
            )[1].strip()

            break

    if not query:

        return False

    encoded_query = urllib.parse.quote_plus(query)

    url = (
        "https://www.youtube.com/results?search_query="
        + encoded_query
    )

    speak(
        f"Searching YouTube for {query}"
    )

    webbrowser.open(url)

    return True


# ============================================================
# OPEN YOUTUBE DIRECTLY
# ============================================================

def open_youtube(command):

    command = normalize_command(command)

    youtube_commands = [

        "youtube",

        "open youtube",

        "launch youtube",

        "start youtube",

        "youtube open",

        "youtube please",

        "open the youtube",

        "launch the youtube"

    ]

    if command in youtube_commands:

        speak("Opening YouTube")

        webbrowser.open(
            "https://www.youtube.com"
        )

        return True

    return False


# ============================================================
# OPEN COMMON WEBSITES DIRECTLY
# ============================================================

def direct_website_command(command):

    command = normalize_command(command)

    for name, url in WEBSITES.items():

        commands = [

            name,

            f"open {name}",

            f"launch {name}",

            f"start {name}",

            f"{name} open",

            f"open the {name}",

            f"launch the {name}"

        ]

        if command in commands:

            speak(f"Opening {name}")

            webbrowser.open(url)

            return True

    return False


# ============================================================
# EXIT COMMAND
# ============================================================

def is_exit_command(command):

    command = normalize_command(command)

    exit_words = [

        "exit",

        "quit",

        "shutdown jarvis",

        "close jarvis",

        "stop jarvis",

        "goodbye",

        "bye jarvis",

        "bye"

    ]

    for word in exit_words:

        if command == word or word in command:

            return True

    return False


# ============================================================
# COMMAND PROCESSOR
# ============================================================

def process_command(command):

    if not command:

        return "continue"

    command = normalize_command(command)

    print(f"\nProcessing: {command}")


    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if is_exit_command(command):

        speak("Goodbye Sir")

        return "exit"


    # --------------------------------------------------------
    # YOUTUBE SEARCH
    # --------------------------------------------------------

    if youtube_search(command):

        return "continue"


    # --------------------------------------------------------
    # DIRECT YOUTUBE
    # --------------------------------------------------------

    if open_youtube(command):

        return "continue"


    # --------------------------------------------------------
    # OPEN WEBSITE
    # --------------------------------------------------------

    if direct_website_command(command):

        return "continue"


    # --------------------------------------------------------
    # Generic OPEN
    # --------------------------------------------------------

    if (
        command.startswith("open ")
        or command.startswith("launch ")
        or command.startswith("start ")
    ):

        if open_website(command):

            return "continue"


    # --------------------------------------------------------
    # GOOGLE SEARCH
    # --------------------------------------------------------

    if (
        command.startswith("search ")
        or command.startswith("search for ")
        or command.startswith("google ")
        or command.startswith("find ")
    ):

        if google_search(command):

            return "continue"


    # --------------------------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------------------------

    speak(
        "I did not understand that command. "
        "Please try again."
    )

    return "continue"


# ============================================================
# WAKE WORD
# ============================================================

def handle_wake_word(command):

    command = normalize_command(command)

    # Jarvis is present
    if "jarvis" in command:

        command = command.replace(
            "jarvis",
            "",
            1
        ).strip()

        # User only said Jarvis
        if not command:

            speak(
                "Yes Sir. "
                "How can I help you?"
            )

            return listen()

        return command

    return command


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    speak("Initializing Jarvis")

    time.sleep(1)

    speak(
        "Jarvis is ready. "
        "You can give me a command."
    )

    while True:

        command = listen()

        if not command:

            continue


        # ----------------------------------------------------
        # Handle wake word
        # ----------------------------------------------------

        command = handle_wake_word(command)

        if not command:

            continue


        # ----------------------------------------------------
        # Process command
        # ----------------------------------------------------

        result = process_command(command)

        if result == "exit":

            break


# ============================================================
# START JARVIS
# ============================================================

if __name__ == "__main__":

    main()

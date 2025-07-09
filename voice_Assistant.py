

import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, service is down.")
        return ""

def main():
    speak("Hello! How can I help you?")
    while True:
        command = get_audio()

        if "your name" in command:
            speak("I am your voice assistant.")
        elif "how are you" in command:
            speak("I am fine. Thank you.")
        elif "bye" in command:
            speak("Goodbye!")
            break
        else:
            speak("I don't understand that.")

main()

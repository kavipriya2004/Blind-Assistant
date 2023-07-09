from PyPDF2 import PdfReader
from gtts import gTTS
import speech_recognition as sr
import pyttsx3

# Initialize TTS engine
tts_engine = pyttsx3.init()

# Set TTS voice properties
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)
tts_engine.setProperty('rate', 175)

# Define a function to speak the given text
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Initialize STT recognizer
stt_recognizer = sr.Recognizer()

# Define a function to listen for user input and return the recognized text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = stt_recognizer.listen(source)
    try:
        text = stt_recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Main program loop
while True:
    # Listen for user input
    input_text = listen()
    if input_text:
        # Process user input
        if "hello" in input_text.lower():
            speak("Hello! How can I assist you today?")
        elif "what's the time" in input_text.lower():
            speak("The time is currently 9:35 PM.")
        elif "read" in input_text.lower():
            

            # creating a pdf reader object
            reader = PdfReader("G:\\OVER ALL PROPER CODES\\sample,py.pdf")

            # printing number of pages in pdf file
            print(len(reader.pages))

            # getting a specific page from the pdf file
            page = reader.pages[0]

            # extracting text from page
            text = page.extract_text()
            print(text)



            

            # This module is imported so that we can
            # play the converted audio
            import os

            # The text that you want to convert to audio
            #mytext = 'Hi I am your voice assistant'

            # Language in which you want to convert
            language = 'en'

            # Passing the text and language to the engine,
            # here we have marked slow=False. Which tells
            # the module that the converted audio should
            # have a high speed
            myobj = gTTS(text=text, lang=language, slow=False)

            # Saving the converted audio in a mp3 file named
            # welcome
            myobj.save("welcome.mp3")

            # Playing the converted file
            os.system(" welcome.mp3")
        elif "thank you" in input_text.lower():
            speak("You're welcome!")
        else:
            speak("I'm sorry, I didn't understand what you said.")
import tkinter as tk
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

# Define a function to handle button click events
def handle_click():
    # Listen for user input
    input_text = listen()
    if input_text:
        # Process user input
        if "hello" in input_text.lower():
            speak("Hello! How can I assist you today?")
        elif "what's the time" in input_text.lower():
            speak("The time is currently 3:00 PM.")
        elif "hi" in input_text.lower():
            speak("Opening file...")
            # Process the PDF file
            with open('sample.pdf', 'r') as f:
                file_data = f.read()
            # Speak the contents of the file
            speak(file_data)
        elif "thank you" in input_text.lower():
            speak("You're welcome!")
        else:
            speak("I'm sorry, I didn't understand what you said.")

# Initialize the GUI
root = tk.Tk()

# Set the title of the GUI window
root.title("Blind Assistant Program")

# Create a label for instructions
label = tk.Label(root, text="Click the button and say something to start the program.")
label.pack()

# Create a button to start the program
button = tk.Button(root, text="Start", command=handle_click)
button.pack()

# Start the main loop for the GUI
root.mainloop()

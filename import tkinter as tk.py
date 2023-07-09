import tkinter as tk
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Define a function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to handle button click event
def handle_click():
    text = entry.get()
    speak(text)

# Create the main window
root = tk.Tk()
root.title("Blind Assistant")

# Create a label and an entry widget for input
label = tk.Label(root, text="Enter text:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to trigger the text-to-speech
button = tk.Button(root, text="Speak", command=handle_click)
button.pack()

# Start the GUI event loop
root.mainloop()
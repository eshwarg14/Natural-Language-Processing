import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import sys
import os
import time

def talk(text):
    log_message(f"Assistant: {text}")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # male/female
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            log_message("🎤 Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            audio = listener.listen(source, timeout=5, phrase_time_limit=5)
            command = listener.recognize_google(audio).lower()
            log_message(f"You: {command}")
            return command
    except Exception as e:
        log_message(f"Could not understand: {e}")
        return ""

root = tk.Tk()
root.title("AI Assistant")
root.geometry("550x350")  
root.configure(bg="white")

log_area = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=65, height=15,
    bg="#f9f9f9", fg="black", font=("Consolas", 10)
)
log_area.pack(pady=10, padx=10)

anim_label = tk.Label(root, text="", font=("Arial", 12), fg="green", bg="white")
anim_label.pack()

btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=10)

start_btn = tk.Button(
    btn_frame, text="▶ Start Listening", width=20,
    bg="#4CAF50", fg="white", font=("Arial", 10), relief="flat"
)
stop_btn = tk.Button(
    btn_frame, text="⏹ Stop Listening", width=20,
    bg="#f44336", fg="white", font=("Arial", 10), relief="flat", state=tk.DISABLED
)
start_btn.grid(row=0, column=0, padx=10)
stop_btn.grid(row=0, column=1, padx=10)

running = False
def log_message(msg):
    log_area.insert(tk.END, msg + "\n")
    log_area.see(tk.END)

def animate_listening():
    dots = ""
    while running:
        dots = "." * ((len(dots) % 3) + 1)
        anim_label.config(text="Listening" + dots)
        time.sleep(0.5)
    anim_label.config(text="")

def run_assistant():
    talk("Hello! I am your AI Assistant. How can I help you?")
    while running:
        command = listen()
        if not command:
            continue

        if "time" in command:
            now = datetime.datetime.now().strftime("%H:%M %p")
            talk(f"The time is {now}")

        elif "date" in command:
            today = datetime.datetime.now().strftime("%A, %B %d, %Y")
            talk(f"Today is {today}")

        elif "open google" in command:
            talk("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            talk("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                talk(f"Searching for {query} in Google")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                talk("Please say what you want me to search")

        elif "close youtube" in command or "close google" in command:
            talk("Closing browser window")
            os.system("taskkill /im chrome.exe /f")
            talk("Browser closed")

        elif "your name" in command:
            talk("I am your Personal AI Assistant!")

        elif "exit" in command or "quit" in command:
            talk("Goodbye! Have a nice day.")
            sys.exit()

        else:
            talk("Sorry, I didn’t understand. Please try again.")

def start_listening():
    global running
    if not running:
        running = True
        start_btn.config(state=tk.DISABLED)
        stop_btn.config(state=tk.NORMAL)
        threading.Thread(target=animate_listening, daemon=True).start()
        threading.Thread(target=run_assistant, daemon=True).start()

def stop_listening():
    global running
    running = False
    start_btn.config(state=tk.NORMAL)
    stop_btn.config(state=tk.DISABLED)

start_btn.config(command=start_listening)
stop_btn.config(command=stop_listening)

root.mainloop()

# 🎙️ AI Voice Assistant (Desktop)

A GUI-based voice-controlled AI assistant built using Python. This application listens to user voice commands, processes them, and responds using text-to-speech. It can perform tasks like opening websites, telling time/date, searching Google, and more.

---

## Preview

![Demo](https://github.com/eshwarg14/Natural-Language-Processing/raw/92fc66d6b8c2d6f5ceb946ea560e84a6b74f3388/Images/VA.png)

---

## ✨ Features

- 🎤 Voice command recognition  
- 🔊 Text-to-Speech (TTS) responses  
- 🌐 Open websites (Google, YouTube)  
- 🔍 Search anything on Google  
- 🕒 Tell current time and date  
- ❌ Stop/start listening control  
- 🖥️ GUI with live interaction logs  
- ⚡ Real-time processing with threading  

---

## 🧠 What is a Voice Assistant?

A voice assistant is an AI system that:

- Listens to user voice 🎤  
- Converts speech → text  
- Processes commands  
- Responds using voice 🔊  

👉 Examples: Siri, Alexa, Google Assistant  

---

## 🤖 How It Works

- 🎤 **Speech Recognition**  
  Converts voice → text using Google Speech API  

- 🧠 **Command Processing**  
  Matches keywords like:
  - "time"  
  - "open google"  
  - "search"  

- 🔊 **Text-to-Speech (TTS)**  
  Uses `pyttsx3` to speak responses  

- 🌐 **Action Execution**  
  Opens browser, searches queries, etc.  

---

## 🧠 Technologies Used

```
tkinter
speechrecognition
pyttsx3
threading
webbrowser
datetime
os
```

📦 Install dependencies:

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🎮 Available Commands

- 🕒 "What is the time?"  
- 📅 "What is today's date?"  
- 🌐 "Open Google"  
- ▶️ "Open YouTube"  
- 🔍 "Search Python programming"  
- ❌ "Close Google / YouTube"  
- 🤖 "What is your name?"  
- 🚪 "Exit"  

---

## 📁 Project Structure

```
├── main.py        # Main application
└── README.md
```

---

## ⚠️ Requirements

- 🎤 Microphone (mandatory)  
- 🐍 Python 3.8+  
- 🌐 Internet connection (for speech recognition)  

---

## ⚠️ Important Notes

- `pyaudio` may require manual installation  
- Works best in quiet environment  
- Speech recognition accuracy depends on clarity  

---

## 👨‍💻 Authors

**Eshwar G & Shivani R**

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project:

- ⭐ Star the repo  
- 🍴 Fork it  
- 🛠️ Contribute  

---

## 🚀 Future Improvements

- LLM integration 🤖  
- Wake word detection ("Hey Assistant") 🎤  
- Smart home control 🏠  
- Mobile app version 📱  

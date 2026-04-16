import tkinter as tk
from tkinter import messagebox
from langdetect import detect, detect_langs, DetectorFactory, LangDetectException

DetectorFactory.seed = 0

LANGUAGE_MAP = {
    'af': 'Afrikaans', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali',
    'ca': 'Catalan', 'cs': 'Czech', 'cy': 'Welsh', 'da': 'Danish',
    'de': 'German', 'el': 'Greek', 'en': 'English', 'es': 'Spanish',
    'et': 'Estonian', 'fa': 'Persian', 'fi': 'Finnish', 'fr': 'French',
    'gu': 'Gujarati', 'he': 'Hebrew', 'hi': 'Hindi', 'hr': 'Croatian',
    'hu': 'Hungarian', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese',
    'kn': 'Kannada', 'ko': 'Korean', 'lt': 'Lithuanian', 'lv': 'Latvian',
    'mk': 'Macedonian', 'ml': 'Malayalam', 'mr': 'Marathi', 'ne': 'Nepali',
    'nl': 'Dutch', 'no': 'Norwegian', 'pa': 'Punjabi', 'pl': 'Polish',
    'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sk': 'Slovak',
    'sl': 'Slovenian', 'so': 'Somali', 'sq': 'Albanian', 'sv': 'Swedish',
    'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tl': 'Tagalog',
    'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese',
    'zh-cn': 'Chinese (Simplified)', 'zh-tw': 'Chinese (Traditional)',
}

class LanguageIdentifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Language Identifier - langdetect")
        self.root.geometry("500x350")

        self.label = tk.Label(
            root, 
            text="Enter or paste text below to detect its language", 
            font=("Arial", 12, "bold")
        )
        self.label.pack(pady=10)

        self.text_input = tk.Text(root, height=6, font=("Arial", 11))
        self.text_input.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.detect_button = tk.Button(
            root, 
            text="Detect Language", 
            command=self.detect_language, 
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10
        )
        self.detect_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 13, "bold"), fg="#2196F3")
        self.result_label.pack(pady=10)

    def detect_language(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Needed", "Please enter or paste some text to detect its language.")
            return

        try:
            lang_code = detect(text)

            lang_name = LANGUAGE_MAP.get(lang_code, lang_code.upper())

            langs = detect_langs(text)
            confidence = langs[0].prob  

            self.result_label.config(
                text=f"Detected Language: {lang_name}\nLanguage Code: {lang_code}\nConfidence: {confidence:.2%}"
            )
        except LangDetectException as e:
            messagebox.showerror("Error", f"Language detection failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageIdentifierApp(root)
    root.mainloop()

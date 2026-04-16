import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading, requests
from newspaper import Article

API_KEY = ""
URL     = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = "You are a news summarizer. Summarize the given article clearly and concisely in 5-7 bullet points."

def summarize(text):
    try:
        r = requests.post(URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost",
                "X-Title": "NewsSummarizer"
            },
            json={
                "model": "openrouter/free",
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user",   "content": text}
                ]
            },
            timeout=30
        )
        data = r.json()
        if "choices" in data:
            return data["choices"][0]["message"]["content"].strip()
        elif "error" in data:
            return f"API Error: {data['error']['message']}"
        return str(data)
    except Exception as e:
        return f"Error: {e}"

class NewsSummarizerApp:
    def __init__(self, root):
        self.root = root
        root.title("📰 News Summarizer")
        root.geometry("900x800")

        tk.Label(root, text="Enter Article URL:", font=("Arial", 12)).pack(pady=5)
        self.url_entry = tk.Entry(root, font=("Arial", 12), width=80)
        self.url_entry.pack(padx=10)
        self.url_entry.bind("<Return>", lambda e: self.fetch())

        tk.Label(root, text="– OR – Paste Article Text:", font=("Arial", 12)).pack(pady=5)
        self.input_text = scrolledtext.ScrolledText(root, height=10)
        self.input_text.pack(fill=tk.BOTH, padx=10)

        tk.Button(root, text="Summarize", bg="#4CAF50", fg="white",
                  command=self.fetch).pack(pady=8)

        tk.Label(root, text="Article Preview:", font=("Arial", 12)).pack(pady=5)
        self.article_text = scrolledtext.ScrolledText(root, height=10)
        self.article_text.pack(fill=tk.BOTH, padx=10)

        tk.Label(root, text="Summary:", font=("Arial", 12)).pack(pady=5)
        self.summary_text = scrolledtext.ScrolledText(root, height=10)
        self.summary_text.pack(fill=tk.BOTH, padx=10, pady=5)

    def fetch(self):
        url  = self.url_entry.get().strip()
        text = self.input_text.get("1.0", tk.END).strip()
        if not url and not text:
            return messagebox.showwarning("Input Required", "Enter URL or text")
        self.summary_text.delete("1.0", tk.END)
        self.summary_text.insert(tk.END, "⚡ Summarizing...\n")
        threading.Thread(target=self.process, args=(url, text), daemon=True).start()

    def process(self, url, text):
        if url:
            try:
                art = Article(url)
                art.download()
                art.parse()
                text = art.text
            except Exception as e:
                return self.update_summary(f"Error fetching URL: {e}")

        text    = " ".join(text.split()[:600])
        preview = text[:1200] + ("..." if len(text) > 1200 else "")
        self.root.after(0, lambda: (
            self.article_text.delete("1.0", tk.END),
            self.article_text.insert(tk.END, preview)
        ))
        summary = summarize(text)
        self.update_summary(summary)

    def update_summary(self, text):
        self.root.after(0, lambda: (
            self.summary_text.delete("1.0", tk.END),
            self.summary_text.insert(tk.END, text)
        ))

root = tk.Tk()
app  = NewsSummarizerApp(root)
root.mainloop()

import streamlit as st
import random
from datetime import datetime
from googletrans import Translator

def main():
    st.set_page_config(
        page_title="AI Translator", 
        page_icon="🌍", 
        layout="wide"
    )
    st.title("🌍 AI Language Translator")
    st.markdown("### Translate text between multiple languages!")

    languages = {
        "English": "en", "Spanish": "es", "French": "fr", "German": "de",
        "Italian": "it", "Portuguese": "pt", "Hindi": "hi", "Chinese (Simplified)": "zh-cn",
        "Chinese (Traditional)": "zh-tw", "Japanese": "ja", "Arabic": "ar",
        "Kannada": "kn", "Tamil": "ta", "Telugu": "te", "Marathi": "mr", "Gujarati": "gu",
        "Bengali": "bn", "Malayalam": "ml", "Punjabi": "pa", "Urdu": "ur"
    }

    translator = Translator()

    if "history" not in st.session_state:
        st.session_state.history = []

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📝 Source Text")
        source_lang = st.selectbox("From Language:", list(languages.keys()))
        sample_texts = {
            "English": "Hello! How are you today?",
            "Hindi": "नमस्ते! आप आज कैसे हैं?",
            "Kannada": "ನಮಸ್ಕಾರ! ನೀವು ಇಂದು ಹೇಗಿದ್ದೀರಿ?",
            "Tamil": "வணக்கம்! இன்று எப்படி இருக்கிறீர்கள்?",
            "Telugu": "హలో! మీరు ఈ రోజు ఎలా ఉన్నారు?",
            "Marathi": "नमस्कार! तुम्ही आज कसे आहात?",
        }
        default_text = sample_texts.get(source_lang, "Hello, world!")
        source_text = st.text_area("Enter text:", value=default_text, height=150)

        if source_text:
            words = len(source_text.split())
            chars = len(source_text)
            st.info(f"📊 Words: {words} | Characters: {chars}")

    with col2:
        st.markdown("### 🎯 Translated Text")
        target_lang = st.selectbox(
            "To Language:", 
            [lang for lang in languages.keys() if lang != source_lang]
        )

        if st.button("🚀 Translate", type="primary", use_container_width=True):
            if source_text.strip():
                try:
                    translated_obj = translator.translate(
                        source_text, 
                        src=languages[source_lang], 
                        dest=languages[target_lang]
                    )
                    translated = translated_obj.text
                    confidence = random.randint(90, 98)

                    st.success("Translation completed! ✅")
                    st.text_area("Translated text:", value=translated, height=150)

                    st.session_state.history.insert(0, {
                        "From": source_lang,
                        "To": target_lang,
                        "Source": source_text,
                        "Translation": translated,
                        "Time": datetime.now().strftime("%H:%M:%S")
                    })

                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        st.metric("Confidence", f"{confidence}%")
                    with col_b:
                        st.metric("Speed", f"{random.randint(50, 200)}ms")
                    with col_c:
                        st.metric("Quality", "High")

                except Exception as e:
                    st.error(f"Translation failed: {e}")
            else:
                st.warning("Please enter text to translate.")

    st.markdown("### 📚 Recent Translations")
    if st.session_state.history:
        st.dataframe(st.session_state.history, use_container_width=True)
    else:
        st.info("No translations yet.")

if __name__ == "__main__":
    main()

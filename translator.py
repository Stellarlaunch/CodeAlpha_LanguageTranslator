import streamlit as st
from googletrans import Translator, LANGUAGES

# Set page config
st.set_page_config(page_title="Language Translator 💬", page_icon="🌍")

# Title
st.title("🌍 Language Translator Tool")
st.markdown("Translate any text from one language to another with a click 💖")

# Initialize translator
translator = Translator()

# Get list of languages
lang_list = list(LANGUAGES.values())
lang_dict = {v: k for k, v in LANGUAGES.items()}

# Input text
input_text = st.text_area("Enter text to translate:", height=150)

# Language selection
col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Source Language", lang_list, index=lang_list.index("english"))
with col2:
    dest_lang = st.selectbox("Target Language", lang_list, index=lang_list.index("hindi"))

translated_text = ""

if st.button("Translate 💫"):
    try:
        translated = translator.translate(input_text, src=lang_dict[src_lang], dest=lang_dict[dest_lang])
        translated_text = translated.text
        st.success("Translated Text 💖")
        st.write(translated_text)

        # Copy button appears ONLY if there's translated text
        if translated_text:
            if st.button("📋 Copy to Clipboard"):
                import pyperclip
                pyperclip.copy(translated_text)
                st.success("Text copied to clipboard! 💖")


    except Exception as e:
        st.error(f"Translation failed: {e}")


import pyperclip  # This lets you copy text to clipboard

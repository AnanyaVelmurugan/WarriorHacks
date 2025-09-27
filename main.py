# Theme: Build a tool that breaks down barriers to learning, making education more inclusive, accessible, and impactful.
# Ananya Velmurugan & Sudarshini Seth (WarriorHacks)

# IMPORTS
import streamlit as st
from gtts import gTTS
import tempfile
import os

# FUNCTIONS
def apply_style(text):
    style = f"font-size:{font_size}px; line-height:1.6;"
    if theme == "Dark":
        style += "background-color:#222; color:#fff; padding:10px; border-radius:10px;"
    elif theme == "High Contrast":
        style += "background-color:#000; color:#FFD700; padding:10px; border-radius:10px;"
    elif theme == "Dyslexia-Friendly":
        style += "font-family: OpenDyslexic, Arial, sans-serif; background-color:#f4f4f4; color:#333; padding:10px; border-radius:10px;"
    else:  # Light
        style += "background-color:#f9f9f9; color:#111; padding:10px; border-radius:10px;"
    return f"<div style='{style}'>{text}</div>"

# STREAMLIT APP
st.set_page_config(page_title="EZText", page_icon="📚", layout="centered")

st.title("EZText")
st.subheader("Making knowledge available to anyone.")

left, center, right = st.columns([10, .1, 10])

# Text Input
with right:
    text_input = st.text_area("Paste your text here:")

    uploaded_file = st.file_uploader("...or upload a text file", type=["txt"])
    if uploaded_file is not None:
        text_input = uploaded_file.read().decode("utf-8")

# Display
    font_size = st.slider("Font size", 12, 40, 18)
    theme = st.selectbox("Color theme", ["Light", "Dark", "High Contrast", "Dyslexia-Friendly"])

with left:
    if text_input:
        st.markdown(apply_style(text_input), unsafe_allow_html=True)

        st.write("\n")
        # TTS
        if st.button("🔊 Convert to Speech"):
            tts = gTTS(text_input)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
                tts.save(tmpfile.name)
                audio_file = tmpfile.name

            st.audio(audio_file, format="audio/mp3")
            os.remove(audio_file)


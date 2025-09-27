import streamlit as st
import flashcard
import os

def app():
    path = 1
    
    chapter = st.sidebar.radio("Go to Chapter", ["Chapter 1", "Chapter 2"])

    if chapter:
        path = int(chapter[8:])
    with st.sidebar:
        flashcard.create_flashcard()

    file_path = os.path.join(f"yawp_chapters\Chapter{path}.txt")

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text_data = f.read()

        st.subheader(f"{chapter}")
        st.text(text_data)
    else:
        st.write("Select a chapter to view its content.")

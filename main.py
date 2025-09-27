# Theme: Build a tool that breaks down barriers to learning, making education more inclusive, accessible, and impactful.
# Ananya Velmurugan & Sudarshini Seth (WarriorHacks)

# IMPORTS
import streamlit as st
import yawp
import flashcard

st.set_page_config(page_title="Learning Tool", layout="wide")

def app():
    st.title("Welcome to the Learning Tool")
    st.write("This tool is designed to help you explore and understand the content of textbooks.")
    st.write("Use the sidebar to navigate through different chapters and sections.")
    st.write("Happy learning!")


page = st.sidebar.radio("Go to page", ["Home", "American Yawp", "Flashcards"])

if page == "Home":
    app()
elif page == "American Yawp":
    yawp.app()

elif page == "Flashcards":
    flashcard.app()
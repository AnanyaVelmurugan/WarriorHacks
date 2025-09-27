import streamlit as st

# Initialize flashcards list in session state
if "flashcards" not in st.session_state:
    st.session_state.flashcards = []

def create_flashcard():
    # --- Flashcard Creation Form ---
    st.markdown("---")
    st.subheader("Create Flashcard")

    # If user has highlighted text, prefill question with it
    with st.form(key="flashcard_form"):
        question = st.text_area("Question", value="", max_chars=500, help="This can be your highlighted text or any question.")
        answer = st.text_area("Answer", max_chars=1000)
        submit = st.form_submit_button("Create Flashcard")

        if submit:
            if question.strip() == "" or answer.strip() == "":
                st.error("Please enter both question and answer.")
            else:
                st.session_state.flashcards.append({"question": question.strip(), "answer": answer.strip()})
                st.success("Flashcard created successfully!")
                # Clear the selected text input and text areas
                st.session_state.selected_text_input = ""
                question = ""
                answer = ""

def app():
    st.title("Flashcards")
    st.write("Create and review flashcards to enhance your learning.")

    st.subheader("Review Flashcards")

    if len(st.session_state.flashcards) == 0:
        st.info("No flashcards available. Create some to get started!")
    else:
        for idx, card in enumerate(st.session_state.flashcards):
            with st.expander(f"Flashcard {idx + 1}: {card['question']}"):
                st.write(card["answer"])
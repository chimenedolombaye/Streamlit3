import speech_recognition as sr
import streamlit as st
# Ajouter une option pour choisir l'API de reconnaissance vocale
selected_api = st.selectbox("Select Speech Recognition API", ["Google", "Sphinx"])

def transcribe_speech(language='french', selected_api='Google') :
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Parler maintenant...")
        audio_text = recognizer.listen(source)
        st.info("Transcribing...")

        try:
            # Utiliser Google Speech Recognition
            if selected_api == "Google":
                text = recognizer.recognize_google(audio_text, language=language)
            # Utiliser Sphinx (sans connexion Internet)
            elif selected_api == "Sphinx":
                text = recognizer.recognize_sphinx(audio_text, language=language)
            else:
                return f"API {selected_api} not supported."

            return text
        except sr.UnknownValueError:
            return "Désolé, je n'ai rien entendu."
        except sr.RequestError as e:
            return f"Erreur avec l'API {selected_api} : {e}"

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # Ajouter une option pour choisir la langue
    selected_language = st.selectbox("Select Language", ["Francais", "Anglais", "mandarin"])

    # Ajouter un bouton pour démarrer et arrêter l'enregistrement
    recording = st.button("Start Recording")

    if recording:
        text = transcribe_speech(language=selected_language)
        st.write("Transcription: ", text)

        # Ajouter un bouton pour sauvegarder le texte transcrit dans un fichier
        if st.button("Save Transcription"):
            with open("transcription.txt", "w") as file:
                file.write(text)
                st.success("Transcription saved successfully!")


if __name__ == "__main__":
    main()

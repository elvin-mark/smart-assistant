import streamlit as st
from io import StringIO
from engine.ai.rag import upload_file
from engine.ai.asr import speech_recognition
from engine.ai.tts import text_to_speech
from engine.agent import agent


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    upload_file(stringio.read())

response = None

st.title("Chat with the Smart Assistant!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What would you like to know?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = agent.run(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

audio_value = st.audio_input("Record a voice message")
if audio_value is not None:
    transcription = speech_recognition(audio_value)
    st.chat_message("user").markdown(transcription)
    st.session_state.messages.append({"role": "user", "content": transcription})

    response = agent.run(transcription)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

if response is not None:
    text_to_speech(response)
    st.audio(open("tmp/spoken.wav", "rb").read())

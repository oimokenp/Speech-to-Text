import os
import pathlib

from google.cloud import speech

import streamlit as st

# You must set a valid json file.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'xxxxxxxxxx.json'

def transcribe_file(content, lang='english'):
    lang_code = {
        'english': 'en-US',
        'japanese': 'ja-JP'
    }

    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content = content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        language_code=lang_code[lang],
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        st.write(result.alternatives[0].transcript)

st.title('Speech_to_Text')
st.header('Summary')
st.write('This is an application that uses "Google Cloud Speech-to-Text".')
st.markdown('<a href="https://cloud.google.com/speech-to-text?hl=ja" target="_blank">Google Speech-to-Text</a>', unsafe_allow_html=True)
st.write('The supported languages are "English, Japanese" and the extension is "wav".')
st.write('Voice data is limited to one minute.')
upload_file = st.file_uploader('File Uploading', type=['wav'])
if upload_file is not None:
    content = upload_file.read()
    
    path = path = pathlib.Path(upload_file)
    
    st.subheader('Details')
    file_detail = {'File name': upload_file.name, 'File type': upload_file.type, 'File size': upload_file.size}
    st.write(file_detail)
    
    st.subheader('Playing')
    st.audio(content)
    
    st.subheader('Language')
    option = st.selectbox('Select Language', ('English','Japanese'))
    st.write('Selected language:', option)
    
    st.write('transcription')
    if st.button('Start'):
        comment = st.empty()
        comment.write('Start transcription')
        transcribe_file(content, lang=option)
        comment.write('Complete')
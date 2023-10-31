import streamlit as st
from modules.analyzer import Analyzer
from modules.qna import questions, answers

anal = Analyzer()

def click_handler(text):
    if len(text) < 50:
        st.warning('Input must be atleast 50 characters long', icon="⚠️")
    else:
        st.pyplot(anal.analyze(text))

st.title("Sentiment Analyzer")
for i in range(len(questions)):
    input = st.text_area(questions[i], value = answers[i], max_chars = 250)
    if st.button('Analyze', key = i): click_handler(input)
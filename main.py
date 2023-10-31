import streamlit as st
from packages.analyzer import Analyzer
from packages.qna import questions, answers

anal = Analyzer()

def click_handler(text):
    if len(text) < 50:
        st.warning('Input must be atleast 50 characters long', icon="⚠️")
    else:
        st.pyplot(anal.analyze(text))

st.title("Sentiment Analyzer")
input1 = st.text_area(questions[0], value = answers[0], max_chars = 250)
if st.button('Analyze', key = 1): click_handler(input1)
input2 = st.text_area(questions[1], value = answers[1], max_chars = 250)
if st.button('Analyze', key = 2): click_handler(input2)
input3 = st.text_area(questions[2], value = answers[2], max_chars = 250)
if st.button('Analyze', key = 3): click_handler(input3)
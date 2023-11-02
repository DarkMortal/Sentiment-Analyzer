import streamlit as st
from modules.analyzer import Analyzer
from modules.qna import questions, answers

anal = Analyzer()
st.set_page_config(
    page_title = 'Synthesized Infinity',
    layout = 'centered',
    initial_sidebar_state = 'collapsed'
)

# TODO: load css styles
with open('./styles/styles.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

def click_handler(text):
    if len(text) < 50:
        st.warning('Input must be atleast 50 characters long', icon="⚠️")
    else:
        st.pyplot(anal.analyze(text))

with st.sidebar:
    st.header("Team members")
    st.markdown("""<ul>
        <li>Ankita Das</li>
        <li>Aishika Datta</li>
        <li>Rohit Shaw</li>
        <li>Saptarshi Dey</li>
        <li>Arkoprabho Dey</li>
        <li>Chandrabha Chatterjee</li>
    </ul>""",
    unsafe_allow_html=True)
    st.header("Share Feedback")
    st.markdown("""
        <form action="https://formsubmit.co/dragonbeast.saiyan@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="true" />
            <input type="text" name="name" placeholder="Your name" required />
            <input type="email" name="email" placeholder="Your email" required />
            <textarea name="message" placeholder="Please enter your valuable feedback" required ></textarea>
            <button type="submit">Share</button>
        </form>
    """, unsafe_allow_html = True)

st.title("Sentiment Analyzer")
for i in range(len(questions)):
    input = st.text_area(questions[i], value = answers[i], max_chars = 500)
    st.caption("Default answer generated by ChatGPT<br/>OpenAI (2023) https://chat.openai.com", unsafe_allow_html = True)
    if st.button('Analyze', key = i): click_handler(input)
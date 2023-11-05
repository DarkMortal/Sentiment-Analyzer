import streamlit as st

# TODO: load css styles
with open('./styles/styles.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

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
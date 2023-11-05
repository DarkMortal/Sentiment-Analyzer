import streamlit as st

def about():
    st.header("Team members")
    st.markdown("""
    <style>
        .list { margin-bottom: -10px; }
        .list li h5 { margin: -7px; }
    </style>
    <ul class="list">
    <li><h5>Ankita Das</h5></li>
    <li><h5>Aishika Datta</h5></li>
    <li><h5>Rohit Shaw</h5></li>
    <li><h5>Saptarshi Dey</h5></li>
    <li><h5>Arkoprabho Dey</h5></li>
    <li><h5>Chandrabha Chatterjee</h5></li>
    </ul>""", unsafe_allow_html=True)

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
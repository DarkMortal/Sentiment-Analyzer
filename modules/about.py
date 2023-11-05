import streamlit as st

def about():
    st.header("Team members")
    st.markdown("""
    <style>.list li {font-size: 1.3rem;}</style>
    <ul class="list">
    <li>Ankita Das</li>
    <li>Aishika Datta</li>
    <li>Rohit Shaw</li>
    <li>Saptarshi Dey</li>
    <li>Arkoprabho Dey</li>
    <li>Chandrabha Chatterjee</li>
    </ul>""", unsafe_allow_html=True)

    # st.header("Share Feedback")
    st.markdown("""
        <form action="https://formsubmit.co/dragonbeast.saiyan@gmail.com" method="POST">
            <h2 style="color: #111827;">Share Feedback</h2>
            <input type="hidden" name="_captcha" value="true" />
            <input type="text" name="name" placeholder="Your name" required />
            <input type="email" name="email" placeholder="Your email" required />
            <textarea name="message" placeholder="Please enter your valuable feedback" required ></textarea>
            <button type="submit">Share</button>
        </form>
    """, unsafe_allow_html = True)
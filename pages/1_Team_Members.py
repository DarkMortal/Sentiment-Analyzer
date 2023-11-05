import streamlit as st

# TODO: load css styles
with open('./styles/styles.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

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
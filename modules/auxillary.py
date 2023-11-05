from streamlit import markdown as md

questions = open('./data/questions.txt',encoding = 'utf-8').read().split('\n')
answers = open('./data/answers.txt',encoding = 'utf-8').read().split('\n')

def load_css(filepath = "./styles/styles.css"):
    with open(filepath) as file:
        md(f'<style>{file.read()}</style>', unsafe_allow_html=True)
import streamlit as st
import json as js
from streamlit_option_menu import option_menu as menu
from modules.analyzer import Analyzer
from modules.auxillary import questions, answers

anal = Analyzer()
answers_array = []

def click_handler(text, graphConfig):
    if len(text) < 50:
        st.warning('Input must be atleast 50 characters long', icon="⚠️")
    else:
        data = anal.analyze(text)
        st.caption("<h3>Output</h3>", unsafe_allow_html = True)
        st.pyplot(anal.generatePlot(data, graphConfig))

def json_handler(text):
    if len(text) < 50:
        st.warning('Input must be atleast 50 characters long', icon="⚠️")
    else:
        data = anal.analyze(text).items()
        json = [{"emotion": key.strip(),"occurence": value} for key,value in data]
        json = js.dumps(json, indent = 3)
        st.caption("<h3>Output</h3>", unsafe_allow_html = True)
        st.code(json, language = 'json', line_numbers = True)

def home():
    with st.sidebar:
        st.title("Graph settings")
        color = st.color_picker("Bar color", '#1F75FE')
        labelColor = st.color_picker("Axis label color", '#000000')
        borderColor = st.color_picker("Plot border color", '#000000')
        faceColor = st.color_picker("Plot background color", '#f0f8ff')
        backColor = st.color_picker("Graph background color", '#ffffff')
        axes = st.checkbox("Show axis names")
        divs = st.checkbox("Show divisions", value = True)
        show_pge = st.checkbox("Show percentage", value = True)
        horizontal_graph = st.checkbox("Horizontal Graph")
    currentGraphConfig = {
        'graphColor': color,
        'isHorizontal': horizontal_graph,
        'showAxes': axes,
        'background': backColor,
        'faceColor': faceColor,
        'labelColor': labelColor,
        'borderColor': borderColor,
        'showP': show_pge,
        'isAxis': divs
    }
    st.title("Sentiment Analyzer")
    for i in range(len(questions)):
        input = st.text_area(
            questions[i], value = answers[i],
            max_chars = 500, placeholder = 'Enter you answer here (min 50 chars)'
        )
        currentGraphConfig = {
            'graphColor': color,
            'isHorizontal': horizontal_graph,
            'showAxes': axes,
            'background': backColor,
            'faceColor': faceColor,
            'labelColor': labelColor,
            'borderColor': borderColor,
            'showP': show_pge,
            'isAxis': divs
        }
        answers_array.append(input)
        generate = st.selectbox(
            'Choose output format',
            ['Bar Graph','Javascript Object Notation (JSON)'],
            key = f'select{i}',
            # label_visibility = 'collapsed'
        )
        if st.button('Analyze', key = f'button1{i}'):
            if generate == 'Bar Graph': click_handler(input, currentGraphConfig)
            if generate == "Javascript Object Notation (JSON)": json_handler(input)
        st.divider()
    st.header("Final report generation")
    generate = st.selectbox(
            'Choose output format',
            ['Bar Graph','Javascript Object Notation (JSON)'],
            key = "final_report_box",
            # label_visibility = 'collapsed'
    )
    if st.button('Analyze', key = "final_report_button"):
        if generate == 'Bar Graph': click_handler(' '.join(answers_array), currentGraphConfig)
        if generate == "Javascript Object Notation (JSON)": json_handler(' '.join(answers_array))
    answers_array.clear()
    st.divider()
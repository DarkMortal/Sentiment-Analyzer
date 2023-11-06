import streamlit as st
from streamlit_option_menu import option_menu as menu
from modules.about import about
from modules.home import home
from modules.auxillary import load_css

st.set_page_config(
    page_title = 'Synthesized Infinity',
    layout = 'centered',
    initial_sidebar_state = 'collapsed'
)

# TODO: load css styles
load_css()

selected = menu(
    menu_title = None,
    # menu_icon = 'menu-button-wide-fill',
    options = ["Home", "About"],
    icons = ["house-door-fill", "info-square-fill"],
    orientation = 'horizontal',
    default_index = 0,
)

if selected == "Home": home()
if selected == "About": about()
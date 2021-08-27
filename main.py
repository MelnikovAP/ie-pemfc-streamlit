from pathlib import WindowsPath
import numpy as np
from requests.api import head
import streamlit as st
import requests
import pandas as pd
from bokeh.plotting import figure

#st.set_page_config(page_title=None, page_icon=None, layout='wide', initial_sidebar_state='auto')

works = ['Introduction', 
        'Work #1: The first work', 
        'Work #2: The second work', 
        'Work #3: The third work',
        'Futher investigation']

# ==============================
# Sidebar
# ==============================

st.sidebar.image('https://raw.githubusercontent.com/MelnikovAP/pv-streamlit/main/Images/logo.png')
st.sidebar.markdown('***')
st.sidebar.header('PEMFC cloud model')
tab_selected = st.sidebar.selectbox('Select the work:', works)

if tab_selected != works[0]:
    st.sidebar.subheader('Model parameters')

# ==============================
# Main page
# ==============================

header_container = st.container()
for item in works:
    if tab_selected == item:
        with header_container:
            st.title(item)
            '''***'''

if tab_selected == works[0]:
    
    introduction_container = st.container()
    scheme_container = st.container()
    basics_container = st.container()
    theory_container = st.container()
    whatnext_container = st.container()

    with introduction_container:
        pass

    with scheme_container:
        pass

    with basics_container:
        pass

    with theory_container:
        pass
    
    with whatnext_container:
        '''
        ### What next?
        Based on the above equations and some more machine learning algorithms we 
        have prepared a mathematical model that describes SOFC single cell. Please, 
        follow up all the works for better understanding of SOFC theoretical basics.
        '''
        '''
        To proceed, select the next section in the left sidebar. 
        '''

if tab_selected == works[1]:
    
    introduction_container = st.container()

    with introduction_container:
        pass


if tab_selected == works[2]:
    introduction_container = st.container()

if tab_selected == works[3]:
    introduction_container = st.container()

if tab_selected == works[4]:
    introduction_container = st.container()


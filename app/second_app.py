import streamlit as st
import numpy as np
import pandas as pd

#x = 4
#st.write(x, 'squared is', x * x)

#x = 4
#x, 'squared is', x * x  # 👈 Magic!

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider1 = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0),
    key = "1"
)

add_slider2 = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0),
    key = "2"
)


add_selectbox
add_slider1
add_slider2
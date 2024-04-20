# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:15:13 2024

@author: inage
"""

import streamlit as st

# Apply custom CSS styles
st.markdown("""
    <style>
        .title {
            color: #3366ff;
            text-align: center;
            font-size: 36px;
            padding: 20px 0;
        }
        .button {
            background-color: #3366ff;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #254EDA;
        }
    </style>
""", unsafe_allow_html=True)

# Set page title and layout
st.set_page_config(page_title="Disease Prediction App", layout="wide")

# Title
st.markdown("<h1 class='title'>Disease Prediction App</h1>", unsafe_allow_html=True)

# Sidebar navigation
selected = st.sidebar.radio("Choose Disease", ("Diabetes", "Heart Disease", "Parkinson's"))

# Main content
if selected == "Diabetes":
    # Add input fields and prediction button for diabetes prediction
    pass
elif selected == "Heart Disease":
    # Add input fields and prediction button for heart disease prediction
    pass
elif selected == "Parkinson's":
    # Add input fields and prediction button for Parkinson's prediction
    pass
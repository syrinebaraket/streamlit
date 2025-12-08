# This home page for all apps "APPS HUB"
# The styling file is style.css under pages/style/style.css path

# Import librairies
# Every librairy should be added in the requirements.txt path: pages/requirements.txt
# flip_box is a function that creates the boxes in the homepage. It takes as input:
# - Box Title
# - Description in the flip back 
# - Link to App

import streamlit as st
from utils import header_with_highlight

st.set_page_config(page_title="Rubix App X", layout="wide")

with open("SBRX/style/style.css") as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)



    
# Call your reusable component
header_with_highlight("App", "Name")

# Custom CSS for rounded box
st.markdown("""
    <style>
    .description-box {
        background-color: #D7E0E9;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
    }
    .description-box h3 {
        font-weight: bold;
        margin-bottom: 10px;
    }
    .description-box p {
        font-size: 16px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# HTML block for the description
st.markdown("""
    <div class="description-box">
        <h3>Description</h3>
        <p>Here where description is written</p>
    </div>
""", unsafe_allow_html=True)


 

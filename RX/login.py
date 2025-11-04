import streamlit as st
from time import sleep

from st_pages import hide_pages

# --- Page Config ---
st.set_page_config(page_title="RUBIX Login", layout="centered")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- Custom CSS ---
st.markdown("""
    <style>
        .login-container {
            background-color: #f5f5f5;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            width: 400px;
            margin: auto;
            margin-top: 5vh;
        }
        .login-header {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            color: #003B70;
            margin-bottom: 1rem;
        }
        .login-logo {
            display: flex;
            justify-content: center;
            margin-bottom: 1rem;
        }
        button[kind="secondary"] {
        background-color: green !important;
        color: white !important;
        font-weight: bold;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)


# --- Login Box ---

st.image("RX/pictures/Picture2.png" )
st.markdown('<div class="login-header">Sign in </div>', unsafe_allow_html=True)

username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", placeholder="Enter your password", type="password")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Sign in", type="secondary",key="login", help="Click to log in",width="stretch"):
        if username == "TechTeam" and password == "danone123":  # Replace with secure logic
            st.success("Login successful!")
            st.session_state.logged_in = True
            sleep(1)
            st.switch_page("pages/homepage.py")
        else:
            st.error("Invalid credentials. Please try again.")
with col2:
    st.button("Cancel",type="primary", key="cancel", width="stretch")

st.markdown('</div>', unsafe_allow_html=True)






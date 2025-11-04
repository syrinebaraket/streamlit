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
        .login-button {
            background-color: #0054A8;
            color: white;
            font-weight: bold;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            width: 100%;
            margin-top: 1rem;
        }
        .cancel-button {
            background-color: #ccc;
            color: black;
            font-weight: bold;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            width: 100%;
            margin-top: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)


# --- Login Box ---

st.image("pictures/Picture2.png" )
st.markdown('<div class="login-header">Sign in </div>', unsafe_allow_html=True)

username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", placeholder="Enter your password", type="password")

if st.button("Sign in", key="login", help="Click to log in"):
    if username == "TechTeam" and password == "danone123":  # Replace with secure logic
        st.success("Login successful!")
        st.session_state.logged_in = True
        sleep(1)

        st.switch_page("pages/homepage.py")



    else:
        st.error("Invalid credentials. Please try again.")

st.button("Cancel", key="cancel")

st.markdown('</div>', unsafe_allow_html=True)

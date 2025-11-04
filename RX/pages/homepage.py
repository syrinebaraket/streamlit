import streamlit as st
from PIL import Image
from modules.nav import Nav



# Check login status
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in to access this page.")
    st.stop()

st.set_page_config(
    layout='centered',
    page_title='Rubix',
    page_icon="🧩"
)



    # Other stuff



# Check login status
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in to access this page.")
    st.stop()

st.html(
    """
<style>
[data-testid="stSidebarContent"] {
    color: white;
}
</style>
"""
)
# --- Page Config ---
st.set_page_config(page_title="RUBIX Platform", layout="wide")

# --- Header ---
st.markdown("""
    <style>
        .header {
            background-color: #0054A8;
            border-radius: 10px;
            padding: 1rem;
            color: white;
            font-size: 24px;
            font-weight: bold;
            margin-top: 0 !important;

        }
        .tile {
            border-radius: 10px;
            padding: 2rem;
            text-align: center;
            color: white;
            font-size: 20px;
            font-weight: bold;
            cursor: pointer;
        }
        .catalog { background-color: #00AEEF; }
        .factory { background-color: #003B70; }
        .data { background-color: #6BBE44; }
        .footer {
            margin-top: 2rem;
            font-size: 14px;
            color: gray;
            text-align: center;
        }
        .feedback-tab {
            position: fixed;
            right: 0;
            top: 50%;
            transform: translateY(-50%);
            background-color: #0077C8;
            color: white;
            padding: 0.5rem 1rem;
            border-top-left-radius: 8px;
            border-bottom-left-radius: 8px;
            font-weight: bold;
        }
         .highlighted-text {
            background-color: #00ACED;
            color: white;
            padding: 0.2rem 0.5rem;
            border-radius: 0px;
        }

    </style>
    <div class="header"> <span class="highlighted-text">Homepage</span></div>
""", unsafe_allow_html=True)



# --- Tiles ---
st.markdown("<br>", unsafe_allow_html=True)
col1, col2,col3,col4= st.columns(4)

with col2:
    st.image("RX/pictures/design.png", width=300)
    
    
with col3:
    st.image("RX/pictures/EventPortal.png", width=300)
    st.markdown('<a href="app.py">', unsafe_allow_html=True)




# --- Feedback Tab ---
st.markdown("""
    <div class="feedback-tab">Feedback</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>©  RUBIX | DANONE </div>", unsafe_allow_html=True)



import streamlit as st

# --- Initialize toggle state ---
if "sidebar_expanded" not in st.session_state:
    st.session_state.sidebar_expanded = False

# --- Styling ---




# --- Adjust Sidebar Width Based on State ---







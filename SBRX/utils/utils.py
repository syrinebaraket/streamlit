# utils.py
import streamlit as st

def header_with_highlight(main_text: str, highlight_text: str):
    st.markdown("""
        <style>
            .header {
                background-color: #0054A8;
                border-radius: 10px;
                padding: 1rem;
                color: white;
                font-size: 23px;
                font-weight: bold;
                margin-top: 0 !important;
            }
            .highlighted-text {
                background-color: #00ACED;
                color: white;
                padding: 0.2rem 0.5rem;
                border-radius: 0px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(
        f'<div class="header">{main_text} <span class="highlighted-text">{highlight_text}</span></div>',
        unsafe_allow_html=True
    )
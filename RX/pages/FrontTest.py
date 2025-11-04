import streamlit as st

# Page config
st.set_page_config(layout="wide")

# Custom CSS for rounded boxes and subtle shadow
st.markdown("""
    <style>
    .rounded-box {
        background-color: #f5f5f5;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        height: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        color: #333;
        
    }
    .rounded-box:hover{transform: translateY(-10px);
            transition:transform 0.9s}
    </style>
""", unsafe_allow_html=True)

# First row
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="rounded-box">Box 1</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="rounded-box">Box 2</div>', unsafe_allow_html=True)

# Spacer
st.markdown("")

# Second row
col3, col4 = st.columns(2)
with col3:
    st.markdown('<div class="rounded-box">Box 3</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="rounded-box">Box 4</div>', unsafe_allow_html=True)

# Optional: subtle arrow or navigation hint
st.markdown("""
    <div style="text-align:center; margin-top:20px;">
        <span style="font-size:24px; color:#007BFF;">&#8595;</span>
    </div>
""", unsafe_allow_html=True)
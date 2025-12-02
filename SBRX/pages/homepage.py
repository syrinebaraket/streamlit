import streamlit as st

st.set_page_config(page_title="Rubix App Hub", layout="wide")




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
    <div class="header"> APPS <span class="highlighted-text">HUB</span></div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .st-key-boxC {  
            MARGIN-top:10px;
        padding: 20px;
        width:100%;
        border-radius: 12px;
        box-shadow: 0px 0px 16px -6px rgba(0, 0, 0, .7);
        background-color: #F2F5F8;}

    </style>
""", unsafe_allow_html=True)


left, LLeft, m, Rright, right = st.columns([1, 2, 2, 2, 1])
with m:
   
        st.image("pictures/HomePageLogo.png")
# Inject CSS

st.markdown(
    """
    <style>
        body {
            background-color: #F2F5F8; /* Solid blue */
        }
        .stApp {
            background-color: #F2F5F8; /* Streamlit app wrapper */
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #24276C;
        color: white;
    }
    [data-testid="stSidebar"] * {
        color: white;
    }
    .footer {
            margin-top: 2rem;
            font-size: 14px;
            color: gray;
            text-align: center;
        }
    .stAppToolbar {
    background-color: #020557;
    color: white;
}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <style>
      /* Force the divider to be pure white */
    .divider {
        width: 60%;
        height: 2px;
        background-color: white;
        margin: 10px 0;
        border: none;
    }
 .highlighted-text-home-blue {
            background: linear-gradient(to top, #020557 25%, transparent 50%);
            color: white;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
        }
 .highlighted-text-home-red {
            background: linear-gradient(to top, #EF3340 20%, transparent 50%);
        }
 .highlighted-text-home-green {
            background: linear-gradient(to top, #54AD18 20%, transparent 50%);
        }

 .highlighted-text-home-yellow {
            background: linear-gradient(to top, #D7B00D 20%, transparent 50%);
        }
 .highlighted-text-home-orange {
            background: linear-gradient(to top, #3C918F 20%, transparent 50%);
        }
.highlighted-text-home-lblue {
            background: linear-gradient(to top, #00ACED 20%, transparent 50%);
        } 
    .rounded-box {
        background-color: #0054A8;
        border-radius: 20px;
        font-weight: bold;
        letter-spacing: 0.1em; 
        padding: 0;
        box-shadow: 0px 0px 25px -9px rgba(0, 0, 0, .9);
        height: 190px;
        display: flex;
        align-items: center;
        justify-content: left;
        color: white;
        font-size: 20px;
        margin-top: 20px;
        transition: transform 0.3s ease;
        overflow: hidden;
            Width:100%;
    }
    .rounded-box:hover {cursor: POINTER;
        transform: translateY(-8px);
        box-shadow: 0px 0px 50px 0px rgb(0 94 184 / 40%); /* cyan-blue glow */

    }
    .accent-strip-blue {
        width: 19px;
        background-color: #00ACED;
        height: 100%;
    }
     .accent-strip-red {
        width: 19px;
        background-color: #EF3340;
        height: 100%;
    }
     .accent-strip-green {
        width: 19px;
        background-color: #54AD18;
        height: 100%;
    }
    .box-content {
        padding: 30px;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .app-button {
        background-color: white;
        letter-spacing: 0em; 
        color: #1E90FF;
        padding: 4px 10px;
        border-radius: 50px;
        font-weight: 600;
        font-size: 13px;
        border: none;
        cursor: pointer;
        text-decoration: none;
        margin-top: 10px;
    }
    .white-layer {
    background-color: #00ACED;
    flex-grow: 1;
    height: 50%;
   
    display: flex;
    flex-direction: column;
    align-items: center;
}

    .app-button:hover {
        background-color: #f0f0f0;
    }
    </style>
""", unsafe_allow_html=True)



# First row
left, col1, col2, col3, right = st.columns([1, 2, 2, 2, 1])


with col1:
    st.markdown("""
        <div class="rounded-box">
            <div class="box-content">
                <span class="highlighted-text-home-yellow">RUBIX CATALOG</span>
                <div class="divider"></div>
                <a href="https://rubixcatalog.apps.eu-1c.mendixcloud.com/" class="app-button" target="_blank">OPEN</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="rounded-box">
            <div class="box-content">
                <span class="highlighted-text-home-blue">CIP CONTROL TOWER</span>
                <div class="divider"></div>
                <a href="/Scanner" class="app-button" target="_self">OPEN</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="rounded-box">
            <div class="box-content">
            <span class="highlighted-text-home-green">SCANNER</span>
                <div class="divider"></div>
                <a href="https://sbrx-log.streamlit.app/Scanner" class="app-button" target="_self">OPEN</a>
            </div>
        </div>
    """, unsafe_allow_html=True)



# Second row
left, col4, col5, col6, right = st.columns([1, 2, 2, 2, 1])

with col4:
    st.markdown("""
        <div class="rounded-box">
            <div class="accent-strip"></div>
            <div class="box-content">
            <span class="highlighted-text-home-red">App X</span>
                <div class="divider"></div>
                <a href="/Reports" class="app-button" target="_self">Open</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
        <div class="rounded-box">
            <div class="accent-strip"></div>
            <div class="box-content">
            <span class="highlighted-text-home-orange">App Y</span>
                <div class="divider"></div>
                <a href="/Settings" class="app-button" target="_self">Open</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
        <div class="rounded-box">
            <div class="accent-strip"></div>
            <div class="box-content">
            <span class="highlighted-text-home-lblue">App Z</span>
                <div class="divider"></div>
                <a href="/Help" class="app-button" target="_self">Open</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

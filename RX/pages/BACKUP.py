import streamlit as st
from PIL import Image


st.html(
'''<div class="productContainer">
        <div class="card">
            <div class="header" style="height: 17rem;"> <img src="images/CortexLogo.png" alt="Product" /> </div>
            <div class="footer">
                <div class="title">
                    <h2>CORTEX</h2>
                </div>
                <p>Data Connectivity</p> <button class="buyNow"  onclick="window.location.href='CORTEX.html'">OPEN</button>
            </div>
        </div>
        <div class="card">
            <div class="header" style="height: 17rem;"> <img src="images/Rubix.png" alt="Rubix"> </div>
            <div class="footer">
                <div class="title">
                    <h2>RUBIX</h2>
                </div>
                <p>Data Modeling</p> <button class="buyNow" onclick="window.location.href='RUBIX.html'">OPEN</button>
            </div>
        </div>
            </div>
            <script src="navscript.js" defer></script>'''
)




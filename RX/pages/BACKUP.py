import streamlit as st
from PIL import Image


st.html(
"<body>
  
    <nav  class="sidebar locked">
        <div class="logo_items flex">
          <span class="nav_image">
            <img src="images/rc.png" alt="logo_img" />
          </span>
          <span class="logo_name">CORTEX-RUBIX</span>
          <i class="bx bx-lock-alt" id="lock-icon" title="Unlock Sidebar"></i>
          <i class="bx bx-x" id="sidebar-close"></i>
        </div>
  
        <div class="menu_container">
          <div class="menu_items">
            
  
            <ul class="menu_item">
              <div class="menu_title flex">
                <span class="title">Setting</span>
                <span class="line"></span>
              </div>
              <li class="item">
                <a href="home.html" class="link flex">
                  <i class="bx bx-home"></i>
                  <span>Home</span>
                </a>
              </li>
              <li class="item">
                <a href="ipconfiguration.html" class="link flex">
                  <i class="bx bx-cog"></i>
                  <span>IP Configuration</span>
                </a>
              </li>
              
              
            </ul>
          </div>
  
         
        </div>
      </nav> 
  


    <div class="productContainer">
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
            <script src="navscript.js" defer></script>
</body>"
    
)

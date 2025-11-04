import streamlit as st
from PIL import Image
st.markdown(
    """
<style>
   body {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #fff;
}


.productContainer {
    margin-left: 270px; /* Adjust to fit sidebar width */
    padding: 2rem;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    width: calc(100% - 270px);
    transition: margin-left 0.3s, width 0.3s;
}

.card {
    height: auto;
    overflow: hidden;
    max-width: 22rem;
    border-radius: 1rem;
    margin: 1rem 2rem;
    font-family: 'Poppins', sans-serif;
    transition: transform 0.5s, box-shadow 0.5s;
    box-shadow: 0px 0px 20px 1px rgb(204 204 204 / 50%);
}

.card:hover {
    transform: translateY(-15px);
    box-shadow: 0px 10px 20px 0px rgb(204 204 204 / 50%);
}

.card .header {
    z-index: 2;
    display: flex;
    position: relative;
    align-items: center;
    justify-content: center;
    background-color: #ff0;
    border-radius: 0rem 0rem 4rem 0rem;
}

.card .header::before {
    content: "";
    top: 0;
    left: 0;
    z-index: -1;
    width: 100%;
    height: 100%;
    position: absolute;
    border-radius: 0rem 0rem 4rem 0rem;
}

.card .header img {
    width: 100%;
}

.card .footer {
    z-index: 2;
    text-align: center;
    position: relative;
    padding: 20px 20px 20px 20px;
}

.card .footer::before {
    content: "";
    top: 0;
    left: 0;
    width: 100%;
    z-index: -1;
    height: 100%;
    position: absolute;
    background-color: #fff;
    border-radius: 3rem 0rem 0rem 0rem;
}

.card .footer .title {
    font-size: 1.4rem;
    margin-bottom: .4rem;
}

.card .footer p {
    font-size: .8rem;
}

.productContainer .card:nth-child(2) .header img {
    width: 120%;
}

.productContainer .card:nth-child(3) .header img {
    width: 120%;
}

.productContainer .card:nth-child(1) .header::before {
    background-image: linear-gradient(to right, #0069B3, #2EA1F2);
}

.productContainer .card:nth-child(1) .footer {
    background: #0069B3;
}

.productContainer .card:nth-child(2) .header::before {
    background-image: linear-gradient(to bottom, #01408f, #011842);
}

.productContainer .card:nth-child(2) .footer {
    background: #173f5f;
}

.productContainer .card:nth-child(3) .header::before {
    background-image: linear-gradient(to bottom, #e93632, #501823);
}

.productContainer .card:nth-child(3) .footer {
    background: #501823;
}

.buyNow {
    cursor: pointer;
    margin-top: 1rem;
    font-size: 1rem;
    border-radius: 5rem;
    padding: .6rem 2rem;
    background-color: #fff;
    transition: all .2s ease-in-out;
}

.productContainer .card:nth-child(1) .buyNow {
    color: #2f354d;
    border: 2px solid #2f354d;
}

.productContainer .card:nth-child(1) .buyNow:hover {
    color: #fff;
    background-color: #2f354d;
}

.productContainer .card:nth-child(2) .buyNow {
    color: #01408f;
    border: 2px solid #01408f;
}

.productContainer .card:nth-child(2) .buyNow:hover {
    color: #fff;
    background-color: #01408f;
}

.productContainer .card:nth-child(3) .buyNow {
    color: #e93632;
    border: 2px solid #e93632;
}

.productContainer .card:nth-child(3) .buyNow:hover {
    color: #fff;
    background-color: #e93632;
}

</style>
""",
    unsafe_allow_html=True,
)

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html



)

st.html(
''' <div class="productContainer">
        <div class="card">
            <div class="header" style="height: 17rem;"> <img src="https://sbtest.streamlit.app/~/+/media/6540bd9addaf2a79cbd1c6a9f0885046c84ef1e8accd4bfe736792ca.png" alt="Product" /> </div>
            <div class="footer">
                <div class="title">
                    <h2>CORTEX</h2>
                </div>
                <p>Data Connectivity</p> <button class="buyNow"  onclick="window.location.href='CORTEX.html'">OPEN</button>
            </div>
        </div>
        <div class="card">
            <div class="header" style="height: 17rem;"> <img src="https://sbtest.streamlit.app/~/+/media/0b958445cb867b9f3676582e967963fab2aa77bb7af65f841114b7b6.png" alt="Rubix"> </div>
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





















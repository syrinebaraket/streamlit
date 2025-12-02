import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pandas as pd
import qrcode
from io import BytesIO
import barcode
from barcode.writer import ImageWriter
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
    
    .stAppToolbar {
    background-color: #020557;
    color: white;
}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
        body {
            background-color: #F2F5F8; /* Solid green */
        }
        .stApp {
            background-color: #F2F5F8; /* Streamlit app wrapper */
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("""
    <style>
        .st-key-boxC , .st-key-boxLiveQR, .st-key-boxCC,.st-key-boxCB{  
            MARGIN-top:10px;
        padding: 27px;
        width:100%;
        border-radius: 12px;
        box-shadow: 0px 0px 16px -6px rgba(0, 0, 0, .7);
        background-color: white;}
         .footer {
            margin-top: 2rem;
            font-size: 14px;
            color: gray;
            text-align: center;
        }

    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="SAP QR & Barcode App", layout="wide")

# --- Split into two main columns ---
col_gen, col_scan = st.columns(2)

# ---------------- QR GENERATION (LEFT COLUMN) ----------------
with col_gen:
    st.markdown("""
    <style>
         button[kind="secondary"] {
        background-color: #669ED4 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 6px;
    }
        .header {
            background-color: #0054A8;
            border-radius: 10px;
            padding: 0.8rem;
            color: white;
            font-size: 18px;
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
    <div class="header"> <span class="highlighted-text">Bar/QR Code Generator</span></div>
""", unsafe_allow_html=True)
    with st.container(key="boxC"):
    # --- Expanded Production Order Inputs ---
     order_id = st.text_input("Production Order Number", "100001682")
     order_date = st.date_input("Date of Production Order", value=pd.to_datetime("2011-02-22"))
     material = st.text_input("Material", "2297")
     dlc = st.date_input("DLC", value=pd.to_datetime("2011-04-23"))
     storage_location = st.text_input("Storage Location", "2002")
     r3_status = st.text_input("R3 Status", "U")
     initial_batch = st.text_input("Initial Batch Number", "2011.04.23")
     process_batch = st.text_input("Process Batch Number", "")
     work_center = st.text_input("Work Center", "LMOCDFLA - Ligne 01 FLAN-TF")
     production_area = st.text_input("Production Area", "FABD - Area de production Dessert")
     quality_status = st.text_input("Quality Status", "U")
     default_quantity = st.number_input("Default Quantity", min_value=0, value=180)
     rtp_code = st.text_input("RTP Code", "10138209")

    # --- Two buttons side by side ---
     col1, col2 = st.columns(2)

    # --- QR Code Generation ---
     with col1:
        if st.button("Generate QR Code", type="secondary", use_container_width=True):
            sap_order = (
                f"Order:{order_id}|Date:{order_date}|Material:{material}|DLC:{dlc}|Storage:{storage_location}|"
                f"R3:{r3_status}|BatchInit:{initial_batch}|BatchProc:{process_batch}|WorkCenter:{work_center}|"
                f"Area:{production_area}|Quality:{quality_status}|Quantity:{default_quantity}|RTP:{rtp_code}"
            )

            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(sap_order)
            qr.make(fit=True)
            img_qr = qr.make_image(fill_color="black", back_color="white")
            img = img_qr.convert("RGB")

            st.image(img, caption="Generated SAP QR Code", use_container_width=True)

            buf = BytesIO()
            img.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.download_button(
                label="⬇️ Download QR Code",
                data=byte_im,
                file_name="sap_order_qr.png",
                mime="image/png"
            )

    # --- Barcode Generation ---
     with col2:
        if st.button("Generate Barcode", type="secondary", use_container_width=True):
            sap_order = (
                f"Order:{order_id}|Date:{order_date}|Material:{material}|DLC:{dlc}|Storage:{storage_location}|"
                f"R3:{r3_status}|BatchInit:{initial_batch}|BatchProc:{process_batch}|WorkCenter:{work_center}|"
                f"Area:{production_area}|Quality:{quality_status}|Quantity:{default_quantity}|RTP:{rtp_code}"
            )

            BARCODE = barcode.get_barcode_class("code128")
            bar = BARCODE(sap_order, writer=ImageWriter())

            buf = BytesIO()
            bar.write(buf)
            buf.seek(0)

            img_bar = Image.open(buf)
            st.image(img_bar, caption="Generated Barcode", use_container_width=True)

            st.download_button(
                label="⬇️ Download Barcode",
                data=buf.getvalue(),
                file_name="barcode.png",
                mime="image/png"
            )

# ---------------- QR SCANNING (RIGHT COLUMN, TOP ROW) ----------------
with col_scan:
    st.markdown("""
    <style>
        .header {
            background-color: #0054A8;
            border-radius: 10px;
            padding: 0.8rem;
            color: white;
            font-size: 18px;
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
    <div class="header"> <span class="highlighted-text">QR Code</span>Reader</div>
""", unsafe_allow_html=True)
    with st.container(key="boxCC"):
     if "orders" not in st.session_state:
        st.session_state["orders"] = []

     uploaded_file = st.file_uploader("Upload a QR code image", type=["png", "jpg", "jpeg"], key="qr_upload")

     if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded QR", use_container_width=True)

        img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        qr_detector = cv2.QRCodeDetector()
        data, points, _ = qr_detector.detectAndDecode(img_cv)

        if data:
            st.success(f"Scanned QR Data: {data}")
            parts = data.split("|")
            order_info = {}
            for p in parts:
                if ":" in p:
                    key, val = p.split(":", 1)
                    order_info[key.strip()] = val.strip()
                else:
                    order_info["OrderID"] = p
            st.session_state["orders"].append(order_info)
        else:
            st.warning("No QR code detected.")

     if st.session_state["orders"]:
        df = pd.DataFrame(st.session_state["orders"])
        st.dataframe(df)

        total_orders = len(df)
        total_quantity = df["Quantity"].astype(int).sum() if "Quantity" in df.columns else 0

      

        

# ---------------- BARCODE READER (RIGHT COLUMN, BOTTOM ROW) ----------------

with col_scan:
    st.markdown("""
    <style>
        .header {
            background-color: #0054A8;
            border-radius: 10px;
            padding: 0.8rem;
            color: white;
            font-size: 18px;
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
    <div class="header"> <span class="highlighted-text">Bar Code</span>Reader</div>
""", unsafe_allow_html=True)
    with st.container(key="boxCB"):
      
     uploaded_barcode = st.file_uploader("Upload a Barcode image", type=["png", "jpg", "jpeg"], key="barcode_upload")

     if uploaded_barcode:
        image = Image.open(uploaded_barcode)
        st.image(image, caption="Uploaded Barcode", use_container_width=True)

        # Convert to OpenCV format
        img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Use OpenCV's BarcodeDetector
        barcode_detector = cv2.barcode_BarcodeDetector()
        ok, decoded_info, decoded_type = barcode_detector.detectAndDecode(img_cv)

        if ok and decoded_info:
            for i, info in enumerate(decoded_info):
                st.success(f"Scanned Barcode Data: {info}")
                st.write(f"Type: {decoded_type[i]}")
        else:

            st.warning("No barcode detected.")


# ---------------- LIVE QR SCANNER (THIRD ROW) ----------------
with col_scan:
 st.markdown("""
    <style>
        .header {
            background-color: #0054A8;
            border-radius: 10px;
            padding: 0.8rem;
            color: white;
            font-size: 18px;
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
    <div class="header"> <span class="highlighted-text">Live QR</span> Scanner</div>
""", unsafe_allow_html=True)



 with st.container(key="boxLiveQR"):
    st.write("📷 Use your webcam to scan QR codes (local run only).")

    if "orders" not in st.session_state:
         st.session_state["orders"] = []
    start_scan = st.button("Start Live Scan")

    if start_scan:
        cap = cv2.VideoCapture(0)
        qr_detector = cv2.QRCodeDetector()
        stframe = st.empty()
        with st.spinner("🔍 Scanning for QR code..."):

         while True:
            ret, frame = cap.read()
            if not ret:
                st.warning("Failed to access webcam.")
                break

            data, points, _ = qr_detector.detectAndDecode(frame)
            stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

            if data:
                st.success(f"Scanned QR Data: {data}")
                parts = data.split("|")
                order_info = {}
                for p in parts:
                    if ":" in p:
                        key, val = p.split(":", 1)
                        order_info[key.strip()] = val.strip()
                    else:
                        order_info["OrderID"] = p
                st.session_state["orders"].append(order_info)
                break

        cap.release()

    # Show table if we have orders
    if st.session_state["orders"]:
        df = pd.DataFrame(st.session_state["orders"])
        st.dataframe(df)

        total_orders = len(df)
        total_quantity = df["Quantity"].astype(int).sum() if "Quantity" in df.columns else 0

        st.info(f"Total Orders: {total_orders} | Total Quantity: {total_quantity}")



 with st.container(key="boxLiveQRg"):
      uploaded_photo = st.camera_input("Take a picture of QR")
      if uploaded_photo:
         image = Image.open(uploaded_photo)
         img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
         qr_detector = cv2.QRCodeDetector()
         data, points, _ = qr_detector.detectAndDecode(img_cv)
         if data:
            st.success(f"Scanned QR Data: {data}")








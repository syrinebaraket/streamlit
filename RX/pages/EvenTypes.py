import streamlit as st
import pandas as pd
import os

# --- File Path ---
EVENT_FILE = "RX/files/event_definitions.csv"
# --- Custom CSS ---
st.markdown("""
    <style>
    
    button[kind="secondary"] {
        background-color: blue !important;
        color: white !important;
        font-weight: bold;
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

# --- Load Existing Events ---
if os.path.exists(EVENT_FILE):
    event_df = pd.read_csv(EVENT_FILE)
else:
    event_df = pd.DataFrame(columns=["EventType", "Version", "Equipment", "Parameters", "Expression"])

# --- Session State ---
if "show_add_form" not in st.session_state:
    st.session_state.show_add_form = False

st.markdown("###  Defined Event Types")

# --- Button Row ---
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    if st.button("Add",type="secondary",width="stretch"):
        st.session_state.show_add_form = True
with col2:
    st.button("Edit",width="stretch")  # Placeholder
with col3:
    st.button("Delete",width="stretch")  # Placeholder
with col4:
    st.button("Select All",width="stretch")  # Placeholder

# --- Display Table ---
st.dataframe(event_df, use_container_width=True)



# --- Add Form ---
if st.session_state.show_add_form:
    st.markdown("### Add New Event Type")

    new_event_type = st.text_input("Event Type Name")
    version = st.text_input("Version")

    metrics_df = pd.read_csv("RX/files/metrics.csv", parse_dates=["Timestamp"])
    available_equipment = sorted(metrics_df['Equipment'].unique())
    selected_equipment = st.multiselect("Select Equipment", available_equipment)

    filtered_metrics = metrics_df[metrics_df['Equipment'].isin(selected_equipment)]
    all_params = [col for col in filtered_metrics.columns if col not in ['Timestamp', 'Site', 'Area', 'AreaID', 'Cell', 'CellID', 'Equipment']]
    selected_params = st.multiselect("Select Parameters", all_params)

    expression = st.text_area("Trigger Expression (Python-like)", height=150, placeholder="e.g., Temperature > 80 and Vibration < 5")

    if st.button("Save"):
        if new_event_type and version:
            new_row = pd.DataFrame([{
                "EventType": new_event_type,
                "Version": version,
                "Equipment": ";".join(selected_equipment),
                "Parameters": ";".join(selected_params),
                "Expression": expression
            }])
            event_df = pd.concat([event_df, new_row], ignore_index=True)
            event_df.to_csv(EVENT_FILE, index=False)
            st.success("Event Type saved successfully!")
            st.session_state.show_add_form = False
        else:

            st.error("Please enter both Event Type and Version.")





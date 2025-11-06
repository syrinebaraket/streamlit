import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime


# Set custom background color
st.markdown(
    """
    <style>
        element.style {
            background-color: #FAFBFC;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.set_page_config(layout="wide") 
# --- Load Data ---
events_df = pd.read_csv("RX/files/events.csv", parse_dates=["StartTime", "EndTime"])
metrics_df = pd.read_csv("RX/files/metrics.csv", parse_dates=["Timestamp"])

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
         .highlighted-text {
            background-color: #00ACED;
            color: white;
            padding: 0.2rem 0.5rem;
            border-radius: 0px;
        }


    </style>
    <div class="header"> <span class="highlighted-text">Events</span></div>
""", unsafe_allow_html=True)

# --- Sidebar Filters ---
st.sidebar.header("Filters")
selected_site = st.sidebar.selectbox("Site", events_df['Site'].unique())
filtered_area = events_df[events_df['Site'] == selected_site]
selected_area = st.sidebar.selectbox("Area", filtered_area['Area'].unique())
filtered_area_id = filtered_area[filtered_area['Area'] == selected_area]
selected_area_id = st.sidebar.selectbox("Area ID", filtered_area_id['AreaID'].unique())
filtered_cell = filtered_area_id[filtered_area_id['AreaID'] == selected_area_id]
selected_cell = st.sidebar.selectbox("Cell", filtered_cell['Cell'].unique())
selected_cell_id = st.sidebar.selectbox("Cell ID", filtered_cell['CellID'].unique())
available_equipment = filtered_cell['Equipment'].unique()
selected_equipment = st.sidebar.multiselect("Equipment", available_equipment, default=available_equipment)
available_statuses = sorted(events_df['EventType'].unique())
selected_statuses = st.sidebar.multiselect("Status Types", available_statuses, default=available_statuses)
st.markdown("""
    <style>
        .st-key-boxC , .st-key-boxCC, .st-key-boxCP, .st-key-container{  
        padding: 27px;
        width:100%;
        border-radius: 8px;
        box-shadow: 0px 0px 16px -6px rgba(0, 0, 0, .7);
        background-color: white;}

    </style>
""", unsafe_allow_html=True)

# --- Parameter Selection ---
all_params = [col for col in metrics_df.columns if col not in ['Timestamp', 'Site', 'Area', 'AreaID', 'Cell', 'CellID', 'Equipment']]
# Add more mock parameters if needed
for param in ['Flowrate', 'Pressure', 'Vibration']:
    if param not in all_params:
        metrics_df[param] = pd.Series([None] * len(metrics_df))  # placeholder
        all_params.append(param)

selected_params = st.sidebar.multiselect("Parameters to Plot", all_params, default=['Temperature', 'Energy'])
# --- Date-Time Filter ---
with st.container(key="boxC"):
    st.subheader("Select Time Range")
    col1, col2 = st.columns(2)
    with col1:
        start_dt = st.date_input("Start Date", value=events_df['StartTime'].min().date())
        start_time = st.time_input("Start Time", value=datetime.min.time())
    with col2:
        end_dt = st.date_input("End Date", value=events_df['EndTime'].max().date())
        end_time = st.time_input("End Time", value=datetime.max.time())
        start_datetime = datetime.combine(start_dt, start_time)
        end_datetime = datetime.combine(end_dt, end_time)

# --- Filtered Data ---
filtered_events = events_df[
    (events_df['Site'] == selected_site) &
    (events_df['Area'] == selected_area) &
    (events_df['AreaID'] == selected_area_id) &
    (events_df['Cell'] == selected_cell) &
    (events_df['CellID'] == selected_cell_id) &
    (events_df['Equipment'].isin(selected_equipment)) &
    (events_df['EventType'].isin(selected_statuses)) &
    (events_df['StartTime'] <= end_datetime) &
    (events_df['EndTime'] >= start_datetime)
]

filtered_metrics = metrics_df[
    (metrics_df['Site'] == selected_site) &
    (metrics_df['Area'] == selected_area) &
    (metrics_df['AreaID'] == selected_area_id) &
    (metrics_df['Cell'] == selected_cell) &
    (metrics_df['CellID'] == selected_cell_id)&
    (metrics_df['Equipment'].isin(selected_equipment))&
    (metrics_df['Timestamp'] <= end_datetime) &
    (metrics_df['Timestamp'] >= start_datetime)
]


# --- Main Content ---

st.markdown(f"**Site:** `{selected_site}` /  `{selected_area}` /  `{selected_area_id}` /  `{selected_cell}` / `{selected_cell_id}` / `{selected_equipment}`")


# --- Event Table Filter ---
st.subheader("Event List")
event_filter_equipment = st.multiselect("Filter Events by Equipment", filtered_events['Equipment'].unique(), default=filtered_events['Equipment'].unique())
event_filter_type = st.multiselect("Filter Events by Type", filtered_events['EventType'].unique(), default=filtered_events['EventType'].unique())

filtered_event_table = filtered_events[
    (filtered_events['Equipment'].isin(event_filter_equipment)) &
    (filtered_events['EventType'].isin(event_filter_type))
]

st.dataframe(filtered_event_table[['EventType', 'Equipment', 'StartTime', 'EndTime']].sort_values('StartTime'), use_container_width=True)

# --- Status Chart ---
st.subheader("Status Timeline")
status_map = {'Started': 1, 'Stopped': 0, 'Idle': 0.5}
status_points = []

for _, row in filtered_event_table.iterrows():
    status = status_map.get(row['EventType'], None)
    if status is not None:
        status_points.append({
            'Timestamp': row['StartTime'],
            'Status': status,
            'Equipment': row['Equipment']
        })
        status_points.append({
            'Timestamp': row['EndTime'],
            'Status': status,
            'Equipment': row['Equipment']
        })

status_df = pd.DataFrame(status_points).dropna()
fig_status = px.line(
    status_df,
    x='Timestamp',
    y='Status',
    color='Equipment',
    line_shape='hv',
    title='Equipment Status Over Time',
    color_discrete_sequence=['#13B1EE'] * len(status_df['Equipment'].unique())
)


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
            transition:transform 0.9s;
        }
    </style>
""", unsafe_allow_html=True)

# First row
with st.container(key="boxCC"):
    st.plotly_chart(fig_status, use_container_width=True)
   


color_palettes = {
    'Temperature': ['#FF5733', '#D68910', '#900C3F'],
    'Energy': [ '#1B4F72', '#28B463', '#1D8348'],
    'Flowrate': ['#3357FF', '#2E86C1', '#1B4F72'],
    'Pressure': ['#F39C12', '#D68910', '#B9770E'],
    'Vibration': ['#8E44AD', '#6C3483', '#512E5F']
}

# --- Parameter Charts ---
container2 = st.container(key="container")

st.markdown("""
    <style>
    .plot-border {
        border: 2px solid black;
        padding: 5px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

if filtered_metrics.empty:
    st.warning("No metrics found for the selected filters and time range.")
else:
    for i in range(0, len(selected_params), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(selected_params):
                param = selected_params[i + j]
                fig = px.line(
                    filtered_metrics,
                    x='Timestamp',
                    y=param,
                    color='Equipment',
                    title=f'{param} Over Time',
                    markers=True,
                    color_discrete_sequence=color_palettes.get(param, px.colors.qualitative.Plotly))
                with cols[j]:
                    st.markdown('<div class="plot-border">', unsafe_allow_html=True)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                






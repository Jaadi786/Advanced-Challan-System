import streamlit as st

def init_state():
    defaults = {
        "events": [], "detections": [], "violations": [],
        "last_analysis": None, "live_source": "Demo Stream", "system_mode": "DEMO"
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

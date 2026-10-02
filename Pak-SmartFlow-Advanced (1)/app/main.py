import streamlit as st
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.state import init_state
from core.engine import SmartFlowEngine
from ui.theme import inject_theme
from ui.dashboard import render_dashboard
from ui.live_monitor import render_live_monitor
from ui.video_analysis import render_video_analysis
from ui.agent_flow import render_agent_flow
from ui.compliance import render_compliance
from ui.analytics import render_analytics

st.set_page_config(page_title="Pak-SmartFlow | AI Traffic Intelligence", page_icon="🚦", layout="wide")
init_state()
inject_theme()

if "engine" not in st.session_state:
    st.session_state.engine = SmartFlowEngine()

with st.sidebar:
    st.markdown('''
    <div class="brand">
      <div class="brand-mark">⚡</div>
      <div><div class="brand-title">PAK-SMARTFLOW</div>
      <div class="brand-sub">AI TRAFFIC INTELLIGENCE</div></div>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("COMMAND NAVIGATION", [
        "◈ Command Center", "◉ Live Intelligence", "▶ Video Forensics",
        "◇ Agent Orchestration", "▣ Compliance", "◫ Analytics"
    ])
    st.markdown("---")
    st.markdown('<div class="system-status"><span class="pulse"></span> SYSTEM ONLINE</div>', unsafe_allow_html=True)
    st.caption("Advanced Demo Build • Model adapters replaceable")

if page == "◈ Command Center":
    render_dashboard()
elif page == "◉ Live Intelligence":
    render_live_monitor()
elif page == "▶ Video Forensics":
    render_video_analysis()
elif page == "◇ Agent Orchestration":
    render_agent_flow()
elif page == "▣ Compliance":
    render_compliance()
else:
    render_analytics()

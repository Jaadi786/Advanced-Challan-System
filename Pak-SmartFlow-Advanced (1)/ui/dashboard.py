import streamlit as st
from ui.theme import hero, metric

def render_dashboard():
    hero("Traffic Intelligence Command Center","Unified situational awareness across detection, evidence, risk, compliance and review workflows.")
    st.write("")
    cols=st.columns(5)
    vals=[
        ("ACTIVE CAMERAS","12","● NETWORK READY"),
        ("VEHICLES TRACKED","1,842","+8.4% / 24H"),
        ("CASES IN REVIEW","37","HUMAN REVIEW"),
        ("RISK EVENTS","19","LIVE SIGNAL"),
        ("RECOVERY PIPELINE","Rs. 2.8M","TRACKED VALUE")
    ]
    for c,(a,b,d) in zip(cols,vals):
        with c: metric(a,b,d)
    st.write("")
    left,right=st.columns([2.1,1])
    with left:
        st.markdown('<div class="card">',unsafe_allow_html=True)
        st.markdown("### ◉ Live Situation Grid")
        st.markdown('<div class="feed"><div class="feed-head"><span>CAM-01 • MAIN CORRIDOR</span><span class="live">● LIVE</span></div><div class="feed-body">LIVE STREAM ADAPTER READY<br>RTSP / HTTP / UPLOADED VIDEO</div></div>',unsafe_allow_html=True)
        st.write("")
        st.markdown('<span class="tag">YOLO ADAPTER</span><span class="tag">ANPR</span><span class="tag">EVIDENCE</span><span class="tag">20-AGENT</span>',unsafe_allow_html=True)
        st.markdown('</div>',unsafe_allow_html=True)
    with right:
        st.markdown('<div class="card">',unsafe_allow_html=True)
        st.markdown("### ⚠ Priority Queue")
        for risk,cam,msg in [("HIGH","CAM-03","Potential wrong-way event"),("HIGH","CAM-07","Pedestrian conflict"),("MED","CAM-02","Helmet evidence pending"),("MED","CAM-09","Plate confidence low")]:
            cls="risk-high" if risk=="HIGH" else "risk-medium"
            st.markdown(f'<div style="padding:10px 0;border-bottom:1px solid #1d2b3d"><b class="{cls}">{risk}</b> &nbsp; {cam}<br><small style="color:#8090a6">{msg}</small></div>',unsafe_allow_html=True)
        st.markdown('</div>',unsafe_allow_html=True)

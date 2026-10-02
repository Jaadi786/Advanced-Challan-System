import streamlit as st
from ui.theme import hero

def render_live_monitor():
    hero("Live Intelligence Grid","Multi-camera operational view with model-ready stream adapters.")
    a,b,c=st.columns(3)
    with a: st.selectbox("SOURCE",["Demo Stream","Local Video","RTSP / HTTP Stream"])
    with b: st.selectbox("PROCESSING PROFILE",["Balanced","Low Latency","High Accuracy"])
    with c: st.selectbox("EVIDENCE POLICY",["Review First","Auto-Queue","Evidence Strict"])
    st.write("")
    cols=st.columns(3)
    for i,col in enumerate(cols,1):
        with col:
            st.markdown(f'<div class="feed"><div class="feed-head"><b>CAM-{i:02d}</b><span class="live"><span class="pulse"></span>LIVE</span></div><div class="feed-body">STREAM {i}<br><small>Connect RTSP/HTTP to activate frames</small></div></div>',unsafe_allow_html=True)
    st.write("")
    st.markdown("### Detection Telemetry")
    a,b,c,d=st.columns(4)
    a.metric("Objects / sec","18.6"); b.metric("Inference","42 ms"); c.metric("Track IDs","31"); d.metric("Evidence Queue","06")
    st.markdown("### Active Signals")
    for title,detail in [("Vehicle Detection","18 tracked objects"),("ANPR","Plate OCR adapter"),("Safety","Helmet / seatbelt adapter"),("Risk Engine","Rule + ML fusion"),("Human Review","Case queue")]:
        st.markdown(f'<div class="agent"><span class="agent-id">PIPELINE</span><span class="agent-name">{title}</span><span class="agent-ok">READY</span><div class="agent-detail">{detail}</div></div>',unsafe_allow_html=True)

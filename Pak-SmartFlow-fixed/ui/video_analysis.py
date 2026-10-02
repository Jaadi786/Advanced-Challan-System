import streamlit as st
import tempfile
from pathlib import Path
from ui.theme import hero

def render_video_analysis():
    hero("Video Forensics Lab","Upload evidence, run the normalized pipeline, inspect events, and preserve an auditable case trail.")
    uploaded=st.file_uploader("DROP VIDEO EVIDENCE",type=["mp4","avi","mov","mkv"])
    a,b,c,d=st.columns(4)
    with a: frame_skip=st.slider("FRAME SKIP",1,15,5)
    with b: confidence=st.slider("CONFIDENCE",0.1,1.0,0.5)
    with c: generate=st.checkbox("QUEUE CHALLAN",True)
    with d: notify=st.checkbox("QUEUE NOTIFICATION",True)
    if uploaded:
        st.video(uploaded)
        if st.button("🚀 RUN FORENSIC PIPELINE",use_container_width=True):
            with tempfile.NamedTemporaryFile(delete=False,suffix=Path(uploaded.name).suffix) as f:
                f.write(uploaded.getbuffer()); path=f.name
            progress=st.progress(0); status=st.empty()
            try:
                def update(cur,total):
                    progress.progress(min(cur/total,1.0) if total else 0)
                    status.caption(f"Processing frame {cur:,} / {total:,}" if total else f"Processing frame {cur:,}")
                result=st.session_state.engine.analyze_video(path,frame_skip,confidence,update)
                st.session_state.last_analysis=result
                st.session_state.violations=result["events"]
                st.success("Pipeline complete. Results are marked according to the active model adapter.")
                a,b,c,d=st.columns(4)
                a.metric("Frames",result["frames_total"]); b.metric("Processed",result["frames_processed"]); c.metric("Duration",f'{result["duration_sec"]}s'); d.metric("Events",len(result["events"]))
                st.markdown("### Evidence Events")
                if not result["events"]: st.info("No normalized events were produced.")
                for event in result["events"][:30]:
                    with st.expander(f'{event["timestamp"]} • {event["plate"]} • {event["violation"]}'):
                        st.json(event)
                        if generate: st.caption("Challan action queued for review; no external enforcement is executed by this demo.")
                        if notify: st.caption("Notification queued as a workflow event.")
            except Exception as e:
                st.error(str(e))
            finally:
                Path(path).unlink(missing_ok=True)
    else:
        st.info("Upload a traffic video to activate the forensic pipeline.")

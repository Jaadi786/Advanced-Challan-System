import streamlit as st
from ui.theme import hero

def render_compliance():
    hero("Compliance Intelligence","Case history, outstanding exposure and review workflows — without automatic irreversible enforcement.")
    ref=st.text_input("Citizen / Vehicle Reference",placeholder="Enter authorized reference")
    if st.button("🔍 LOAD CASE",use_container_width=True):
        data={"reference":ref or "DEMO-REFERENCE","unpaid":8,"outstanding":18500,"oldest":127,"notices":3,"attempts":0,"score":87}
        a,b,c,d=st.columns(4)
        a.metric("Unpaid Cases",data["unpaid"]); b.metric("Outstanding",f'Rs. {data["outstanding"]:,}'); c.metric("Oldest",f'{data["oldest"]} days'); d.metric("Review Score",f'{data["score"]}/100')
        st.write("")
        st.markdown('<div class="card">',unsafe_allow_html=True)
        st.markdown(f'### Case Reference: `{data["reference"]}`')
        st.warning("Recommended workflow: departmental review. External identity-system or financial actions require authorized integration and approval.")
        x,y=st.columns(2)
        with x: st.button("Prepare Departmental Request",use_container_width=True)
        with y: st.button("Prepare Citizen Notification",use_container_width=True)
        st.markdown('</div>',unsafe_allow_html=True)

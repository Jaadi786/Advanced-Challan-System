import streamlit as st
from ui.theme import hero

def render_agent_flow():
    hero("Agent Orchestration Matrix","A normalized 20-agent architecture with transparent stages, timing hooks and human-review boundaries.")
    left,right=st.columns([1.8,1])
    with left:
        for agent_id,name,purpose in st.session_state.engine.pipeline.AGENTS:
            st.markdown(f'<div class="agent"><span class="agent-id">{agent_id}</span><span class="agent-name">{name}</span><span class="agent-ok">READY</span><div class="agent-detail">{purpose}</div></div>',unsafe_allow_html=True)
    with right:
        st.markdown('<div class="card"><h3>Execution Contract</h3><p><b>Input → Evidence → Intelligence → Decision → Review</b></p><ul><li>Normalized data between stages.</li><li>Structured outputs for UI.</li><li>Sensitive actions remain reviewable.</li><li>LLM reasoning is optional.</li><li>Model adapters are replaceable.</li></ul></div>',unsafe_allow_html=True)
        st.write("")
        st.markdown('<div class="card"><h3>Last Event</h3>',unsafe_allow_html=True)
        if st.session_state.violations: st.json(st.session_state.violations[-1])
        else: st.info("No event in the current session.")
        st.markdown('</div>',unsafe_allow_html=True)

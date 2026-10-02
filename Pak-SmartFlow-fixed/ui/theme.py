import streamlit as st

def inject_theme():
    st.markdown('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600&display=swap');
    :root{--bg:#070b12;--panel:#0d1420;--panel2:#111b2a;--line:#203047;--text:#e9f1fb;--muted:#8090a6;--cyan:#00e5ff;--green:#00e6a7;--amber:#ffc857;--red:#ff5573}
    .stApp{background:radial-gradient(circle at 15% 0%,#102338 0,#070b12 42%);color:var(--text)}
    section[data-testid="stSidebar"]{background:#080d15;border-right:1px solid var(--line)}
    .block-container{max-width:1500px;padding-top:1.5rem}
    .brand{display:flex;gap:12px;align-items:center}.brand-mark{width:42px;height:42px;border-radius:12px;display:grid;place-items:center;background:linear-gradient(135deg,var(--cyan),var(--green));color:#001014;font-size:22px;font-weight:900}.brand-title{font-weight:800;letter-spacing:1.4px;font-size:15px}.brand-sub{color:var(--muted);font-size:9px;letter-spacing:1.6px}
    .hero{border:1px solid var(--line);border-radius:22px;padding:26px;background:linear-gradient(135deg,rgba(17,27,42,.96),rgba(8,14,23,.96));box-shadow:0 20px 70px rgba(0,0,0,.25)}.eyebrow{color:var(--cyan);font-family:'JetBrains Mono';font-size:11px;letter-spacing:2px}.hero h1{margin:5px 0 7px;font-size:35px}.hero p{color:var(--muted);margin:0}
    .card{background:rgba(13,20,32,.92);border:1px solid var(--line);border-radius:18px;padding:18px}.metric{background:linear-gradient(135deg,#0e1826,#0b111b);border:1px solid var(--line);border-radius:16px;padding:17px;min-height:105px}.metric .label{color:var(--muted);text-transform:uppercase;font-size:10px;letter-spacing:1.4px}.metric .value{font-size:27px;font-weight:800;margin-top:8px}.metric .delta{color:var(--green);font-family:'JetBrains Mono';font-size:11px;margin-top:4px}
    .live{color:var(--green);font-family:'JetBrains Mono';font-weight:700;font-size:11px}.pulse{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 14px var(--green);margin-right:7px}.system-status{color:var(--green);font-family:'JetBrains Mono';font-size:10px}
    .feed{border:1px solid #263a52;border-radius:18px;overflow:hidden;background:#05090e}.feed-head{padding:11px 14px;display:flex;justify-content:space-between;border-bottom:1px solid #1b2a3c}.feed-body{min-height:300px;display:grid;place-items:center;text-align:center;color:#53657b;font-family:'JetBrains Mono'}.tag{display:inline-block;border:1px solid #2a415c;border-radius:999px;padding:4px 9px;color:#a8bbd0;font-size:10px;font-family:'JetBrains Mono';margin-right:5px}
    .agent{border:1px solid var(--line);border-radius:14px;padding:13px 15px;margin:7px 0;background:linear-gradient(90deg,#0d1521,#0a111a)}.agent-id{color:var(--cyan);font-family:'JetBrains Mono';font-size:10px}.agent-name{font-weight:700;margin-left:7px}.agent-detail{color:var(--muted);font-size:12px;margin-top:5px}.agent-ok{float:right;color:var(--green);font-family:'JetBrains Mono';font-size:10px}
    .risk-high{color:var(--red)}.risk-medium{color:var(--amber)}
    .stButton>button{border:1px solid #2a4059;border-radius:11px;background:#0d1724;color:#dce8f5}.stButton>button:hover{border-color:var(--cyan);color:white}
    </style>
    ''', unsafe_allow_html=True)

def hero(title, subtitle, eyebrow="PAK-SMARTFLOW / COMMAND SYSTEM"):
    st.markdown(f'<div class="hero"><div class="eyebrow">{eyebrow}</div><h1>{title}</h1><p>{subtitle}</p></div>', unsafe_allow_html=True)

def metric(label, value, delta="SYSTEM"):
    st.markdown(f'<div class="metric"><div class="label">{label}</div><div class="value">{value}</div><div class="delta">{delta}</div></div>', unsafe_allow_html=True)

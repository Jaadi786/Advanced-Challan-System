# 🚦 Pak-SmartFlow — Advanced AI Traffic Intelligence

A modular Streamlit command platform for traffic video intelligence, evidence workflows, multi-agent orchestration, compliance analytics and human-review queues.

## Architecture

Camera / Video
→ Detection
→ Tracking
→ ANPR
→ Safety Signals
→ Evidence
→ Risk
→ 20-Agent Orchestration
→ Reviewable Event
→ Dashboard / Analytics

## Important

The included detector is an explicit **DEMO adapter**. It does not pretend that a real YOLO/ANPR model is running. Replace `core/video_processor.py` with real model adapters while keeping the normalized output contract.

## Run

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/main.py
```

## Production direction

Add real YOLO/ANPR/safety adapters, persistent database storage, authenticated departmental integrations, notification providers, and an accessible RTSP/HTTP/HLS stream gateway.

Sensitive enforcement actions should remain authorized/reviewable workflows rather than automatic irreversible actions.

from dataclasses import asdict
from datetime import datetime
from core.models import Event  # noqa: F401
from core.pipeline import AgentPipeline
from core.video_processor import VideoProcessor

class SmartFlowEngine:
    def __init__(self):
        self.processor = VideoProcessor()
        self.pipeline = AgentPipeline()

    def analyze_frame(self, frame, source="Camera-01"):
        result = self.processor.detect(frame)
        if not result["objects"]:
            return None
        return self.pipeline.process(result, source)

    def analyze_video(self, path, frame_skip=5, confidence=0.5, progress=None, source="Uploaded Video"):
        return self.processor.process_video(
            path, frame_skip, confidence,
            callback=progress, pipeline=self.pipeline, source=source
        )

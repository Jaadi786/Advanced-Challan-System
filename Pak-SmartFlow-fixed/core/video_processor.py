import cv2

class VideoProcessor:
    def detect(self, frame):
        # Explicit DEMO adapter. Replace this boundary with a real detector.
        if frame is None:
            return {"objects":[]}
        return {
            "objects":[{"class":"vehicle","confidence":0.94}],
            "plate":"DEMO-0001",
            "violation":"Needs Review",
            "mode":"DEMO"
        }

    def process_video(self, path, frame_skip=5, confidence=0.5, callback=None, pipeline=None, source="Uploaded Video"):
        cap = cv2.VideoCapture(str(path))
        if not cap.isOpened():
            raise RuntimeError("Unable to open video.")
        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
        fps = cap.get(cv2.CAP_PROP_FPS) or 25
        frame_index = 0
        processed = 0
        events = []
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            if frame_index % max(1, frame_skip) == 0:
                processed += 1
                result = self.detect(frame)
                if result["objects"] and pipeline:
                    events.append(pipeline.process(result, source))
            frame_index += 1
            if callback:
                callback(frame_index, total)
        cap.release()
        return {
            "frames_total": total,
            "frames_processed": processed,
            "duration_sec": round(total / fps, 2) if total else 0,
            "events": events,
            "mode": "DEMO_ADAPTER"
        }

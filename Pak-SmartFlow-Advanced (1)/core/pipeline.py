from dataclasses import asdict
from datetime import datetime
from core.engine import Event

class AgentPipeline:
    AGENTS = [
        ("A01","Detection","Object detection"),
        ("A02","ANPR","License plate recognition"),
        ("A03","Evidence","Evidence consistency"),
        ("A04","Safety","Helmet / seatbelt signals"),
        ("A05","Risk","Risk scoring"),
        ("A06","Prediction","Trajectory / collision risk"),
        ("A07","Fuzzy Decision","Violation decision"),
        ("A08","Multi-Violation","Violation consolidation"),
        ("A09","Action","Challan preparation"),
        ("A10","Explainability","Human-readable reasoning"),
        ("A11","Emergency","Emergency signal analysis"),
        ("A12","Pedestrian","Pedestrian safety"),
        ("A13","Optimization","Traffic optimization"),
        ("A14","Compliance","Compliance history"),
        ("A15","Payment","Payment workflow"),
        ("A16","Parking","Parking intelligence"),
        ("A17","Consolidation","Case consolidation"),
        ("A18","Documents","Document workflow"),
        ("A19","Vehicle Condition","Vehicle condition"),
        ("A20","Behavior","Behavioral signals"),
    ]

    def process(self, detection, source):
        obj = detection["objects"][0]
        confidence = float(obj.get("confidence", 0.91))
        risk = "HIGH" if confidence >= 0.90 else "MEDIUM"
        violation = detection.get("violation", "Needs Review")
        fine = {"No Helmet":500, "Red Light":1000, "Wrong Way":1500}.get(violation, 0)
        return asdict(Event(
            timestamp=datetime.now().strftime("%H:%M:%S"),
            camera=source, plate=detection.get("plate","PENDING"),
            violation=violation, confidence=confidence, risk=risk, fine=fine
        ))

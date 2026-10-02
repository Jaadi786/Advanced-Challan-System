from dataclasses import dataclass


@dataclass
class Event:
    timestamp: str
    camera: str
    plate: str
    violation: str
    confidence: float
    risk: str
    fine: int
    status: str = "REVIEW"

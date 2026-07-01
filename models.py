from pydantic import BaseModel
from typing import List

class EmotionAnalysis(BaseModel):
    dominant_emotion: str
    confidence: float

    def __repr__(self):
        return (
            "EmotionAnalysis(\n"
            f"  dominant_emotion='{self.dominant_emotion}',\n"
            f"  confidence={self.confidence:.2%}\n"
            ")"
        )

    def to_dict(self):
        return {
            "dominant_emotion": self.dominant_emotion,
            "confidence": self.confidence,
        }

class ReflectionAnalysis(BaseModel):
    observations: List[str]
    possible_patterns: List[str]
    reflection: str

    def __repr__(self):
        observations_text = "\n".join(
            f"- {obs}" for obs in self.observations
        )

        patterns_text = "\n".join(
            f"- {pattern}" for pattern in self.possible_patterns
        )

        return (
            "ReflectionAnalysis(\n"
            f"  Observations:\n{observations_text}\n\n"
            f"  Possible Patterns:\n{patterns_text}\n\n"
            f"  Reflection:\n{self.reflection}\n"
            ")"
        )
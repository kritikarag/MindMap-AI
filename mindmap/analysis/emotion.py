from transformers import pipeline

from mindmap.config import EMOTION_MODEL
from mindmap.models import EmotionAnalysis

classifier = pipeline("text-classification", model=EMOTION_MODEL, top_k=None)

def predict(text):
    results = classifier(text)
    results = results[0]

    strongest_result = max(results, key=lambda item: item["score"])
    analysis = EmotionAnalysis(
        dominant_emotion=strongest_result["label"],
        confidence=strongest_result["score"]
    )
    return analysis
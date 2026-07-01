from models import EmotionAnalysis
from transformers import pipeline

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

def predict(text):
    results = classifier(text)
    results = results[0]

    strongest_result = max(results, key=lambda item: item["score"])
    analysis = EmotionAnalysis(
        dominant_emotion=strongest_result["label"],
        confidence=strongest_result["score"]
    )
    return analysis
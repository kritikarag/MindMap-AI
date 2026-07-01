from hf_analyzer import predict
from gemini_service import analyze
from database import save_entry

def analyze_entry(journal_text):
    """
        Complete journal analysis pipeline.

        Input:
            journal text

        Output:
            ReflectionAnalysis
    """
    journal_text = journal_text.lower()

    emotion_analysis = predict(journal_text)

    reflection_analysis = analyze(journal_text, emotion_analysis)

    save_entry(journal_text, emotion_analysis, reflection_analysis)

    return reflection_analysis
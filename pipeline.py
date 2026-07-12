from hf_analyzer import predict
from gemini_service import analyze
from database import save_entry
from memory import find_similar_entries

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

    similar_entries = find_similar_entries(emotion_analysis)

    reflection_analysis = analyze(journal_text, emotion_analysis, similar_entries)

    save_entry(journal_text, emotion_analysis, reflection_analysis)

    return reflection_analysis
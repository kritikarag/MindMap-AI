from mindmap.analysis.emotion import predict
from mindmap.analysis.reflection import analyze
from mindmap.memory.embeddings import find_similar_entries
from mindmap.storage.database import save_entry

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

    similar_entries = find_similar_entries(journal_text)

    reflection_analysis = analyze(journal_text, emotion_analysis, similar_entries)

    save_entry(journal_text, emotion_analysis, reflection_analysis)

    return reflection_analysis
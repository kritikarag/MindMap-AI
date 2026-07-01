import os
from google import genai
from datetime import time
from dotenv import load_dotenv

from models import ReflectionAnalysis
from models import EmotionAnalysis

load_dotenv(verbose=True)


client = genai.Client(
    api_key=os.getenv("GENAI_CLIENT_KEY"),
)

def analyze(journal_text, emotion_analysis: EmotionAnalysis ):
    prompt = f"""
    You are a journaling reflection assistant.

    Your job is to help users reflect on their thoughts.

    Rules:
    - Do not diagnose mental health conditions.
    - Do not make assumptions about the person.
    - Use words like "may", "might", "could".
    - Return only JSON.

    Journal entry:

    {journal_text}


    Detected emotion:

    {emotion_analysis.dominant_emotion}

    Confidence:

    {emotion_analysis.confidence}


    Return JSON in this format:

    {{
     "observations": [
        "..."
     ],

     "possible_patterns": [
        "..."
     ],

     "reflection": "..."
    }}
    """

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            break

        except Exception as e:
            if "503" in str(e):
                print("Gemini busy, retrying...")
                time.sleep(5)
            else:
                raise e

    clean_json = response.text.replace("```json", "").replace("```", "").strip()

    return ReflectionAnalysis.model_validate_json(
        clean_json
    )
"""Central configuration: paths and model names live here instead of being hardcoded per file."""

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# SQLite database. Override with MINDMAP_DB_PATH if you want it elsewhere.
DB_PATH = Path(os.getenv("MINDMAP_DB_PATH", PROJECT_ROOT / "data" / "mindmap.db"))

EMOTION_MODEL = "j-hartmann/emotion-english-distilroberta-base"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
GEMINI_MODEL = "gemini-2.5-flash"

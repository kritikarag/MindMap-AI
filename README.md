# MindMap AI 🧠

MindMap AI is a journaling assistant that helps people notice recurring emotional and cognitive patterns in what they write. Each entry is analysed for emotion, compared against the user's past entries, and turned into a gentle, non-diagnostic reflection.

The longer-term goal is a domain-agnostic cognitive reflection engine. Its flagship application is helping people recognise patterns in emotionally harmful relationships and supporting their recovery, especially people who don't have access to professional support.

> MindMap AI is a self-reflection tool, not a medical or therapeutic service. It does not diagnose, and it is not a substitute for professional care.

---

## How it works

```
Journal entry
     │
     ├──► Emotion analysis        Hugging Face (distilroberta emotion model)
     │
     ├──► Memory retrieval        Sentence embeddings + cosine similarity over past entries
     │
     ▼
Reflection                         Gemini, given the entry, emotion signal and similar past entries
     │
     ▼
Structured output (Pydantic)  ──►  saved to SQLite with its embedding  ──►  shown in the Gradio UI
```

1. **Emotion analysis.** A transformer classifier (`j-hartmann/emotion-english-distilroberta-base`) picks the dominant emotion and a confidence score.
2. **Memory.** The entry is embedded with `all-MiniLM-L6-v2` and compared against every saved entry. The three closest matches go forward, and those above a 0.5 similarity score are offered to the model as possible context.
3. **Reflection.** Gemini returns observations, possible patterns and a short reflection. The prompt forbids diagnosis and assumptions and asks for hedged language ("may", "might", "could"). The model may mention a resemblance to earlier entries, but it isn't allowed to quote them or force a connection.
4. **Validation and storage.** The response is validated against a Pydantic schema, then saved together with the emotion result and the entry's embedding.

Example output:

```json
{
  "observations": ["The entry mentions prolonged working hours"],
  "possible_patterns": ["This may resemble earlier entries about work-related exhaustion"],
  "reflection": "The entry may suggest frustration with workload..."
}
```

---

## Safety layer

Safety features came first, before any other feature work, and they are always on:

- **Get Help Now panel.** A crisis and support resource directory that is visible on every screen. It never depends on the system detecting distress in what the user typed.
- **Quick Exit.** A button that leaves the page instantly. It runs in the browser with no server round-trip.
- **Journal-only mode.** A "Just let me write" option for entries the user doesn't want analysed. *(The toggle is in the UI, but it isn't connected to the pipeline yet. See Status.)*

The resource list currently covers US services. Region-specific resources can be added in `mindmap/safety/resources.py`.

---

## Project structure

```
MindMap-AI/
├── app.py                       # Entry point: python app.py
├── mindmap/
│   ├── config.py                # DB path and model names
│   ├── models.py                # Pydantic schemas (EmotionAnalysis, ReflectionAnalysis)
│   ├── pipeline.py              # Orchestrates analysis → retrieval → reflection → storage
│   ├── analysis/
│   │   ├── emotion.py           # Hugging Face emotion classifier
│   │   └── reflection.py        # Gemini reflection generation
│   ├── memory/
│   │   └── embeddings.py        # Embeddings and similar-entry retrieval
│   ├── storage/
│   │   ├── connection.py        # SQLite connection
│   │   └── database.py          # Schema and saving entries
│   ├── safety/
│   │   ├── layer.py             # Get Help Now, Quick Exit, journal-only toggle
│   │   └── resources.py         # Support resource directory
│   └── ui/
│       └── gradio_app.py        # Gradio interface
├── scripts/                     # Database utilities (run with python -m)
├── tests/
│   └── test_pipeline.py         # End-to-end pipeline check
└── data/                        # mindmap.db lives here (gitignored)
```

---

## Getting started

**1. Install**

```bash
git clone https://github.com/kritikarag/MindMap-AI.git
cd MindMap-AI
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

**2. Add your Gemini API key** to a `.env` file in the project root:

```
GENAI_CLIENT_KEY=your_gemini_api_key
```

**3. Create the database**

```bash
python3 -m scripts.init_db
```

This creates `data/mindmap.db`. Set `MINDMAP_DB_PATH` to keep it somewhere else.

**4. Run**

```bash
python3 app.py                     # Gradio UI at http://127.0.0.1:7860
python3 -m tests.test_pipeline     # run one sample entry through the pipeline
```

Database utilities:

```bash
python3 -m scripts.view_db                  # print all entries
python3 -m scripts.backfill_embeddings      # embed entries saved without one
python3 -m scripts.migrate_add_embedding    # add the embedding column to an older DB
```

The first run downloads the Hugging Face and sentence-transformer models, which can take a few minutes.

---

## Tech stack

| Layer | Now | Planned |
|---|---|---|
| Emotion model | Hugging Face Transformers | Trained, calibrated classifiers |
| Reflection | Gemini (`gemini-2.5-flash`) | |
| Memory | sentence-transformers, brute-force cosine similarity | ChromaDB or FAISS |
| Schemas | Pydantic | |
| Storage | SQLite | |
| Backend | Python | FastAPI |
| Frontend | Gradio | React + Vite PWA |

---

## Status

**Done**

- ✅ Emotion analysis and Gemini reflection with validated, structured output
- ✅ Persistent storage of entries, analyses and embeddings
- ✅ Similar-entry retrieval passed into the reflection prompt
- ✅ Safety layer: Get Help Now panel and Quick Exit

**In progress**

- Connecting the journal-only toggle to the pipeline, so "Just let me write" skips analysis
- Replacing brute-force similarity with a vector index (ChromaDB or FAISS)
- Supporting domain profiles in the extraction schema

---

## Roadmap

- **Validation safety.** Guardrails so the system never quietly endorses the user's judgments about other people. They include noticing inconsistencies across entries and spotting rumination loops, and pointing to professional support instead of repeating the same story with more confidence.
- **Pattern glossary.** Recognising relational tactics (DARVO, love bombing, minimisation, triangulation, blame-shifting), with relational dynamics such as attachment styles and the Drama Triangle written about non-judgmentally and kept separate.
- **Long-term memory.** Retrieval across a user's full history, plus a separate entry type for childhood and origins.
- **Idiographic modelling.** Building a model for each person rather than relying on population averages. This covers mining patterns from their entries, vector autoregressive (VAR) network models, and scoring how confident a suspected cause-and-effect link really is (Granger causality, convergent cross mapping). It also includes a tracker that checks a user's early intuitions against the evidence as it builds up over time.
- **Trained classifiers** with calibrated confidence.
- **Grounding** in schema therapy, attachment theory and trauma-informed frameworks.
- **Research validation.**
- **Web delivery.** A FastAPI backend and a React PWA, so the app works on a phone without going through an app store.

Ideas beyond that include voice journaling, handwritten-diary OCR, narrative identity modelling and a privacy-preserving architecture.

---

## License

[MIT](LICENSE)

# MindMap-AI 🧠

An AI-powered journaling assistant that transforms personal journal entries into structured emotional insights and reflective feedback.

MindMap-AI combines **emotion analysis**, **LLM-powered reflection**, and **structured AI outputs** to help users understand patterns in their thoughts and experiences.

---

# Overview

Traditional journaling helps people record experiences, but it often lacks reflection and pattern discovery.

MindMap-AI aims to bridge that gap:

```
Journal Entry
      |
      v
Emotion Analysis
      |
      v
AI Reflection
      |
      v
Structured Insight
```

A user writes a journal entry, the system analyzes emotional signals, and an AI model generates a reflection while maintaining a safe, non-diagnostic approach.

---

# Current Features

## 1. Emotion Analysis

Uses a Hugging Face transformer model to detect the dominant emotion in a journal entry.

Example:

Input:

```
I hate working for long hours. I feel exhausted.
```

Output:

```json
{
  "dominant_emotion": "sadness",
  "confidence": 0.62
}
```

The emotion model provides a structured emotional signal that is passed to the reflection layer.

---

## 2. AI Reflection Generation

Uses Gemini to generate a structured reflection based on:

* Journal content
* Detected emotion
* Confidence score

The model does not diagnose or make assumptions.

Instead, it provides:

* Observations
* Possible patterns
* Reflection

Example output:

```json
{
  "observations": [
    "The entry mentions prolonged working hours"
  ],

  "possible_patterns": [
    "Possible work-related exhaustion"
  ],

  "reflection": "The entry may suggest frustration related to workload..."
}
```

---

# Architecture

Current system design:

```
                 User Journal Entry

                         |
                         v

                    pipeline.py

                         |
          +--------------+--------------+
          |                             |
          v                             v

   hf_analyzer.py              gemini_service.py

   Hugging Face                 Gemini API

          |                             |

          +--------------+--------------+

                         |

                         v

              ReflectionAnalysis

                         |

                         v

                    Gradio UI
```

---

# Project Structure

```
MindMap-AI/

├── app.py
│   └── Gradio user interface
│
├── pipeline.py
│   └── Connects all AI components
│
├── hf_analyzer.py
│   └── Emotion classification using Hugging Face
│
├── gemini_service.py
│   └── Reflection generation using Gemini
│
├── models.py
│   └── Pydantic schemas for structured outputs
│
├── test_pipeline.py
│   └── Backend pipeline testing
│
├── requirements.txt
│
└── .env
    └── API keys
```

---

# Technology Stack

## AI / ML

* Hugging Face Transformers
* Emotion classification model:

  * `j-hartmann/emotion-english-distilroberta-base`

## LLM

* Gemini API

Used for:

* Reflection generation
* Structured reasoning

## Backend

* Python
* Pydantic

Used for:

* Data validation
* Structured AI responses

## UI

* Gradio

Used for:

* Interactive journal interface

---

# Installation

## 1. Clone repository

```bash
git clone <repository-url>

cd MindMap-AI
```

---

## 2. Create virtual environment

```bash
python3 -m venv .venv
```

Activate:

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Setup environment variables

Create:

```
.env
```

Add:

```
GENAI_CLIENT_KEY=your_gemini_api_key
```

---

# Running the Project

## Test AI pipeline

```bash
python3 test_pipeline.py
```

Expected flow:

```
Journal Text
      |
      v
Emotion Analysis
      |
      v
Gemini Reflection
      |
      v
Structured Output
```

---

## Run Gradio App

```bash
python3 app.py
```

Open:

```
http://127.0.0.1:7860
```

---

# Design Principles

## Separation of Responsibilities

The project separates:

### UI Layer

`app.py`

Responsible for:

* User interaction
* Formatting output

### Pipeline Layer

`pipeline.py`

Responsible for:

* Connecting components

### AI Layer

`hf_analyzer.py`

Responsible for:

* Emotion detection

`gemini_service.py`

Responsible for:

* Reflection generation

### Data Layer

`models.py`

Responsible for:

* Structured schemas

This keeps the system modular and allows future additions without rewriting existing components.

---

# Safety Approach

MindMap-AI is designed as a reflection assistant.

It:

* Does not diagnose mental health conditions
* Avoids making assumptions
* Uses uncertainty-aware language:

  * "may"
  * "might"
  * "could"

The goal is self-reflection, not medical analysis.

---

# Future Roadmap

## Multimodal Journaling

Future support:

### Voice Journaling

Flow:

```
Voice Input
      |
      v
Speech-to-text
      |
      v
Journal Pipeline
```

### Diary Image Parsing

Flow:

```
Handwritten Diary Image
          |
          v
OCR / Vision Model
          |
          v
Journal Pipeline
```

---

## Long-Term Memory

Future versions will store journal history and use embeddings to discover patterns over time.

Example:

```
Past Entries
      |
      v
Vector Search
      |
      v
Historical Context
      |
      v
Personalized Reflection
```

---

# Current Status

Implemented:

✅ Emotion analysis
✅ Gemini reflection generation
✅ Structured AI outputs
✅ Pipeline architecture
✅ Gradio interface

Next milestone:

Adding persistent memory and historical journal understanding.

---

# License

This project is currently for learning and experimentation.

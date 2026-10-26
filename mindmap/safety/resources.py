"""
resources.py

Static resource directory for the safety layer. Deliberately hardcoded rather
than fetched from an API, so it's available even if the network / Gemini
API is down, and so it can be bundled offline later in the PWA version.

IMPORTANT: Review and update this list yourself before relying on it.
Phone numbers, text lines, and hours of operation change. This is a
starting point, not a vetted final list — cross-check against the
organizations' own sites before shipping this to anyone but yourself.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class Resource:
    name: str
    description: str
    contact: str
    kind: str # "crisis", "hotline", "warmline", "text"


# General crisis resources (US-focused; add region-specific ones as needed)
CRISIS_RESOURCES: List[Resource] = [
    Resource(
        name="988 Suicide & Crisis Lifeline",
        description="24/7, free and confidential support for anyone in suicidal crisis or emotional distress.",
        contact="Call or text 988",
        kind="crisis",
    ),
    Resource(
        name="Crisis Text Line",
        description="Free 24/7 text-based crisis support.",
        contact="Text HOME to 741741",
        kind="text",
    ),
]

# Abuse-recovery specific resources
ABUSE_RECOVERY_RESOURCES: List[Resource] = [
    Resource(
        name="National Domestic Violence Hotline",
        description="24/7 confidential support for anyone experiencing domestic abuse.",
        contact="Call 1-800-799-7233 or text START to 88788",
        kind="hotline",
    ),
    Resource(
        name="loveisrespect (for younger users / dating abuse)",
        description="24/7 support specifically for dating abuse and unhealthy relationships.",
        contact="Call 1-866-331-9474 or text LOVEIS to 22522",
        kind="hotline",
    ),
]

# Free / low-cost peer support (not crisis-specific, but addresses the
# affordability gap that's part of this project's motivation)
WARMLINES: List[Resource] = [
    Resource(
        name="Warmline Directory (mentalhealthsf.org list, maintained by NAMI affiliates)",
        description="State-by-state directory of free, non-crisis peer support warmlines — for when you need to talk but it's not an emergency.",
        contact="See https://warmline.org for a directory by state",
        kind="warmline",
    ),
]

def get_all_resources() -> List[Resource]:
    return CRISIS_RESOURCES + ABUSE_RECOVERY_RESOURCES + WARMLINES

def format_resources_markdown() -> str:
    """Render the full resource list as Markdown for display in the Gradio UI."""
    sections = [
        ("If you're in immediate crisis", CRISIS_RESOURCES),
        ("If you're experiencing abuse", ABUSE_RECOVERY_RESOURCES),
        ("If you just need to talk (free, non-crisis)", WARMLINES),
    ]
    lines = []
    for heading, resources in sections:
        lines.append(f"### {heading}")
        for r in resources:
            lines.append(f"- **{r.name}** — {r.description}\n  {r.contact}")
        lines.append("")
    return "\n".join(lines)
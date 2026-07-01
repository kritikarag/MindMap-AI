import gradio as gr

from pipeline import analyze_entry


def reflect(journal_text):
    if not journal_text.strip():
        return "Please enter a journal entry."

    analysis = analyze_entry(journal_text)

    output = f"""
## Observations

"""

    for obs in analysis.observations:
        output += f"- {obs}\n"

    output += """

## Possible Patterns

"""

    for pattern in analysis.possible_patterns:
        output += f"- {pattern}\n"

    output += f"""

## Reflection

{analysis.reflection}
"""

    return output


demo = gr.Interface(
    fn=reflect,
    inputs=gr.Textbox(
        lines=8,
        placeholder="Write what happened today..."
    ),
    outputs=gr.Markdown(),
    title="MindMap AI",
    description="Reflect on your journal entries with AI"
)

demo.launch()
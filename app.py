import gradio as gr
from safety_layer import (
    build_get_help_now_panel,
    build_quick_exit_button,
    build_mode_toggle,
)

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

with gr.Blocks() as demo:

    mode_toggle = build_mode_toggle()
    journal_input = gr.Textbox(label="Journal entry", lines=8)
    submit_btn = gr.Button("Submit")
    output = gr.Markdown()

    submit_btn.click(
        fn=analyze_entry,
        inputs=[journal_input, mode_toggle],
        outputs=output,
    )

    with gr.Row():
        build_get_help_now_panel()
        build_quick_exit_button()

demo.launch()
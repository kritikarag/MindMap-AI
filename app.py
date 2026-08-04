import gradio as gr
from safety_layer import (
    build_get_help_now_panel,
    build_quick_exit_button,
    build_mode_toggle,
)
from pipeline import analyze_entry


def reflect(journal_text, mode):
    if not journal_text.strip():
        return "Please enter a journal entry."

    result = analyze_entry(journal_text)

    # "Just let me write" mode returns a plain string -- pass it straight through.
    if isinstance(result, str):
        return result

    # "Reflect on this" mode returns a ReflectionAnalysis object.
    analysis = result
    output = "## Observations\n"
    for obs in analysis.observations:
        output += f"- {obs}\n"

    output += "\n## Possible Patterns\n"
    for pattern in analysis.possible_patterns:
        output += f"- {pattern}\n"

    output += f"\n## Reflection\n{analysis.reflection}\n"
    return output


with gr.Blocks(title="MindMap AI") as demo:
    gr.Markdown("# MindMap AI\nReflect on your journal entries with AI")

    mode_toggle = build_mode_toggle()
    journal_input = gr.Textbox(
        label="Journal entry",
        lines=8,
        placeholder="Write what happened today...",
    )
    submit_btn = gr.Button("Submit")
    output = gr.Markdown()

    submit_btn.click(
        fn=reflect,
        inputs=[journal_input, mode_toggle],
        outputs=output,
    )

    with gr.Row():
        build_get_help_now_panel()
        build_quick_exit_button()

demo.launch()
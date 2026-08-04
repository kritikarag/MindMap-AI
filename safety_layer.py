"""
safety_layer.py

Reusable Gradio components for the Phase 0 safety layer:
  - Get Help Now panel (always visible, not keyword-triggered)
  - Quick-exit button (instant client-side redirect, no server roundtrip)
  - "Just let me write" mode toggle (skips analysis entirely)
"""

import gradio as gr
from resources import format_resources_markdown


# ---------------------------------------------------------------------------
# 1. Get Help Now panel
# ---------------------------------------------------------------------------
def build_get_help_now_panel() -> gr.Accordion:
    """
    An always-visible, collapsed-by-default accordion containing the full
    resource directory. Deliberately NOT keyword-triggered — it's present
    on every screen regardless of what the user has typed, so finding it
    never depends on the system correctly detecting distress.
    """
    with gr.Accordion("🆘 Get Help Now", open=False) as panel:
        gr.Markdown(format_resources_markdown())
    return panel


# ---------------------------------------------------------------------------
# 2. Quick-exit button
# ---------------------------------------------------------------------------
QUICK_EXIT_JS = """
() => {
    window.location.href = "https://www.weather.com";
}
"""


def build_quick_exit_button() -> gr.Button:
    btn = gr.Button("⚠️ Quick Exit", elem_id="quick-exit-btn", variant="stop")
    # fn=None means no Python function runs — this is instant and client-side only.
    btn.click(fn=None, inputs=None, outputs=None, js=QUICK_EXIT_JS)
    return btn


# ---------------------------------------------------------------------------
# 3. Journal-only mode toggle
# ---------------------------------------------------------------------------
def build_mode_toggle() -> gr.Radio:
    """
    Lets the user choose between:
      - "Reflect on this": the normal pipeline (emotion analysis + Gemini reflection)
      - "Just let me write": pure release, no analysis at all

    The returned component's value should be passed into your pipeline
    call so it can skip the HF/Gemini steps entirely when "Just let me
    write" is selected — see pipeline.py changes below.
    """
    return gr.Radio(
        choices=["Reflect on this", "Just let me write"],
        value="Reflect on this",
        label="How do you want to use this entry?",
        info="'Just let me write' skips all analysis — nothing is processed by the AI, it's just saved.",
    )


# ---------------------------------------------------------------------------
# Suggested integration snippet for app.py
# ---------------------------------------------------------------------------
"""
Example of how these slot into an existing gr.Blocks() layout in app.py.
Adjust to match your actual structure — this assumes a simple single-column
layout with a textbox for journal entry and a submit button.

    import gradio as gr
    from safety_layer import (
        build_get_help_now_panel,
        build_quick_exit_button,
        build_mode_toggle,
    )
    from pipeline import run_pipeline

    with gr.Blocks() as demo:
        # Top of every screen, regardless of what else is on it
        with gr.Row():
            build_get_help_now_panel()
            build_quick_exit_button()

        mode_toggle = build_mode_toggle()
        journal_input = gr.Textbox(label="Journal entry", lines=8)
        submit_btn = gr.Button("Submit")
        output = gr.Markdown()

        submit_btn.click(
            fn=run_pipeline,
            inputs=[journal_input, mode_toggle],
            outputs=output,
        )

    demo.launch()
"""
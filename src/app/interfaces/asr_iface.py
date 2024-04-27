import gradio as gr
from typing import Callable
from .utils import languages


class ASRIface:
    title = f"""<style>
            .gr-title {{
                background: linear-gradient(90deg, #ff6161 0%, #f7af74 20%, #ffc574 40%, #98ff90 60%, #74ffd6 80%, #66a8ff 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            </style><span class="gr-title">Automatic Speech Recognition</span> 🐅"""
    description = """ASR (Automatic Speech Recognition) is a technology that allows computers to recognize and transcribe human speech from audio recordings."""

    def __init__(
        self,
        fn: Callable[[str, str], str],
    ) -> None:
        self.fn = fn

    def create_interface(self, source, label) -> gr.Interface:
        return gr.Interface(
            fn=self.fn,
            inputs=[
                gr.Audio(sources=source, label=label, type="filepath"),
                gr.CheckboxGroup(
                    choices=languages.keys(),
                    label="Languages",
                    value=["English"],
                ),
                gr.Dropdown(
                    choices=languages.keys(),
                    label="Translate",
                    value="",
                ),
            ],
            outputs=[
                gr.Textbox(label="Transcription", show_copy_button=True),
            ],
            allow_flagging="never",
            title=self.title,
            description=self.description,
        )

    def make_interface(self) -> gr.Interface:
        microphone = self.create_interface("microphone", None)
        audio_file = self.create_interface("upload", "Audio file")
        iface = gr.Blocks()
        with iface:
            gr.TabbedInterface([microphone, audio_file], ["Microphone", "Audio file"])
        return iface

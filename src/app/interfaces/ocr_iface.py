import numpy as np
import pandas as pd
import gradio as gr
from PIL import Image
from typing import Callable, Union, List, Tuple, Literal
from .utils import languages


class OCRIface:
    title = f"""<style>
            .gr-title {{
                background: linear-gradient(90deg, #ff6161 0%, #f7af74 20%, #ffc574 40%, #98ff90 60%, #74ffd6 80%, #66a8ff 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            </style><span class="gr-title">Optical Character Recognition</span> 🦚"""
    description = """OCR (Optical Character Recognition) is a technology that allows computers to recognize and read text from images of printed or typed documents."""
    image_input = gr.Image(label="Input")
    file_input = gr.File(label="Input")
    image_output = gr.Image(label="Output")
    file_output = gr.File(label="Output")

    def __init__(
        self,
        fn: Callable[
            [Union[np.ndarray, Image.Image], List[str]],
            Tuple[Image.Image, pd.DataFrame],
        ],
    ) -> None:
        self.fn = fn

    def create_interface(
        self,
        mode: Literal["image", "file"] = "image",
    ) -> gr.Interface:
        if mode == "image":
            mode_input = self.image_input
            mode_output = self.image_output
        elif mode == "file":
            mode_input = self.file_input
            mode_output = self.file_output
        else:
            raise NotImplementedError
        return gr.Interface(
            fn=self.fn,
            inputs=[
                mode_input,
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
                mode_output,
                gr.Textbox(label="Text"),
                gr.Dataframe(
                    label="Dataframe",
                    headers=["text", "confidence"],
                ),
            ],
            title=self.title,
            description=self.description,
            allow_flagging="never",
        )

    def make_interface(self) -> gr.Interface:
        image = self.create_interface(mode="image")
        file = self.create_interface(mode="file")
        iface = gr.Blocks()
        with iface:
            gr.TabbedInterface([image, file], ["Image", "File"])
        return iface

import gradio as gr
from typing import Callable, Dict, Literal
from .utils import create_animation
from .ocr_iface import OCRIface
from .asr_iface import ASRIface


class SupremeIface:
    def __init__(self, fns: Dict[Literal["OCR", "ASR"], Callable]):
        self.fns = fns

    def get_supreme_iface(self):
        supreme_iface = gr.Blocks(js=create_animation())
        sub_ifaces = [
            OCRIface(self.fns["OCR"]).make_interface(),
            ASRIface(self.fns["ASR"]).make_interface(),
        ]
        with supreme_iface:
            gr.TabbedInterface(sub_ifaces, ["OCR", "ASR"])
        return supreme_iface

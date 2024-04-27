import numpy as np
from PIL import Image
from typing import List, Callable, Union
from app.interfaces.utils import languages
from app.interfaces.supreme_iface import SupremeIface
from models.vision.ocr.easy_ocr import EasyOCR


class Interface:
    def __init__(self):
        self.title = "神"

    def ocr(
        self,
        image: Union[np.ndarray, Image.Image],
        lang: List[str] = ["English"],
        translate: str = "English",
    ) -> Callable:
        lang = [languages[l] for l in lang]
        fn = EasyOCR(lang=lang).predict
        # TODO : Implement translate
        return fn(image)

    def asr(
        self,
        audio_file: str,
        lang: str = "English",
        task: str = "transcribe",
    ):
        # TODO : Implement ASR
        return "Transribed text"

    def launch(self):
        fns = {
            "OCR": self.ocr,
            "ASR": self.asr,
        }
        iface = SupremeIface(fns).get_supreme_iface()
        iface.queue(max_size=10)
        iface.launch()


if __name__ == "__main__":
    transcriber = Interface()
    transcriber.launch()

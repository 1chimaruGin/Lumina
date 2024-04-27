import easyocr
import numpy as np
from PIL import Image
from typing import Literal, Union, List
from .utils import draw_boxes_ocr, post_process_ocr
from ..base_model import BaseModel


__all__ = ["inference", "draw_boxes"]


class EasyOCR(BaseModel):
    def __init__(self, lang: List[str] = ["en"]):
        self.reader = easyocr.Reader(lang)

    def predict(
        self,
        image: Union[np.ndarray, Image.Image],
        output_mode: Literal["all", "dataframe", "text"] = "all",
        **kwargs
    ):
        """
        Predicts text from an image using EasyOCR
        """
        bounds = self.reader.readtext(image)
        image = draw_boxes_ocr(image, bounds)
        if not isinstance(image, Image.Image):
            image = Image.fromarray(image)
        result = post_process_ocr(bounds, output_mode)
        return [image, *result]

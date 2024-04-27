import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from typing import List, Union, Literal


def draw_boxes_ocr(
    image: Union[np.ndarray, Image.Image],
    bounds: List[List[List[int]]],
    color: str = "yellow",
    width: int = 2,
):
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image


def post_process_ocr(
    bounds: list, output_mode: Literal["all", "dataframe", "text"] = "all"
):
    df = pd.DataFrame(bounds, columns=["", "text", "confidence"]).iloc[:, 1:]
    text = " ".join([x[0] for x in bounds])
    if output_mode == "dataframe":
        return "", df
    elif output_mode == "text":
        return text, pd.DataFrame(columns=["", "text", "confidence"])
    elif output_mode == "all":
        return text, df

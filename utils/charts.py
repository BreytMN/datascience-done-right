from io import BytesIO

import altair as alt
from IPython.display import Image


def display_static_altair_images(chart: alt.Chart) -> Image:
    with BytesIO() as buffer:
        chart.save(buffer, format="png")
        return Image(buffer.getvalue())

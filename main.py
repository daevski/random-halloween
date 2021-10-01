from pathlib import Path
from typing import List

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

import randomizer as app_random

app = FastAPI()
app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")
img_path = Path('./web/static/img').resolve()

# TODO: Mount static directory with images
# TODO: Count total number of images, and use that value as `end` argument to get_spooky_number()
# TODO: Render image from images directory based on random number.
# TODO: Create page header with app version and copyright


@app.get('/')
def root(request: Request):
    images: List[Path] = app_random.get_images(img_path)

    if len(images) < 1:
        return 'No images found!'

    spooky_number: int = app_random.get_spooky_number(1, len(images) - 1)
    selection: str = images[spooky_number].name
    return templates.TemplateResponse(
        "index.html", {"request": request, "selection": selection}
    )

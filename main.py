#!/usr/bin/env python3

from PIL import Image

carpeta = "Imagenes/"
nombre = "bottom_moving"
with Image.open(carpeta + nombre + ".png") as image:
    with image.quantize(colors=256, method=2) as converted:
        converted.save(carpeta + nombre + "1.png")

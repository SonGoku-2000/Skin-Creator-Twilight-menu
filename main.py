#!/usr/bin/env python3

from PIL import Image

nombre = 'bottom_moving'
with Image.open(nombre + ".png" ) as image:
    with image.quantize(colors=256, method=2) as converted:
        converted.save(nombre+'1.png')
#!/usr/bin/env python3

from PIL import Image

carpetaImagenes = "Imagenes/"
carpetaPlantillas = "Plantillas/"
carpetaPruebas = "Pruebas/"
carpetaDestino = "Destino/"
nombre = "gine.jpg"


def guardarImagen(nombreImagen: str, nombreSalida: str = ""):
    if(nombreSalida == ""):
        nombreSalida = nombreImagen
    tamanoImagen = (256,192)
    with Image.open(carpetaImagenes + carpetaPruebas + nombre) as image:
        image = image.resize(tamanoImagen)
        with image.quantize(colors=256, method=2) as converted:
            converted.save(carpetaImagenes + carpetaDestino + nombreSalida)

if __name__ == "__main__":
    guardarImagen(nombre,"bottom.png")
    guardarImagen(nombre,"bottom_bubble.png")
    guardarImagen(nombre,"bottom_bubble_macro.png")
    guardarImagen(nombre,"bottom_moving.png")

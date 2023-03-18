#!/usr/bin/env python3

from PIL import Image
from pathlib import Path

carpetaImagenes = "Imagenes/"
carpetaPlantillas = carpetaImagenes + "Plantillas/"
carpetaPruebas = carpetaImagenes + "Pruebas/"
carpetaSkins = "Skins/"


def guardarImagen(dirImagen: str, dirSalida: str, nombreSalida: str):
    tamanoImagen = (256, 192)
    Path(dirSalida).mkdir(parents=True, exist_ok=True)
    with Image.open(dirImagen) as image:
        image = image.resize(tamanoImagen)
        with image.quantize(colors=256, method=2) as converted:
            converted.save(dirSalida + nombreSalida)


def crearPaquete(imagenBase: str, nombrePaquete: str = "white", paqueteBase: str = ""):
    carpetaSkin = Path(carpetaSkins + nombrePaquete + "/")
    carpetaSkin.mkdir(parents=True, exist_ok=True)
    guardarImagen(dirImagenBase, carpetaSkin.__str__() +
                  "/background/", "bottom.png")
    guardarImagen(dirImagenBase, carpetaSkin.__str__() +
                  "/background/", "bottom_bubble.png")
    guardarImagen(dirImagenBase, carpetaSkin.__str__() +
                  "/background/", "bottom_bubble_macro.png")
    guardarImagen(dirImagenBase, carpetaSkin.__str__() +
                  "/background/", "bottom_moving.png")


if __name__ == "__main__":
    dirImagenBase = carpetaPlantillas + "gine.jpg"
    crearPaquete(dirImagenBase, "test1")

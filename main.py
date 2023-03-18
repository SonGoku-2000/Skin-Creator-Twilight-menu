#!/usr/bin/env python3

from PIL import Image
from pathlib import Path
from tkinter.filedialog import askopenfilename
import tkinter as Tk
from tkinter import TclError

carpetaImagenes = "Imagenes/"
carpetaPlantillas = carpetaImagenes + "Plantillas/"
carpetaPruebas = carpetaImagenes + "Pruebas/"
carpetaSkins = "Skins/"


def seleccionarImagen():
    frame = Tk.Tk()
    frame.withdraw()

    # vvv Ocultar archivos ocultos
    try:
        frame.tk.call('tk_getOpenFile', '-foobarbaz')
    except TclError:
        pass
    frame.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
    # ^^^ Ocultar archivos ocultos

    archivo = askopenfilename(title='Seleccione un juego',
                              filetypes=(('Imagenes', ('*.jpg', '*.jpeg', '*.png')),
                                         ('All', '*.*')))
    return archivo


def guardarImagen(dirImagen: str, dirSalida: str, nombreSalida: str):
    tamanoImagen = (256, 192)
    Path(dirSalida).mkdir(parents=True, exist_ok=True)
    with Image.open(dirImagen) as image:
        image = image.resize(tamanoImagen)
        with image.quantize(colors=256, method=2) as converted:
            converted.save(dirSalida + nombreSalida)


def imagenBottom(dirImagenBase: str, carpetaSkin: Path):
    temp = Path(".temp")
    temp.mkdir(parents=True, exist_ok=True)
    dirImagenTemp = temp.joinpath("temp.png")

    with Image.open(dirImagenBase) as imagenBase:
        reescalada = imagenBase.resize((256, 192))
        with Image.open(carpetaPlantillas + "white/background/bottom.png") as bottom:
            reescalada.paste(bottom, (0, 0), bottom)
        reescalada.save(dirImagenTemp)

    guardarImagen(dirImagenTemp.__str__(), carpetaSkin.__str__() +
                  "/background/", "bottom.png")
    dirImagenTemp.unlink()
    temp.rmdir()


def crearPaquete(dirImagenBase: str, nombrePaquete: str = "white", paqueteBase: str = ""):
    carpetaSkin = Path(carpetaSkins + nombrePaquete + "/")
    carpetaSkin.mkdir(parents=True, exist_ok=True)
    imagenBottom(dirImagenBase, carpetaSkin)
    guardarImagen(dirImagenBase, carpetaSkin.__str__() +
                  "/background/", "bottom_bubble.png")
    guardarImagen(dirImagenBase, carpetaSkin.__str__() +
                  "/background/", "bottom_bubble_macro.png")
    guardarImagen(dirImagenBase, carpetaSkin.__str__() +
                  "/background/", "bottom_moving.png")


if __name__ == "__main__":
    dirImagenBase = seleccionarImagen()
    crearPaquete(dirImagenBase, "test")

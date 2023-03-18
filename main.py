#!/usr/bin/env python3

from tkinter.filedialog import askopenfilename
import tkinter as Tk
from tkinter import TclError
from src.crearPaquete import crearPaquete


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


if __name__ == "__main__":
    dirImagenBase = seleccionarImagen()
    crearPaquete(dirImagenBase, "test")

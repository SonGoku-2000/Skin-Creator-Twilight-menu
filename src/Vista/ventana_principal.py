import tkinter as Tk
from tkinter import TclError
from PIL import Image
from PIL import ImageTk
from pathlib import Path


class ventanaPrincipal():
    def __init__(self, master):
        self.frame = Tk.Frame(master)

        # vvv Ocultar archivos ocultos
        try:
            self.frame.tk.call('tk_getOpenFile', '-foobarbaz')
        except TclError:
            pass
        self.frame.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
        # *** Ocultar archivos ocultos

        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.panelLateral = PanelLateral(master)
        self.panelImagen = PanelImagen(master)


class PanelImagen():
    def __init__(self, root):
        self.width = 480
        self.height = 320

        self.frame = Tk.Frame(root, width=self.width, height=self.height)
        self.frame.pack(side=Tk.RIGHT, fill=Tk.BOTH, expand=1)
        self.frame.config(bd=10)
        self.frame.config(relief=Tk.SUNKEN)
        self.imagenTk = ImageTk.PhotoImage(Image.open("src/Vista/a.jpg"))

        self.label = Tk.Label(self.frame, width=self.width,
                              height=self.height, image=self.imagenTk)
        self.label.pack()

    def setImagen(self, dirImagen: Path):
        """
        Establece la imagen de la previsualizacion

        Parameters
        ----------
        dirImagen : Path
            Ruta de la imagen la cual se va a usar para la previsualizacion.
        """
        with Image.open(dirImagen) as imagen:
            self.imagenTk = ImageTk.PhotoImage(
                imagen.resize((self.width, self.height)))
            self.label.configure(image=self.imagenTk)


class PanelLateral():
    def __init__(self, root):
        self.frame = Tk.Frame(root)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.frame.config(bd=10)

        self.textoSelectImagen = Tk.Label(self.frame,
                                          text='Seleccionar Imagen Base')
        self.textoSelectImagen.pack(side='top', fill=Tk.BOTH)
        self.botonSelectImagen = Tk.Button(self.frame,
                                           text="Selecionar Imagen")
        self.botonSelectImagen.pack(side="top", fill=Tk.BOTH)

        self.textoCrearSkin = Tk.Label(self.frame, text='Crear Skin')
        self.textoCrearSkin.pack(side='top', fill=Tk.BOTH)
        self.botonCrearSkin = Tk.Button(self.frame,
                                        state='disabled',
                                        text="Crear Skin")
        self.botonCrearSkin.pack(side="top", fill=Tk.BOTH)

    def desactivarBotonCrearSkin(self):
        self.botonCrearSkin['state'] = Tk.DISABLED

    def activarBotonCrearSkin(self):
        self.botonCrearSkin['state'] = Tk.NORMAL

    def cambiarEstadoBotonCrearSkin(self):
        """
        Invierte el estado del boton crearSkin de NORMAL a DISABLED y de DISABLED a NORMAL
        """
        if (self.botonCrearSkin['state'] == Tk.NORMAL):
            self.botonCrearSkin['state'] = Tk.DISABLED
        else:
            self.botonCrearSkin['state'] = Tk.NORMAL


if __name__ == '__main__':
    raiz = Tk.Tk()
    v = ventanaPrincipal(raiz)
    v.panelImagen.setImagen(Path(
        "/home/songoku/Documentos/Proyectos_programacion/Python/Skin Creator Twiligt menu++/Imagenes/Plantillas/gine.jpg"))
    raiz.mainloop()

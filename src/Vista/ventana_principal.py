import tkinter as Tk
from tkinter import TclError


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
        self.frame = Tk.Frame(root, width=480, height=320)
        self.frame.pack(side=Tk.RIGHT, fill=Tk.BOTH, expand=1)
        self.frame.config(bd=10)
        self.frame.config(relief=Tk.SUNKEN)


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
        if (self.botonCrearSkin['state'] == Tk.NORMAL):
            self.botonCrearSkin['state'] = Tk.DISABLED
        else:
            self.botonCrearSkin['state'] = Tk.NORMAL


if __name__ == '__main__':
    raiz = Tk.Tk()
    ventanaPrincipal(raiz)
    raiz.mainloop()

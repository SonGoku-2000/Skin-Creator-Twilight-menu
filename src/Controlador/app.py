import tkinter as Tk

from pathlib import Path
from src.Modelo.modelo import modelo
from src.Vista.ventana_principal import ventanaPrincipal


class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("Skin Creator for TWiLight Menu++")
        self.root.deiconify()

        self.modelo = modelo()

        self.view = ventanaPrincipal(self.root)
        self.view.panelLateral.botonSelectImagen.bind("<Button>",
                                                      self.seleccionarImagen)
        self.view.panelLateral.botonCrearSkin.bind("<Button>", self.crearSkin)
        self.view.panelLateral.listaTemas["values"] = self.modelo.TEMAS
        self.view.panelLateral.listaTemas.set(self.modelo.TEMAS[0])

    def run(self):
        """
        Ejecuta la aplicacion.
        """
        self.root.mainloop()

    def seleccionarImagen(self, event):
        """
        Accion para el boton de seleccionarImagen. Mostrando una previsualizacion de la imagen seleccionada.
        En caso de no elegir una imagen se pondra en blanco la previsualizacion.
        """
        self.modelo.seleccionarImagen()
        if self.modelo.dirImagen != "":
            self.view.panelLateral.activarBotonCrearSkin()
            self.view.panelImagen.setImagen(Path(self.modelo.dirImagen))
        else:
            self.view.panelLateral.desactivarBotonCrearSkin()
            self.view.panelImagen.setImagen(Path("src/Vista/a.jpg"))
        self.root.mainloop()

    def crearSkin(self, event):
        """
        Accion para el boton crearSkin. Crea las carpetas necesarias para crear la skin usando la funcion del modelo.py
        """
        self.modelo.crearSkin(paqueteBase=self.view.panelLateral.listaTemas.get())


if __name__ == "__main__":
    pass

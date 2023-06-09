import tkinter as Tk
from tkinter import messagebox

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

        self.view.setFuncBotonSelectImagen(command=self.seleccionarImagen)
        self.view.setFuncBotonCrearSkin(command=self.crearSkin)
        self.view.setListaTemas(self.modelo.TEMAS)
        self.view.setImagen(Path("src/Vista/a.jpg"))

    def run(self):
        """
        Ejecuta la aplicacion.
        """
        self.root.mainloop()

    def seleccionarImagen(self):
        """
        Accion para el boton de seleccionarImagen. Mostrando una previsualizacion de la imagen seleccionada.
        En caso de no elegir una imagen se pondra en blanco la previsualizacion.
        """
        self.modelo.seleccionarImagen()
        if self.modelo.dirImagen != "":
            self.view.activarBotonCrearSkin()
            self.view.setImagen(Path(self.modelo.dirImagen))
        else:
            self.view.desactivarBotonCrearSkin()
            self.view.setImagen(Path("src/Vista/a.jpg"))
        self.root.mainloop()

    def crearSkin(self):
        """
        Accion para el boton crearSkin. Crea las carpetas necesarias para crear la skin usando la funcion del modelo.py
        """
        self.modelo.seleccionarNombre()
        if(self.modelo.nombrePaquete == ""):
            messagebox.showerror(
                "Advertencia", "No puede dejar el nombre vacio")
            self.view.setLabelEstado("Estado: error nombre no valido")
        else:
            self.view.setLabelEstado("Estado: creando skin...")
            self.modelo.crearSkin(
                paqueteBase=self.view.panelLateral.listaTemas.get())
            self.view.setLabelEstado("Estado: Skin creada")


if __name__ == "__main__":
    pass

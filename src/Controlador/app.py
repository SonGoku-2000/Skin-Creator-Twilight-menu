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
        self.view.panelLateral.botonSelectImagen.bind("<Button>", self.seleccionarImagen)
        self.view.panelLateral.botonCrearSkin.bind("<Button>", self.crearSkin)

    def run(self):
        self.root.mainloop()
    
    def seleccionarImagen(self,event):
        pass

    def crearSkin(self,event):
        pass

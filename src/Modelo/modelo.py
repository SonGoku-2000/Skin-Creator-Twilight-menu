from pathlib import Path
from tkinter.filedialog import askopenfilename

class modelo():
    def __init__(self) -> None:
        self.dirImagen = ''
        self.dirWBFS = ''

    def __selectorImagen(self, dirBase: str = '.') -> str:
        """
        Despliega una ventana para seleccionar una imagen

        Returns
        -------
        str
            Retorna la imagen seleccionada en la ventana emergente.
        """
        archivo = askopenfilename(title='Seleccione un juego',
                                  initialdir=dirBase,
                                  filetypes=(('Imagenes', ('*.jpg', '*.jpeg', '*.png')),
                                             ('All', '*.*')))
        if archivo == ():
            return ""
        else:
            return archivo

    def seleccionarImagen(self):
        self.dirImagen = self.__selectorImagen()

    def crearSkin(self):
        pass


if __name__ == '__main__':
    model = modelo()
    model.seleccionarImagen()
    print(model.dirImagen)

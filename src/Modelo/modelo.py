from pathlib import Path
from distutils.dir_util import copy_tree
from tkinter.filedialog import askopenfilename
from PIL import Image


class modelo():
    def __init__(self) -> None:
        self.CARPETA_IMAGENES = Path("Imagenes")
        self.CARPETA_PLANTILLAS = self.CARPETA_IMAGENES.joinpath("Plantillas")
        self.CARPETA_SKINS = Path("Skins")
        self.dirImagen = ""
        self.TAMANO_A_CONVERTIR = (256, 192)

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

    def __guardarImagen(self, dirImagen: Path, dirSalida: Path, nombreSalida: str):
        """
        Parameters
        ----------
        dirImagenBase : Path
            Directorio que de la imagen que va a ajustar al formato necesitado.

        dirSalida : Path
            Carpeta de a la que se va a mover la imagen.

        nombreSalida : str
            Nombre que va a tener la imagen en la carpeta de destino.
        """
        
        dirSalida.mkdir(parents=True, exist_ok=True)
        with Image.open(dirImagen) as image:
            image = image.resize(self.TAMANO_A_CONVERTIR)
            with image.quantize(colors=256, method=2) as converted:
                converted.save(dirSalida.joinpath(nombreSalida))

    def seleccionarImagen(self):
        self.dirImagen = self.__selectorImagen()

    def crearSkin(self):
        pass


if __name__ == '__main__':
    model = modelo()
    model.seleccionarImagen()
    print(model.dirImagen)

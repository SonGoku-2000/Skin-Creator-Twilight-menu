from pathlib import Path
from distutils.dir_util import copy_tree
from tkinter.filedialog import askopenfilename
from PIL import Image


class modelo():
    def __init__(self) -> None:
        self.CARPETA_IMAGENES = Path("Imagenes")
        self.CARPETA_PLANTILLAS = self.CARPETA_IMAGENES.joinpath("Plantillas")
        self.CARPETA_SKINS = Path("Skins")

        self.TAMANO_A_CONVERTIR = (256, 192)
        self.dirImagen = ""

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

    def __imagenBottom(self, dirImagenBase: Path, carpetaSkin: Path):
        """
        Parameters
        ----------
        dirImagenBase : Path
            Directorio que de la imagen que se usara como base para el paquete.

        carpetaSkin : Path
            Carpeta de la skin en donde se van a guardar la imagen bottom.
        """

        temp = Path(".temp")
        temp.mkdir(parents=True, exist_ok=True)
        dirImagenTemp = temp.joinpath("temp.png")

        dirImagenDecoracion = self.CARPETA_PLANTILLAS.joinpath(
            "white/background/bottom.png")

        with Image.open(dirImagenBase) as imagenBase:
            imagenBase = imagenBase.resize(self.TAMANO_A_CONVERTIR)

            with Image.open(dirImagenDecoracion) as bottom:
                imagenBase.paste(bottom, (0, 0), bottom)
            imagenBase.save(dirImagenTemp)

        self.__guardarImagen(dirImagenTemp,
                             carpetaSkin.joinpath("background"),
                             "bottom.png")
        dirImagenTemp.unlink()
        temp.rmdir()

    def __imagenBottomBubble(self, dirImagenBase: Path, carpetaSkin: Path):
        """
        Parameters
        ----------
        dirImagenBase : Path
            Directorio que de la imagen que se usara como base para el paquete.

        carpetaSkin : Path
            Carpeta de la skin en donde se van a guardar la imagen bottom_bubble.
        """

        temp = Path(".temp")
        temp.mkdir(parents=True, exist_ok=True)
        dirImagenTemp = temp.joinpath("temp.png")

        dirImagenDecoracion = self.CARPETA_PLANTILLAS.joinpath(
            "white/background/bottom_bubble.png")

        with Image.open(dirImagenBase) as imagenBase:
            imagenBase = imagenBase.resize(self.TAMANO_A_CONVERTIR)

            with Image.open(dirImagenDecoracion) as bottom_bubble:
                imagenBase.paste(bottom_bubble, (0, 0), bottom_bubble)
            imagenBase.save(dirImagenTemp)

        self.__guardarImagen(dirImagenTemp,
                             carpetaSkin.joinpath("background"),
                             "bottom_bubble.png")
        dirImagenTemp.unlink()
        temp.rmdir()

    def crearSkin(self, nombrePaquete: str = "white", paqueteBase: str = "white"):
        """
        Parameters
        ----------
        dirImagenBase : str
            Directorio que de la imagen que se usara como base para el paquete.

        nombrePaquete : str, default "white"
            Nombre que se le dara al paquete creado.

        paqueteBase : str, default "white"
            Nombre de la decoracion base que se usa para crear el paquete puede ser "white" o "dark".
        """

        carpetaSkin = self.CARPETA_SKINS.joinpath(nombrePaquete)
        carpetaSkin.mkdir(parents=True, exist_ok=True)
        dirImagenBase = Path(self.dirImagen)
        
        self.__imagenBottom(dirImagenBase, carpetaSkin)
        self.__imagenBottomBubble(dirImagenBase, carpetaSkin)


if __name__ == '__main__':
    model = modelo()
    model.seleccionarImagen()
    model.crearSkin()

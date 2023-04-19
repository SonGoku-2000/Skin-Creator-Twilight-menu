from pathlib import Path
from distutils.dir_util import copy_tree
from distutils.file_util import copy_file
from tkinter.filedialog import askopenfilename, askdirectory, asksaveasfilename
from PIL import Image


class modelo():
    def __init__(self) -> None:
        self.CARPETA_IMAGENES = Path("Imagenes")
        self.CARPETA_PLANTILLAS = self.CARPETA_IMAGENES.joinpath("Plantillas")
        self.CARPETA_SKINS = Path("Skins")
        self.TEMAS = ("white", "black")

        self.TAMANO_A_CONVERTIR = (256, 192)
        self.dirImagen = ""
        self.nombrePaquete = ""

    def __selectorImagen(self, dirBase: str = '.') -> str:
        """
        Despliega una ventana para seleccionar una imagen

        Parameters
        ----------
        dirBase : str
            Carpeta inicial de la ventana para seleccionar.

        Returns
        -------
        str
            Retorna la imagen seleccionada en la ventana emergente.
        """
        archivo = askopenfilename(title='Seleccione una imagen',
                                  initialdir=dirBase,
                                  filetypes=(('Imagenes', ('*.jpg', '*.jpeg', '*.png')),
                                             ('All', '*.*')))
        if archivo == ():
            return ""
        else:
            return archivo

    def __selectorNombre(self, dirBase: str = './Skins') -> str:
        """
        Despliega una ventana para seleccionar un nombre para el paquete

        Parameters
        ----------
        dirBase : str
            Carpeta inicial de la ventana para seleccionar.

        Returns
        -------
        str
            Retorna el nombre del paquete.
        """
        archivo = asksaveasfilename(title='Seleccione un nombre',
                                    initialdir=dirBase)
        if archivo == ():
            return ""
        else:
            return archivo

    def seleccionarNombre(self):
        """
        Establece el valor de la variable nombrePaquete usando el metodo __selectorNombre()
        """
        self.nombrePaquete = self.__selectorNombre()

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
        """
        Establece el valor de la variable dirImagen usando el metodo __selectorImagen()
        """
        self.dirImagen = self.__selectorImagen()

    def __backgroundHelper(self, dirImagenBase: Path, carpetaSkin: Path, pantalla: str, plantillaBase: str = "white"):
        """
        Funcion auxiliar que permite la facil creacion de las imagenes de la carpeta background

        Parameters
        ----------
        dirImagenBase : Path
            Directorio que de la imagen que se usara como base para el paquete.

        carpetaSkin : Path
            Carpeta de la skin en donde se van a guardar la imagen bottom.

        pantalla: str
            Nombre que le da TWiLight Menu++ a los diferentes estados de la pantalla
                posibles valores:
                "bottom_bubble_macro.png" ,                                                                        
                "bottom_bubble.png",                                   
                "bottom_moving.png",                            
                "bottom.png",
                "top.png"
        """

        temp = Path(".temp")
        temp.mkdir(parents=True, exist_ok=True)
        dirImagenTemp = temp.joinpath("temp.png")

        dirImagenDecoracion = self.CARPETA_PLANTILLAS.joinpath(plantillaBase,
                                                               "background",
                                                               pantalla)

        with Image.open(dirImagenBase) as imagenBase:
            imagenBase = imagenBase.resize(self.TAMANO_A_CONVERTIR)

            with Image.open(dirImagenDecoracion) as decoracion:
                imagenBase.paste(decoracion, (0, 0), decoracion)
            imagenBase.save(dirImagenTemp)

        self.__guardarImagen(dirImagenTemp,
                             carpetaSkin.joinpath("background"),
                             pantalla)
        dirImagenTemp.unlink()
        temp.rmdir()

    def __imagenBottom(self, dirImagenBase: Path, carpetaSkin: Path, paqueteBase: str):
        """
        Parameters
        ----------
        dirImagenBase : Path
            Directorio que de la imagen que se usara como base para el paquete.

        carpetaSkin : Path
            Carpeta de la skin en donde se van a guardar la imagen bottom.
        """
        self.__backgroundHelper(dirImagenBase,
                                carpetaSkin,
                                "bottom.png",
                                paqueteBase)

    def __imagenBottomBubble(self, dirImagenBase: Path, carpetaSkin: Path, paqueteBase: str):
        """
        Parameters
        ----------
        dirImagenBase : Path
            Directorio que de la imagen que se usara como base para el paquete.

        carpetaSkin : Path
            Carpeta de la skin en donde se van a guardar la imagen bottom_bubble.
        """
        self.__backgroundHelper(dirImagenBase,
                                carpetaSkin,
                                "bottom_bubble.png", paqueteBase)

    def __imagenBottomBubbleMacro(self, dirImagenBase: Path, carpetaSkin: Path, paqueteBase: str):
        """
        Parameters
        ----------
        dirImagenBase : Path
            Directorio que de la imagen que se usara como base para el paquete.

        carpetaSkin : Path
            Carpeta de la skin en donde se van a guardar la imagen bottom_bubble_macro.
        """
        self.__backgroundHelper(dirImagenBase,
                                carpetaSkin,
                                "bottom_bubble_macro.png",
                                paqueteBase)

    def __imagenBottomMoving(self, dirImagenBase: Path, carpetaSkin: Path, paqueteBase: str):
        """
        Parameters
        ----------
        dirImagenBase : Path
            Directorio que de la imagen que se usara como base para el paquete.

        carpetaSkin : Path
            Carpeta de la skin en donde se van a guardar la imagen bottom_moving.
        """
        self.__backgroundHelper(dirImagenBase,
                                carpetaSkin,
                                "bottom_moving.png",
                                paqueteBase)

    def __imagenTop(self, dirImagenBase: Path, carpetaSkin: Path, paqueteBase: str):
        """
        Parameters
        ----------
        dirImagenBase : Path
            Directorio que de la imagen que se usara como base para el paquete.

        carpetaSkin : Path
            Carpeta de la skin en donde se van a guardar la imagen top.
        """
        self.__guardarImagen(self.CARPETA_PLANTILLAS.joinpath("white/background/top.png"),
                             carpetaSkin.joinpath("background"),
                             "top.png")

    def crearSkin(self, paqueteBase: str = "white"):
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

        carpetaSkin = self.CARPETA_SKINS.joinpath(self.nombrePaquete)
        carpetaSkin.mkdir(parents=True, exist_ok=True)
        dirImagenBase = Path(self.dirImagen)

        self.__imagenBottom(dirImagenBase, carpetaSkin, paqueteBase)
        self.__imagenBottomBubble(dirImagenBase, carpetaSkin, paqueteBase)
        self.__imagenBottomBubbleMacro(dirImagenBase, carpetaSkin, paqueteBase)
        self.__imagenBottomMoving(dirImagenBase, carpetaSkin, paqueteBase)
        self.__imagenTop(dirImagenBase, carpetaSkin, paqueteBase)

        copy_tree(self.CARPETA_PLANTILLAS.joinpath(paqueteBase, "battery").__str__(),
                  carpetaSkin.joinpath("battery").__str__())

        copy_tree(self.CARPETA_PLANTILLAS.joinpath(paqueteBase, "grf").__str__(),
                  carpetaSkin.joinpath("grf").__str__())

        copy_tree(self.CARPETA_PLANTILLAS.joinpath(paqueteBase, "quickmenu").__str__(),
                  carpetaSkin.joinpath("quickmenu").__str__())

        copy_tree(self.CARPETA_PLANTILLAS.joinpath(paqueteBase, "ui").__str__(),
                  carpetaSkin.joinpath("ui").__str__())

        copy_tree(self.CARPETA_PLANTILLAS.joinpath(paqueteBase, "volume").__str__(),
                  carpetaSkin.joinpath("volume").__str__())

        copy_file(self.CARPETA_PLANTILLAS.joinpath(paqueteBase, "theme.ini").__str__(),
                  carpetaSkin.joinpath("theme.ini").__str__())


if __name__ == '__main__':
    model = modelo()
    model.seleccionarNombre()
    print(model.nombrePaquete)
    model.seleccionarImagen()
    model.crearSkin()

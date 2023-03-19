from pathlib import Path
from distutils.dir_util import copy_tree
from PIL import Image

carpetaImagenes = "Imagenes/"
carpetaPlantillas = carpetaImagenes + "Plantillas/"
carpetaSkins = "Skins/"


def guardarImagen(dirImagen: str, dirSalida: str, nombreSalida: str):
    """
    Parameters
    ----------
    dirImagenBase : str
        Directorio que de la imagen que va a ajustar al formato necesitado.

    dirSalida : str
        Carpeta de ale que se va a mover la imagen.
    
    nombreSalida : str
        Nombre que va a tener la imagen en la carpeta de destino.
    """
    tamanoImagen = (256, 192)
    Path(dirSalida).mkdir(parents=True, exist_ok=True)
    with Image.open(dirImagen) as image:
        image = image.resize(tamanoImagen)
        with image.quantize(colors=256, method=2) as converted:
            converted.save(dirSalida + nombreSalida)


def imagenBottomMoving(dirImagenBase: str, carpetaSkin: Path):
    """
    Parameters
    ----------
    dirImagenBase : str
        Directorio que de la imagen que se usara como base para el paquete.

    carpetaSkin : Path
        Carpeta de la skin en donde se van a guardar la imagen bottom_moving.
    """

    temp = Path(".temp")
    temp.mkdir(parents=True, exist_ok=True)
    dirImagenTemp = temp.joinpath("temp.png")

    with Image.open(dirImagenBase) as imagenBase:
        reescalada = imagenBase.resize((256, 192))
        with Image.open(carpetaPlantillas + "white/background/bottom_moving.png") as bottomMoving:
            reescalada.paste(bottomMoving, (0, 0), bottomMoving)
        reescalada.save(dirImagenTemp)
        reescalada.close()

    guardarImagen(dirImagenTemp.__str__(), carpetaSkin.__str__() +
                  "/background/", "bottom_moving.png")
    dirImagenTemp.unlink()
    temp.rmdir()


def imagenBottomBubble(dirImagenBase: str, carpetaSkin: Path):
    """
    Parameters
    ----------
    dirImagenBase : str
        Directorio que de la imagen que se usara como base para el paquete.

    carpetaSkin : Path
        Carpeta de la skin en donde se van a guardar la imagen bottom_bubble.
    """

    temp = Path(".temp")
    temp.mkdir(parents=True, exist_ok=True)
    dirImagenTemp = temp.joinpath("temp.png")

    with Image.open(dirImagenBase) as imagenBase:
        reescalada = imagenBase.resize((256, 192))
        with Image.open(carpetaPlantillas + "white/background/bottom_bubble.png") as bottomBubble:
            reescalada.paste(bottomBubble, (0, 0), bottomBubble)
        reescalada.save(dirImagenTemp)
        reescalada.close()

    guardarImagen(dirImagenTemp.__str__(), carpetaSkin.__str__() +
                  "/background/", "bottom_bubble.png")
    dirImagenTemp.unlink()
    temp.rmdir()


def imagenBottomBubbleMacro(dirImagenBase: str, carpetaSkin: Path):
    """
    Parameters
    ----------
    dirImagenBase : str
        Directorio que de la imagen que se usara como base para el paquete.

    carpetaSkin : Path
        Carpeta de la skin en donde se van a guardar la imagen bottom_bubble_macro.
    """

    temp = Path(".temp")
    temp.mkdir(parents=True, exist_ok=True)
    dirImagenTemp = temp.joinpath("temp.png")

    with Image.open(dirImagenBase) as imagenBase:
        reescalada = imagenBase.resize((256, 192))
        with Image.open(carpetaPlantillas + "white/background/bottom_bubble_macro.png") as bottomBubbleMacro:
            reescalada.paste(bottomBubbleMacro, (0, 0), bottomBubbleMacro)
        reescalada.save(dirImagenTemp)
        reescalada.close()

    guardarImagen(dirImagenTemp.__str__(), carpetaSkin.__str__() +
                  "/background/", "bottom_bubble_macro.png")
    dirImagenTemp.unlink()
    temp.rmdir()


def imagenBottom(dirImagenBase: str, carpetaSkin: Path):
    """
    Parameters
    ----------
    dirImagenBase : str
        Directorio que de la imagen que se usara como base para el paquete.

    carpetaSkin : Path
        Carpeta de la skin en donde se van a guardar la imagen bottom.
    """

    temp = Path(".temp")
    temp.mkdir(parents=True, exist_ok=True)
    dirImagenTemp = temp.joinpath("temp.png")

    with Image.open(dirImagenBase) as imagenBase:
        reescalada = imagenBase.resize((256, 192))
        with Image.open(carpetaPlantillas + "white/background/bottom.png") as bottom:
            reescalada.paste(bottom, (0, 0), bottom)
        reescalada.save(dirImagenTemp)
        reescalada.close()

    guardarImagen(dirImagenTemp.__str__(), carpetaSkin.__str__() +
                  "/background/", "bottom.png")
    dirImagenTemp.unlink()
    temp.rmdir()


def imagenTop(dirImagenBase: str, carpetaSkin: Path):
    """
    Parameters
    ----------
    dirImagenBase : str
        Directorio que de la imagen que se usara como base para el paquete.

    carpetaSkin : Path
        Carpeta de la skin en donde se van a guardar la imagen top.
    """

    guardarImagen(carpetaPlantillas + "white/background/top.png", carpetaSkin.__str__() +
                  "/background/", "top.png")


def crearPaquete(dirImagenBase: str, nombrePaquete: str = "white", paqueteBase: str = "white"):
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

    carpetaSkin = Path(carpetaSkins + nombrePaquete)
    carpetaSkin.mkdir(parents=True, exist_ok=True)
    imagenBottom(dirImagenBase, carpetaSkin)
    imagenBottomBubble(dirImagenBase, carpetaSkin)
    imagenBottomBubbleMacro(dirImagenBase, carpetaSkin)
    imagenBottomMoving(dirImagenBase, carpetaSkin)
    imagenTop(dirImagenBase, carpetaSkin)
    copy_tree(carpetaPlantillas + "white/battery",
              carpetaSkin.__str__()+"/battery")
    copy_tree(carpetaPlantillas + "white/grf", carpetaSkin.__str__()+"/grf")
    copy_tree(carpetaPlantillas + "white/quickmenu",
              carpetaSkin.__str__()+"/quickmenu")
    copy_tree(carpetaPlantillas + "white/ui", carpetaSkin.__str__()+"/ui")
    copy_tree(carpetaPlantillas + "white/volume",
              carpetaSkin.__str__()+"/volume")

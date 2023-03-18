from pathlib import Path
from PIL import Image

carpetaImagenes = "Imagenes/"
carpetaPlantillas = carpetaImagenes + "Plantillas/"
carpetaSkins = "Skins/"

def guardarImagen(dirImagen: str, dirSalida: str, nombreSalida: str):
    tamanoImagen = (256, 192)
    Path(dirSalida).mkdir(parents=True, exist_ok=True)
    with Image.open(dirImagen) as image:
        image = image.resize(tamanoImagen)
        with image.quantize(colors=256, method=2) as converted:
            converted.save(dirSalida + nombreSalida)


def imagenBottomMoving(dirImagenBase: str, carpetaSkin: Path):
    temp = Path(".temp")
    temp.mkdir(parents=True, exist_ok=True)
    dirImagenTemp = temp.joinpath("temp.png")

    with Image.open(dirImagenBase) as imagenBase:
        reescalada = imagenBase.resize((256, 192))
        with Image.open(carpetaPlantillas + "white/background/bottom_moving.png") as bottomMoving:
            reescalada.paste(bottomMoving, (0, 0), bottomMoving)
        reescalada.save(dirImagenTemp)

    guardarImagen(dirImagenTemp.__str__(), carpetaSkin.__str__() +
                  "/background/", "bottom_moving.png")
    dirImagenTemp.unlink()
    temp.rmdir()


def imagenBottomBubble(dirImagenBase: str, carpetaSkin: Path):
    temp = Path(".temp")
    temp.mkdir(parents=True, exist_ok=True)
    dirImagenTemp = temp.joinpath("temp.png")

    with Image.open(dirImagenBase) as imagenBase:
        reescalada = imagenBase.resize((256, 192))
        with Image.open(carpetaPlantillas + "white/background/bottom_bubble.png") as bottomBubble:
            reescalada.paste(bottomBubble, (0, 0), bottomBubble)
        reescalada.save(dirImagenTemp)

    guardarImagen(dirImagenTemp.__str__(), carpetaSkin.__str__() +
                  "/background/", "bottom_bubble.png")
    dirImagenTemp.unlink()
    temp.rmdir()


def imagenBottomBubbleMacro(dirImagenBase: str, carpetaSkin: Path):
    temp = Path(".temp")
    temp.mkdir(parents=True, exist_ok=True)
    dirImagenTemp = temp.joinpath("temp.png")

    with Image.open(dirImagenBase) as imagenBase:
        reescalada = imagenBase.resize((256, 192))
        with Image.open(carpetaPlantillas + "white/background/bottom_bubble_macro.png") as bottomBubbleMacro:
            reescalada.paste(bottomBubbleMacro, (0, 0), bottomBubbleMacro)
        reescalada.save(dirImagenTemp)

    guardarImagen(dirImagenTemp.__str__(), carpetaSkin.__str__() +
                  "/background/", "bottom_bubble_macro.png")
    dirImagenTemp.unlink()
    temp.rmdir()


def imagenBottom(dirImagenBase: str, carpetaSkin: Path):
    temp = Path(".temp")
    temp.mkdir(parents=True, exist_ok=True)
    dirImagenTemp = temp.joinpath("temp.png")

    with Image.open(dirImagenBase) as imagenBase:
        reescalada = imagenBase.resize((256, 192))
        with Image.open(carpetaPlantillas + "white/background/bottom.png") as bottom:
            reescalada.paste(bottom, (0, 0), bottom)
        reescalada.save(dirImagenTemp)

    guardarImagen(dirImagenTemp.__str__(), carpetaSkin.__str__() +
                  "/background/", "bottom.png")
    dirImagenTemp.unlink()
    temp.rmdir()


def imagenTop(dirImagenBase: str, carpetaSkin: Path):
    guardarImagen(carpetaPlantillas + "white/background/top.png", carpetaSkin.__str__() +
                  "/background/", "top.png")


def crearPaquete(dirImagenBase: str, nombrePaquete: str = "white", paqueteBase: str = ""):
    carpetaSkin = Path(carpetaSkins + nombrePaquete + "/")
    carpetaSkin.mkdir(parents=True, exist_ok=True)
    imagenBottom(dirImagenBase, carpetaSkin)
    imagenBottomBubble(dirImagenBase, carpetaSkin)
    imagenBottomBubbleMacro(dirImagenBase, carpetaSkin)
    imagenBottomMoving(dirImagenBase, carpetaSkin)
    imagenTop(dirImagenBase, carpetaSkin)
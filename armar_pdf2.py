"""
Arma un PDF tipo carrusel SOLO con las figuras (para publicar en LinkedIn).
Correr DESPUES de ejecutar la notebook (que genera los PNG).

Orden de esta publicacion: DEM -> direcciones de flujo -> red de drenaje.
Este script va APARTE del repo: agrega '*.pdf' a tu .gitignore si no querés subirlo.
"""
from PIL import Image

# Orden de las laminas (editable: reordena, comenta o agrega).
IMAGENES = [
    "dem_original.png",      # 1. Modelo de Elevacion Digital
    "flujo_direccion.png",   # 2. Direcciones de flujo (D8)
    "mapa_red.png",          # 3. Red de drenaje
]

SALIDA = "suquia_paso_a_paso.pdf"
FONDO  = (13, 8, 38)   # #0d0826, igual al fondo de los graficos

ims = [Image.open(f).convert("RGB") for f in IMAGENES]

# Lienzo uniforme (todas las paginas del mismo tamano), imagen centrada
W = max(i.width for i in ims)
H = max(i.height for i in ims)
paginas = []
for im in ims:
    lienzo = Image.new("RGB", (W, H), FONDO)
    lienzo.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
    paginas.append(lienzo)

paginas[0].save(SALIDA, save_all=True, append_images=paginas[1:], resolution=220.0)
print(f"Listo: {SALIDA}  ({len(paginas)} paginas)")
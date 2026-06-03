"""
Arma un PDF tipo carrusel SOLO con las figuras (para publicar en LinkedIn).
Correr DESPUES de ejecutar la notebook (que genera los PNG).

Este script va APARTE del repo: agrega '*.pdf' a tu .gitignore si no querés subirlo.
"""
from PIL import Image

# Orden de las laminas. La red de drenaje va primera.
# Comentá / reordená las que no quieras en el carrusel.
IMAGENES = [
    "mapa_red.png",          # 1. Red de drenaje (portada)
    "dem_original.png",      # 2. El dato de partida (DEM Copernicus)
    "hillshade.png",         # 3. Relieve sombreado
    "mapa_subcuencas.png",   # 4. Subcuencas
    "perfil_suquia.png",     # 5. Perfil del cauce principal
    # "flujo_direccion.png", # (opcional, mas tecnica)
]

SALIDA = "suquia_publicacion.pdf"
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

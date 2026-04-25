import sys
import os
from PIL import Image

def crear_icono(nombre_imagen):
    try:
        # 1. Cargar la imagen
        img = Image.open(nombre_imagen)
        
        # 2. Generar el nombre de salida (cambia la extensión a .ico)
        nombre_salida = os.path.splitext(nombre_imagen)[0] + ".ico"
        
        # 3. Definir tamaños estándar de Windows
        tamanos = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        
        # 4. Guardar
        img.save(nombre_salida, sizes=tamanos)
        print(f"✅ ¡Éxito! Icono guardado como: {nombre_salida}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Verificamos si pasaste un argumento
    if len(sys.argv) > 1:
        crear_icono(sys.argv[1])
    else:
        print("⚠️ Uso: python convertidor.py nombre_de_tu_imagen.png")

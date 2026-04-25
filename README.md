# Create ico from png
Es una utilidad básica para crear un archivo ICO (.ico) desde una imagen PNG (.png).

## Prerrequisitos
1. Es necesario contar con Python3 instalado.

## Modo de uso
1. Descarga el repositorio.
2. Copia el/los archivo/s PNG en la raíz del directorio donde está el fichero create-ico.py
3. Crea y activa tu venv  
    `python -m venv .venv`  
    **Windows:**  
    `.venv\Scripts\activate`  
    **macOS / Linux:**  
    `source .venv/bin/activate`
4. Instala la dependencia del requirements.txt  
    `pip install -r requirements.txt`
5. En una terminal, ejecuta el script  
   `python create-ico.py nombre_imagen.png`
6. El archivo .ico resultante será depositado en el mismo directorio.

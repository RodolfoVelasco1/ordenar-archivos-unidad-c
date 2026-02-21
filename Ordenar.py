import shutil
from pathlib import Path
import os


nombre_script = Path(__file__).name

extensiones_imagenes = {'.jpg', '.jpeg', '.png', '.gif', '.psd', '.bmp', '.tiff', '.webp', '.svg', '.heic', '.jfif'}
extensiones_videos = {'.mp4', '.mkv', '.avi', '.wmv', '.mov', '.ts'}
extensiones_audios = {'.mp3', '.m4a', '.aac', '.wav', '.ac3', '.flac', '.ogg', '.wma', '.aiff'}
extensiones_documentos = {'.pdf', '.txt', '.docx', '.rtf', '.xlsx', '.pptx', '.doc', '.xls', '.ppt', '.epub'}

todas_extensiones = extensiones_imagenes | extensiones_videos | extensiones_audios | extensiones_documentos

def mover_imagenes():
    carpeta_origen = Path.cwd()   
    carpeta_destino = Path.home() / "Pictures"
    carpeta_destino.mkdir(exist_ok=True)
    
    if carpeta_origen == carpeta_destino:
        print("Imágenes: Finalizado.")
        return
 
    for archivo in carpeta_origen.iterdir():
        if archivo.is_file() and archivo.suffix.lower() in extensiones_imagenes:
            try:
                directorio_final = carpeta_destino / archivo.name
                
                if directorio_final.exists():
                    nombre_archivo = archivo.stem
                    extension = archivo.suffix
                    numero = 1
                    while directorio_final.exists():
                        archivo_numerado = (f"{nombre_archivo}_{numero}{extension}")
                        directorio_final = carpeta_destino / archivo_numerado
                        numero+=1

                shutil.move(str(archivo), str(directorio_final))

            except Exception as e:
                print(f"Error con el archivo {archivo.name}: {e}")

    print(f"Imágenes: Finalizado.")

def mover_videos():
    carpeta_origen = Path.cwd()   
    carpeta_destino = Path.home() / "Videos"
    carpeta_destino.mkdir(exist_ok=True)
     
    if carpeta_origen == carpeta_destino:
        print("Videos: Finalizado.")
        return
 
    for archivo in carpeta_origen.iterdir():
        if archivo.is_file() and archivo.suffix.lower() in extensiones_videos:
            try:
                directorio_final = carpeta_destino / archivo.name
                
                if directorio_final.exists():
                    nombre_archivo = archivo.stem
                    extension = archivo.suffix
                    numero = 1
                    while directorio_final.exists():
                        archivo_numerado = (f"{nombre_archivo}_{numero}{extension}")
                        directorio_final = carpeta_destino / archivo_numerado
                        numero+=1

                shutil.move(str(archivo), str(directorio_final))

            except Exception as e:
                print(f"Error con el archivo {archivo.name}: {e}")

    print(f"Videos: Finalizado.")

def mover_audios():
    carpeta_origen = Path.cwd()   
    carpeta_destino = Path.home() / "Music"
    carpeta_destino.mkdir(exist_ok=True)
    
    if carpeta_origen == carpeta_destino:
        print("Audios: Finalizado.")
        return
 
    for archivo in carpeta_origen.iterdir():
        if archivo.is_file() and archivo.suffix.lower() in extensiones_audios:
            try:
                directorio_final = carpeta_destino / archivo.name
                
                if directorio_final.exists():
                    nombre_archivo = archivo.stem
                    extension = archivo.suffix
                    numero = 1
                    while directorio_final.exists():
                        archivo_numerado = (f"{nombre_archivo}_{numero}{extension}")
                        directorio_final = carpeta_destino / archivo_numerado
                        numero+=1

                shutil.move(str(archivo), str(directorio_final))

            except Exception as e:
                print(f"Error con el archivo {archivo.name}: {e}")

    print(f"Audios: Finalizado.")

def mover_documentos():
    carpeta_origen = Path.cwd()   
    carpeta_destino = Path.home() / "Documents"
    carpeta_destino.mkdir(exist_ok=True)
    
    if carpeta_origen == carpeta_destino:
        print("Documentos: Finalizado.")
        return
 
    for archivo in carpeta_origen.iterdir():
        if archivo.is_file() and archivo.suffix.lower() in extensiones_documentos:
            try:
                directorio_final = carpeta_destino / archivo.name
                
                if directorio_final.exists():
                    nombre_archivo = archivo.stem
                    extension = archivo.suffix
                    numero = 1
                    while directorio_final.exists():
                        archivo_numerado = (f"{nombre_archivo}_{numero}{extension}")
                        directorio_final = carpeta_destino / archivo_numerado
                        numero+=1

                shutil.move(str(archivo), str(directorio_final))

            except Exception as e:
                print(f"Error con el archivo {archivo.name}: {e}")

    print(f"Documentos: Finalizado.")

def mover_otros():
    carpeta_origen = Path.cwd()   
    carpeta_destino = Path.home() / "Downloads"

    escritorio = Path.home() / "Desktop"
    
    if carpeta_origen == escritorio:
        print("Estás en el Escritorio. 'Mover Otros' se ha desactivado.")
        return
    
    carpeta_destino.mkdir(exist_ok=True)
    
    if carpeta_origen == carpeta_destino:
        print("Otros: Finalizado.")
        return
 
    for archivo in carpeta_origen.iterdir():
        if archivo.is_file() and archivo.name != nombre_script and archivo.suffix.lower() not in todas_extensiones:
            try:
                directorio_final = carpeta_destino / archivo.name
                
                if directorio_final.exists():
                    nombre_archivo = archivo.stem
                    extension = archivo.suffix
                    numero = 1
                    while directorio_final.exists():
                        archivo_numerado = (f"{nombre_archivo}_{numero}{extension}")
                        directorio_final = carpeta_destino / archivo_numerado
                        numero+=1

                shutil.move(str(archivo), str(directorio_final))

            except Exception as e:
                print(f"Error con el archivo {archivo.name}: {e}")

    print(f"Otros: Finalizado.")
    
if __name__ == "__main__":
    mover_imagenes()
    mover_videos()
    mover_audios()
    mover_documentos()
    mover_otros()

🧹 Organizador Automático de Archivos (Python)
Un script inteligente escrito en Python que limpia y organiza automáticamente cualquier carpeta desordenada dentro de la unidad C:. Clasifica los archivos según su extensión y los mueve a las carpetas predeterminadas de tu sistema (Imágenes, Videos, Música, Documentos y Descargas).

✨ Características Principales
Clasificación Inteligente: Detecta el tipo de archivo y lo envía instantáneamente a su carpeta correspondiente.

Protección Anti-Sobrescritura: Si en el destino ya existe un archivo con el mismo nombre, el script lo renombra automáticamente usando un sistema numérico (ej. foto.jpg -> foto_1.jpg -> foto_2.jpg).

Seguro de Escritorio (Desktop Safe): Incluye un "freno de mano" que desactiva el movimiento de archivos varios si se ejecuta en el Escritorio, protegiendo así tus accesos directos (.lnk) y configuraciones.

Autoconservación: El script es capaz de reconocerse a sí mismo; nunca se moverá a otra carpeta durante la limpieza.

Efecto "Aspiradora": Cualquier formato de archivo desconocido (ej. .zip, .exe, .rar) es enviado automáticamente a la carpeta de Descargas para que lo revises manualmente, dejando tu carpeta de origen 100% limpia.

📂 ¿Dónde va cada archivo?
El script incluye listas de extensiones predefinidas que puedes modificar fácilmente:

🖼️ Imágenes (~/Pictures): .jpg, .jpeg, .png, .gif, .psd, .bmp, .tiff, .webp, .svg, .heic

🎬 Videos (~/Videos): .mp4, .mkv, .avi, .wmv, .mov, .ts

🎵 Audios (~/Music): .mp3, .m4a, .aac, .wav, .ac3, .flac, .ogg, .wma, .aiff

📄 Documentos (~/Documents): .pdf, .txt, .docx, .rtf, .xlsx, .pptx, .doc, .xls, .ppt, .epub

📦 Otros (~/Downloads): Todo lo que no pertenezca a las listas anteriores se mueve a la carpeta de Descargas.

🚀 Cómo usarlo
Asegúrate de tener Python 3 instalado en tu computadora. No necesitas instalar librerías externas, ya que utiliza pathlib y shutil que vienen por defecto.

Descarga el archivo .py (ej. organizar.py).

Coloca el archivo dentro de la carpeta que deseas limpiar.

Ejecuta el script:

Haciendo doble clic sobre el archivo (en Windows).

O desde la terminal ejecutando: python organizar.py

¡Listo! Revisa tus carpetas del sistema, todo estará organizado.

⚙️ Compatibilidad
Gracias al uso de Path.home(), este script es universal y detectará tu carpeta de usuario sin importar si usas Windows, macOS o Linux.
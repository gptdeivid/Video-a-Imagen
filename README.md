# 🎬 Extractor de Frames de Video

**Una aplicación sencilla y visual para convertir tus videos en imágenes individuales**

## 📖 ¿Qué hace este programa?

Este programa toma un video (como .mp4, .mov, .avi, etc.) y lo convierte en muchas imágenes PNG individuales. Cada imagen es un "frame" o fotograma del video.

**Ejemplo:**
- Tienes un video llamado `vacaciones.mp4`
- El programa crea una carpeta `vacaciones_frames/` con:
  - `frame_0000.png` (primer fotograma)
  - `frame_0001.png` (segundo fotograma)
  - `frame_0002.png` (tercer fotograma)
  - ... y así sucesivamente hasta el final del video

## ✨ Características

✅ **Interfaz Web Moderna** - No necesitas escribir comandos complicados  
✅ **Muy Fácil de Usar** - Solo haz click en el video y presiona un botón  
✅ **Instalación Automática** - Todo se instala solo la primera vez  
✅ **Compatible con Múltiples Formatos** - .mp4, .mov, .avi, .mkv, .flv, .wmv  
✅ **Organizado Automáticamente** - Los frames se guardan en carpetas con el nombre del video

## 🚀 Inicio Rápido (3 Pasos)

### Paso 1: Verifica que tienes Python

Python es un programa gratuito que necesita estar instalado en tu computadora.

**¿Cómo saber si ya lo tienes?**
1. Busca "cmd" en Windows y ábrelo
2. Escribe: `python --version`
3. Si ves un número, ¡ya lo tienes! Si no, descárgalo aquí: [python.org/downloads](https://www.python.org/downloads/)

> ⚠️ **MUY IMPORTANTE**: Cuando instales Python, marca la casilla que dice **"Add Python to PATH"**

### Paso 2: Inicia la aplicación

**Opción A - La más fácil (RECOMENDADA):**

Haz doble click en:
```
⭐ HACER DOBLE CLICK AQUI.bat
```

**Opción B - Directa:**

Haz doble click en:
```
INICIAR_APP.bat
```

### Paso 3: Usa la interfaz web

1. Automáticamente se abrirá tu navegador web
2. Verás una lista de videos disponibles
3. Haz click en el video que quieras procesar
4. Presiona el botón **"Extraer Frames"**
5. ¡Espera y listo! 🎉

## 📁 ¿Dónde pongo mis videos?

Coloca tus archivos de video en la **misma carpeta** donde están todos estos archivos del programa.

## 📂 ¿Dónde encuentro los resultados?

Los frames extraídos se guardan en una carpeta nueva con el nombre:
```
nombre_de_tu_video_frames/
```

Por ejemplo, si procesas `mi_video.mp4`, encontrarás los frames en la carpeta `mi_video_frames/`

## 🎯 ¿Para qué sirve esto?

Este programa es útil para:

- 🔍 **Analizar videos** fotograma por fotograma
- 🤖 **Entrenar inteligencia artificial** con imágenes de videos
- 🎨 **Crear animaciones** o GIFs personalizados
- 📊 **Detectar objetos** en videos
- 🎬 **Control de calidad** en producción de video
- 📚 **Crear datasets** de imágenes para proyectos

## 📚 Archivos de Ayuda

Si es tu primera vez, consulta estos archivos:

| Archivo | Para qué sirve |
|---------|---------------|
| 📖 **INSTRUCCIONES.html** | Guía visual paso a paso (¡ÁBRELA PRIMERO!) |
| 🚀 **EMPIEZA AQUI.txt** | Índice de todos los archivos |
| 📄 **LEEME.txt** | Resumen rápido |
| 📄 **INSTRUCCIONES_FACILES.txt** | Guía detallada en texto |

## ❓ Solución de Problemas

### "Python no está instalado"
➡️ Descarga e instala Python desde [python.org](https://www.python.org/downloads/)  
➡️ Recuerda marcar "Add Python to PATH" durante la instalación

### "No veo videos en la lista"
➡️ Asegúrate de que tus videos estén en la misma carpeta que la aplicación  
➡️ Haz click en el botón "🔄 Actualizar lista de videos"

### "La página no carga"
➡️ Verifica que la ventana negra (terminal) siga abierta  
➡️ Intenta abrir manualmente: `http://localhost:5000`

### "Error al extraer frames"
➡️ Verifica que el archivo de video no esté dañado  
➡️ Intenta con otro video para descartar problemas

## 💻 Para Usuarios Técnicos

Si sabes usar la línea de comandos:

```bash
# Instalar dependencias
pip install -r requirements.txt

# Iniciar servidor web
python app.py

# O usar el script original
python extract_frames.py ruta/al/video.mp4
```

## 🛠️ Tecnologías Utilizadas

- **Flask** - Framework web para la interfaz
- **MoviePy** - Procesamiento de video
- **Pillow** - Manipulación de imágenes
- **ImageIO** - Guardado de imágenes

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras errores o tienes ideas para mejorar el programa:

1. Abre un "Issue" en GitHub describiendo el problema o sugerencia
2. Si sabes programar, puedes hacer un "Pull Request" con tus mejoras

## 🙏 Agradecimientos

Este proyecto utiliza la biblioteca [MoviePy](https://zulko.github.io/moviepy/) para el procesamiento de video.

---

## ⚠️ Nota Importante

- Asegúrate de tener permisos sobre los videos que procesas
- Respeta los derechos de autor del contenido
- La extracción puede consumir bastante espacio en disco
- El tiempo de procesamiento depende de la duración y calidad del video

---

**💡 Desarrollado para facilitar el trabajo con videos - Sin complicaciones técnicas**

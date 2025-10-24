# 🎬 Frame Extractor - Versión Web

Aplicación web sencilla para extraer frames de videos y guardarlos como imágenes PNG individuales.

## 🌟 Características

- **Interfaz Web Intuitiva**: Interfaz moderna y fácil de usar
- **Selección Simple**: Visualiza y selecciona videos de la carpeta con un click
- **Extracción Rápida**: Genera todas las capturas del video seleccionado
- **Múltiples Formatos**: Soporta .mp4, .mov, .avi, .mkv, .flv, .wmv
- **Organización Automática**: Los frames se guardan en carpetas con el nombre del video

## 📋 Requisitos

- Python 3.7 o superior
- Las dependencias listadas en `requirements.txt`

## 🚀 Instalación

1. **Clona o descarga este repositorio**

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Uso

### Modo Web (Recomendado)

1. **Coloca tus videos** en la misma carpeta donde está `app.py`

2. **Ejecuta la aplicación web:**
   ```bash
   python app.py
   ```

3. **Abre tu navegador** y ve a:
   ```
   http://localhost:5000
   ```

4. **Selecciona un video** de la lista y haz click en "Extraer Frames"

5. **Los frames se guardarán** en una carpeta con el nombre: `nombre_del_video_frames/`

### Modo Línea de Comandos (Original)

También puedes usar el script original:

```bash
python extract_frames.py ruta/al/video.mp4
```

## 📁 Estructura de Salida

Cuando extraes frames de un video llamado `mi_video.mp4`, se crea la siguiente estructura:

```
mi_video_frames/
├── frame_0000.png
├── frame_0001.png
├── frame_0002.png
└── ...
```

## 🎯 Casos de Uso

- **Análisis de Video**: Descompón videos en frames individuales para análisis detallado
- **Machine Learning**: Crea datasets de imágenes para entrenamiento de modelos
- **Detección de Objetos**: Extrae frames para etiquetar objetos
- **Control de Calidad**: Inspecciona videos frame por frame
- **Creación de Thumbnails**: Genera previsualizaciones de videos

## 🛠️ Tecnologías

- **Flask**: Framework web ligero
- **MoviePy**: Procesamiento de video
- **Pillow**: Manipulación de imágenes
- **ImageIO**: Guardado de imágenes

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## ⚠️ Notas Importantes

- Asegúrate de tener permisos sobre los videos que procesas
- La extracción de frames puede consumir bastante espacio en disco
- El tiempo de procesamiento depende de la duración y resolución del video

## 🙏 Agradecimientos

Este proyecto utiliza la biblioteca [MoviePy](https://zulko.github.io/moviepy/) para el procesamiento de video.

---

**Desarrollado con ❤️ para facilitar el trabajo con videos**

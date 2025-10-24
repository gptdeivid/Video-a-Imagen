import os
from flask import Flask, render_template, request, jsonify
from moviepy import VideoFileClip
import imageio
from PIL import Image

app = Flask(__name__)

# Carpeta donde se buscan los videos
VIDEO_FOLDER = os.path.dirname(os.path.abspath(__file__))

def get_videos():
    """Obtiene la lista de videos disponibles en la carpeta"""
    video_extensions = ('.mov', '.mp4', '.avi', '.mkv', '.flv', '.wmv')
    videos = []
    
    for file in os.listdir(VIDEO_FOLDER):
        if file.lower().endswith(video_extensions):
            videos.append(file)
    
    return sorted(videos)

def extract_frames(video_path):
    """Extrae frames de un video"""
    try:
        # Verificar si el archivo existe
        if not os.path.exists(video_path):
            return {"success": False, "error": f"Archivo no encontrado: {video_path}"}
        
        # Cargar el video
        video_clip = VideoFileClip(video_path)
        
        # Obtener tamaño del video
        value = video_clip.size
        
        # Crear directorio para guardar los frames
        frames_output_dir = os.path.splitext(video_path)[0] + '_frames'
        os.makedirs(frames_output_dir, exist_ok=True)
        
        # Extraer frames
        frame_count = 0
        for idx, frame in enumerate(video_clip.iter_frames()):
            # Redimensionar el frame
            frame_img = Image.fromarray(frame)
            frame_img = frame_img.resize((value[0], value[1]), Image.LANCZOS)
            
            frame_path = os.path.join(frames_output_dir, f'frame_{idx:04d}.png')
            imageio.imsave(frame_path, frame_img)
            frame_count = idx + 1
        
        # Cerrar el video
        video_clip.reader.close()
        
        return {
            "success": True, 
            "message": f"Se extrajeron {frame_count} frames exitosamente",
            "output_folder": os.path.basename(frames_output_dir)
        }
        
    except Exception as e:
        return {"success": False, "error": f"Error: {str(e)}"}

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/videos')
def api_videos():
    """API para obtener la lista de videos"""
    videos = get_videos()
    return jsonify({"videos": videos})

@app.route('/api/extract', methods=['POST'])
def api_extract():
    """API para extraer frames de un video"""
    data = request.get_json()
    video_name = data.get('video')
    
    if not video_name:
        return jsonify({"success": False, "error": "No se especificó un video"})
    
    video_path = os.path.join(VIDEO_FOLDER, video_name)
    result = extract_frames(video_path)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

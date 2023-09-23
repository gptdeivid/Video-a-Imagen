import os
import sys
import moviepy.editor as mp
import imageio
from PIL import Image
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import AudioClip
from moviepy.editor import concatenate_videoclips,concatenate_audioclips,TextClip,CompositeVideoClip
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize

from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex

def extract_frames(video_path):
    try:
        # Check if the file exists
        if not os.path.exists(video_path):
            print(f"File not found: {video_path}")
        elif not video_path.lower().endswith(('.mov', '.mp4', '.avi')):
            print("Unsupported file format. Please provide a .mov, .mp4, or .avi video file.")
        else:
            # Load the video clip
            video_clip = mp.VideoFileClip(video_path)
            
            # getting clip size
            value = video_clip.size
            
            # Create a directory to save the frames
            frames_output_dir = os.path.splitext(video_path)[0] + '_frames'
            os.makedirs(frames_output_dir, exist_ok=True)

            # Extract frames and save them as PNG images
            for idx, frame in enumerate(video_clip.iter_frames()):
                # Resize the frame to the desired size
                frame = Image.fromarray(frame)
                frame = frame.resize((value[1], value[0]), Image.ANTIALIAS)
                
                frame_path = os.path.join(frames_output_dir, f'frame_{idx:04d}.png')
                imageio.imsave(frame_path, frame)
                
                print(f'Exported frame {idx + 1} to {frame_path}')

            # Close the video clip
            video_clip.reader.close()
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py path_to_video.mov")
    else:
        video_path = sys.argv[1]
        extract_frames(video_path)
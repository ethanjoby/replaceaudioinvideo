import sys
import os
from moviepy.editor import *


def display_help():
    print("Usage: python replace_audio.py [-h]")
    print("\nReplace the audio in a video file (mp4) with a provided audio file (wav or mp3).")
    print("Arguments:")
    print("  -h  Show this help message and exit.")



def calculate_speed_factor():
    video_file = "video.mp4"
    audio_file = "video1.mp3"

    if not (os.path.exists(video_file) and os.path.exists(audio_file)):
        print(f'Video file {video_file} or audio file {audio_file} not found.')
        return

    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)
    return audio.duration/video.duration
        
import subprocess
input_file = "video1.mp3"
output_file = "video.mp3"
speed_factor = calculate_speed_factor()

ffmpeg_command = [
    "ffmpeg",
    "-i", input_file,
    "-filter:a", f"atempo={speed_factor}",
    output_file
]
def replace_audio():
    current_folder = os.getcwd()
    video_file = "video.mp4"
    audio_file = "video.mp3"

    if not (os.path.exists(video_file) and os.path.exists(audio_file)):
        print(f'Video file {video_file} or audio file {audio_file} not found.')
        return

    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)
    video_with_new_audio = video.set_audio(audio)
    video_with_new_audio.write_videofile(os.path.join(current_folder, f'video_ad.mp4'))


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Error: This script does not take any command-line arguments.")
        display_help()
        sys.exit(1)

    if '-h' in sys.argv:
        display_help()
        sys.exit(0)
        
    print('Speed Factor:' + str(calculate_speed_factor()))
    subprocess.run(ffmpeg_command)
    replace_audio()


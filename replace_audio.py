import sys
import os
from moviepy.editor import *





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
    print('Speed Factor:' + str(calculate_speed_factor()))
    subprocess.run(ffmpeg_command)
    replace_audio()


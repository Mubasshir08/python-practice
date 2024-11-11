
import os
import shutil
from pytube import YouTube

def youtube_video_mp3(url : str):
    video_files = YouTube(url).streams.filter().get_audio_only()
    video_files.download()

    mp4_name : str = video_files.default_filename
    mp3_name : str = mp4_name.replace('.mp4', 'mp3')

    os.rename(mp4_name, mp3_name)
    shutil.move(mp3_name, 'audio')

def main():
    try:
        input_url : str = input("Give Your Url : \n")
        youtube_video_mp3(url = input_url)
        print('Finished !')
    except Exception as e:
        print(f'Something is wrong {e}')

main(); 
    
# Autor: makan leboss
# Email: makan.dianka@hotmail.com
# This script convert any video file.mp4 to audio file.mp3
# This script required module moviepy

import moviepy.editor as mp 

def  video_to_audio(video, audio):
    try:
        source = mp.VideoFileClip(r"{}".format(video))
        source.audio.write_audiofile(r"{}".format(audio))
    except AttributeError as error:
        print("\nUne Erreur s'est produite lors de l'exécution du code.\n Verifier bien si la video a de l'audio.\nsource de l'erreur: ", error)
        
print("\nPaste the full path of your video ")    
video = input("video's path: ")

print("\nEnter the full path of your audio's destination ")
audio = input("audio's path: ")

video_to_audio(video, audio)
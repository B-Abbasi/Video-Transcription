# -*- coding: utf-8 -*-

#@author: burhan abbasi

from moviepy.editor import VideoFileClip
from FilesInfo import FilesInfo  
      
class Vid2Aud:
    outputFolder= "\\audio-extract\\"
    # def __init__(self):
        # self.
    
    def extractAudioFromVideoFiles(path):
        vidFileNames= FilesInfo.getFileNames(path)
        
        print("FileNames in the location " +path+"  are :"   )
        print(vidFileNames)
        for name in vidFileNames:
            if (name=="audio-extract" or name=="transcript"):
                print(name)
                continue
            else:
                # Load the video
                print(path+"\\"+name)
                video = VideoFileClip(path+"\\"+name)
                # Extract the audio from the video
                audio_file = video.audio
                audio_file.write_audiofile(path+Vid2Aud.outputFolder+name+".wav")

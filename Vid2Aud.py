# -*- coding: utf-8 -*-
"""
@author: burhan abbasi
"""

import moviepy.editor as VideoFileClip
        
class Vid2Aud:
    def __init__(self, name):
        self.outputFolder= "audio-extract/"
    
    def extractAudioFromVideoFiles(self, path):
        vidFileNames= getFileNames(path)

        for name in vidFileNames:
          # Load the video
          video = VideoFileClip(path+name)
          # Extract the audio from the video
          audio_file = video.audio
          audio_file.write_audiofile(path+outputFolder+name+".wav")


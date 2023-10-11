# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 02:24:14 2023
@author: burhan
"""

from FilesInfo import FilesInfo
from Aud2Text import Aud2Text
from Vid2Aud import Vid2Aud


def main():
    print("Hello Worlds of Spyder")
    
    PROJECT_DIRECTORY = "E:\\Scripts\\Projects\\Video Transcription\\"
    
    VIDEO_SHORT_PATH= PROJECT_DIRECTORY +"video-short\\"
    AUDIO_SHORT_PATH= VIDEO_SHORT_PATH+"audioExtracts\\"
    TRANCRIPT_FILES_PATH=''
    
    
    
    # Extracting Audio From Videos
    Vid2Aud.extractAudioFromVideoFiles(VIDEO_SHORT_PATH)

    # GoogleSpeechRecognitionAPI(AUDIO_SHORT_PATH)
    

    

if __name__ == "__main__":
    main()



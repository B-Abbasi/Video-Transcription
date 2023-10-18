# -*- coding: utf-8 -*-

#@author: burhan

from Aud2Text import Aud2Text
from Vid2Aud import Vid2Aud


def main():
    print("Hello Worlds of Spyder")
    
    PROJECT_DIRECTORY = "E:\\Scripts\\Projects\\Video Transcription\\DataFiles"
    
    VIDEO_SHORT_PATH= PROJECT_DIRECTORY +"\\video-short"
    AUDIO_SHORT_PATH= VIDEO_SHORT_PATH+"\\audio-extract"
    TRANCRIPT_FILES_PATH=VIDEO_SHORT_PATH+"\\transcript"
        
    # Extracting Audio From Videos
    Vid2Aud.extractAudioFromVideoFiles(VIDEO_SHORT_PATH)

    # Extracting Text from Audio
    Aud2Text.GoogleSpeechRecognitionAPI(AUDIO_SHORT_PATH, TRANCRIPT_FILES_PATH)
        

if __name__ == "__main__":
    main()

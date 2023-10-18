# -*- coding: utf-8 -*-

#@author: burhan abbasi

from FilesInfo import FilesInfo
import speech_recognition as sr
import time

class Aud2Text:
  # !pip install SpeechRecognition

  def GoogleSpeechRecognitionAPI( audio_path, transcript_path):
    
    

    audFileNames= FilesInfo.getFileNames(audio_path)

    # using google speech recognition
    r = sr.Recognizer() #Initiаlize  reсоgnizer

    for audio in audFileNames:

      #Reading Audio file as source
      with sr.AudioFile(audio_path+'\\'+audio) as source:
        audio_text = r.listen(source)

        # recoginize_() method throws a request error if the API call is not successfull, using exception handling
        try:
            #text = r.recognize_google(audio_text)
            text='cricket and basketball as sports as well and'
            print(text)
            Aud2Text.writeTranscription(transcript_path+'\\',audio,text)
            
            time.sleep(3)
        except:
            print('Sorry.. run again...')


  def writeTranscription( path,filename, text):
    with open(path+filename+'.txt', 'w') as f:
      f.write(text)
      f.close()
      
      

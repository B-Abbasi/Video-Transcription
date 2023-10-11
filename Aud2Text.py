# -*- coding: utf-8 -*-
"""
@author: burhan abbasi
"""

class Aud2Text:
  # !pip install SpeechRecognition

  def GoogleSpeechRecognitionAPI(self, path):
    import speech_recognition as sr
    import time

    audFileNames= getFileNames(path)

    # using google speech recognition
    r = sr.Recognizer() #Initiаlize  reсоgnizer

    for audio in audFileNames:

      #Reading Audio file as source
      with sr.AudioFile(AUDIO_SHORT_PATH+audio) as source:
        audio_text = r.listen(source)

        # recoginize_() method throws a request error if the API call is not successfull, using exception handling
        try:
            text = r.recognize_google(audio_text)
            print(text)
            writeTranscription(AUDIO_SHORT_PATH+'Transcripts/GoogleSpeechRecognition/',audio,text)
            time.sleep(3)
        except:
            print('Sorry.. run again...')


  def writeTranscription(self, path,filename, text):
    with open(path+filename+'.txt', 'w') as f:
      f.write(text)
      f.close()
      
      
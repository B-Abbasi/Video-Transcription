# -*- coding: utf-8 -*-

#@author: Burhan Abbasi

#this function may be used for excuting code on google colab.
def connectDrive():
  #Access to Drive
  from google.colab import drive
  drive.mount ('/content/gdrive')

  # to attempt to forcibly remount
  # drive.mount("/content/gdrive", force_remount=True)

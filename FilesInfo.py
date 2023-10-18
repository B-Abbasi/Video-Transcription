# -*- coding: utf-8 -*-

#@author: burhan abbasi


class FilesInfo:
  def getFileNames( path):
    # import OS module
    import os

    # Get the list of all files and directories
    dir_list = os.listdir(path)

    # print(dir_list) # prints all files
    return dir_list

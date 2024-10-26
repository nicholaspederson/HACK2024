import cv2
import os
import pandas as pd

# Initialization
FILE_PATH = './'

for folder in os.listdir(FILE_PATH):
    files = os.listdir(FILE_PATH + '/' + folder)
    for file in files:
        if not os.path.isfile(folder + '/' + folder + '/' + file):
            continue
        if 'transcript' in file.lower():
            
             
    
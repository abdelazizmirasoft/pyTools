import cv2
import os,glob,re
from PIL import Image
from os import listdir,makedirs
from os.path import isfile,join

def convert_image(source_path, dest_path):
    image = cv2.imread(source_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    
    cv2.imwrite(dest_path, image_gray)
    print(f'Would convert {source_path} -> {dest_path}')

pwd = os.getcwd()
source_dir = os.path.join(pwd, 'img') # Source Folder
dest_dir = os.path.join(pwd, 'imgGray') # Destination Folder

for dirpath, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
        if filename.endswith('.jpg'):
            source_path = os.path.join(dirpath, filename)
            dest_path = os.path.join(dest_dir, os.path.relpath(dirpath, source_dir), filename)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            convert_image(source_path, dest_path)


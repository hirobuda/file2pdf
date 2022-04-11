from PIL import Image as img
from PIL import ImageFile
from os import listdir
from os import path
from natsort import natsorted

import sys
import numpy as np

ImageFile.LOAD_TRUNCATED_IMAGES = True

def list_images(path):
    list = listdir(str(path))
    for i in range(len(list)):
        if list[i].split('.')[1] in ["jpg", "png"]:
            list[i] = path+'/'+list[i]
    return natsorted(list)

while True:
    file = input("file with the images: ")
    
    images = list_images(str(file))
    to_pdf = []

    img1 = images[0]
    for i in range(len(images)):
        to_pdf.append(img.open(images[i]))

    for i in range(len(to_pdf)):
        width, height = to_pdf[i].width, to_pdf[i].height
        to_pdf[i] = to_pdf[i].resize((int(np.ceil(width*1.74)), int(np.ceil(height*1.41))), resample=img.Resampling.LANCZOS)
    pdf1_filename = input("final location: ")
    to_pdf[0].save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images = to_pdf)
    
    to_pdf.clear()
    images.clear()


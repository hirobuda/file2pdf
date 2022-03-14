from PIL import Image as img
from PIL import ImageFile
from os import listdir
from natsort import natsorted
import sys

ImageFile.LOAD_TRUNCATED_IMAGES = True

def list_images(path, ext):
    list = listdir(str(path))
    for i in range(len(list)):
        list[i] = path+'/'+list[i]
    return natsorted(list)

while True:
    file = input("file with the images: ")
    ext = input("image extension: ")

    imagens = list_images(str(file),ext)
    to_pdf = []

    img1 = imagens[0]
    for i in range(len(imagens)):
        to_pdf.append(img.open(imagens[i]))

    for i in range(len(to_pdf)):
        to_pdf[i] = to_pdf[i].resize((1700,2400), resample=img.ANTIALIAS)
    pdf1_filename = input("pdf name: ")
    to_pdf[0].save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images = to_pdf)


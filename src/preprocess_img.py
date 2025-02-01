#Script que recibe el arreglo proveniente de read_img.py, 
# realiza las siguientes modificaciones: resize a 512x512. 
# Conversión a escala de grises. ecualización del histograma con 
# CLAHEnormalización de la imagen entre 0 y 1. 
# conversión del arreglo de imagen a formato de batch (tensor).

import pydicom
import numpy as np
from PIL import Image
import cv2


def preprocess(array):
    array = cv2.resize(array, (512, 512))
    array = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))
    array = clahe.apply(array)
    array = array / 255
    array = np.expand_dims(array, axis=-1)
    array = np.expand_dims(array, axis=0)
    
    return array


#Es un módulo que integra los demás scripts y retorna solamente lo necesario 
# para ser visualizado en la interfaz gráfica. Retorna la clase, 
# la probabilidad y una imagen el mapa de calor generado por Grad-CAM.


import cv2
import numpy as np
from prediction import predict
from read_img import read_dicom_file, read_jpg_file


def prediction(array):
    #retorna la probabilidad
    return predict(array)

def read_dicom(path):
    #retorna la imagen 
    return read_dicom_file(path)

def read_jpg(path):
    #retorna la imagen 
    return read_jpg_file(path)


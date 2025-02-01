#Script que lee la imagen en formato DICOM para visualizarla en la interfaz gráfica. 
# Además, la convierte a arreglo para su preprocesamiento.
# Módulo encargado de la lectura de las imágenes

import os
import cv2
import numpy as np
import pydicom as dicom
from PIL import Image


def read_dicom_file(path):
   
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"El archivo {path} no existe.")

        img = dicom.dcmread(path)
        img_array = img.pixel_array

        # Normalización
        img2 = img_array.astype(float)
        if img2.max() > 0:
            img2 = (img2 - img2.min()) / (img2.max() - img2.min()) * 255.0
        img2 = np.uint8(img2)

        # escala de grises
        img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)

        return img_RGB, Image.fromarray(img_array)
    #error
    except Exception as e:
        print(f"Error al leer el archivo DICOM: {e}")
        return None, None


def read_jpg_file(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"El archivo {path} no existe.")

        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        if img is None:
            raise ValueError(
                "No se pudo leer la imagen")

        
        if len(img.shape) == 2:  # Imagen en escala de grises
            img2 = img
        else:
            img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Normalización 
        img2 = img2.astype(float)
        if img2.max() > 0:
            img2 = (img2 - img2.min()) / (img2.max() - img2.min()) * 255.0
        img2 = np.uint8(img2)

        return img2, Image.fromarray(img)

    except Exception as e:
        print(f"Error al leer el archivo de imagen: {e}")
        return None, None


def read_image_file(path):
  
    extension = path.lower().split('.')[-1]
    
    if extension in ['dcm', 'dicom']:
        return read_dicom_file(path)
    elif extension in ['jpg', 'jpeg', 'png', 'bmp', 'tiff']:
        return read_jpg_file(path)
    else:
        print(f"Formato no soportado: {extension}")
        return None, None

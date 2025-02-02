#  **DIAGNOSTICO MEDICO DE NEUMONIA** 

### **Nombres:**
1. DANIEL SANIN RAMIREZ
2. JULIANA MEDINA GUERREO
3. JESSICA VIVIANA MARTINEZ MARIN
4. ANDRES FELIPE GARCIA TURRIAGO

# 

### **¿Qué es la neumonia?**
Es una infeccion que inflama los sacos de aire en uno o ambos pulmones, los cuales pueden llenarse de liquido o pus. Esto hace que cause tos con flema, fiebre, escalofrios y dificultades para respirar. Esta enfermedad puede ser causada por bacterias y virus, afectand especificamente a niñs, adultos mayores y personas con sistemas inmunológicos debiitados.

![image](https://github.com/user-attachments/assets/90e1190c-7ef8-46c4-a8aa-cc6c9b7979a9)

# 
### **Propósito y Funcionalidades Principales**  

Este proyecto utiliza **Deep Learning** para la detección rápida de **neumonía** a partir de imágenes radiográficas de tórax en formato **DICOM y JPG**. A través de una red neuronal clasifica las imágenes en tres categorías: **Neumonía Bacteriana, Neumonía Viral y Sin Neumonía**.  

Además, incorpora la técnica **Grad-CAM**, que genera un **mapa de calor** resaltando las áreas más relevantes en la imagen para la toma de decisiones del modelo, permitiendo una mayor interpretabilidad de los resultados y una mejor visualización.  

El proyecto incluye una **interfaz gráfica** que permite a los doctores cargar los examenes medicos de los pacientes, y en base a ellos visualizar las predicciones, guardar historial de resultados del diagnostico en **archivos CSV** y generar **informes en PDF** de manera rápida y sencilla.

#
### **Requisitos previos**

Antes de instalar y ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

#### **Sistema operativo**
- Windows 10/11

### **Dependencias y librerias necesarias**
- Python (versión recomendada: 3.7 hasta 3.9)
- Visual Studio Code
- TensorFlow (para carga y ejecución del modelo)
- Pillow (Procesamiento de imágenes)
- Pydicom (lectura de imágenes en formato DICOM)
- Matplotlib (visualización de imágenes y mapas de calor)
- Tkinter (interfaz gráfica)
- ReportLab (generación de informes en PDF)
- Docker(Contenedorización del proyecto)

Ademas de las utilizadas en **requirements.txt**

#
### **Instalación**

#### 1. Crea una carpeta en "archivos"

#### 2. Abre VS code - click derecho dentro de la carpeta, click en "Abrir en Terminal"", escribe "code . " 

#### 3. Clonar el repositorio - control + mayuscula + p, click en "Git: Clone", pega:

https://github.com/julianamedinaa/Neumonia_Grupo4.git

#### 4. Crear un entorno virtual: control + mayuscula + p, buscas "python: select interprete", click en "create virtual enviroment", click en "venv", eliges el python V. 3.9

#### 5. Instalar dependencias:

pip install -r requirements.txt

#### 6. Ejecutar la aplicación:

python main.py

#### 7. Uso con Docker

docker build -t neumonia-detector .
docker run -p 8501:8501 neumonia-detector
#
### Diagrama de flujo
![WhatsApp Image 2025-02-01 at 8 25 10 PM](https://github.com/user-attachments/assets/6de210d0-c1c3-492b-a98a-1207a3028b08)

#
### **Uso de la Interfaz Gráfica:**
![WhatsApp Image 2025-02-01 at 8 06 12 PM](https://github.com/user-attachments/assets/6c1124ce-6fd1-4b5b-9f1e-4949570c9a66)

- Ingrese la cédula del paciente en la caja de texto
- Presione el botón 'Cargar Imagen', seleccione la imagen del explorador de archivos del computador
- Presione el botón 'Predecir' y espere unos segundos hasta que observe los resultados
- Presione el botón 'Guardar' para almacenar la información del paciente en un archivo excel con extensión .csv
- Presione el botón 'PDF' para descargar un archivo PDF con la información desplegada en la interfaz
- Presión el botón 'Borrar' si desea cargar una nueva imagen

# 
### **Explicación de los scripts**

- **detector_neumonia.py**
  Contiene el diseño de la interfaz gráfica utilizando Tkinter.
  Los botones llaman métodos contenidos en otros scripts.

- **integrator.py**
  Es un módulo que integra los demás scripts y retorna solamente lo necesario para ser visualizado en la interfaz gráfica. Retorna la clase, la probabilidad y una imagen el mapa de calor generado por Grad-CAM.

- **read_img.py**
  Script que lee la imagen en formato DICOM para visualizarla en la interfaz gráfica. Además, la convierte a arreglo para su preprocesamiento.

- **preprocess_img.py**
  Script que recibe el arreglo proveniento de read_img.py, realiza las siguientes modificaciones:
  resize a 512x512
  conversión a escala de grises
  ecualización del histograma con CLAHE
  normalización de la imagen entre 0 y 1
  conversión del arreglo de imagen a formato de batch (tensor)
  load_model.py
  Script que lee el archivo binario del modelo de red neuronal convolucional previamente entrenado llamado 'WilhemNet86.h5'.

- **grad_cam.py**
  Script que recibe la imagen y la procesa, carga el modelo, obtiene la predicción y la capa convolucional de interés para obtener las características relevantes de la imagen.


NOTA: Aunque exista una carpeta llamada test, esta solamente aloja archivos como imagenes y CSV.
En el lado de documentos, tenemos una carpeta llamada "test" en donde se detallan las pruebas realizadas

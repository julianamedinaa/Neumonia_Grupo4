# interfaz gráfica con la que interactua el paciente la cual muestra la probabilidad de tener neumonia

import os
import csv
import tkinter as tk
import tkcap
from tkinter.messagebox import WARNING, askokcancel, showinfo 
from tkinter import END, Image, StringVar, Text, Tk, ttk, font, filedialog
from PIL import ImageTk, Image, ImageGrab


from integrator import read_dicom, read_jpg, prediction #lo que retorna para visualizar en la GUI el cual integra la GUI con los demas metodos

class App:
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Herramienta para la detección rápida de neumonía Grupo 4")

         # Definir tamaño y font de la interfaz
        self.root.geometry("815x560")
        fonti = font.Font(weight="bold")
        self.root.resizable(0, 0)

        # Crear widgets (labels, botones, etc.)
        self.lab1 = ttk.Label(self.root, text="Imagen Radiográfica", font=fonti)
        self.lab2 = ttk.Label(self.root, text="Imagen con Heatmap", font=fonti)
        self.lab3 = ttk.Label(self.root, text="Resultado:", font=fonti)
        self.lab4 = ttk.Label(self.root, text="Cédula Paciente:", font=fonti)
        self.lab5 = ttk.Label(self.root, text="SOFTWARE PARA EL APOYO AL DIAGNÓSTICO MÉDICO DE NEUMONÍA",font=fonti)
        self.lab6 = ttk.Label(self.root, text="Probabilidad:", font=fonti)

        # Variables de texto
        self.ID = StringVar()
        self.result = StringVar()

        # Entrada para cédula de paciente
        self.text1 = ttk.Entry(self.root, textvariable=self.ID, width=10)
        # primero debe ir la creacion de las variables antes de llamarlas 
        self.text_img1 = Text(self.root, width=31, height=15)
        self.text_img2 = Text(self.root, width=31, height=15)
        self.text2 = Text(self.root)
        self.text3 = Text(self.root)

         # Configuración de la interfaz
        self.ID_content = self.text1.get()

        # Botones de acción
        self.button1 = ttk.Button(self.root, text="Predecir", state="disabled", command=self.run_model)
        self.button2 = ttk.Button(self.root, text="Cargar Imagen", command=self.load_img_file)
        self.button3 = ttk.Button(self.root, text="Borrar", command=self.delete)
        self.button4 = ttk.Button(self.root, text="PDF", command=self.create_pdf)
        self.button6 = ttk.Button(self.root, text="Guardar", command=self.save_results_csv)

        #   WIDGETS la posicion 
        self.lab1.place(x=110, y=65)
        self.lab2.place(x=545, y=65)
        self.lab3.place(x=500, y=350)
        self.lab4.place(x=65, y=350)
        self.lab5.place(x=122, y=25)
        self.lab6.place(x=500, y=400)
        self.button1.place(x=220, y=460)
        self.button2.place(x=70, y=460)
        self.button3.place(x=670, y=460)
        self.button4.place(x=520, y=460)
        self.button6.place(x=370, y=460)
        self.text1.place(x=200, y=350)
        self.text2.place(x=610, y=350, width=90, height=30)
        self.text3.place(x=610, y=400, width=90, height=30)
        self.text_img1.place(x=65, y=90)
        self.text_img2.place(x=500, y=90)


       
        #   FOCUS ON PATIENT ID
        self.text1.focus_set()

        #  se reconoce como un elemento de la clase
        self.array = None

        # num para pdf
        self.reportID = 0

        # Ejecutar la interfaz
        self.root.mainloop()

    #   metodos
    def load_img_file(self):
       
        filepath = filedialog.askopenfilename(
            initialdir="/",
            title="Select image",
            filetypes=(
                ("DICOM", "*.dcm"),
                ("JPEG", "*.jpeg"),
                ("jpg files", "*.jpg"),
                ("png files", "*.png"),
            ),
        )

         # Cargar y mostrar la imagen 
        if filepath:
           
            ext = os.path.splitext(filepath)[1].lower()
             #valida la extencion o formato
            if ext == ".dcm":
                try:
                    self.array, img2show = read_dicom(filepath)
                except Exception as e:
                    return
            elif ext in (".jpg", ".jpeg", ".png",".JPG",".JPEG"):
                self.array, img2show = read_jpg(filepath)
            else:
                self.mostrarDato("error de formato")
                return

            #self.img1 = img2show.resize((250, 250), Image.ANTIALIAS) #esta linea se cambio por lanzos ya que esta obsoleta
            self.img1 = img2show.resize((250, 250), Image.LANCZOS)
            self.img1 = ImageTk.PhotoImage(self.img1)
            self.text_img1.image_create(END, image=self.img1)
            self.button1["state"] = "enabled"
        else:
            self.mostrarDato("error")
            return
 
    def guardar_jpeg(self):
        # Nombre de salida
        filename = "mi_formulario.jpg"
        # Creamos el objeto de captura
        cap = tkcap.CAP(self.root)
        # Capturamos la ventana principal y guardamos
        cap.capture(filename) # Esto genera "mi_formulario.jpg"
        showinfo("Captura", f"El formulario se guardó como {filename}") 

    def run_model(self):      #con este metodo se corre el modelo entregado por el profesor *.h5 
        self.label, self.proba, self.heatmap = prediction(self.array) 
        self.img2 = Image.fromarray(self.heatmap)
        self.img2 = self.img2.resize((250, 250), Image.LANCZOS)
        self.img2 = ImageTk.PhotoImage(self.img2)
        print("OK")
        self.text_img2.image_create(END, image=self.img2)
        self.text2.insert(END, self.label)
        self.text3.insert(END, "{:.2f}".format(self.proba) + "%")

   
    def save_results_csv(self):
    # Definir la carpeta donde se guardará el archivo
        folder_path = "test"
    
    # Si la carpeta no existe, crearla
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Definir las cabeceras para el CSV
        fieldnames = ["ID Paciente", "Etiqueta", "Probabilidad"]
    
    # Ruta completa para guardar el archivo CSV en la carpeta 'test'
        file_path = os.path.join(folder_path, "historial_proba.csv")
    
    # Intentar abrir el archivo CSV
        try:
            with open(file_path, mode="a", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Si el archivo está vacío, escribir las cabeceras
                if csvfile.tell() == 0:
                    writer.writeheader()

            # Escribir los resultados
                writer.writerow({
                    "ID Paciente": self.text1.get(),  # Cédula o ID del paciente
                    "Etiqueta": self.label,  # La etiqueta del diagnóstico
                    "Probabilidad": "{:.2f}".format(self.proba) + "%"  # Probabilidad formateada
                 })
        
        # Mostrar un mensaje de confirmación
            showinfo(title="Guardar", message="Los datos se guardaron con éxito.")

        except Exception as e:
        # En caso de error, mostrar el error
            showinfo(title="Error", message=f"Hubo un error al guardar los datos: {str(e)}")
   

    def create_pdf(self):
        
            # se puede elegir la ruta en el cual 
            # se guarda el pdf ya que el codigo anterior solo lo guardaba dentro del proyecto 
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Ruta para guardar PDF"
        )
        
        if not file_path:
            return  

        # Capturar la ventana principal (self.root)
        x = self.root.winfo_rootx()
        y = self.root.winfo_rooty()
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        # Tomar captura de la ventana completa
        img = ImageGrab.grab(bbox=(x, y, x + width, y + height))

        # Guardar la imagen
        img.save(file_path, "PDF", resolution=100)

        showinfo(title="PDF", message="El PDF fue generado con éxito.")

    

    def delete(self):
        # Borrar los resultados de la interfaz
        answer = askokcancel(title="Confirmación", message="Se borrarán todos los datos.")
        if answer:
            self.text1.delete(0, "end")
            self.text_img1.delete("1.0", "end")
            self.text_img2.delete("1.0", "end")
            showinfo(title="Borrar", message="Los datos se borraron con éxito")

             
# Ejecutar la aplicación
def main():
    my_app = App()
    return 0


if __name__ == "__main__":
    main()
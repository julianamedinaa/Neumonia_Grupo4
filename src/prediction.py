# para realizar la prediccion se requiere este metodo el cual necesita hacer coneccion con el modelo 
import numpy as np
from grad_cam import grad_cam
from load_model import modelp
from preprocess_img import preprocess


def predict(array):
    
    
    batch_array_img = preprocess(array)
   
    model = modelp()
   
    prediction = np.argmax(model.predict(batch_array_img))
    proba = np.max(model.predict(batch_array_img)) * 100
    label = ""
    if prediction == 0:
        label = "bacteriana"
    if prediction == 1:
        label = "normal"
    if prediction == 2:
        label = "viral"
    
    heatmap = grad_cam(array)
    return (label, proba, heatmap)



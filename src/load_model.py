# Módulo encargado de cargar el modelo entrenado
import tensorflow as tf
from tensorflow.keras.models import load_model


def modelp():
    # Carga un modelo ya entrenado
    model = load_model("conv_MLP_84.h5",
                       compile=False)
    return model

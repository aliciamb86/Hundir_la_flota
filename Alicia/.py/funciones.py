import numpy as np
import random
import time

def crear_tablero(tamaño=(10,10)):
    tablero = np.full(tamaño, "·")
    return tablero
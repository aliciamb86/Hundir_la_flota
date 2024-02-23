import numpy as np
import random
import time
import variables as v
import funciones as f

tablero_jug = f.crear_tablero_jug()
print(tablero_jug)

barco_1_1 = f.crear_barco_jug(1, tablero_jug, v.contador)
barco_2_1 = f.crear_barco_jug(1, tablero_jug, v.contador)
barco_3_1 = f.crear_barco_jug(1, tablero_jug, v.contador)
barco_4_1 = f.crear_barco_jug(1, tablero_jug, v.contador)
barco_5_1 = f.crear_barco_jug(2, tablero_jug, v.contador)
barco_6_1 = f.crear_barco_jug(2, tablero_jug, v.contador)
barco_7_1 = f.crear_barco_jug(2, tablero_jug, v.contador)
barco_8_1 = f.crear_barco_jug(3, tablero_jug, v.contador)
barco_9_1 = f.crear_barco_jug(3, tablero_jug, v.contador)
barco_10_1 = f.crear_barco_jug(4, tablero_jug, v.contador)
print(tablero_jug)
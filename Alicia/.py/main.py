import numpy as np
import random
import time
import variables as v
import funciones as f

# creamos el tablero del jugador 1
tablero_jug = f.crear_tablero()
# print(tablero_jug)

# creamos los barcos del jugador 1
barco_1j = f.crear_barco(1, tablero_jug, v.contador)
barco_2j = f.crear_barco(1, tablero_jug, v.contador)
barco_3j = f.crear_barco(1, tablero_jug, v.contador)
barco_4j = f.crear_barco(1, tablero_jug, v.contador)
barco_5j = f.crear_barco(2, tablero_jug, v.contador)
barco_6j = f.crear_barco(2, tablero_jug, v.contador)
barco_7j = f.crear_barco(2, tablero_jug, v.contador)
barco_8j = f.crear_barco(3, tablero_jug, v.contador)
barco_9j = f.crear_barco(3, tablero_jug, v.contador)
barco_10j = f.crear_barco(4, tablero_jug, v.contador)
print('TABLERO JUGADOR \n', tablero_jug)


# creamos el tablero de la máquina
tablero_maq = f.crear_tablero()
# print(tablero_maq)

# creamos los barcos de la máquina
barco_1m = f.crear_barco(1, tablero_maq, v.contador)
barco_2m = f.crear_barco(1, tablero_maq, v.contador)
barco_3m = f.crear_barco(1, tablero_maq, v.contador)
barco_4m = f.crear_barco(1, tablero_maq, v.contador)
barco_5m = f.crear_barco(2, tablero_maq, v.contador)
barco_6m = f.crear_barco(2, tablero_maq, v.contador)
barco_7m = f.crear_barco(2, tablero_maq, v.contador)
barco_8m = f.crear_barco(3, tablero_maq, v.contador)
barco_9m = f.crear_barco(3, tablero_maq, v.contador)
barco_10m = f.crear_barco(4, tablero_maq, v.contador)
# print(tablero_maq)

# ocultamos el tablero de la máquina
tablero_maq_oculto = f.ocultar_tablero(tablero_maq)
print('TABLERO MÁQUINA \n', tablero_maq_oculto)
import numpy as np
import random
import time
import funciones as f
import variables as v

lista_barcos_jug = []

# creamos los barcos del jugador 1
barco_1j = f.crear_barco(1, v.tablero_jug, v.contador, lista_barcos_jug)
barco_2j = f.crear_barco(1, v.tablero_jug, v.contador, lista_barcos_jug)
barco_3j = f.crear_barco(1, v.tablero_jug, v.contador, lista_barcos_jug)
barco_4j = f.crear_barco(1, v.tablero_jug, v.contador, lista_barcos_jug)
barco_5j = f.crear_barco(2, v.tablero_jug, v.contador, lista_barcos_jug)
barco_6j = f.crear_barco(2, v.tablero_jug, v.contador, lista_barcos_jug)
barco_7j = f.crear_barco(2, v.tablero_jug, v.contador, lista_barcos_jug)
barco_8j = f.crear_barco(3, v.tablero_jug, v.contador, lista_barcos_jug)
barco_9j = f.crear_barco(3, v.tablero_jug, v.contador, lista_barcos_jug)
barco_10j = f.crear_barco(4, v.tablero_jug, v.contador, lista_barcos_jug)
print('TABLERO JUGADOR \n', v.tablero_jug)
print(lista_barcos_jug)



# # creamos los barcos de la máquina
# barco_1m = f.crear_barco(1, v.tablero_maq, v.contador, v.lista_barcos)
# barco_2m = f.crear_barco(1, v.tablero_maq, v.contador, v.lista_barcos)
# barco_3m = f.crear_barco(1, v.tablero_maq, v.contador, v.lista_barcos)
# barco_4m = f.crear_barco(1, v.tablero_maq, v.contador, v.lista_barcos)
# barco_5m = f.crear_barco(2, v.tablero_maq, v.contador, v.lista_barcos)
# barco_6m = f.crear_barco(2, v.tablero_maq, v.contador, v.lista_barcos)
# barco_7m = f.crear_barco(2, v.tablero_maq, v.contador, v.lista_barcos)
# barco_8m = f.crear_barco(3, v.tablero_maq, v.contador, v.lista_barcos)
# barco_9m = f.crear_barco(3, v.tablero_maq, v.contador, v.lista_barcos)
# barco_10m = f.crear_barco(4, v.tablero_maq, v.contador, v.lista_barcos)
# # print(tablero_maq)

# # ocultamos el tablero de la máquina
# tablero_maq_oculto = f.crear_tablero()
# print('TABLERO MÁQUINA \n', tablero_maq_oculto)
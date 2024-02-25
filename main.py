
import time as t
import funciones as f
import variables as v


print(v.inicio)


if v.inicio == 'D':
    f.juego_difícil(v.tablero_jug, v.lista_barcos_jug, v.tablero_maq, v.lista_barcos_maq, v.tablero_maq_oculto)

elif v.inicio == 'F':
    f.juego_fácil(v.tablero_jug, v.lista_barcos_jug, v.tablero_maq, v.lista_barcos_maq, v.tablero_maq_oculto)

elif v.inicio == 'P':
    f.juego_prueba(v.tablero_jug, v.lista_barcos_jug, v.tablero_maq, v.lista_barcos_maq, v.tablero_maq)

else:
    print('Opción incorrecta, escribe "D", "F" o "P"')

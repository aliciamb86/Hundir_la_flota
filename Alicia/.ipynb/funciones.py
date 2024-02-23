import numpy as np
import random
import time

def crear_tablero(tamaño=(10,10)):
    tablero = np.full(tamaño, "·")
    return tablero

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def crear_barco(eslora, tablero, contador, lista_barcos):    
    # elegimos aleatoriamente el punto de partida desde el que se colocará nuestro barco
    fila_a = random.randint(0,9)
    columna_a = random.randint(0,9)

    # declaramos como primera posición de nuestro barco los valores obtenidos aleatoriamente
    # declaramos nuestro barco, con la ubicación del punto de partida
    fila_inicio = fila_a
    columna_inicio = columna_a
    barco = [(fila_inicio, columna_inicio)]

    # elegimos aleatoriamente la dirección en la que se posicionará nuestro barco
    orientacion = random.choice(["S","O","E","N"])

    while len(barco) < eslora:
        match orientacion:
            case "O":
                if columna_a - (eslora - 1) >= 0:
                    columna_inicio -= 1 
                else:
                    orientacion = random.choice(["S","E","N"])

                    continue
            case "E":
                if columna_a + (eslora - 1) <= 9:
                    columna_inicio += 1
                else:
                    orientacion = random.choice(["S","O","N"])

                    continue
            case "S":
                if fila_a + (eslora - 1) <= 9:
                    fila_inicio += 1
                else:
                    orientacion = random.choice(["O","E","N"])

                    continue
            case "N":
                if fila_a - (eslora - 1) >= 0:
                    fila_inicio -= 1
                else:
                    orientacion = random.choice(["S","O","E"])

                    continue
        barco.append((fila_inicio, columna_inicio))
    else:
        for casilla in barco:
            if tablero[casilla] != "O":
                contador +=1
                if contador == eslora:
                    lista_barcos = lista_barcos.append(barco)
                    tablero = colocar_barco(barco, tablero)

                    break
            else:
                # print('Creando nuevo barco')
                crear_barco(eslora, tablero, contador)
                break

def ocultar_tablero(tablero):
    tablero[::,::] = '·'
    return tablero
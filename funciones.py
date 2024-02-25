import numpy as np
import random
import time as t


def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero


def crear_barco(eslora, tablero, lista_barcos):    
    fila_a = random.randint(0,9)
    columna_a = random.randint(0,9)

    fila_inicio = fila_a
    columna_inicio = columna_a
    barco = [(fila_inicio, columna_inicio)]

    orientacion = random.choice(["S","O","E","N"])

    contador = 0

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
                crear_barco(eslora, tablero, lista_barcos)
                break


def crear_barcos(tablero, lista_barcos, eslora_1=4, eslora_2=3, eslora_3=2, eslora_4=1):
    contador = 0
    while contador < eslora_1:
        crear_barco(1, tablero, lista_barcos)
        contador +=1
        
    contador = 0
    while contador < eslora_2:
        crear_barco(2, tablero, lista_barcos)
        contador +=1
        
    contador = 0
    while contador < eslora_3:
        crear_barco(3, tablero, lista_barcos)
        contador +=1
        
    contador = 0
    while contador < eslora_4:
        crear_barco(4, tablero, lista_barcos)
        contador +=1

    # print(tablero)
    # print(lista_barcos)
    # return lista_barcos



def vidas(lista_barcos):
    vidas = []
    for i in range(len(lista_barcos)):
        if len(vidas) < len(lista_barcos):
            vidas.append(len(lista_barcos[i]))    
    return (sum(vidas))


def barcos_por_hundir(lista_barcos):
    barcos = 0
    for i in range(len(lista_barcos)):
        if len(lista_barcos[i]) > 0:
            barcos += 1
    return (barcos)


def disparar_jugador(lista_barcos_maq, tablero_maq_oculto, lista_barcos_jug):
    print('\n\n¡Comienza tu turno!')
    print('Te quedan', barcos_por_hundir(lista_barcos_maq), 'barcos por hundir')
    t.sleep(2)
    print('Tienes', vidas(lista_barcos_jug), 'vidas')
    t.sleep(2)
    print(tablero_maq_oculto)
    print('Elige las coordenadas de tu disparo:')
    fila = int(input('Introduce la fila de tu disparo: '))
    columna = int(input('Introduce la columna de tu disparo: '))
    contador_fallos = 0
    contador_aciertos = 0
    disparo = (fila, columna)
    print('Disparas a la posición', disparo)
    t.sleep(2)
    for i in range(len(lista_barcos_maq)):
        if (fila,columna) not in lista_barcos_maq[i]:
            contador_fallos += 1
            if contador_fallos == len(lista_barcos_maq):
                tablero_maq_oculto[fila,columna] = 'A'
                print('¡AGUA!')
                print(tablero_maq_oculto)
                t.sleep(2)
                break
        elif (fila,columna) in lista_barcos_maq[i]:
            contador_aciertos += 1
            if contador_aciertos == 1:
                lista_barcos_maq[i].remove((fila,columna))
                tablero_maq_oculto[fila,columna] = 'X'
                if len(lista_barcos_maq[i]) > 0:
                    print('¡TOCADO!')
                    print(tablero_maq_oculto)
                    t.sleep(2)
                else:
                    print('¡BARCO HUNDIDO!')
                    print(tablero_maq_oculto)
                    t.sleep(2)
            if vidas(lista_barcos_maq) > 0:
                print('¡VUELVES A TIRAR!')
                t.sleep(2)  
                disparar_jugador(lista_barcos_maq, tablero_maq_oculto, lista_barcos_jug)
                t.sleep(2)
            elif vidas(lista_barcos_maq) == 0:
                break


def disparar_maquina(lista_barcos_jug, tablero_jug, lista_barcos_maq):
    print('\n\n¡Comienza el turno de la máquina!')
    print('Le quedan', barcos_por_hundir(lista_barcos_jug), 'barcos por hundirte')
    t.sleep(2)
    print('Tiene', vidas(lista_barcos_maq), 'vidas')
    t.sleep(2)
    fila = random.randint(0,9)
    columna = random.randint(0,9)
    contador_fallos = 0
    contador_aciertos = 0
    disparo = (fila, columna)
    print('La máquina te dispara a la posición', disparo)
    t.sleep(2)
    for i in range(len(lista_barcos_jug)):
        if (fila,columna) not in lista_barcos_jug[i]:
            contador_fallos += 1
            if contador_fallos == len(lista_barcos_jug):
                tablero_jug[fila,columna] = 'A'
                print('¡AGUA!')
                print(tablero_jug)
                t.sleep(2)
                break
        elif (fila,columna) in lista_barcos_jug[i]:
            contador_aciertos += 1
            if contador_aciertos == 1:
                lista_barcos_jug[i].remove((fila,columna))
                tablero_jug[fila,columna] = 'X'
                if len(lista_barcos_jug[i]) > 0:
                    print('¡TOCADO!')
                    print(tablero_jug)
                    t.sleep(2)
                else:
                    print('¡BARCO HUNDIDO!')
                    print(tablero_jug)
                    t.sleep(2)
            if vidas(lista_barcos_jug) > 0:
                print('¡VUELVE A TIRAR LA MÁQUINA!')
                t.sleep(2)  
                disparar_maquina(lista_barcos_jug, tablero_jug, lista_barcos_maq)
                t.sleep(2)
            elif vidas(lista_barcos_jug) == 0:
                break



def juego(lista_barcos_jug, lista_barcos_maq, tablero_jug, tablero_maq_oculto):

    while (vidas(lista_barcos_jug) > 0) and (vidas(lista_barcos_maq) > 0):

        if vidas(lista_barcos_jug) > 0:
            disparar_jugador(lista_barcos_maq, tablero_maq_oculto, lista_barcos_jug)
        else:
            break      

        if vidas(lista_barcos_maq) > 0:
            disparar_maquina(lista_barcos_jug, tablero_jug, lista_barcos_maq)
        else:
            break

    if vidas(lista_barcos_jug) == 0:
        print('¡LO SIENTO, HAS PERDIDO!')
    else:
        print('¡ENHORABUENA, HAS GANADO!')

        

def juego_difícil(tablero_jug, lista_barcos_jug, tablero_maq, lista_barcos_maq, tablero_maq_oculto):
    
    crear_barcos(tablero_jug, lista_barcos_jug)

    crear_barcos(tablero_maq, lista_barcos_maq)

    juego(lista_barcos_jug, lista_barcos_maq, tablero_jug, tablero_maq_oculto)


def juego_fácil(tablero_jug, lista_barcos_jug, tablero_maq, lista_barcos_maq, tablero_maq_oculto):

    crear_barcos(tablero_jug, lista_barcos_jug)

    crear_barcos(tablero_maq, lista_barcos_maq, 0, 0, 2, 1)

    juego(lista_barcos_jug, lista_barcos_maq, tablero_jug, tablero_maq_oculto)


def juego_prueba(tablero_jug, lista_barcos_jug, tablero_maq, lista_barcos_maq, tablero_maq_oculto):
    
    crear_barcos(tablero_jug, lista_barcos_jug, 0, 0, 0, 1)

    crear_barcos(tablero_maq, lista_barcos_maq, 0, 0, 0, 1)

    juego(lista_barcos_jug, lista_barcos_maq, tablero_jug, tablero_maq_oculto)



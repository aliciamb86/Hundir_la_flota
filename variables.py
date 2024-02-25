import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

lista_barcos_jug = []
lista_barcos_maq = []
tablero_jug = np.full((10,10), "·")
tablero_maq = np.full((10,10), "·")
tablero_maq_oculto = np.full((10,10), "·")
inicio = input('¡BIENVENIDOS A HUNDIR LA FLOTA!\n\nEl juego consiste en hundir la flota del contrincante.\nPara ello, debe colocar su propia flota de forma estratégica y encontrar y hundir con los disparos la flota contraria.\nCada uno de los jugadores dispone de dos tableros que ocultará al otro jugador:\nen una debe colocar sus barcos y en la otra irá anotando los resultados de los disparos que realiza en cada turno.\n\nEn la opción DIFÍCIL ambos jugadores tenéis los siguientes barcos:\n* 4 barcos de 1 posición de eslora\n* 3 barcos de 2 posiciones de eslora\n* 2 barcos de 3 posiciones de eslora\n* 1 barco de 4 posiciones de eslora\n\nEn la opción FÁCIL el jugador tiene los siguientes barcos:\n* 4 barcos de 1 posición de eslora\n* 3 barcos de 2 posiciones de eslora\n* 2 barcos de 3 posiciones de eslora\n* 1 barco de 4 posiciones de eslora\npero tu contrincante sólo tiene los siguientes barcos:\n* 2 barcos de 3 posiciones de eslora\n* 1 barco de 4 posiciones de eslora\n\nEn la opción PRUEBA ambos jugadores tenéis un solo barco:\n* 1 barco de 4 posiciones de eslora\ny podrás ver el tablero de tu contrincante con sus barcos\n\nCada jugador dispone de un turno de disparo que se irá alternando.\nAl disparar, el otro jugador comprobará el resultado en su tablero:\nSi la casilla está en blanco, responderá “agua”.\nSi en la casilla se encuentra parte de un barco responderá “tocado”.\nEn ese caso el jugador tiene derecho a un nuevo disparo en el mismo turno.\nSi en la casilla se encuentra un barco de un cuadro o la última parte de un barco\nya tocado, responderá “hundido” y también tiene derecho a un nuevo disparo.\n\nFinalmente, gana el jugador que antes consigue hundir la flota del otro.\n\n¿Qué opción quieres jugar?\n"D" difícil\n"F" fácil\n"P" prueba:\n').upper()


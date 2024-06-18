# Hundir la Flota

Un juego de Hundir la Flota implementado en Python.

## Descripción

Este proyecto consiste en un juego clásico de Hundir la Flota. El juego se desarrolla en una cuadrícula de 10x10 donde el jugador y la máquina colocan sus barcos y se turnan para disparar a las coordenadas del oponente. El objetivo es hundir todos los barcos del oponente.

## Características

- Colocación aleatoria de barcos
- Disparos por turno entre el jugador y la máquina
- Detección de impactos y hundimientos
- Tres modos de juego: fácil, difícil y prueba

## Requisitos

- Python 3.x
- Librerías: numpy, random, time

## Cómo jugar

1. Clona este repositorio: 
    ```bash
    git clone https://github.com/aliciamb86/hundir_la_flota.git
    ```
2. Ejecuta el archivo principal del juego:
    ```bash
    python hundir_la_flota.py
    ```
3. Sigue las instrucciones en pantalla para jugar.

## Código

### Colocación de Barcos

```python
def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

Creación de Barcos

python

def crear_barco(eslora, tablero, lista_barcos):
    # Código para crear un barco en el tablero

Turnos del Jugador y la Máquina

python

def disparar_jugador(lista_barcos_maq, tablero_maq_oculto, lista_barcos_jug):
    # Código para el turno del jugador

python

def disparar_maquina(lista_barcos_jug, tablero_jug, lista_barcos_maq):
    # Código para el turno de la máquina

Juego Principal

python

def juego(lista_barcos_jug, lista_barcos_maq, tablero_jug, tablero_maq_oculto):
    # Código principal del juego

Contacto

Creado por Alicia Martínez - si tienes alguna pregunta, no dudes en contactarme.

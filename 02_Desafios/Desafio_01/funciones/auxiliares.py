# Copyright (C) 2024 <UTN FRA>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame.mixer as mixer
import time


def limpiar_pantalla():
    """
    The function `limpiar_pantalla` clears the console screen and waits for user input to continue.
    """
    import os
    _ = input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name in ['nt', 'dos'] else 'clear')

def play_sound():
    """
    The `play_sound` function initializes the mixer, loads a sound file, sets the volume to 0.4, and
    plays the sound.
    """
    mixer.init()
    mixer.music.load('./assets/snd/select.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play()
    time.sleep(0.4)

def mostrar_nombre(lis_nom: list, i: int) -> str:
    return lis_nom[i]

def obtener_maximo(lis_num: list) -> float:
    numero = None

    for num in lis_num:
        if not numero or numero < num:
            numero = num
    
    return float(numero)

def promedio(lis_num: list) -> float:
    sum = 0

    for n in lis_num:
        sum += n

    return sum/len(lis_num)

def obtener_mitad_de_maximo(lis_num: list) -> float:
    maximo = obtener_maximo(lis_num)

    return maximo/2

if __name__ == '__main__':
    mostrar_nombre(['Scott Summers, Jean Grey, Erik Lenhsherr, Hank McCoy'], 0)
    obtener_maximo([-8, -3, -4, 0, -7])
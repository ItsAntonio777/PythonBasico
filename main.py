from Enemigo import *
from Zombie import *
from Ogro import *
import random

# Crear instancias de enemigos
zombie = Zombie(10, 1)
ogro = Ogro(20, 3)

def batalla(e1: Enemigo, e2: Enemigo):
    e1.habla()
    e2.habla()

    while e1.puntos_energia > 0 and e2.puntos_energia > 0:
        print("#####################")
        e1.ataque_especial()
        e2.ataque_especial()

        print(f"{e1.get_tipo_enemigo()}: queda {e1.puntos_energia} puntos de energía!!!!")
        print(f"{e2.get_tipo_enemigo()}: quedan {e2.puntos_energia} puntos de energía!!!!!!")

        print(f"Ataque: {e1.ataque}")
        e1.puntos_energia -= e2.ataque

        print("=====================")
        print(f"Ataque: {e2.ataque}")
        e2.puntos_energia -= e1.ataque

    print("#####################")
    if e1.puntos_energia > 0:
        print(f"{e1.get_tipo_enemigo()} ganó!!")
    else:
        print(f"{e2.get_tipo_enemigo()} ganó!!")

print("=============== Batalla ===============")
batalla(zombie, ogro)
print("=============== Fin de la batalla ===============")

# Información final de los enemigos
print(f"{zombie.get_tipo_enemigo()} tiene {zombie.puntos_energia} de energía y ataca con {zombie.ataque}")
print(f"{ogro.get_tipo_enemigo()} tiene {ogro.puntos_energia} de energía y ataca con {ogro.ataque}")


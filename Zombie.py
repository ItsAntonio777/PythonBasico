from Enemigo import *

class Zombie(Enemigo):
    def __init__(self, puntos_energia=10, ataque=1):
        super().__init__(tipo_enemigo='Zombie', puntos_energia=puntos_energia,ataque=ataque)

    def habla(seif):
        print("Hummmmm. . .*")

    def propagador_enfermedad(self):
        print("El Zombie esta tratando de propogar la enfermedad")
from Enemigo import *
import random

class Ogro(Enemigo):
    def __init__(self, puntos_energia=20, ataque=3):
        super().__init__(tipo_enemigo='Ogro',
                         puntos_energia=puntos_energia,
                         ataque=ataque)

    def habla(self):
        print("¡Ogro aplastar todo!!!")

    def ataque_especial(self):
        print("Ogro usa ataque especial")
        funciona_ataque_especial = random.random() < 0.40  # 40% de probabilidad

        if funciona_ataque_especial:
            self.ataque += 3
            print("Ogro se enfurece y aumenta su ataque en +3!!!")


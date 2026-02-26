from Enemigo import *

class Ogro(Enemigo):
    def __init__(self, puntos_energia=20, ataque=3):
        super().__init__(tipo_enemigo='Ogro', puntos_energia=puntos_energia, ataque=ataque)

        def habla(self):
            print("Ogro aplastar todo")
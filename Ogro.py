from Enemigo import * import random

class Ogro(Enemigo):

def 		init	(self, puntos_energia=20, ataque=3): super().		init	(tipo_enemigo='Ogro',
puntos_energia=puntos_energia, ataque=ataque)


def habla(self):
print("Ogro aplastar todo!!!")

class Enemigo: tipo_enemigo: str puntos_energia: int = 10 ataque = 1

def 	init	(self, tipo_enemigo, puntos_energia=10, ataque=1):

self.	tipo_enemigo = tipo_enemigo self.puntos_energia = puntos_energia self.ataque = ataque

def get_tipo_enemigo(self): return self.	tipo_enemigo

def habla(self):
print(f"Yo son {self.	tipo_enemigo}. Preparado para palear!!")


def camina(self):
print(f"{self.	tipo_enemigo} se mueve cerca de ti!!")


def atacar(self):
print(f"{self.	tipo_enemigo} ataca con un {self.ataque} de daño!!")


def ataque_especial(self):
print("Enemigo no tiene ataque especial")


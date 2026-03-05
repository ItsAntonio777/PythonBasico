class Enemigo:
    def __init__(self, tipo_enemigo: str, puntos_energia: int = 10, ataque: int = 1):
        self.tipo_enemigo = tipo_enemigo
        self.puntos_energia = puntos_energia
        self.ataque = ataque

    def get_tipo_enemigo(self):
        return self.tipo_enemigo

    def habla(self):
        print(f"Yo soy {self.tipo_enemigo}. ¡Preparado para pelear!!")

    def camina(self):
        print(f"{self.tipo_enemigo} se mueve cerca de ti!!")

    def atacar(self):
        print(f"{self.tipo_enemigo} ataca con {self.ataque} de daño!!")

    def ataque_especial(self):
        print("Este enemigo no tiene ataque especial")

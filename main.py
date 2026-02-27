from Enemigo import *
from Zombie import *
from Ogro import *

zombie = Zombie(10, 1)
ogro = Ogro(20, 3)

print(f"{zombie.get_tipo_enemigo()} tiene {zombie.puntos_energia} de energia y atacra con {zombie.ataque}")
print(f"{ogro.get_tipo_enemigo()} tiene {ogro.puntos_energia} de energia y ataca con {ogro.ataque}")

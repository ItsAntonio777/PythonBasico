from Enemigo import * from Zombie import * from Ogro import * import random

zombie = Zombie(10, 1) ogro = Ogro(20, 3)

def batalla(e1: Enemigo, e2: Enemigo): e1.habla()
e2.habla()


while e1.puntos_energia > 0 and e2.puntos_energia > 0: print("#####################")
e1.ataque_especial() e2.ataque_especial()
print(f"{e1.get_tipo_enemigo()}: queda:
{e1.puntos_energia} puntos de energia!!!!")
print(f"{e2.get_tipo_enemigo()}: quedan:
{e2.puntos_energia} puntos de energia!!!!!!") print(f"Ataque: {e1.ataque}") e1.puntos_energia -= e2.ataque print("=====================")
print(f"Aatque: {e1.ataque}")

e2.puntos_energia


print("#####################")
if e1.puntos_energia > 0: print(f"{e1.get_tipo_enemigo()} ganooo!!")
else:
print(f"{e2.get_tipo_enemigo()} ganooo!!")


print("===============Batalla===============")
batalla(zombie, ogro) print("===============Fin de la batalla") #print(f"{zombie.get_tipo_enemigo()} tiene
{zombie.puntos_energia} de energia y atacra con {zombie.ataque}")
#print(f"{ogro.get_tipo_enemigo()} tiene {ogro.puntos_energia} de energia y ataca con {ogro.ataque}")

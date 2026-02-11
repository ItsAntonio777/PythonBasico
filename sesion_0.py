# Numeros
print(int(7))
print(float(7.7))
print(type(7))
print(type(7.7))
print(int(1+2))
print(int(10*2))
print(int(1 + 4 - 2))
print(float(1 + 2.0))

# operadores matematicos


print(int(2**3))
print(int(4**8))
print(float(10%3))
print(float(25%4))
print(float(16%2))
print(float(10/3))

#variables
print("====Variables====")
x = 100
Y = 1
print(x + Y)

ventas = 1999991
print("Nuestras ventas fueron: ", ventas)

is_active = True
print(is_active)
game_over = False
print(game_over) 

some_string = "Hola soy un string"
print(some_string)

print("====Condicionales====")
edad = 15

if (edad >= 18):
    print("Si puedes entrar al bar!!!")
else:
    print("No puedes entrar al bar:(")
    mi_numero = int(input("Cual es el numero que deseas verificar?"))
    print(f"El numero  que desea verificar es: {mi_numero}")
    if mi_numero % 2 == 0:
        print(f"El numero {mi_numero} es par!")
    else:
                print(f"El numero {mi_numero} es impar!")

                def par_impar(numero):
                      if numero % 2 == 0:
                            print(f"El numero{numero} es par!")
                      else:
                            print(f"El numero{numero} es impar!")
                            print("====Funcion par impar====")
                            mi_numero = int(input("Cual es el numero que deseas verificar?:"))
                            print(f"El numero que desea verificar es{mi_numero}")
                            print(par_impar(mi_numero))

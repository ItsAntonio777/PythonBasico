print("========  Calculadora ==========")


num_1 = float(input("Escriba el valor del primer número: "))
num_2 = float(input("Escriba el valor del segundo número: "))
operacion = input("¿Qué operación deseas hacer? +, -, *, / -> ")


def calculadora(num_1, num_2, operacion):
    if operacion == "+":
        return num_1 + num_2
    elif operacion == "-":
        return num_1 - num_2
    elif operacion == "*":
        return num_1 * num_2
    elif operacion == "/":
        if num_2 != 0:
            return num_1 / num_2
        else:
            return "Error: No se puede dividir entre cero"
    else:
        return "Operación no válida"


resultado = calculadora(num_1, num_2, operacion)
print("El resultado es:", resultado)

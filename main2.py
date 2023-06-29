from decimal import Decimal 

print("Ingrese un dividendo: ") 
dividendo = input()

print("Ingrese un divisor: ")
divisor = input()

operador1 = Decimal(dividendo)
operador2 = Decimal(divisor)

division = operador1/operador2

operacion = str(division) 
print("Resultado de la division: " + operacion)

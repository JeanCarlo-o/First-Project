class Calculadora:
    def sumar(self, a, b, c=0):
        return a + b + c

#Ejemplo
calc = Calculadora()
print(calc.sumar(5, 10)) #Suma de 2 valores
print(calc.sumar(5, 10, 15)) #Suma de 3 valores
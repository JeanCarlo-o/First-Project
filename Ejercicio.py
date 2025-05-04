def sumar():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"La suma es: {resultado}")
    except ValueError:
        print("Error: Debes ingresar números válidos.")

sumar()
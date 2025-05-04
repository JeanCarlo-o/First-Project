def dividir(a, b):
    try:
        resultado = a / b
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
dividir(10, 2)
dividir(5, 0)
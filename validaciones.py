def validar_entrada_numerica(entrada):
    try:
        numero = int(entrada)

        if numero < 0:
            print("ERROR: No se permiten números negativos.")
            return False
        
        if numero == 0:
            print("ERROR: El monto debe ser mayor a 0.")
    

        if numero > 1_000_000_000:
            print("ERROR: El número es demasiado grande.")
            return False

        return True

    except ValueError:
        print("ERROR: Debe ingresar un número entero válido.")
        return False

# Que no sea un número extremadamente grande que rompa lógica
def validar_entrada_numerica_extrema(entrada):
   
    try:
        numero = float(entrada.replace(".", ""))
        if abs(numero) > 1e10: 
            print("ERROR: El número es demasiado grande.")
            return False
        
        return True
    except ValueError:
        print("ERROR: Tiene que ingresar un valor numerico.")
        return False

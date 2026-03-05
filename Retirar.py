def retiro(saldo):
    valor = int(input("Digite el valor a retirar: "))

    if valor <= 0:
        print("El valor debe ser mayor que 0")
    elif valor <= saldo:
        saldo -= valor
        print("Retiro exitoso. Saldo actual:", saldo)
    else:
        print("Saldo insuficiente")

    return saldo
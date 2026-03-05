def retiro(saldo):
    while True:
        valor = int(input("Digite el valor a retirar: "))
        if valor <= saldo:
            saldo -= valor
            print("Retiro exitoso. Saldo actual:", saldo)
            return saldo
        else:
            print("Saldo insuficiente")

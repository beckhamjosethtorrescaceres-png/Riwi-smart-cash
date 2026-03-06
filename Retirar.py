from validaciones import validar_entrada_numerica

def retiro(saldo):
    entrada = input("Digite el valor a retirar: ")
    valor = validar_entrada_numerica(entrada)

    if valor is None:
        print("Retiro cancelado por entrada inválida.")
        return saldo

    if valor > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= valor
        print("Retiro exitoso. Saldo actual:", saldo)

    return saldo
from validaciones import validar_entrada_numerica

def deposito(saldo):
    entrada = input("Digite el valor a depositar: ")
    valor = validar_entrada_numerica(entrada)

    if valor is None:
        print("Depósito cancelado por entrada inválida.")
        return saldo

    saldo += valor
    print("Depósito exitoso. Saldo actual:", saldo)
    return saldo
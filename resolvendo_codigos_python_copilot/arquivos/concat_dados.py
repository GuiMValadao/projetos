# Vamos receber dois dados diferentes do usuário
# e concatená-los em uma única string.
def concatenar_dados(dado1, dado2):
    return str(dado1) + str(dado2)


# Exemplo de uso
if __name__ == "__main__":
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    resultado = concatenar_dados(dado1, dado2)
    print("Dados concatenados:", resultado)

# Vamos receber uma string e um número inteiro como entrada. Então retornaremos
# a string repetida o número de vezes indicado pelo inteiro. Acrescente um espaço
# entre cada repetição da string.


def repetir_string(string, vezes):
    return (string + " ") * vezes


# Exemplo de uso
if __name__ == "__main__":
    string = input("Digite uma string: ")
    vezes = int(input("Digite um número inteiro: "))
    resultado = repetir_string(string, vezes)
    print("String repetida:", resultado)

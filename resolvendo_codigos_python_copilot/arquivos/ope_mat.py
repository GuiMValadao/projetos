# Vamos receber dois números e realizar operações matemáticas básicas:
# soma, subtração, multiplicação e divisão. Retornaremos os resultados dessas operações
def operacoes_matematicas(num1, num2):
    """
    Executa operações matemáticas básicas entre dois números.
    Args:
        num1 (float): O primeiro número para a operação.
        num2 (float): O segundo número para a operação.
    Returns:
        float or str: O resultado da operação matemática escolhida, ou uma mensagem de erro
        se a operação for inválida ou se houver tentativa de divisão por zero.
    A operação desejada deve ser inserida pelo usuário e pode ser uma das seguintes:
        - '+' para adição
        - '-' para subtração
        - '*' para multiplicação
        - '/' para divisão
    """
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    operacoes = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 if num2 != 0 else "Erro: Divisão por zero não é permitida",
    }

    return operacoes.get(operacao, "Operação inválida")


# Exemplo de uso
if __name__ == "__main__":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = operacoes_matematicas(num1, num2)
    print("Resultado da operação:", resultado)

def cadastrar_usuario(nome, data_nascimento, cpf, 
                      endereco, usuarios_cadastrados):
    """
    Cadastra o usuário contendo os seguites parâmetros:
    nome: string contendo o nome do cliente.
    data_nascimento: string contendo a data de nascimento.
    cpf: string contendo somente os números do CPF; apenas um por usuário.
    endereco: string no formato rua, nº - bairro - cidade/sigla estado.
    """
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco,
    }
    
    if usuarios_cadastrados == []:
        return usuario
    else:
        for individuo in usuarios_cadastrados:    
            print(individuo['cpf'])
            if usuario['cpf'] not in individuo['cpf']:
                return usuario
            else:
                print('Usuário já cadastrado!')
                return cpf

def criar_conta_corrente(cpf, contas_cadastradas, extrato):
    """
    Armazena contas em uma lista. Cada conta possuirá:
    agencia: número da agência, fixo = '0001'.
    numero_conta: número da conta, possui um único usuário. Inicia em 1.
    usuario: usuario da conta, pode possuir multiplas contas. 
            Identificado pelo CPF.
    """
    conta = {
        'cpf': cpf,
        'numero_da_conta': 0,
        'agencia': '0001',
        'numero_saques': 0,
        'extrato': extrato,
        'saldo': 0.0,
    }
    if contas_cadastradas == []:
        conta['numero_da_conta'] = 1            
    else:
        ultima_conta = contas_cadastradas[-1]['numero_da_conta']
        conta['numero_da_conta'] = ultima_conta + 1        
    return conta

def saque(saldo, valor, extrato, limite, 
          numero_saques, LIMITE_SAQUES):
    """ 
    Função que permite um usuário realizar saque.
    Aceita apenas argumento passados com nome.
    
    Argumentos de entrada:
    saldo: float contendo o saldo da conta.
    valor: float contendo o valor do saque.
    extrato: histórico de transações.
    limite: valor máximo de saque disponível.
    numero_saques: numero de saques realizados pela conta.
    limite_saques: limite de saques permitido por conta.
    
    Parâmetros de saída:
    saldo: saldo após saque, inalterado se saque inválido.
    extrato: histórico de transações.
    """

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato = modificar_extrato(extrato, 'Saque', valor)
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    return round(saldo,2), extrato, numero_saques

def deposito(saldo, valor, extrato):
    """
    Permite que um usuário faça depósito.
    
    Parâmetros de entrada:
    saldo: saldo da conta.
    valor: valor do depósito.
    extrato: histórico de transações.

    Parâmetros de saída:
    saldo: saldo após depósito, inalterado se inválido.
    extrato: histórico de transações.
    """
    if valor > 0:
        saldo += valor
        extrato = modificar_extrato(extrato = extrato, operacao = 'Depósito', valor = valor)

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def modificar_extrato(extrato, operacao, valor):
    """ 
    Salva o histórico de transações de uma conta.
    Parâmetros:
    saldo: saldo da conta.
    extrato: histórico de transações.
    """
    extrato += f"{operacao}: R$ {valor:.2f}\n"
    return extrato

def menu_inicial():
    """
    Exibe o menu para criação de conta para o usuário.
    Recebe a escolha em uma string e a retorna.
    """
    menu = """
--------------
-MENU INICIAL-
--------------
Bem vindo ao Banco! O que deseja fazer?
    
[c] Criar conta
[e] Entrar com conta existente
[q] Sair

=> """
    escolha = input(menu).lower()
    return escolha

def menu_escolha_transacao():
    """
    Exibe o menu de escolha de transação para o usuário.
    Recebe a escolha em uma string e a retorna.
    """
    menu = """
--------------------
-MENU DE TRANSAÇÕES-
--------------------
Qual operação deseja realizar?
        
[d] Depositar
[s] Sacar
[e] Extrato
[q] Retornar ao menu inicial

=> """
    escolha = input(menu).lower()
    return escolha

def main():
    extrato = ''
    LIMITE = 1000
    LIMITE_SAQUES = 3
    usuarios_cadastrados = []
    contas_cadastradas = []
    opcao_criar_conta, criar_conta_usuario_existente = '', '' 

    while True:

        opcao = menu_inicial()

        if opcao == "c":
        # Seção para criação de novos usuários e/ou novas contas
            print("""
    ------------------
    -MENU DE CADASTRO-                              
    ------------------
    """)
            novo_usuario = cadastrar_usuario(input('Digite seu nome: '), 
                                            input('Digite sua data de nascimento: '),
                                            input('Digite seu cpf: '), 
                                            input('Digute seu endereço completo: '),
                                            usuarios_cadastrados)
            if type(novo_usuario) != dict:
                criar_conta_usuario_existente = input(
                    """ 
    Deseja criar uma nova conta?
                            
    1 - Sim
    2 - Não
                    
    => """)             
                if criar_conta_usuario_existente == '1':
                    contas_cadastradas.append(criar_conta_corrente(novo_usuario, contas_cadastradas))
                    print('Conta corrente criada com sucesso.')
                elif criar_conta_usuario_existente == '2':
                    print('Criação de contada negada pelo usuário')
                else:
                    print('Escolha inválida, retornando ao menu inicial.')

            else:
                usuarios_cadastrados.append(novo_usuario)
                opcao_criar_conta = input(
                    """Usuário criado com sucesso. Deseja criar uma conta?
                            
    1 - Sim
    2 - Não
                    
    => """)
                if opcao_criar_conta == '1':
                    contas_cadastradas.append(criar_conta_corrente(novo_usuario['cpf'], contas_cadastradas, extrato))
                    print('Conta corrente criada com sucesso.')    
                elif opcao_criar_conta == '2':          
                    print('Criação de contada negada pelo usuário')
                else:
                    print('Escolha inválida, retornando ao menu inicial.')

        elif opcao == "e":
            cpf = input(" Informe seu CPF: ")
            for conta in contas_cadastradas:
                conta_acessada = False
                if cpf == conta['cpf']:
                    conta_acessada = True
                    while True:                
                        opcao2 = menu_escolha_transacao()
                        if opcao2 == "d":
                            conta['saldo'], conta['extrato']  = \
                            deposito(
                                    saldo = conta['saldo'], 
                                    valor = float(input("Informe o valor do depósito: ")),
                                    extrato = conta['extrato']
                                    )

                        elif opcao2 == "s":
                            conta['saldo'],conta['extrato'],conta['numero_saques'] = \
                            saque(
                                saldo = conta['saldo'],
                                valor = float(input("Informe o valor do saque: ")),
                                extrato = conta['extrato'],
                                limite = LIMITE,
                                numero_saques = conta['numero_saques'],
                                LIMITE_SAQUES = LIMITE_SAQUES
                                )
                            
                        elif opcao2 == "e":
                            print("""
    ---------
    -EXTRATO-
    ---------\n          
    """)
                            print(conta['extrato'])
                            print('_'*20)
                            print(f"Saldo: R$ {conta['saldo']:.2f}\n")

                        elif opcao2 == "q":
                            print("Obrigado por ser nosso cliente!")
                            break

                        else:
                            print('Escolha inválida, escolha a transação apropriada.')

            if  conta_acessada == False:
                print('Conta não cadastrada.')

        elif opcao == "q":
            print(" Tenha um bom dia.")
            break

        else:
            print("Opção inválida. Escolha entre os valores disponíveis.")

main()


    
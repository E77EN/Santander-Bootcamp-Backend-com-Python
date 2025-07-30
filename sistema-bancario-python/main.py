saldo = 0
limite = 500
historico_transacoes = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []

def deposito(saldo, valor, historico_transacoes, /):
    if valor > 0:
        saldo += valor
        historico_transacoes += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, historico_transacoes

def saque(*, saldo, valor, historico_transacoes, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        historico_transacoes += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, historico_transacoes, numero_saques

def extrato(saldo, /, *, historico_transacoes):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not historico_transacoes else historico_transacoes)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\nUsuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")
        return

    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    print("\nConta criada com sucesso!")

def menu():
    menu_str = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[q] Sair

=> """
    return input(menu_str)

while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, historico_transacoes = deposito(saldo, valor, historico_transacoes)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, historico_transacoes, numero_saques = saque(saldo=saldo, valor=valor, historico_transacoes=historico_transacoes, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    elif opcao == "e":
        extrato(saldo, historico_transacoes=historico_transacoes)
    elif opcao == "nu":
        criar_usuario(usuarios)
    elif opcao == "nc":
        numero_conta = len(contas) + 1
        agencia = "0001"
        criar_conta(agencia, numero_conta, usuarios, contas)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



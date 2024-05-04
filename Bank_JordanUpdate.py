import textwrap

def interface():

    interface = '''
    ==================MENU==================
    [1] DEPOSITAR
    [2] SACAR
    [3] EXTRATO 
    [4] NOVO USUÁRIO
    [5] LISTAR CONTAS
    [6] NOVA CONTA
    [7] SAIR
    ==>  '''
    return input(textwrap.dedent(interface))

def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
       print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! Você não tem limite o suficiente. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Você não possui saques disponíveis. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n === Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é invalido. @@@")
    return saldo, extrato

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:2f}\n"
        print("\n===Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def e_extrato(saldo, /, *, extrato):
    print("\n==========EXTRATO==========")
    print("Não foram realizadas movimentações na conta." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================")

def criar_user(usuarios):
    cpf = input("Informe o CPF(somente números): ")
    usuario = filtragem(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço ( logradouro, Nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def filtragem(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtragem(cpf, usuarios)

    if usuario:
        print("\n===Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
    print("=" * 100)
    print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES=3
    AGENCIA="0001"

    saldo=0
    limite=500
    extrato=""
    numero_saque=0
    usuarios=[]
    contas=[]

    while True:
        opcao = interface()
        if opcao == "1":
           valor = float(input("Informe o valor do depósito: "))
           saldo, extrato = deposito(saldo, valor, extrato)
        
        elif opcao == "2":
           valor = float(input("Informe o valor do saque: "))

           saldo,extrato = saque(             
               saldo=saldo,
               valor=valor,
               extrato=extrato,
               limite=limite,
               numero_saques=numero_saque,
               limite_saques=LIMITE_SAQUES,
                ) 
        elif opcao == "3":
            e_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            criar_user(usuarios)
        elif opcao == "6":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "5":
            listar_contas(contas)
        
        elif opcao == "7":
            break

main()
menu="""
==========BANCO AGUIAR==========

    [1]DEPÓSITO
    [2]SAQUE
    [3]EXTRATO
    [4]ENCERRAR OPERAÇÃO

================================
Digite a operação desejada:
"""
saldo = 0
numero_saque = 0
extrato = ""
LIMITE_SAQUE = 3
LIMITE_POR_SAQUE = 500.00


while True:
        opcao = input(menu)
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                 saldo += valor
                 extrato += f"Depósito: R$ {valor:.2f}\n"
                 retorno = str(input("DEPÓSITO REALIZADO! DESEJA FAZER OUTRA OPERAÇÃO? [1 - SIM] OU [2 - NÃO]\n"))
                 if retorno == "1":
                    print(menu)   
                 else:
                    print("OPERAÇÃO ENCERRADA")
                    break     
            else:
                 print("Operação falhou! O valor informado é inválido.")     
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > LIMITE_POR_SAQUE
            excedeu_saques = numero_saque >= LIMITE_SAQUE
            if excedeu_saldo:
                 print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                 print("Operação falhou! O valor de saque excede o limite.")
            elif excedeu_saques:
                 print("Operação falhou! Número máximo de saques excedidos.")
            elif valor > 0:
                 saldo -= valor
                 extrato += f"Saque: R$ {valor:.2f}\n"
                 numero_saque += 1
                 retorno = str(input("SAQUE REALIZADO.\n DESEJA FAZER OUTRA OPERAÇÃO? [1 - SIM] OU [2 - NÃO]\n"))
                 if retorno == "1":
                    print(menu)  
                 else:
                    print("OPERAÇÃO ENCERRADA")
                    break           
            else:
                 print("Operação falhou! O valor informado é inválido.")
        elif opcao == "3":
            print("\n==========EXTRATO==========")
            print("Não foram realizadas movimentações na conta." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=============================")
            retorno = str(input("DESEJA FAZER OUTRA OPERAÇÃO? [1 - SIM] OU [2 - NÃO]\n"))
            if retorno == "1":
                print(menu)
            else:
                print("OPERAÇÃO ENCERRADA")
                break        
        elif opcao == "4":
            print("OPERAÇÃO ENCERRADA")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")    
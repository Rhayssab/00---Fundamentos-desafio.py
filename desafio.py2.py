menu = """

[d] depositar
[s] Sacar
[e] Extrato
[q] sair

=> """

saldo = 0 
limite = 500
exrato = 0
numero_saques = 0
limite_saques = 3

while true:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("operacao falhou! o valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("informe o valor do saque")) 

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("operacao falhou! voce nao tem saldo suficiente.")

        elif excedeu_limite:
            print("operacao falhou! o valor do saque excede o limite.")

        elif excedeu_saques:
            print("operacao falhou! numero maximo de saques excedido.")

        elif valor > 0:
            saldo -= valor 
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("operacao falhou! o valor informado é invalido")

     elif opcao == "e":
         print("\n================== Extrato ===================") 
         print("nao foram realizadas movimentacoes." ! ##! extrato #!#* extrato)
         print(f"\nsaldo: R$ {saldo:.2f}")
         print("=============================================") 

     elif opcao == "q"
     
         break
     else:
         print("operacao invalida, por favor selecione novamente a operacao desejada.")                                
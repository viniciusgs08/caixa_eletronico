usuario = input("Digite seu nome: ")
senha = int(input("Digite sua senha: "))
senha_correta = 1234
saldo = 1000.0

if senha == senha_correta:
    print(f"\nOlá, {usuario}!")
    print("1 - Consultar saldo")
    print("2 - Sacar dinheiro")
    print("3 - Depositar dinheiro")

    escolha = input("Digite o número correspondente: ")

    if escolha == "1":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif escolha == "2":
        saque = float(input("Quanto deseja sacar? R$ "))

        if saque <= 0:
            print("Valor inválido!")
        elif saque > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= saque
            print("Saque realizado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}")

    elif escolha == "3":
        depositar = float(input("Quanto deseja depositar? R$ "))

        if depositar <= 0:
            print("Valor inválido!")
        else:
            saldo += depositar
            print("Depósito realizado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}")

    else:
        print("Opção inválida!")

else:
    print("Senha incorreta!")
# Define o Menu
menu = '''
    Selecione a operação desejada:
    (d)Deposito
    (s)Saque
    (e)Extrato
    (q)Sair
=>'''

# Define os parametros da conta.
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

# Loop infinito para execução do menu
while True:

    # Chama o menu e atribui uma variavel para a escolha do usuario
    opcao = input(menu)

    # Opção Deposito
    if opcao == "d":

        # Solicita o valor a ser depositado
        valor_depositado = float(input("Informe o valor a ser depositado: "))

        # Verifica se o valor entrado é valido ( > 0)
        if valor_depositado > 0:

            saldo += valor_depositado  # adiciona o valor do deposito ao saldo

            # adiciona a informação do deposito ao extrato
            extrato += f"Deposito : {valor_depositado :.2f}\n"
            # Exibe uma mensagem confirmando o deposito
            print("Deposito efetuado com com sucesso")

        else:
            '''Caso o valor não é valido
            exibe a mensgem informando o usuario => retorna ao menu'''
            print("Somente valores positivos são permitidos para deposito")

    # Opção Saque
    elif opcao == "s":

        # Verifica se o limite de saques não foi atingido
        if numero_de_saques >= LIMITE_SAQUES:
            ''' Alerta o usuario que o limite de saque
            diarios foi atingido'''
            print(f"O seu limite de {LIMITE_SAQUES} diarios foi excedido.")
        else:
            # Solicita o valor a ser sacado
            valor_sacado = float(input("Informe o valor a ser sacado: "))

            '''verifica se valor desejado esta no limite por saque
            retorna ao menu caso esteja acima'''
            if valor_sacado > limite:
                # Informa que o valor deseja ultrapassa o limite
                print(f"O seu limite para saque é de {limite} por saque")

            elif valor_sacado > saldo:  # verifica se há saldo
                # informa que saldo é insuficiente => menu
                print("Você não possui saldo suficiente")

            else:

                saldo -= valor_sacado  # retira valor sacado do saldo
                numero_de_saques += 1  # altera o numero diario de saldo
                # adiciona operação ao extrato
                extrato += f"Saque : {valor_sacado :.2f}\n"
                # informa que o saque foi feito com sucesso
                print("Saque efetuado com sucesso")

    # Opção Extrato:
    elif opcao == "e":
        # verifica se houve oprações
        if extrato == "":
            # informa que não há extrato
            print("Não há nenhuma informação de extrato disponivel. ")

        else:
            # Exibe extrato + saldo
            print("========Extrato========")
            print(extrato+"=======================\n"+f"Saldo : {saldo:.2f}")

    # Opção Sair
    elif opcao == "q":
        # sai da operação
        break

    # Nenhuma das Opções
    else:
        # informa o usuario de opção selecionada invalida
        print("""Opção selecionada INVALIDA.
Tente novamente:""")

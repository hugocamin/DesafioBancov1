def cabecalho():
    return ('\033[1m*-*-' * 6)[:-1] + '\033[0m'


def mensagem_retorno():
    return input('\033[96mDeseja voltar ao menu?\nSIM : aperte ENTER\nNÃO : digite N pra encerrar a sessão\033[0m')

def mensagem_tchaU():
    print('\033[93mOBRIGADO E VOLTE SEMPRE\033[0m')


def verificar_retorno():
    opcao = mensagem_retorno().upper()
    if opcao == 'N':
        mensagem_tchaU()
        return False
    return True

menu ="""
\033[1m[1] Depositar\033[0m
\033[1m[2] Sacar\033[0m
\033[1m[3] Extrato\033[0m
\033[1m[4] Sair\033[0m
"""



saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(cabecalho())
    print('\033[32m\tBANCO DIGITAL\033[0m')
    print(cabecalho())
    print(menu)

    opcao = input('\033[1mDIGITE O NUMERO DA OPÇÂO DESEJADA:\033[0m')
    if opcao == "1":
        valor = float(input("\033[1mInforme o valor do depósito: \033[0m"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f'\033[1mSeu novo saldo é de: R${saldo:.2f}\033[0m')

        else:
            print("\033[91mERRO, O VALOR INFORMADO É INVÁLIDO\033[0m")

        if verificar_retorno() == False:
            break

    elif opcao == '2':
        valor = float(input("\033[1mInforme o valor do saque: \033[0m"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES


        if excedeu_saldo:
            print("\033[1;31mERRO, SALDO INSUFICIENTE.\033[0m")

        elif excedeu_limite:
            print("\033[1;31mERRO, O VALOR DO SAQUE EXCEDEU LIMITE.\033[0m")

        elif excedeu_saques:
            print("\033[1;31mERRO, NUMERO MAXIMO DE SAQUES REALIZADOS.\033[0m")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f'\033[1mSeu novo saldo é de: R${saldo:.2f}\033[0m')

        else:
            print("\033[1;31mERRO, VALOR INVÁLIDO\033[0m")

        if verificar_retorno() == False:
            break

    elif opcao == '3':
        print("\033[1m\n================ EXTRATO ================\033[0m")
        print("\033[1mNão foram realizadas movimentações.\033[0m" if not extrato else extrato)
        print(f"\033[1m\nSaldo: R$ {saldo:.2f}\033[0m")
        print("\033[1m==========================================\033[0m")

        if verificar_retorno() == False:
            break

    elif opcao == "4":
        mensagem_tchaU()
        break

    else:
        print("\033[91mERRO, OPERAÇÃO INVÁLIDA\033[0m")


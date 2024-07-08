menu = """

Selecione a operação desejada:

[1] Depositar
[2] Sacar
[3] Consultar Extrato
[0] Sair

=> """

saldo = 0
limite_saque = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print('Depósito')
        print('Digite o valor do depósito: ')
        deposito = int(input())
        if deposito > 0:
            saldo += deposito
            extrato += f'\nDepósito de: R${deposito:.2f}'
        else:
            print('Não fo possível depositar, Valor inválido.')


    elif opcao == 2:
        print('Saque')
        print('Informe o valor que deseja sacar: ')
        saque = int(input())
        if saldo < saque:
            print('Não foi possivel executar a operação. Saldo insuficiente.')
        elif saque <= 0:
            print('Não foi possivel executar a operação. Valor inválido.')
        elif saque > limite_saque:
            print('Não foi possivel executar a operação. Valor acima do limite.')
        elif numero_saques == LIMITE_SAQUES:
            print('Não foi possivel executar a operação. Limite de saques excedido.')
        else:
            saldo -= saque
            numero_saques += 1
            extrato += f'\nSaque de: R$ {saque:.2f}'

    elif opcao == 4:
        print('Extrato \n',extrato)
        print(f'Saldo Total: R$ {saldo:.2f}')

    
    elif opcao == 0:
        print('Sair')
        break

    else:
        print('Opção inválida, Por favor, selecione novamente a opção desejada.')


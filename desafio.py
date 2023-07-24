menu ='''
--------------Menu---------------
[s]Sacar
[d]Depositar
[e]Extrato
[q]sair 
=> '''

saldo = 0
limite = 1500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True :

    opçao = input(menu)
    if opçao == 'd':
        valor = float(input('informe o valor do deposito: '))
        if valor > 0 :
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
        else:
            print('operação falhou o valor informando é invalido ')
    elif opçao == 's':
        valor = float(input('informe o valor do saque: '))
        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite 
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print('operação falhou! você não tem saldo suficiente. ')
        elif excedeu_limite :
            print('operação falhou! o valor do saque excede o limite ')
        elif excedeu_saques :
            print('voce já fez o limte maximo de saques diarios ')
        elif valor > 0:
            saldo -= valor 
            extrato += f'Saque: R${valor:.2f}\n'
            print('Retire o valor na boca do caixa. ')
            numero_saques += 1
        else:
            print('operação falhou! valor informado é invalido')
    elif opçao == 'e':
        print('\n===================Extrato==================')
        print('não foram realizadas movimentações.'if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('===============================================')
    elif opçao == 'q' :
        break
    
    else:
        print('operação invalida! por favor digite a operação desejada.')



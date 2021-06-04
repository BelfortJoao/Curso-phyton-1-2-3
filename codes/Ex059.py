import time

y = 0
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro: '))
while y != 5:
    print("""Escolha uma opção:
    [1] Qual o maior numero?
    [2] Somar numeros
    [3] Multiplicar numeros
    [4] Subtrair numeros
    [5] Escolher novos numeros
    [6] Sair do programa""")
    x = int(input("Resposta: "))
    if x == 1:
        if n1 > n2:
            print('O numero {} é o maior'.format(n1))
        if n1 < n2:
            print('O numero {} é o maior'.format(n2))
        else:
            print(' Os dois numero são iguais')
    elif x == 2:
        print('{} + {} = {}'.format(n2, n1, n1+n2))
    elif x == 3:
        print('{} x {} = {}'.format(n2, n1, n1 * n2))
    elif x == 4:
        print('{} - {} = {}'.format(n2, n1, n2 - n1))
    elif x == 5:
        print('\n')
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro: '))
    elif x == 6:
        print('Você escolheu sair.')
        y = 5
    else:
     print('Opção invalida')
    time.sleep(1.5)
    print('\n'*13)

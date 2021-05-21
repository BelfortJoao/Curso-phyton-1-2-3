r =0
while r == 0:
    x1 = int(input('Digite o 1º numero: '))
    x2 = int(input('Digite o 2º numero: '))
    if x1 > x2:
        print('O primeiro numero é o maior.')
    elif x1 < x2:
        print('O segundo numero é o maior.')
    else:
        print('os dois numeros são iguais')

    r = int(input('Quer continuar? digite [0]Sim [1]Não: '))
    print('\n'*2, '_'*30)

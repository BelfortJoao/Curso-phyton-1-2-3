y = 0
while y != 1:
    x = int(input('Escolha um numero para calcular o fatorial: '))
    n = 1
    c = 0
    while c < x:
        c += 1
        n = n * c
    print('o fatorial de {} é {}'.format(x, n))
    y = int(input("Quer sair? [1]Sim [2]Não: "))
    print('\n'* 3)



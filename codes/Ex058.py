import time

n = ' '
while n not in 'MH':
    n = str(input('Qual seu sexo?\n[M] mulher [H] Homem: ')).strip().upper()[0]
    if n == 'M':
        print('Prazer em te conhecer moça')
    elif n == 'H':
        print('Prazer em te conhecer moço')
    else:
        print('Opção invalida')
    time.sleep(3)
    print('\n' * 10)


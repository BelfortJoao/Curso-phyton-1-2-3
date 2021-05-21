import random

r = 0
while r == 0:
    print('Vamos jogar pedra, papel ou tesoura')
    print('[1] pedra')
    print('[2] papel')
    print('[3] tesoura')
    print('[4] Sair')
    z = str(input('Escolha uma opção: '))
    x = int(random.choice([1, 2, 3]))
    print('-'*20)
    if z == '1':
        print('Você escolheu pedra')
        if x == 1:
            print(' O computador escolheu pedra \n \033[0;33mEmpatou\033[m')
        elif x == 2:
            print(' O computador escolheu papel \n \033[0;31m Você perdeu\033[m')
        elif x == 3:
            print(' O computador escolheu tesoura \n \033[0;32m Você ganhou\033[m')
    elif z == '2':
        print('Você escolheu papel')
        if x == 1:
            print(' O computador escolheu pedra \n \033[0;32m Você ganhou \033[m')
        elif x == 2:
            print(' O computador escolheu papel \n \033[0;33m Empatou \033[m')
        elif x == 3:
            print(' O computador escolheu tesoura \n \033[0;31m Você perdeu \033[m')
    elif z == '3':
        print('Você escolheu tesoura')
        if x == 1:
            print(' O computador escolheu pedra \n \033[0;31m Você perdeu \033[m')
        elif x == 2:
            print(' O computador escolheu papel \n \033[0;32m Você ganhou \033[m')
        elif x == 3:
            print(' O computador escolheu tesoura \n \033[0;33m Empatou \033[m')
    elif z == '4':
        r = 1
    else:
        print('Opção invalida')
    print('-' * 25)
print('\n' * 100)
print('\033[0;31m Você saiu \033[m')

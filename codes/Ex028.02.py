import random
z = 0
while z <= 1:
    x = random.uniform(0, 5)
    y = int(input("Digite um numero de \033[1;36m0 a 5\033[m e descubra se acertou: "))
    print("O computador escolheu \033[36m {} \033[m".format(int(x)))
    if y == int(x):
        print('\033[0;32m voce acertou o numero\033[m')
    else:
        print(' \033[31m voce errou\033[m')
    z = int(input("quer continuar a jogar? \033[0;32m Sim[1]\033[m \033[31mNao[2]\033[m"))
    print('\n' * 10)

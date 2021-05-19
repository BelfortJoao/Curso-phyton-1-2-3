import random
z = 0
while z <= 1:
    x = random.uniform(0, 5)
    y = int(input("Digite um numero de 0 a 5 e descubra se acertou: "))
    print("O computador escolheu {} ".format(int(x)))
    if y == int(x):
        print('voce acertou o numero')
    else:
        print(' voce errou')
    z = int(input("quer continuar a jogar? Sim[1] Nao[2]"))
    print('\n' * 10)
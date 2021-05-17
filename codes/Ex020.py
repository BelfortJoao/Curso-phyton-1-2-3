from random import shuffle
print("-------BEM VINDO OA Sequenciador-------")
print('escolha os nomes que quer sortear')
N1 = input('nome 1: ')
N2 = input('nome 2: ')
N3 = input('nome 3: ')
N4 = input('nome 4: ')
Li = [N1, N2, N3, N4]
shuffle(Li)
print('A ordem é {}'.format(Li))
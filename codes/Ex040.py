x = int(input('Nota 1: '))
y = int(input('Nota 2: '))
z = int(input('Nota 3: '))
if (x+y+z)/3 <= 5:
    print(' Você não passou de ano')
elif 6.9 >= (x + y + z)/3 > 5:
    print('Você esta de recuperação')
else:
    print('\nVocê Passou de ano')
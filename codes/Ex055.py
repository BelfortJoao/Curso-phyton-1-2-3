y = 0
w = 0
z = 0
T = 0
for x in range(0, 4):
    n = str(input('Qual o nome? '))
    i = int(input('Qual a idade? '))
    p = int(input('Qual o sexo?\n[1] para homem.  \n[2] para mulher:  '))
    y += i
    if i > T and p == 1:
        w = n
        T = i
    if i >= 20 and p == 2:
        z += 1
    print('\n'* 100)
print('A media das idades é de {} anos.'.format(y/4))
print('O homem mais velho é {}.'.format(w))
print('{} mulheres tem mais de 20 anos.'.format(z))




print('Irei gerar uma PA')
x = int(input('qual o primeiro termo? '))
y = int(input("Qual a razão? "))
n = x
w = 1
while w <= 10:
    print('{} ->'.format(n), end='')
    n += y
    w += 1
j = 1
while j != 0:
    j = int(input('\n quantos numero a mais quer mostrar? ')) + w
    while w < j:
        print('{} ->'.format(n), end='')
        n += y
        w += 1
print(" A AP terminou em seu {}º termo".format(j))

print('Irei gerar uma PA')
x = int(input('qual o primeiro termo? '))
y = int(input("Qual a razão? "))
n = x
w = 1
while w <= 10:
    print('{} ->'.format(n), end='')
    n += y
    w += 1
print('Fim')

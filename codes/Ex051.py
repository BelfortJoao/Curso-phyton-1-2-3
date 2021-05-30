import time

y = int(input('Diga qual o primero numero da progressão aritimetica: '))
x = int(input('Diga qual a razão: '))
f = int(input('Diga qual o fim: '))
print('os 20 primeiros numeros da PA são:\n')
for n in range(y, f, x):
    print('{}'.format(y))
    y += x
    time.sleep(0.3)
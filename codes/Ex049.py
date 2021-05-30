import time

n = int(input('Escreva um numero para ver sua tabuada:'))
x = int(input('quer ver a tabuada do {}, de 1 até quanto?'.format(n)))
for i in range(1, x+1):
    print('{} x {}= {}'.format(i, n, n*i))
    time.sleep(0)
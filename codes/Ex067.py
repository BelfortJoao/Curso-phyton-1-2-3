import time
i = 0
while True:
    n = int(input('Escreva um numero para ver sua tabuada:'))
    if n < 0:
        break
    print("-------------------------------------------")
    while i < 10:
        i += 1
        print('{} x {}= {}'.format(i, n, n*i))
        time.sleep(0.1)
    print("-------------------------------------------")
    time.sleep(2)
    print('\n' * 16)
    i=0
print('Você digitou um numero negativo.')

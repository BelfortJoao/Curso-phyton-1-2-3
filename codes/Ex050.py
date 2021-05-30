s = 0
for i in range(0, 6):
    x = int(input('Digite um numero: '))
    if x % 2 == 0:
        s += x
print('A soma dos numeros pares é igual a {}'.format(s))

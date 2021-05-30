x = int(input('digite um numero: '))
y = 0

for i in range(2, x):
    if x % i == 0:
        print('o numero não é primo pois é divisivel por {}'.format(i))
        y = 1
if y != 1:
    print('O numero é primo')



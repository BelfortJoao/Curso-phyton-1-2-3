print('Bem vindo ao Contador numerico')
print('------------------------------')
x = int(input('Digite um numero: '))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print('------------------------------')
print('unidade: {}'.format(u))
print('dezenas: {}'.format(d))
print('centenas: {}'.format(c))
print('milhar: {}'.format(m))
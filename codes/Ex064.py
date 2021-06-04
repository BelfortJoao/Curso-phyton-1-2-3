n = 0
s = 0
h = 0
while n != 999:
    n = int(input('Digite um numero para somar [ou digite 999 para parar].'))
    s += n
    h += 1
print('Você digitou {} numeros e a  soma foi de {}'.format(h, s-999))

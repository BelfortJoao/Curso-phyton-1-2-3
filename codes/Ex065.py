n = 0
h = 0
s = 0
M = 0
m = 0
while n != 'N':
    h += 1
    x = int(input("digite um numero: "))
    n = str(input('Quer continuar? [S/N]: ')).upper()
    if x > M:
        M = x
    elif x < m:
        m = x
    s += x
print("""Você digitou {} numeros
A soma entre os valores foi de {}.
Sua media foi de {:.2f}
O maior foi {}
E o menor foi {}""".format(h, s, s/h, M, m))

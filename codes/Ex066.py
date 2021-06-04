n = 0
h = -1
s = 0
M = 0
m = 0
while True:
    h += 1
    x = int(input("digite um numero [ou digite 999 para parar]: "))
    if x == 999:
        break
    elif x > M:
        M = x
    elif x < m:
        m = x

    s += x
print("""Você digitou {} numeros
A soma entre os valores foi de {}.
Sua media foi de {:.2f}
O maior foi {}
E o menor foi {}""".format(h, s, s/h, M, m))
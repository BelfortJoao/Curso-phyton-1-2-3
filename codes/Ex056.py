n = str(input('Escreva uma frase: '))
s = n.split()
j = ''.join(s)
i = ''
for L in range(len(j) -1, -1, -1):
    i += j[L]
if i == j:
    print('{} e {} são iguais\nisso é um palindromo'.format(i, j))
else:
    print('{} e {} não são iguais\nisso não é um palindromo'.format(i, j))
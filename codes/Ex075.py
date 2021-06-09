x= int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: '))

print(f'Você digitou os valores {x}')
print(f'O valor 9 apareceu {x.count(9)} vezes')
if "3" in x:
    print(f'O três apareceu na posição {x.index(3)+1}')
else:
    print('O numero 3 não apareceu')
print('Os valores pares digitos foram: ', end=' ')
for n in x:
    if n % 2 == 0:
        print(n, end=" ")

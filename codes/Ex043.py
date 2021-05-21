k = float(input('Qual seu peso? '))
H = float(input('Qual sua altura? '))
i = k/H**2
print('-'*16)
if i <= 18.5:
    print('Abaixo do peso')
elif 18.5 < i <= 25:
    print('Peso ideal')
elif 25 < i <= 30:
    print('Sobrepeso')
elif 30 < i <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
y=0
for i in range(0, 5):
    x = float(input('Qual o peso? '))
    if x > y:
        y = x
print('O maior peso foi o de {:.2f}Kg'.format(y))
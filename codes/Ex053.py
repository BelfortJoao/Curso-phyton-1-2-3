y = 0
for i in range(0, 7):
    x = int(input('Qual a idade? '))
    if x >= 21:
        y += 1
print('{} pessoas são maiores de idade entre as 7.'.format(y))
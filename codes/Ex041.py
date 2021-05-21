print("Descubra sua categoria de natação")
x = int(input('Qual sua idade? '))
print('Sua categoria é : ')
if x <= 9:
    print('MIRIM')
elif 9 < x <= 14:
    print('INFANTIL')
elif 14 < x <= 19:
    print('JUNIOR')
elif 19 < x <= 20:
    print('SÊNIOR')
else:
    print('MASTER')

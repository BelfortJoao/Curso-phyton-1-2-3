
x = int(input('Lado 1: '))
y = int(input('Lado 2: '))
z = int(input('Lado 3: '))
if y-z < x < y+z:
    print("isso é um triangulo")
else:
    print("isso não é um triangulo")
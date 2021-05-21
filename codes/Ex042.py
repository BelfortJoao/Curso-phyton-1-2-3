x = int(input('Lado 1: '))
y = int(input('Lado 2: '))
z = int(input('Lado 3: '))
if y-z < x < y+z:
    print("Isso é um triangulo")
else:
    print("Isso não é um triangulo")
if x == y or y == z or z == x:
    print('Podemos formar um triangulo Isoceles')
    if x == y == z:
        print('Podemos formar um triangulo Equilatero')
else:
    print("Podemos formar um triangulo Escaleno")
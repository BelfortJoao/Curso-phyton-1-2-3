
x = int(input('1º numero: '))
y = int(input('2º numero: '))
z = int(input('3º numero: '))
m = x
if z < x and z < y:
    m = z
if y < x and y < z :
    m = y
ma = x
if z > x and z > y:
    ma = z
if y > x and y > z :
    ma = y
print("O maior numero foi {} e o menor foi {}".format(ma, m))

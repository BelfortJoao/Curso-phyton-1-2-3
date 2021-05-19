print("Vou advinhar se o ano é bissexto")
x = int(input('Digite o ano: '))
y = x % 4
z = x % 100
if y <= 0 or z <= 0:
    print("o o ano é bissexto")
else:
    print("o ano não é bissexto")
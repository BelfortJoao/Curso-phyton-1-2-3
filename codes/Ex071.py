Duz = 0
Cem = 0
Que = 0
Vin = 0
Dez = 0
cin = 0
um = 0
x = int(input('Quanto voce quer sacar: R$'))
while x > 200 and x > 0:
    Duz += 1
    x -= 200
while x > 100 and x > 0:
    Cem += 1
    x -= 100
while x > 50 and x > 0:
    Que += 1
    x -= 50
while x > 20 and x > 0:
    Vin += 1
    x -= 20
while x > 10 and x > 0:
    Dez += 1
    x -= 10
while x > 5 and x > 0:
    cin += 1
    x -= 5
while x > 1 and x > 0:
    um += 1
    x -= 1
print('--------------------------------------------------------------')
if Duz > 0:
    print(f"Total de {Duz} cedulas de R$200")
if Cem > 0:
    print(f"Total de {Cem} cedulas de R$100")
if Que > 0:
    print(f"Total de {Que} cedulas de R$50")
if Vin > 0:
    print(f"Total de {Vin} cedulas de R$20")
if Dez > 0:
    print(f"Total de {Dez} cedulas de R$10")
if cin > 0:
    print(f"Total de {cin} cedulas de R$5")
if um > 0:
    print(f"Total de {um} cedulas de R$1")
if x != 0:
    print(f'Alem de {x:.2f} centavos')
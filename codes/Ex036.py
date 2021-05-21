x = float(input('Qual o valor da casa que quer comprar? '))
y = int(input("em quantos anos quer comprar a casa? "))
z = int(input("Qual seu salario? "))
w = y*12
if x / w > (z/100)*30:
    print("Voce não pode comprar a casa")
else:
    print('Voce pode comprar a casa a parcela é de {:.2f}'.format(x/y))

print("""------------------------------------------------
BEM VINDO A COMPANIA DE VIAGENS DE ONIBUS
Cada passagem custa R$0.45 para viagens acima de 
 e R$050 para viagens abaixo de 200km
 ------------------------------------------------""")
x = int(input('Qual a distancia da viagem em Km: '))
if x <= 200:
    y = x*0.50
    print("Cada quilometro custa R$0.50\na viagem custou R${:.2f}".format(y))
else:
    y = x*0.45
    print("Cada quilometro custa R$0.45\na viagem custou R${:.2f}".format(y))
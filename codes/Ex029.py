print("""-----------------------------------------------------
 A multa para velocidade acima de 80 km é DE R$100.00
 para cada km acima da velocidade limite,
 serão adicionados R$7.25 a multa.
 ----------------------------------------------------""")
x = int(input("Qual velocidade do carro? "))
if x <= 80:
    print(" voce não foi multado")
else:
    print("Voce foi multado")
    y = 100 + ((x-80)*7.25)
    print('O valor da multa é de {:.2f}'.format(y))
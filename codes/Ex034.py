print(""" ----------------------------------------------------------------------
Funcionarios com salario acima de R$1250.00 vão receber 15% de aumento 
Funcionarios com salario menor que R$1250.00 vão receber 10% de aumento
 ----------------------------------------------------------------------""")
x = int(input('Qual seu salario? '))
if x <= 1250:
    y = (x/100)*115
    print("Voce recebeu 15% de aumento\nseu novo salario é de R${:.2f}".format(y))
else:
    y = (x/100)*110
    print("voce recebeu 10% de aumento\nseu novo salario é de R${:.2f}".format(y))

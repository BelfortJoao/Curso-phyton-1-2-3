h = 0
j = 0
k = 0
while True:
    print('--------------------------------------------------------------')
    print('CADASTRE UMA PESSOA')
    print('--------------------------------------------------------------')
    y = int(input('Idade: '))
    x = str(input('Sexo[M/F]: ')).upper()[0]
    z = str(input('Quer continuar? ')).upper()[0]

    if y >= 18:
        h += 1
    if x == 'M':
        j += 1
    if x == 'F' and y < 20:
        k += 1
    if z == 'N':
        print('Você escolheu sair.')
        break
print('--------------------------------------------------------------')
print(f"""RESULTADOS
Total de pessoas com mais de 18 anos: {h} 
Ao todo temos {j} homens cadastrados
E temos {k} mulheres com menos de 20 anos """)

print('--------------------------------------------------------------')



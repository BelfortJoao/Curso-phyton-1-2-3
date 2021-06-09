h = 0
j = 0
k = 0
c = 0
print('--------------------------------------------------------------')
print('LOJÃO BARATASSO')
print('--------------------------------------------------------------')
while True:
    y = str(input('Produto: '))
    x = float(input('preço: R$'))
    z = str(input('Quer continuar? ')).upper()[0]
    c += 1
    if c == 1:
        k = x
    j += x
    if x >= 1000:
        h += 1
    if x < k:
        k=x
    if z == 'N':
        print('Você escolheu sair.')
        break
print('--------------------------------------------------------------')
print(f"""RESULTADOS
print('--------------------------------------------------------------')
O total da compra foi R${j:.2f} 
Ao todo temos {h} produtos acima de R$1000.00
E o produto mais barato custou R${k:.2f} """)
print('--------------------------------------------------------------')
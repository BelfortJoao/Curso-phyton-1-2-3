r = 0
while r == 0:
    x = int(input('Qual o valor da Compra? '))
    print('[1] Dinheiro/cheque')
    print('[2] Debito')
    print('[3] 2X no Credito')
    print('[4] Mais parcelas')
    print('[5] Sair')
    z = str(input('Escolha uma forma de pagamento: '))
    if z == '1':
        print('O valor da compra é R${:.2f} com 10% de desconto'.format(x/100*90))
    elif z== '2':
        print('O valor da compra é R${:.2f} Com 5% de desconto'.format(x/100*95))
    elif z == '3':
        print('O valor da compra é R${:.2f} sem desconto'.format(x))
    elif z == '4':
        print('O valor da compra é R${:.2f} com 20% de juros'.format(x/100*120))
    elif z == '5':
        print('Voce saiu')
        r = 1
    else:
        print('Opção invalida')
    print('-'*25)
print('\n'*100)


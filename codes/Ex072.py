x = 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', ' treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
y=0
while True:
    y = -1
    while y not in range(0, 19):
        y = int(input('escolha um numero de 1 a 20 para que eu possa escrevelo: '))-1
    print(f'Voce escolheu o numero {x[y]}')
    n =str(input('Quer continuar?[S/N] ')).upper()
    if n == "N":
        break
print('Você saiu do programa.')
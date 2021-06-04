import random
s =0
Pi=0
h=0
while True:
    print('--------------------------------------------------------------')
    x = int(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    y = int(input('Escolha um numero de 1 a 10: '))
    if 0 > y or y > 10 :
        print('Numero invalido. ')
        break
    Pi = str(input('Escolha par ou impar [P/I]: ')).upper()

    s = x + y
    if Pi != "P" and Pi != 'I':
        print('Escolha invalida. ')
        break
    elif Pi == 'P':
        if s % 2 != 0:
            print('--------------------------------------------------------------\n'
                  "Você ficou com Par\n"
                  f"o computador escolheu {x} voce escolheu {y}  a soma deu {s}.\n"
                  "A resposta foi Impar\n")
            break
        else:
            print('--------------------------------------------------------------\n'
                  "Você ficou com Par\n"
                  f"o computador escolheu {x} voce escolheu {y}  a soma deu {s}.\n"
                  "A resposta foi Par\n")
    elif Pi == 'I':
        if s % 2 != 0 :
            print('--------------------------------------------------------------\n'
                "Você ficou com Impar\n"
                  f"o computador escolheu {x} voce escolheu {y}  a soma deu {s}.\n"
                  "A resposta foi Impar\n"
                  '--------------------------------------------------------------\n'
                  'VOCÊ GANHOU')

        else:
            print('--------------------------------------------------------------\n'
                "Você ficou com Impar\n"
                  f"o computador escolheu {x} voce escolheu {y}  a soma deu {s}.\n"
                  "A resposta foi Par\n")
            break
    h += 1
print('--------------------------------------------------------------\n'
      'VOCÊ PERDEU\n'
      '--------------------------------------------------------------\n'
      f'Total de vitorias seguidas {h}')



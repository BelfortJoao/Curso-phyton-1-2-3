import emoji
x1 = float(input('Qual a sua 1ª nota? '))
x2 = float(input('Qual a sua 2ª nota? '))
x3 = float(input('Qual a sua 3ª nota? '))
med = (x1+x2+x3)/3
print('Sua media foi de {:.2f} pontos esse ano '.format(med))
if med < 60:
    print(emoji.emojize('Voce não passou de ano :sob:', use_aliases=True, variant="emoji_type"))
else:
    print('Voce passou de ano!!!!')

x = 'Fortaleza', 'Athletico Paranaense', 'Atlético GO', 'Bragantino', 'Bahia', 'Fluminense', 'Palmeiras', 'Flamengo', 'Atlético Mineiro', 'Corinthians', 'Ceará', 'Santos', 'Cuiabá', 'Sport Recife', 'São Paulo', 'Juventude', 'Internacional', 'Grêmio', 'América Mineiro', 'Chapecoense'
print(f'A lista de times do brasileirão é: {x}')
print(f'Os cinco primeiros colocados são {x[0:6]}')
print(f'Os quatro ultimos colocados são{x[-4:]}')
print('Em ordem alfabetica os 20 colocados são: ', sorted(x))
print(f'E o chapecoense esta em {x.index("Chapecoense")+1}º lugar')

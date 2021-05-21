x = int(input('Qual sua idade? '))
n = str(input('Qual seu nome? '))
if x == 18:
    print('{}, você precisa se alistar esse ano'.format(n))
elif x < 18:
    print('Olá, {} você precisa se alistar em {} anos.'.format(n, 18-x))
else:
    print('Ei {}!!!! Já passou {} anos da sua idade de se alistar'.format(n, x-18))
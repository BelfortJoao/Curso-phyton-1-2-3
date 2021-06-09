from random import  randint
x = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('sorteei os numeros:', end='')
for n in x:
    print(f'{n}', end=", ")
print(f"\nO maior valor na ordem foi {max(x)}")
print(f"\nO menor valor na ordem foi {min(x)}")

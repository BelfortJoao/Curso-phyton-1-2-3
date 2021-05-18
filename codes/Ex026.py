x = input('Digite algo para eu achar os As: ').upper()
print('Em {} existem {} A'.format(x, x.count('A')))
print('A aparece na na {}ª casa'.format(x.find('A') + 1))
print('E aparece por ultimo na {}ª casa'.format(x.rfind('A')+1))
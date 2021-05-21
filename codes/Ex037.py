r = 0
while r == 0:
    x = int(input('write any number in decimal: '))
    print('[1] Hexadecimal')
    print('[2] Binary')
    print('[3] Octal')
    print('[4] Exit')
    z = str(input('What base do you want? '))
    if z == '1':
        print('The value in Hexadecimal is {}'.format(hex(x)))
    elif z== '2':
        print('The value in Binary is {}'.format(bin(x)))
    elif z == '3':
        print('The value in Octal is {}'.format(oct(x)))
    elif z == '4':
        print('you Exit the convertor')
        r = 1
    else:
        print('Invalid Option')
    print('-'*25)
print('\n'*100)





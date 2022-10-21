while True:
    number = int(input('Elige un numbero del 1 al 8: '))
    if number >= 1 and number <= 8:
        print('Height: {}'.format(number))
        break

for i in range(number):    
    print(' ' * (number - i) + '#' * (i + 1) + ' ' * 3 + '#' * (i + 1))

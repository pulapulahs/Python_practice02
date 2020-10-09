while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 5:
        print('Too small')
        continue
    print('Input is of sufficient length')
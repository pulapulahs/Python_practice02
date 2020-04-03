number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # 新程序块的开始处
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # 新程序块的结尾处
elif guess < number:
    # 另一个程序块
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')

print('Done')
# 在 if 语句执行结束后，最后这句总是会被执行。

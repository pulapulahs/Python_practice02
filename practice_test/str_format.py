age = 20
name = 'Swaroop'
book = 'A Byte of Python'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# 取十进制小数点后的精度为  3 ，得到的浮点数为 '0.333'
print('{0:.3f}'.format(1.0/3))

# 填充下划线 (_)，文本居中
# 将 '___hello____' 的宽度扩充为 11
print('{0:_^20}'.format('hello'))

print("#用基于关键字的方法打印显示 'Swaroop wrote A Byte of Python':")
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print('指定end为空格或空：a', end=' ')
print('b')

print('以下是转义序列')
print('What\'s your name?')
print("What's your name?")

print('This is the first line\nThis is the second line')

print("This is the first sentence.\
      This is the second sentence.")

print("#原始字符串")

s = "This is a string.\
    This continues the string."
print(s)



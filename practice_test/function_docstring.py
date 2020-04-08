# 文档字符串 - DocStrings
# DocStrings 的书写惯例是：首行首字母大写，结尾有句号；第二行为空行；第三行以后为详细的描述。
# 我们 强烈建议 你在编写任何非平凡函数时都遵守这种惯例，那些只有几行的平凡函数可以不遵守这个惯例。


def print_max(x, y):  # 通过 print_max 函数的 __doc__ 属性来访问它的 DocStrings
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # 如果有必要，将参数转为整数
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(3, 5)
print(print_max.__doc__)

help(print_max)  # help() 函数，可以抓取对应函数的 __doc__属性，并以美观的方式打印出来。

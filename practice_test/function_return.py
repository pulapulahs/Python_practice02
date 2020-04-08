# return语句


def maximum(x, y):  # maximum函数 会返回参数中的最大值
    if x > y:   # 使用简单的if else 语句找到并返回最大值
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y


print(maximum(3, 2))

# 注：没有返回值的return 语句 等价于 return None


# 如果函数没有return语句，系统会自己在函数尾部添加 return None 语句
# 可以通过 print(some_funciton()) 来观察


def some_function():
    pass


print(some_function())


# global语句


x = 50
y = 20
z = 30


def func():
    global x, y, z  # global 用于声明 x 是一个全局变量，在函数内为 x 赋值时，主程序块中的 x 值也变了
    # 可以同时指定多个全局变量

    print('x,y,z are', x, y, z)
    x = 2
    y = 1
    z = 5
    print('Changed global x,y,z to', x, y, z)


func()
print('Value of x, y, z is', x, y, z)

# 默认参数值
# 默认值不可改变，且必须是常数


def say(message, times=1):   # say 函数用于多次输出指定的字符串，不指定次数，默认只打印一次，通过将默认值 1 赋给形参 times实现
    print(message * times)


say('love')  # 打印默认值次数
say('you', 5)   # 重新指定打印次数

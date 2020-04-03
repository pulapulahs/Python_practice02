# jump7
# 目标： 写入代码，打印 1 到 100 之间（包含 1 和100），不是7的倍数，且不包含7 的数字，每行打印一个数字。

for a in range(1, 101):
    if a % 7 == 0:  # 除以7 余数为0，证明是7的倍数
        pass
    elif a % 10 == 7:  # 除以10 余数为7，证明数中有7
        pass
    elif a // 10 == 7:  # 可以整除10，等于7，是7的10数倍
        pass
    else:
        print('我是与7无关的数字{}'.format(a))
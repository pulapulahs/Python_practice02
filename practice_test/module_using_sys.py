import sys  # 利用import 引入 sys模块（sys模块包含着python解释器和它的环境有关的函数）
import os


print('The command line arguments are:')
for i in sys.argv:   # sys模块中的 argv 变量，可以通过点表示法 sys.argv 访问
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

# 运行使用：python module_using_sys.py we are arguments


print(os.getcwd())  # 查看程序的当前目录

# print((2 + 3) * 4)
# 矩形的长和宽分别保存在变量 length 和 breadth 中。
# 在表达式的帮助下，我们使用长和宽来计算矩形的面积和周长。
# 我们将表达式 length * breadth 的计算结果保存到变量 area 中，然后用 print 函数将其打印输出。
# 第二种情况是，我们直接在 print 函数中使用表达式 2 * (length + breadth) 的值。

length = 5
breadth = 2

area = length * breadth
print('面积 = ', area)
print('周长 = ', 2 *(length + breadth))

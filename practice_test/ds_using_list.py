# 这是我的购物清单
shoplist = ['apple', 'mango', 'carrot', 'banana', 'durian']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end='')
for item in shoplist:  # 遍历列表中的元素
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')  # 使用列表对象中的  append 方法向列表中添加一个元素
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()   # sort方法进行排序
print('Sorted shopping list is', shoplist)

print('The first item I will buy is ', shoplist[0])
olditem = shoplist[1]
del shoplist[0]   # 删除指定项
print('The first item I will buy is', olditem)
print('My shopping list is now', shoplist)

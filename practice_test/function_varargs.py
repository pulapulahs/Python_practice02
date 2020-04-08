# 可变参数


def total(a=5, *numbers, **phonebook):   # 当声明一个带星号的参数 *param 时，从这个参数开始，之后所有的参数都会被收入名为 param的字典中
    print('a', a)

    # 遍历元祖中的所有项
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))

# 后续深入学习元组和字典

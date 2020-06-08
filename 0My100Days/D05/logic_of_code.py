# -*- coding: utf-8 -*-
# AUTHOR: Haotian Fan   TIME: 2020/6/3

# 水仙花数
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
#

# 正整数的反转
num2 = int(input('num = '))
reversed_num = 0
while num2 > 0:
    reversed_num = reversed_num * 10 + num2 % 10
    num2 //= 10
print(reversed_num)
#

# 百鸡百钱
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (x, y, z))

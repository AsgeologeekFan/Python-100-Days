# -*- coding: utf-8 -*-
# AUTHOR: Haotian Fan   TIME: 2020/6/3
#
# #
# from random import randint
# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fmn = 1
# for num in range(1, m - n + 1):
#     fmn *= num
# print(fm // fn // fmn)
# #
#
# # 定义函数测试
#
#
# def factorial(num):
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return result
#
#
# m = int(input('m = '))
# n = int(input('n = '))
# print(factorial(m) // factorial(n) // factorial(m - n))
#
# # 函数的参数
# def roll_dice(n=2):
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total
#
#
# def add(a=0, b=0, c=0):
#     return a + b + c
#
# # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
# # 摇三颗色子
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# # 传递参数时可以不按照设定的顺序进行传递
# print(add(c=50, a=100, b=200))
# #

######


def add(*args):
    total = 0
    for val in args:
        total += val
    return total


def main():
    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    print(add(1, 3, 5, 7, 9))
    return


if __name__ == '__main__':
    main()

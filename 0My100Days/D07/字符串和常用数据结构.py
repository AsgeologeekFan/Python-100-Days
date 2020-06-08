# -*- coding: utf-8 -*-
# AUTHOR: Haotian Fan   TIME: 2020/6/3
a, b = 5, 10
print('%.2f * %.3f = %d' % (a, b, a * b))

scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)

import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(1.0)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()

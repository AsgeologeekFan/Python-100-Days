# -*- coding: utf-8 -*-
# AUTHOR: Haotian Fan   TIME: 2020/6/2
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('Please input: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('运气不佳')

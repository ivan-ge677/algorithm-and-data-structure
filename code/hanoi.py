#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   hanoi.py    
@Contact :   ivan.ge@nio.com
@License :   (C)Copyright 2015-2021, NIO

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/2/8 8:22 下午   Ivan.GE      1.0         None
'''


def hanoi(n,a,b,c):
    # 汉诺塔问题
    # 把n个盘子从a经过b移动到c
    if n > 0:
        hanoi(n-1,a,c,b)
        print("moving plate %s from %s to %s"%(n,a,c))
        hanoi(n-1,b,a,c)


if __name__ == '__main__':
    hanoi(20,'a','b','c')
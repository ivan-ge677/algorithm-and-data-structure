#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   search_algorithm.py
@Contact :   ivan.ge@nio.com
@License :   (C)Copyright 2015-2021, NIO

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/2/8 8:34 下午   Ivan.GE      1.0         None
'''
from calc_time import calc_time


@calc_time
def linear_search(li,val):
    # 线性查找
    # 时间复杂度O(n)
    # python自带的index函数使用线性查找
    for ind,value in enumerate(li):
        if value == val:
            return ind
    return -1


@calc_time
def binary_search(li,val):
    # 二分查找
    # 时间复杂度O(logn)
    # 列表必须是排好序的
    left = 0
    right = len(li) - 1
    while left <= right:
        middle = (left + right)//2
        now = li[middle]
        if now > val:
            right = middle - 1
        elif now < val:
            left = middle + 1
        elif now == val:
            return middle
    return -1


if __name__ == '__main__':
    li = list(range(1000))
    val = 900
    ind1 = linear_search(li,val)
    ind2 = binary_search(li,val)

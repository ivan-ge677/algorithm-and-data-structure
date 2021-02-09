#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        :   sort_algorithm.py    
@Contact     :   ivan.ge@nio.com
@License     :   (C)Copyright 2015-2021, NIO
@Modify Time :   2021/2/8 10:19 下午
@Author      :   Ivan.GE 
@Version     :   1.0
@Desciption  :   None
"""
from calc_time import calc_time
import random
import sys
# 设置递归最大深度
sys.setrecursionlimit(100000)


@calc_time
def baseline_sort(li):
    li.sort()


@calc_time
def bubble_sort(li):
    # 冒泡排序
    # 复杂度:O(n^2)
    N = len(li)
    for i in range(N - 1):
        for j in range(N - i - 1):
            now = li[j]
            next = li[j + 1]
            if now > next:
                li[j], li[j + 1] = next, now


@calc_time
def select_sort(li):
    # 选择排序
    # 复杂度：O(n^2)
    N = len(li)
    for i in range(N - 1):
        max_ind = 0
        for j in range(1, N - i):
            if li[max_ind] < li[j]:
                max_ind = j
        li[max_ind], li[j] = li[j], li[max_ind]


@calc_time
def insert_sort(li):
    # 插入排序
    # 复杂度：O(n^2)
    N = len(li)
    for i in range(1, N):
        now = li[i]
        j = i - 1
        while now < li[j] and j >= 0:
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = now


@calc_time
def quick_sort(li):
    # 快速排序
    # 复杂度：O(nlogn)
    def _quick_sort(li, left, right):

        def partition1(li, left, right):
            # 第一种快速排序算法
            now = li[left]
            flag = True
            while left < right:
                if flag:
                    if li[right] < now:
                        li[left] = li[right]
                        left = left + 1
                        flag = not flag
                    else:
                        right = right - 1
                else:
                    if li[left] > now:
                        li[right] = li[left]
                        right = right - 1
                        flag = not flag
                    else:
                        left = left + 1
            li[left] = now
            return left

        def partition2(li, left, right):
            # 第二种快速排序算法
            now = li[left]
            while left < right:
                while left < right and li[right] >= now:
                    right = right - 1
                li[left] = li[right]
                while left < right and li[left] <= now:
                    left = left + 1
                li[right] = li[left]
            li[left] = now
            return left

        if left < right:
            mid = partition1(li, left, right)
            _quick_sort(li, mid + 1, right)
            _quick_sort(li, left, mid - 1)

    left = 0
    right = len(li) - 1
    _quick_sort(li, left, right)


if __name__ == '__main__':
    li = list(range(1000))
    li.append(3)
    li.append(8)
    random.shuffle(li)
    li1 = li.copy()
    baseline_sort(li1)
    li2 = li.copy()
    bubble_sort(li2)
    li3 = li.copy()
    select_sort(li3)
    li4 = li.copy()
    insert_sort(li4)
    li5 = li.copy()
    quick_sort(li5)

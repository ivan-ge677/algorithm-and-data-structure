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


"""
NB三人组
时间：快速排序<归并排序<堆排序
缺点：快速排序最差时间复杂度为O(n^2)，最差空间复杂度O(n)
     归并排序需要开辟新空间
     堆排序最慢
稳定性：归并排序是稳定排序，快速排序与堆排序是不稳定排序
"""


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


@calc_time
def heap_sort(li):
    # 堆排序
    # 复杂度：O(nlogn)
    def sift(li, low, high):
        top = li[low]
        i = low
        j = 2 * i + 1
        while j <= high:
            if j + 1 <= high and li[j + 1] > li[j]:
                j = j + 1
            if top < li[j]:
                li[i] = li[j]
                i = j
                j = 2 * i + 1
            else:
                li[i] = top
                break
        li[i] = top

    N = len(li)
    # 建一个大根堆
    for i in range((N - 1) // 2, -1, -1):
        sift(li, i, N - 1)
    # 将堆顶与堆底置换，堆长度减一，把新堆进行正序
    for j in range(N - 1, 0, -1):
        li[j], li[0] = li[0], li[j]
        sift(li, 0, j - 1)


@calc_time
def heap_sort_inner(li):
    # 内置堆排序
    import heapq
    # 建一个小根堆
    heapq.heapify(li)
    result = []
    for i in range(len(li)):
        result.append(heapq.heappop(li))
    return result


"""
top k问题
heap排序后切片：O(nlogn)
lowB三人组：O(nk)
heap排序：O(nlogk)
"""


@calc_time
def topk_heap(li, k):
    def sift(li, low, high):
        top = li[low]
        i = low
        j = 2 * i + 1
        while j <= high:
            if j + 1 <= high and li[j + 1] < li[j]:
                j = j + 1
            if top > li[j]:
                li[i] = li[j]
                i = j
                j = 2 * i + 1
            else:
                li[i] = top
                break
        li[i] = top

    topk = li[:k]
    # 1.建一个小根堆（sift进行修改）
    for i in range((k - 1) // 2, -1, -1):
        sift(topk, i, k - 1)
    # 2.将剩下的数按条件插入小根堆
    for j in range(k, len(li)):
        if li[j] > topk[0]:
            topk[0] = li[j]
            sift(topk, 0, k - 1)
    # 3.依次取数为列表
    for j in range(k - 1, 0, -1):
        topk[j], topk[0] = topk[0], topk[j]
        sift(topk, 0, j - 1)
    return topk


@calc_time
def merge_sort(li):
    # 归并排序
    # 复杂度：O(nlogn)
    # 需要开辟新空间，所以不是原地排序，空间复杂度为O(n)
    def _merge_sort(li, left, right):
        if right != left:
            mid = (left + right) // 2
            # 对左边排序
            _merge_sort(li, left, mid)
            # 对右边排序
            _merge_sort(li, mid + 1, right)
            # 进行归并操作
            le_p = left
            ri_p = mid + 1
            ltmp = []
            while le_p <= mid and ri_p <= right:
                if li[le_p] < li[ri_p]:
                    ltmp.append(li[le_p])
                    le_p = le_p + 1
                else:
                    ltmp.append(li[ri_p])
                    ri_p = ri_p + 1
            while le_p <= mid:
                ltmp.append(li[le_p])
                le_p = le_p + 1
            while ri_p <= right:
                ltmp.append(li[ri_p])
                ri_p = ri_p + 1
            li[left:right + 1] = ltmp

    _merge_sort(li, 0, len(li) - 1)


@calc_time
def shell_sort(li):
    # 希尔排序
    # 分组的内部使用插入排序
    def insert_sort_gap(li, gap):
        for i in range(gap, len(li)):
            val = li[i]
            j = i - gap
            while j >= 0 and val < li[j]:
                li[j + gap] = li[j]
                j -= gap
            li[j + gap] = val

    N = len(li)
    while N >= 1:
        N = N // 2
        insert_sort_gap(li, N)


@calc_time
def count_sort(li):
    # 计数排序
    # 明确最大值与最小间隔(这里默认为1）
    max_val = max(li)
    count_li = [0 for i in range(max_val + 1)]
    for val in li:
        count_li[val] += 1
    li.clear()
    for j, value in enumerate(count_li):
        li.extend([j] * value)


@calc_time
def bucket_sort(li):
    # 桶排序
    # 桶内部使用冒泡排序的思想进行排序
    bucket_num = len(li) // 10
    bucket = [[] for i in range(bucket_num)]
    for val in li:
        ind = min(val // 10, bucket_num - 1)
        N = len(bucket[ind])
        bucket[ind].append(val)
        for i in range(N - 1, -1, -1):
            if val < bucket[ind][i]:
                bucket[ind][i], bucket[ind][i + 1] = bucket[ind][i + 1], bucket[ind][i]
    li.clear()
    for i in range(bucket_num):
        li.extend(bucket[i])


@calc_time
def radix_sort(li):
    # 基数排序
    # 利用分桶是稳定的特性，先对个位数分桶，在对十位数分桶，以此类推
    max_value = max(li)
    i = 0
    while 10 ** i <= max_value:
        bucket = [[] for _ in range(10)]
        for var in li:
            ind = (var // 10 ** i) % 10
            bucket[ind].append(var)
        li.clear()
        for buc in bucket:
            li.extend(buc)
        i += 1


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
    li6 = li.copy()
    heap_sort(li6)
    # li6_10 = li.copy()
    # top10 = topk_heap(li6_10, 10)
    li7 = li.copy()
    merge_sort(li7)
    li8 = li.copy()
    shell_sort(li8)
    li9 = li.copy()
    count_sort(li9)
    li10 = li.copy()
    bucket_sort(li10)
    li11 = li.copy()
    radix_sort(li11)

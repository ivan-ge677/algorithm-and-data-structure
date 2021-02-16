#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        :   greedy algorithm.py    
@Contact     :   ivan.ge@nio.com
@License     :   (C)Copyright 2015-2021, NIO
@Modify Time :   2021/2/15 2:09 下午
@Author      :   Ivan.GE 
@Version     :   1.0
@Desciption  :   None
"""
# problem1：拼接最大数字问题
# 有n个非负整数，将其按照字符串拼接的方式拼接成一个整数，如何拼接可以得到整数最大
# [32,94,128,1286,6,71]
# ex：32与92相比，由于9232>3292,所以将92排在32前面，这种比较方法排序之后，可以保证整数最大

# problem2：活动选择问题
# 有n个活动，每个活动有开始时间和结束时间，要求安排活动使能够开展的活动数最多
# [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),8,11),(8,12),(2,14),(12,16)]
# 最先结束的活动一定是最优解的一部分（反证法可以证明）

from functools import cmp_to_key


def compare_rule(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


def number_join(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(compare_rule))
    return "".join(li)


def activity_selection(activity):
    activity.sort(key=lambda x: x[1])
    res = [activity[0]]
    for i in range(1, len(activity)):
        if activity[i][0] >= res[-1][1]:  # 当前活动的开始时间小于等于最后一个入选活动的结束时间
            res.append(activity[i])
    return res


if __name__ == '__main__':
    li = [32, 94, 128, 1286, 6, 71]
    print(number_join(li))
    act = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    print(activity_selection(act))

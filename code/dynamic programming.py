#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        :   dynamic programming.py    
@Contact     :   ivan.ge@nio.com
@License     :   (C)Copyright 2015-2021, NIO
@Modify Time :   2021/2/15 5:08 下午
@Author      :   Ivan.GE 
@Version     :   1.0
@Desciption  :   None
"""


# 钢条切割问题
def cut_rod(p, n):
    # 利润
    profit = [0]
    # 切割的第一部分
    cut = [0]
    # 切割方案
    solution = []
    len_p = len(p)
    for i in range(1, n + 1):
        maximum = 0
        if i < len_p:
            for j in range(1, i + 1):
                if maximum < p[j] + profit[i - j]:
                    maximum = p[j] + profit[i - j]
                    first = j
            profit.append(maximum)
            cut.append(first)
        else:
            for j in range(1, len_p):
                if maximum < p[j] + profit[i - j]:
                    maximum = p[j] + profit[i - j]
                    first = j
            profit.append(maximum)
            cut.append(first)
    nn = n
    while nn > 0:
        solution.append(cut[nn])
        nn -= cut[nn]
    return solution


# 最长公共子序列
def LCS(x, y):
    m = len(x)
    n = len(y)
    # 当前位置最长子序列长度
    A = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    # source 1:左上方；2：上方；3：左方
    S = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    lcs = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[j - 1] == y[i - 1]:
                A[i][j] = A[i - 1][j - 1] + 1
                S[i][j] = 1
            elif A[i - 1][j] > A[i][j - 1]:
                A[i][j] = A[i - 1][j]
                S[i][j] = 2
            else:
                A[i][j] = A[i][j - 1]
                S[i][j] = 3
    # print(S)
    # 输出最大序列
    while i > 0 and j > 0:
        if S[i][j] == 1:
            lcs.append(x[j - 1])
            i -= 1
            j -= 1
        elif S[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return "".join(lcs)


if __name__ == '__main__':
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
    print(cut_rod(p, 22))
    x = "BDCABA"
    y = "ABCBDAB"
    print(LCS(x, y))

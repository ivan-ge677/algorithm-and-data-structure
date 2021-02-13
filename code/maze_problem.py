#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        :   maze_problem.py    
@Contact     :   ivan.ge@nio.com
@License     :   (C)Copyright 2015-2021, NIO
@Modify Time :   2021/2/11 10:13 上午
@Author      :   Ivan.GE 
@Version     :   1.0
@Desciption  :   None
"""
from collections import deque
import copy


def find_path_stack(maze, start, end):
    # 深度搜索算法
    # 使用栈结构实现
    # path列表中存放的是走过的路径
    next_path = [
        lambda x, y: (x + 1, y),
        lambda x, y: (x, y + 1),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y - 1)
    ]
    path = [start]
    while len(path) > 0:
        curnode = path[-1]
        if curnode == end:
            print(path)
            break
        for pa in next_path:
            nextnode = pa(curnode[0], curnode[1])
            if maze[nextnode[0]][nextnode[1]] == 0:
                path.append(nextnode)
                maze[nextnode[0]][nextnode[1]] = 2
                break
        else:
            maze[curnode[0]][curnode[1]] = 2
            path.pop()
    else:
        print('no way out')


def print_path(path):
    node = path[-1]
    pathway = [node[0:2]]
    while (node[0], node[1]) != (start[0], start[1]):
        ind = node[2]
        node = path[ind]
        pathway.append(node[0:2])
    for i in range(len(pathway) - 1, -1, -1):
        print(pathway[i], end=', ')


def find_path_deque(maze, start, end):
    # 广度搜索算法
    # 使用队列结构实现
    # path列表中存放的是当前所在的节点
    next_path = [
        lambda x, y: (x + 1, y),
        lambda x, y: (x, y + 1),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y - 1)
    ]
    path = deque()
    path.append((start[0], start[1], -1))
    maze[start[0]][start[1]] = 2
    node = []
    while len(path) > 0:
        curnode = path.popleft()
        node.append(curnode)
        if curnode[0] == end[0] and curnode[1] == end[1]:
            print("find way out")
            print_path(node)
            break
        for pa in next_path:
            nextnode = pa(curnode[0], curnode[1])
            if maze[nextnode[0]][nextnode[1]] == 0:
                path.append((nextnode[0], nextnode[1], len(node) - 1))
                maze[nextnode[0]][nextnode[1]] = 2
    else:
        print("no way out")


if __name__ == '__main__':
    maze_max = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    start = (1, 1)
    end = (10, 12)
    maze1 = copy.deepcopy(maze_max)
    find_path_stack(maze1, start, end)
    # maze2 = copy.deepcopy(maze_max)
    # find_path_deque(maze2, start, end)

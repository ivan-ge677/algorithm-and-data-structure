#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        :   tree.py    
@Contact     :   ivan.ge@nio.com
@License     :   (C)Copyright 2015-2021, NIO
@Modify Time :   2021/2/13 10:05 上午
@Author      :   Ivan.GE 
@Version     :   1.0
@Desciption  :   None
"""


class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __repr__(self):
        # 重写print方法与调用Node的打印方式
        return self.name

    def __str__(self):
        # 覆盖__repr__中的print方法
        return self.name + " " + self.type


class FileSystemTree:
    def __init__(self):
        self.root = Node(name="/")
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != "/":
            name += "/"
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError('invalid dir')


if __name__ == '__main__':
    tree = FileSystemTree()
    tree.mkdir("var/")
    tree.mkdir("bin/")
    tree.mkdir("bin")

    tree.cd("bin/")
    tree.mkdir("python/")

    print(tree.ls())

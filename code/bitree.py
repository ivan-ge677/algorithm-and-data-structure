#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        :   bitree.py    
@Contact     :   ivan.ge@nio.com
@License     :   (C)Copyright 2015-2021, NIO
@Modify Time :   2021/2/13 10:35 上午
@Author      :   Ivan.GE 
@Version     :   1.0
@Desciption  :   None
"""
from collections import deque


class BiTreeNode:
    # 二叉树
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:
    # 二叉搜索树
    def __init__(self, data=[]):
        self.root = None
        for val in data:
            self.insert(val)

    def insert(self, val):
        # 递归插入法
        if self.root:
            self._insert(self.root, val)
        else:
            self.root = BiTreeNode(val)

    def _insert(self, node, val):
        if val < node.data:
            if not node.lchild:
                node.lchild = BiTreeNode(val)
                node.lchild.parent = node
            else:
                self._insert(node.lchild, val)
        elif val > node.data:
            if not node.rchild:
                node.rchild = BiTreeNode(val)
                node.rchild.parent = node
            else:
                self._insert(node.rchild, val)
        elif val == node.data:
            raise ValueError('value exists')

    def insert_no_rec(self, val):
        # 循环插入法
        if not self.root:
            self.root = BiTreeNode(val)
            return
        p = self.root
        while p:
            if val < p.data:
                if not p.lchild:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    break
                else:
                    p = p.lchild
            elif val > p.data:
                if not p.rchild:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    break
                else:
                    p = p.rchild
            elif val == p.data:
                raise ValueError('value exists')

    def query(self, val):
        if self.root:
            return self._query(self.root, val)
        else:
            raise ValueError("empty tree")

    def _query(self, node, val):
        if not node:
            raise ValueError('value not exists')
        elif val < node.data:
            return self._query(node.lchild, val)
        elif val > node.data:
            return self._query(node.rchild, val)
        elif val == node.data:
            return node

    def query_no_rec(self, val):
        if not self.root:
            raise ValueError("empty tree")
        else:
            p = self.root
        while p:
            if val < p.data:
                p = p.lchild
            elif val > p.data:
                p = p.rchild
            elif val == p.data:
                return p
        else:
            raise ValueError("value not exists")

    def delete_node_leaf(self, node):
        if node.parent:
            if node.parent.lchild == node:
                node.parent.lchild = None
            elif node.parent.rchild == node:
                node.parent.rchild = None
        else:
            self.root = None

    def delete_node_l(self, node):
        if node.parent:
            if node.parent.lchild == node:
                node.parent.lchild = node.lchild
            elif node.parent.rchild == node:
                node.parent.rchild = node.lchild
        else:
            self.root = node.lchild

    def delete_node_r(self, node):
        if node.parent:
            if node.parent.lchild == node:
                node.parent.lchild = node.rchild
            elif node.parent.rchild == node:
                node.parent.rchild = node.rchild
        else:
            self.root = node.rchild

    def delete(self, value):
        node = self.query(value)
        if not node.lchild and not node.rchild:
            self.delete_node_leaf(node)
        elif not node.lchild:
            self.delete_node_r(node)
        elif not node.rchild:
            self.delete_node_l(node)
        else:
            p = node
            while p.lchild:
                p = p.lchild
            node.data = p.data
            self.delete_node_r(p)

    def in_order(self, node):
        if node:
            self.in_order(node.lchild)
            print(node.data, end=',')
            self.in_order(node.rchild)


def level_order(root):
    # 二叉树的层次遍历法
    queue = deque()
    queue.append(root)
    while (len(queue)) > 0:
        node = queue.popleft()
        print(node.data, end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


if __name__ == '__main__':
    tree = BST([1, 2, 3, 9, 8, 4, 6, 7, 5])
    tree.in_order(tree.root)
    print(tree.query(5).data)
    tree.delete(5)
    tree.in_order(tree.root)
    tree.delete(6)
    tree.in_order(tree.root)
    tree.delete(1)
    tree.in_order(tree.root)

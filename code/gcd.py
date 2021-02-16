#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        :   gcd.py    
@Contact     :   ivan.ge@nio.com
@License     :   (C)Copyright 2015-2021, NIO
@Modify Time :   2021/2/16 12:38 下午
@Author      :   Ivan.GE 
@Version     :   1.0
@Desciption  :   None
"""
class fraction:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        g = fraction.gcd(self.a,self.b)
        self.a = self.a/g
        self.b = self.b/g

    def __repr__(self):
        return "%s/%s"%(int(self.a),int(self.b))

    @staticmethod
    def gcd(a,b):
        while b>0:
            r = a%b
            a = b
            b = r
        return a

    @staticmethod
    def zgb(a,b):
        g = fraction.gcd(a,b)
        return a*b/g

    def __add__(self, other):
        a1 = self.a
        b1 = self.b
        a2 = other.a
        b2 = other.b
        z = fraction.zgb(b1,b2)
        a = a1*z/b1+a2*z/b2
        return fraction(a,z)


if __name__ == '__main__':
    f1 = fraction(33,12)
    f2 = fraction(22,8)
    print(f1)
    print(f2)
    print(f1+f2)

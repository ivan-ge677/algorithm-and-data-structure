#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   calc_time.py    
@Contact :   ivan.ge@nio.com
@License :   (C)Copyright 2015-2021, NIO

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/2/8 9:11 下午   Ivan.GE      1.0         None
'''
import time

def calc_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print("%s running time %s secs."%(func.__name__,-start+end))
        return result
    return wrapper
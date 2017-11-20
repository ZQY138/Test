#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# @Author:Zhang
# @Time:2017/11/20 20:13
import time, functools
'''
装饰器打印函数运行时间
'''


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        startTime = time.time()
        res = fn(*args, **kw)
        endTime = time.time()
        print '%s execued in %s ms' % (fn.__name__, endTime - startTime)
        print res
    return wrapper


def begin_end(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print "%s begin call" % fn.__name__
        print "%s result is:" % fn.__name__, fn(*args, **kw)
        print "%s end call" % fn.__name__
    return wrapper


# 测试
# @begin_end
# @metric
# def add(n):
#     time.sleep(0.123)
#     s = 0
#     for i in range(n):
#         s = s+i
#     return s


@begin_end
# @metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


# a = add(101)
s = slow(11, 22, 33)






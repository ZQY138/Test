#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# @Author:Zhang
# @Time:2017/11/20 10:43


class Test():
    """
    用于初始化类
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def res(self):
        return (self.a, self.b)

    def __str__(self):
        return '这是一个类'


t = Test(2, 3)
print t.__doc__
print "**************"
print t

def foo(arg, a):
    x = 1
    y = 'xxxxxx'
    for i in range(10):
        j = 1
        k = i
    print locals()


foo(1, 2)

# coding: utf-8
'''
Created on 2012/01/24
'''

class A(object):
    def append(self, val, L=[]):
        L.append(val)
        print L
        
a=A()
a.append(1)

a2=A()
a2.append(2)
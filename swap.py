# -*- coding: utf-8 -*-

def swap(a,b):
  a = a + b
  b = a - b
  a = a - b
  return a,b

############test###########

x = 42
y = 69
print "Las variables X e Y antes de intercamviar valores",x,y
x,y = swap(x,y)
print "Las variables X e Y antes de intercamviar valores",x,y

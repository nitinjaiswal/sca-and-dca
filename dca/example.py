#!/usr/bin/python2.6

import timetravelpdb
timetravelpdb.set_trace()
import os

x = 500

def add10(number):
  return number + 10

print "foo"
print "bar"
print "baz"



y = add10(x)
x = 15
z = x + y

for i in range(15):
  print "THE NUMBER IS", i
y = add10(i)

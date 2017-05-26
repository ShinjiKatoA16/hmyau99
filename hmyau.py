#!/usr/bin/python
#-*- coding: utf-8 -*-

# Python2 version. does not work on Python3
for row in range(1,10):
    for col in range(1,10):
        print '%dx%d=%2d ' %(col,row,row*col),
    print

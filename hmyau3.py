#!/usr/bin/python3
#-*- coding: utf-8 -*-

for row in range(1,10):
    for col in range(1,9):
        print ("{0:d}x{1:d}={2:2d}".format(col,row,row*col), end=" ")
    print ("{0:d}x{1:d}={2:2d}".format(9,row,row*9))


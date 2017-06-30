#!/usr/bin/python3
#-*- coding: utf-8 -*-

# constant definition
FORMULA_STR = "{0:d}x{1:d}={2:2d}"
MIN_NUM = 1
MAX_NUM = 9

for row in range(MIN_NUM,MAX_NUM+1):
    for col in range(MIN_NUM,MAX_NUM+1):
        if col != MAX_NUM: separator = ' '
        else: separator = '\n'
        print (FORMULA_STR.format(col,row,row*col), end=separator)


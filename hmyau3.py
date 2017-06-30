#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Python3 sample program to display 1x1 - 9x9 multiplier result
2017/Jun/30 Shinji Kato (github: ShinjiKatoA16)
'''

# constant definition
FORMULA_STR = "{0:d}x{1:d}={2:2d}"
MIN_NUM = 1
MAX_NUM = 9

for row in range(MIN_NUM,MAX_NUM+1):
    for col in range(MIN_NUM,MAX_NUM+1):
        if col != MAX_NUM: terminator = ' '
        else: terminator = '\n'
        print (FORMULA_STR.format(col,row,row*col), end=terminator)


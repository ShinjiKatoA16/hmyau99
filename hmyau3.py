#!/usr/bin/python3
# -*- coding: utf-8 -*-

# constant definition
MIN_NUM = 1
MAX_NUM = 9

for row in range(MIN_NUM,MAX_NUM+1):
    for col in range(MIN_NUM,MAX_NUM+1):
        result = row*col
        if result < 10:
            padding = ' '
        else:
            padding = ''

        if col != MAX_NUM: separator = ' '
        else: separator = '\n'

        print (col, 'x', row, '=', padding, result, sep='', end=separator)


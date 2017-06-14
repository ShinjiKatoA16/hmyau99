#!/usr/bin/python3
#-*- coding: utf-8 -*-

# constant definition
FORMULA_STR = "{0:d}x{1:d}={2:2d}"
MIN_NUM = 1
MAX_NUM = 9


# Variation-0: 1 extra trailing space
for row in range(MIN_NUM,MAX_NUM+1):
    for col in range(MIN_NUM,MAX_NUM+1):
        print(FORMULA_STR.format(col,row,row*col), end=" ")
    print()


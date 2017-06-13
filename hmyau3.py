#!/usr/bin/python3
#-*- coding: utf-8 -*-

output_str = "{0:d}x{1:d}={2:2d}"

for row in range(1,10):
    for col in range(1,9):
        print (output_str.format(col,row,row*col), end=" ")
    print (output_str.format(9,row,row*9))


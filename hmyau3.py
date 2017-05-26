#!/usr/bin/python3
#-*- coding: utf-8 -*-

for row in range(1,10):
    for col in range(1,10):
#       print (str(col)+"x"+str(row)+"="+str(row*col), end=" ")
#       print ("%dx%d=%2d" %(col,row,row*col), end=" ")
#       print (str(col)+"x"+str(row)+"="+"{0:2d}".format(row*col), end=" ")
        print ("{0:d}x{1:d}={2:2d}".format(col,row,row*col), end=" ")
    print()


#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    #print(sys.argv)
    #print(len(sys.argv))
    print(dir(sys.argv[1]))
else:
    print('Provide python module as argument - for example list')
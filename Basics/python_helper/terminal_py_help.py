#!/usr/bin/python3
import sys
import os
import pandas

if len(sys.argv) > 1:
    #print(sys.argv)
    #print(len(sys.argv))
    input('Press any key and Python help will appear. Press "q" to exit')
    print(help(eval(sys.argv[1])))
else:
    print('Provide python module and methon as argument - for example list.index')
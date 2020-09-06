#!/usr/bin/python3
import sys
import ast

desired_module = sys.argv 
print(desired_module)
if len(desired_module) > 1:
    #print(sys.argv)
    #print(len(sys.argv))
    
    print(desired_module[1])
    #NOTE: eval is needed to distinguish between string argument and real module
    #without eval always will make dir(str), because we receive 'int' as string!
    print(dir(eval(desired_module[1])))
else:
    print('Provide python module as argument - for example list')
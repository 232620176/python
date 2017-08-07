#-------------------------------------------------------------------------------
# Name:        函数模块
# Purpose:
#
# Author:      Hydra
#
# Created:     07/08/2017
# Copyright:   (c) Hydra 2017
# Licence:     <com.hydra>
#-------------------------------------------------------------------------------

def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


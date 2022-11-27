#!/usr/bin/python3 -x
#SPDX-FileCopyrightText: 2022 Haruki Matsukawa 
#SPDX-License-Identifier: BSD-3-Clause
import sys

def tonum(s):
    try:
        return int(s)
    except:
        return float(s)
        
ans = 0  
def product(a,b):
    ans = a * b
    return ans

x = product(3,4)

print(x)
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      moise
#
# Created:     13/02/2024
# Copyright:   (c) moise 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def primoA2(x):
    c = 0
    if x == 0 or x == 1:
        return false
    for i in range(2,x):
        if(x%i == 0):
            break
        else:
            c = 1

    if(c == 1):
        return true
    else:
        return false


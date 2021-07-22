#!/bin/python3

import math
import os
import random
import re
import sys

# problem name: throttling gateway

#
# Complete the 'droppedRequests' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY requestTime as parameter.
#

def droppedRequests(requestTime):
    # Write your code here
    drop = 0
    win10 = 0
    win60 = 0
    count = 1
    prev_time = requestTime[0]
    i = 1
    for i in range(1, len(requestTime)):
        curtime = requestTime[i]
        if curtime == prev_time:
            if count == 3:
                drop += 1
            elif i - win10 + 1  > 20:
                drop += 1
            elif i - win60 + 1  > 60:
                drop += 1
            else:
                count += 1
        else: 
            begin_win10 = max(1, curtime-9)
            while requestTime[win10] < begin_win10:
                win10 += 1
            while requestTime[win60] < max(1, curtime-59):
                win60 += 1

            if i - win10 + 1 > 20:
                drop += 1
            elif i - win60 + 1 > 60:
                drop += 1
            else:
                count = 1
            prev_time = curtime
    return drop

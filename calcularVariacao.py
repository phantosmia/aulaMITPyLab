from __future__ import division
import math
def stdDevOfLengths(L):
    n = len(L)
    if n == 0:
        return float('NaN')
    m = 0
    for x in L:
        m = m + len(x)
    finalM = m/n
    t = 0
    for x in L:
        minus = len(x) - finalM
        powElement = pow(minus,2)
        t = t + powElement
    division = t / n
    finalResult = math.sqrt(division)
    return finalResult

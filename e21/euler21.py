
# coding: utf-8

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

# In[57]:

def getProperDivisors(n):
    assert n > 1;
    pDivs = [1]
    for r in range (2, int(n/n**.5 + 1)):
        if n%r == 0:
            pDivs = (pDivs + [r, n/r]) if r != n/r else (pDivs + [r])
    
    pDivs.sort()
    return pDivs

def getSum(arr):
    return reduce(lambda x,y: x+y, arr)

def e20(n):
    parseThru = [False] + [True] * (n-1)
    amicables = []
    for i in range (1,len(parseThru)):
        val = i+1
        if parseThru[i]:
            divisorSum = getSum(getProperDivisors(val))
            if(divisorSum < n and divisorSum >1):
                checkAmicSum = getSum(getProperDivisors(divisorSum))
                if(val == checkAmicSum):
                    amicables = (amicables + [val,divisorSum]) if val != divisorSum else amicables
                    parseThru[divisorSum -1] = False
    return sum(amicables)
e20(10000)


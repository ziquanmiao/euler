
# coding: utf-8

# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

# In[8]:

def isEven(n):
    return n%2 == 0

def newValue(n):
    return n/2 if isEven(n) else 3*n+1

def numTerms(n):
    chainLen = 1
    old = n
    new = newValue(n)
    while new != 1:
        old = new
        new = newValue(new)
        chainLen +=1
    return chainLen + 1

def Euler14(upperLimit):
    maxHolder = 0
    index = 0
    for i in range(1,upperLimit):
        numT = numTerms(i)
        if numT > maxHolder:
            maxHolder = numT
            index = i
    return {"index":index, "numTerms":maxHolder}

Euler14(1000000)


# In[ ]:




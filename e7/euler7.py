
# coding: utf-8

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

# In[5]:

def Euler3(inputval):
    assert isinstance(inputval,int)
    
    Upper = inputval
    factors = []
    iterator = 0
    while iterator < Upper:
        iterator += 1
        if (Upper % iterator == 0):
            factors.append(iterator)
            Upper /= iterator
            iterator = 1
        elif (iterator == Upper):
            break
    factors.pop(0)
    return factors

Euler3(1)


# In[7]:

# get a list of all the primefactors for each number as we count up
# we know its a prime if that list is length 1
def Euler7(N):
    assert isinstance(N,int) or isinstance(N,float)
    
    countPrime = 0
    lastPrime = 0
    Iterator = 2
    while countPrime < N:
#         isprime
        
        if (len(Euler3(Iterator)) == 1):
            countPrime += 1
            lastPrime = Iterator
        
        Iterator += 1
    return lastPrime

Euler7(10001)


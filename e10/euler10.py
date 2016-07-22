
# coding: utf-8

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

# In[39]:

def Euler10(upper):
    possible = [True] * upper
    primes = []
    possible[0] = False
    count= 0
    for i in range(1,upper):
        if possible[i]:
            count += 1
            p = i+1
            primes.append(p)
            multiples = xrange(p+p-1, upper, p)
            for j in multiples:
                possible[j] = False
    sumPrimes = sum(i+1 for i in range(0,len(possible)) if possible[i])
    print count
    return sumPrimes
Euler10(2000000)


# Takeaway
# I need to be more mindful of indexing


# coding: utf-8

# The sum of the squares of the first ten natural numbers is,
# 
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# In[7]:

# add 2*x*y for every pair combination x!=y
#x,y in range (1,N+1)
def Euler6(N):
    tempSum = 0
    for i in range(1,N+1):
        for j in range (1,i):
            tempSum += 2*i*j
    return tempSum

Euler6(100)


# In[ ]:




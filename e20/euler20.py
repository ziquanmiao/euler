
# coding: utf-8

# n! means n × (n − 1) × ... × 3 × 2 × 1
# 
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!

# In[4]:

def Euler20(n):
    tempProd = 1
    for i in range(1,n+1):
        tempProd *= i
    tempStr = str(tempProd)
    
    tempSum = 0
    for val in tempStr:
        tempSum += int(val)
    return tempSum


# In[6]:

Euler20(100)


# In[ ]:




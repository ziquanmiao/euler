
# coding: utf-8

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?
# 

# In[5]:

base = 10
def Euler16(n):
    return reduce(lambda x,y: x+y, [int(i) for i in str(2**n)])
    
Euler16(1000)


# In[ ]:




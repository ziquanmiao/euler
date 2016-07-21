
# coding: utf-8

# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

# In[9]:

def Euler3(inputval):
    assert isinstance(inputval,long) or isinstance(inputval,int)
    
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
            

Euler3(600851475143)


# In[ ]:




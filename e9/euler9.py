
# coding: utf-8

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# In[2]:

4**2


# In[20]:

def getHypot(a,b):
    return (a**2 + b**2 )**.5
# a**2 + b**2 = c**2
# c = 1000 - a - b

# gives surface: 1000**2 - 2000(a+b) + 2ab = 0
# find all values a,b where b in 1,1000 and a in 1,b
# since c is by design > a,b
def Euler9():
    
    for b in range (1,1000):
        for a in range(1,b):
#             a<b by design
            if (1000000 - 2000 * (a + b) + 2*a*b == 0):
                parts = [a,b,int(getHypot(a,b))]
                return reduce(lambda x,y: x*y, parts)
                
                


# In[21]:

Euler9()


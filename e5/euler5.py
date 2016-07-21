
# coding: utf-8

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# In[13]:

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


# In[87]:

# use Euler 3 to as helper function to get raw prime factors of each value 
def Euler5(number):
    participants = {}
#     for each number in 1-20
    for i in reversed(range(1,number+1)):
        candidates = Euler3(i)
        for Val in set(candidates):
            tempFrequency = candidates.count(Val)
            if Val not in participants:
                participants[Val] = tempFrequency
            else:
                if participants[Val] < tempFrequency:
                    participants[Val] = tempFrequency
                    
    rawFactors = []
    for ele in participants:
        rawFactors += [ele]*participants[ele]
    return reduce(lambda x,y: x*y, rawFactors)

Euler5(20)


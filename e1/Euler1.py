
# coding: utf-8

# 1.
# we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.
# 
# 

# In[11]:

def Euler1(multipleTokens,under):
#     multiple TOkens is the array [3,5]
#     under represents 1000
    assert isinstance(under,int)
# done is the array that keeps track of all the multiples
    done = []
    for ele in multipleTokens:
        assert isinstance(ele, int)
        cap = 1
        temp = 0
        while temp < under:
            temp = cap*ele
            if (temp not in done and temp < under):
                done.append(temp)
            cap += 1
    return sum(done)
Euler1([3,5],1000)


# In[ ]:




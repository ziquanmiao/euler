
# coding: utf-8

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# 
#     See file

# In[13]:

def Euler13():
    with open('data.txt','r') as f:
        data = f.readlines()
        data = "".join(data)
        data = data.split("\n")
        data = [int(ele) for ele in data]
        tempSum = reduce(lambda x,y: x+y,data)
        string = str(tempSum)
        print string[0:10]

Euler13()


# In[ ]:




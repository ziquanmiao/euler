
# coding: utf-8

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# 
# 
# How many such routes are there through a 20×20 grid?

# In[19]:

# wrote  ahelper function
# takes a coordinate given by the obj input
# increments for the two directions (left and right) that it can go and
# selfreferences the number in hashRefernce so we do not get a memory overload
hashReference = {}
def helper(obj):
#     obj is an tuple array [down,right]
    if (obj[0] == 0 and obj[1] == 0):
        return 1
    
    if obj[0] == 0:
        return helper([0,obj[1]-1])
    elif obj[1] == 0:
        return helper([obj[0]-1,0])
    else:
        tentLeft = [obj[0]-1,obj[1]]
        tentRight = [obj[0],obj[1]-1]
        left = None
        right = None
        if str(tentLeft) in hashReference:
            left = hashReference[str(tentLeft)]
        else:
            left = helper(tentLeft)
            hashReference[str(tentLeft)] = left
        if str(tentRight) in hashReference:
            right = hashReference[str(tentRight)]
        else:
            right = helper(tentRight)
            hashReference[str(tentRight)] = right
        return left + right
    
def Euler15(n):
#     nxn matrix
# you can only go down or right
    hashReference = {}
    return helper([n,n])

Euler15(20)


# Original Code below
# 
# This ended up taking too much memory

# In[13]:

def helper(obj):
#     obj is an tuple array [down,right]
    if (obj[0] == 0 and obj[1] == 0):
        return 1
    
    elif obj[0] == 0:
        return helper([0,obj[1]-1])
    elif obj[1] == 0:
        return helper([obj[0]-1,0])
    else:
        left = [obj[0]-1,obj[1]]
        right = [obj[0],obj[1]-1]
        return helper(left) + helper(right)
def Euler15(n):
    return helper([n,n])

Euler15(2)


# In[ ]:




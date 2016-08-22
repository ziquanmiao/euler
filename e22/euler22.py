
# coding: utf-8

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?

# In[12]:

import string

def getNameWorth(name):
    return sum(map(lambda x: string.uppercase.index(x) + 1, name))

with open('names.txt','r') as f:
    text = f.readline().replace('"','')
    text = text.split(",")
    text.sort()
    values = map(lambda x,y: getNameWorth(x)*y, text,range(1,len(text)+1))
    
    print sum(values)


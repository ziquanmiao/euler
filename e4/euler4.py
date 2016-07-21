
# coding: utf-8

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

# In[6]:

#     Define helper function to determine if a number is palindromic
def isPalindromic(num):
    string = num
    if (isinstance(num,int)):
        string = str(num)
    
    for i in range (0,len(string)/2 +1):
        if (string[i-1] != string[-1*i]):
            return False
    return True

# parse through the possible space and collect all the palindroms
def Euler4():
    maxx = []
    for i in range (900,1000):
        for j in range(900,1000):
            tempProduct = i*j
            if (isPalindromic(tempProduct)):
                maxx.append(tempProduct)
    return max(maxx)

Euler4()


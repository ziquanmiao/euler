
# coding: utf-8
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
# In[26]:

# misunderstood the question and wrote a search algorithm
# with open('18data.txt','r') as f:
#     localMaxes = [map(lambda x: int(x),(rawLine.strip().split(" "))) for rawLine in f.readlines() ]
#     tempSum = localMaxes[0][0]
#     index = 1
#     inlineIndex = 0
#     while index < len(localMaxes):
#         leftVal = localMaxes[index][inlineIndex]
#         rightVal = localMaxes[index][inlineIndex+1]
#         if leftVal > rightVal:
#             tempSum += leftVal
#             print leftVal
#         else:
# #             right > left
#             tempSum += rightVal
#             inlineIndex += 1
#             print rightVal
#         index += 1
        
#     print tempSum
            


# In[40]:

# very good question. But our algorithm will solve the question from the bottom up
def helper(top,bottom):
    for ind,val in enumerate(top):
        if bottom[ind] > bottom[ind+1]:
            top[ind] += bottom[ind]
        else:
            top[ind] += bottom[ind+1]
    return top

with open('18data.txt','r') as f:
    data = [map(lambda x: int(x), rawline.strip().split()) for rawline in f.readlines()[::-1]]
    print data
    last = data[0]
    for nums in data[1:]:
        last = helper(nums,last)
    print last


# In[ ]:




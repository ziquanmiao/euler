
# coding: utf-8

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# 
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# In[38]:

singles = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
tens = {
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}
def toEnglish(n):
    string = str(n)
    length = len(string)
    assert length < 5
    output = ""
    if length == 4:
        if (int(string[1:4]) > 0):
    #         add thousands
            output += singles[int(string[0])] + " thousand "
            if (int(string[2:4]) > 0):
        #     add hundreds
                output += singles[int(string[1])] + " hundred and "
        #     add tens
                if (int(string[2:4]) < 20):
                    output += singles[int(string[2:4])]
                else:
                    output += tens[int(string[2]) * 10]
                    output += singles[int(string[3])]
            else:
                output += singles[int(string[1])] + " hundred"
        else:
            output += singles[int(string[0])] + " thousand"
#  add ones
        
    elif length == 3:
        if (int(string[1:3]) > 0):
            output += singles[int(string[0])] + " hundred and "
            if (int(string[1:3])<20):
    #             add < 20s
                output += singles[int(string[1:3])]
            else:
    #             add tens
                output += tens[int(string[1]) * 10]
    #     add ones
                output += singles[int(string[2])]
        else:
            output += singles[int(string[0])] + " hundred"

    elif length == 2:
        if (n < 20):
            #  add ones
            output += singles[n]
        else:
            output += tens[int(string[0]) * 10]
            #  add ones
            output += singles[int(string[1])]
    else:
        #  add ones
        output += singles[n]
    return output

def getLength(IN):
    noWhiteSpace = IN.replace(" ","")
    return len(noWhiteSpace)
def euler17():
    
    lengths = [getLength(toEnglish(i)) for i in range(1,1001)]
    return reduce(lambda x,y: x+y, lengths)
  
euler17()


# In[ ]:




'''Retrieve only phone numbers from a file'''
p_nums='''
040-1231
044---5645
022-2135
033-2122
033*5321
044.5423
'''

import re
patter = re.compile(r"\d\d\d[-]\d\d\d") #only 3 nums,then -,then 4 nums.Doesnt match 4nums -- 4nums

patter = re.compile(r"\d\d\d[-.]\d\d\d") #only 3 nums,then - or .,then 4 nums


#what if the pattern is 30 characters long?Will you go on using \d\d..?
#ans:No,we will use quantifier - checks for more than one character specified using {number_count}

patter = re.compile(r"\d{3}[-.]\d{4}") #Exact match for 3 \d and 4 \d in the end

matches = patter.finditer(p_nums)
for m in matches:
    print(m)
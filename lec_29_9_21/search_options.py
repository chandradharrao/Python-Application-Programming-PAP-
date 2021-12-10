#input with multipe lines - MULTILINE OR DOTALL

#multiline - ^ and $ rules work for each line in addition to start and end of string respectively

import re
from sys import version
txt="UPSC Exams.\nKCET Exams"
pattern=r'(^\w+)|(\w+\S*$)'
single_line = re.compile(pattern)
multi_line = re.compile(pattern,re.MULTILINE) #^  will apply for every line along with start of string

for m in single_line.findall(txt):
    print(m)

for m in multi_line.findall(txt):
    print(m)    

'''
. -> matches everything except new line character
'''
#py3 uses unicode by default,hence no need to use that flag anywere

pattern=r'.+'
single_line = re.compile(pattern,re.DOTALL) #new lines are also matched
for m in single_line.findall(txt):
    print(m)

#verbose - divide the pattern and comment out each divide groups
pattern=re.compile(
    '''
    [\w\d.+-]+ #one or more amnt of digits,chars and spl chars
    ([\w\d,]+\.) #domain name prefix
    (com|org|edu) #top level domain
    ''',
    re.VERBOSE|re.IGNORECASE
)

'''
Flags abbrevations:
IGNORE CASE i
MULTILINE m
DOTALL s
UNICODE u
VERBOSE x
'''

#embedding flags - if we dont want to pass the flags during the re.compile function,then we can pass it directly to the string pattern itself
txt="String Safari storem tata\nSugar yes Please"
toMatch = r'(?mi)\bS\w+'
pattern = re.compile(toMatch)
print(pattern.findall(txt))

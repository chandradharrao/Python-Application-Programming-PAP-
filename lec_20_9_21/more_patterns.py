import re

t='''
123
ABCD
abcd
#$%#@
man
can
ran
'''

#range of numbers or letters
patter = re.compile(r'[1-5]')
patter = re.compile(r'[a-zA-z]')

# ^ - negate if used within character set
patter=re.compile(r'[^r]an') #doesnt begin with r but has -'an' - rhyming


ms = patter.finditer(t)
for m in ms:
    print(m)
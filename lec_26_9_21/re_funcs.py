'''
re.search
->doesnt give an iterable
->returns first match
->re.Match type object
'''
import re

txt='''i watch ipl 
i play in ipl
i am ipl
what is ipl
'''
pattern='ipl'
m = re.search(pattern,txt) #not an iterable
print(m)

'''
re.findAll -> returns all(multiple) matches
->this is an plane array without giving a re object unlike re.finditer or re.search
->dosnt give index
'''
ms = re.findall(pattern,txt)
for m in ms:
    print(m)
    
pattern=re.compile(r"ipl")
ms = pattern.finditer(txt)
for m in ms:
    print(txt[m.start():m.end()])

'''
re.match return a re.match object only if the pattern is in the exact begenning of the text only,else it will return none
'''
pattern=re.compile(r"i")
m = re.match(pattern,txt)
print(m)
#search options - allow us to put condition with re search
import re

text='This is scam text'

#try to match text and this only
toMatch = r'\bT\w+'
pattern = re.compile(toMatch)
matches = pattern.findall(text) #case sentive

#case insensitive
pattern = re.compile(toMatch,re.IGNORECASE)
matches = pattern.findall(text)

for m in matches: print(m)
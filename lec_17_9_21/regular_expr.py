# '''
# Regular Expression
# spl seq of characters to match set of strings in a text
# '''
# #raw string is used to prevent treatment of \t as spl escape seq
print(r'\tTab')

#re - regular expression
import re

sentence='''abcdefgh
ABCDEF
123
@#$%
abc
.'''
#re.compile converts pattern we want to search for to a variable so that it can be used later - important for exam
pattern = re.compile('abc')

#finditer - iterate through text and search for ALL matching pattern 
matches =pattern.finditer(sentence)
for match in matches:
    print(f"Found {sentence[match.span()[0]:match.span()[-1]]} @ {match.span()}") #span returns(startIndx,endIndx+1)

print(sentence[0:3]) #(startIndx,endIndx+1)

pattern=re.compile(r".")
matches=pattern.finditer(sentence)
for m in matches:
    print(m.span()) #match for every charavter except new line

#hence "." is a spl character that matches every character except new line

def printer(matches):
    print("------")
    for m in matches:
        print(m)
    print("------")

#if we want to match a . too,then
p = re.compile(r"\.")
printer(p.finditer(sentence))


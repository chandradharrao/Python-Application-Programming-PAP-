import re

'''
\d - matches digits b/w 0 to 9
\D - macthes !a digit
\w - word char match(a-z,A-Z,0-9 or _)
\W - !\w (ie spl characters and \n)

\bword_to_match - word boundary - words end with \n or space only.

\Bword_to_match - not a word boundary - selects all words that match word_to_match iff they are not seperated by \n or space ie not a word boundary

^word_to_match - match sentence if begenning of a string begins with word_to_match

$word_to_match -match string if end of string is word_to_match

\s - match whitespaces like space,\n
\S - not a white space
'''
sentence1='''
abc
cric criccric crickcric
cic
ABC
09 09909 91091
'''
def printer(matches):
    print("------")
    for m in matches:
        print(m)
    print("------")
p=re.compile(r'\bcric') #3 matches since only 3crics are seperated by \n or space
printer(p.finditer(sentence1))

p=re.compile(r'\Bcric')
printer(p.finditer(sentence1)) #prints the two cric inner words not seperated by word boundaries

sentence2="start end the PAP class"
p=re.compile(r"^start")
printer(p.finditer(sentence2)) #match sentence as the sentence begins with start

p=re.compile(r"class$")
printer(p.finditer(sentence2)) #match sentence as the sentence ends with class

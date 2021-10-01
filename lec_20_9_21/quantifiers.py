import re

'''
Quantifiers:    
    match multiple characters at a time
    * - 0 or more
    + - 1 or more
    ? - 0 or one 
    {m,n} - range of number between m and n
    '''

names='''
Mr. Saket
Mr Adithya
Mr. Likith
Mrs. Devi
Ms. Kareena
Mr Archit Raj
Mrs Reena
Mr. V
Ms. Mahima
'''

'''
match Mr and Mr.
Match white space
Match Remaining entire first name 
'''
pattern = re.compile(r"Mr\.?\s[A-Z]\w*")

'''
match Mr,Mr.,Mrs.,Ms.
match white space
match entire first name
'''
pattern = re.compile(r"M[rs]s?\.?\s[A-Z]\w*")

'''
Groups allow us to match sever diff patterns
starts with (multiple_params)
'''
pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*')

emails='''
ramadevi@gmail.com
chandradhar.rao@gmail.com
mi-123-prasad.sundar@gmail.com
mahima.12.123@my-space.net
aditya.sundar@hotmail.com
'''
#[a-zA-Z]+ => one or more characters of this
#[a-zA-Z0-9.-]+ => a to z,A to Z,0 to 9,. and + one or more
toMatch = r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)'
pattern = re.compile(toMatch)

urls='''
https://www.google.com
http://pes.edu
https://www.irctc.co.in
http://mahima.com
http://guru-99.in
'''
toMatch = r'http[s]?://[a-zA-Z0-9.-]+\.[a-zA-z]+'
pattern = re.compile(toMatch)

matches = pattern.finditer(urls)
for m in matches:
    print(m.group(0)) #print the groups present : here only one group since we havent used any groups
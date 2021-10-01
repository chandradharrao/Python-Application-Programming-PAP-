import re

pattern = re.compile(r"\d{3}[*.]\d{5}")

#phone nums that start with 8 or 9
pattern=re.compile(r"[89]\d{9}")

with open("phone.txt","r") as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for m in matches:
        print(m)
    f.close()


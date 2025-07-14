import re
p = re.compile('[a-z]+')
m = p.search('3 python')
if m:
    print('Match found: ', m.group())
else:
    print("No match")

n = re.match('[a-z]+', 'Abc',re.I)
if n:
    print(n.group())
else:
    print("No match")

p = re.compile("^python\s\w+")
data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
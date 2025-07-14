import re
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m.group())

p = re.compile(r"(\w+)\s+(\d+)[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group())
print(m.group(1))
print(m.group(2))
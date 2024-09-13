import re
s = input()
out = re.sub(r'[^\w\s]',' ',s)
print(out)
import re
a="This 22 yesvanthra"
b=re.search(r"(.+) +(\d\d)",a)
print(b.group(2))

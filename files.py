import re

with open('file.txt','r') as fp:
    lines = fp.readlines()

#fp = open('file.txt','r')
#lines = fp.readlines()
for f in lines:
    a = re.match(r'[a-zA-Z0-9-_]+@[a-z]+\.(com)',f)
    if a:
        print(a.group())
    
fp.close()




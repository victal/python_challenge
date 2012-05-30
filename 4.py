#!/usr/bin/env python
import re

text_4 = open('4.txt')

lines_4 = [i for i in text_4.readlines()]

ans = []
for i in lines_4:
    s = ''.join(re.split('[A-Z]{4,}',i))
    print(s)
    ans.append(re.findall('[A-Z]{3}[a-z][A-Z]{3}',s))


print(''.join(re.split('[A-Z]+',''.join([''.join(i) for i in ans]))))

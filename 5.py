#!/usr/bin/env python
import urllib.request,re
#16044
#82682
#nothing = '12345'
nothing = '16044'
i = 0
spam = True
while spam:

    f = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nothing)
    s = f.read().decode()
    nothing = s.split(' ')[-1]
    if nothing.endswith('html'):
        print(nothing)
        spam = False
    i+=1

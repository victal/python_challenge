#!/usr/bin/env python2
import urllib,re
#16044
#82682
#nothing = '12345'
nothing = '16044'
i = 0
spam = True
while spam:

    f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nothing)
    s = f.read()
    nothing = s.split(' ')[-1]
    if nothing.endswith('html'):
        print(nothing)
        spam = False
    i+=1

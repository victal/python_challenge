#!/usr/bin/env python2
import pickle
import urllib

#http://www.pythonchallenge.com/pc/def/channel.zip
a = pickle.load(urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
print(zip(a))

for i in a:
    print(''.join([char*(int(num)) for char,num in i]))

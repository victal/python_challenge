#!/usr/bin/env python2
import pickle
import urllib

a = pickle.load(urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

for i in a:
    print(''.join([char*(int(num)) for char,num in i]))

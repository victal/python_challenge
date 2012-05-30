#!/usr/bin/env python2
import zipfile
import urllib.request
import io

#http://www.pythonchallenge.com/pc/def/channel.zip
zip_file = zipfile.ZipFile("channel.zip")
readme = io.TextIOWrapper(zip_file.open('readme.txt','r'))
nothing = 0
for i in readme.readlines():
   print(i.strip())
   if i.find('start') != -1:
       nothing = i.split(" ")[-1].strip()

comments = []
run = True
while run:
    comments.append(zip_file.getinfo(nothing+'.txt'))
    text_file = io.TextIOWrapper(zip_file.open(nothing+'.txt','r'))
    s = text_file.read()
    if s.find('nothing') != -1:
       nothing = s.split(" ")[-1].strip()
    else:
        print(s)
        run = False

comments
print(''.join([c.comment.decode() for c in comments]))

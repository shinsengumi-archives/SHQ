import sys
import os
from os.path import isdir
import json

charsets = ['windows-1252', 'iso-8859-1', 'shift_jis']

enc = 'euc_jp'
"""
_encoding = 'ISO-8859-1'
t = "���������@���������������������������������A�i���j|&quot;����������B������������".encode(_encoding, 'ignore').decode("utf-8", 'ignore')
print(t)
"""

"""
t = b'\xc2\xa2 \xc2\xa2\xc3\xa2 \xc2\xa2\xc3\xa8 \xc2\xb5\xc3\xbb \xc2\xa2\xc3\x85 \xc2\xa2\xc2\xb5 \xc2\xa2\xc3\x84 \xc2\xa2\xc3\x8b \xc2\xa1A\xe2\x82\xac\xc2\xa0\xc2\xa0 \xc2\xa1i\xe2\x82\xac\xc2\xa0\xc2\xa0 \xc2\xb7\xc2\xaa \xc2\xa1j | \xe2\x82\xac\xc2\xa0\xc2\xa0 \xc2\xa1 \xc2\xa2\xc3\xb0 \xc2\xae \xc2\xbd \xc2\xa2\xc3\x81 \xc2\xa2\xc3\x84 \xc2\xa9B\xe2\x82\xac\xc2\xa0\xc2\xa0 \xc2\xa2\xc3\xaa \xe2\x82\xac\xc2\xa0\xc2\xa0 \xc2\xa2\xc3\x84 \xc2\xa2\xc2\xa2 \xc2\xa2\xc3\xa9 \xc2\xa2\xc3\x8c \xc2\xa2\xc3\x85'
print(t.decode('utf8', 'ignore'))
"""

"""
s=u'汉语 / 漢語'
#print(s.encode('utf8').decode('mbcs'))
t = s.encode('utf8').decode('utf8').encode('utf8')
print(t)
print(t.decode('utf8').encode('utf8').decode('utf8'))
"""

enc = 'iso-8859-1'
fh = open('1826.json', "r", encoding=enc)
f = fh.read()
fh.close()
out = open('test.json', "w", encoding='shift_jis')	
out.write(f.encode(enc).decode('shift_jis', 'ignore'))
out.close()


"""
print(len(f))
t = []
for c in f:
    t.append(int(c))
#print(f)
#print(t)

enc = 'iso-8859-1'
out = open('test.json', "w", encoding=enc)	
out.write(f.decode(enc, 'ignore'))
out.close()
"""

"""
s = u'父の教育法はち'
print(s.encode('utf8').decode('utf8').encode('utf8'))

t = b'\xe7\x88\xb6\xe3\x81\xae\xe6\x95\x99\xe8\x82\xb2\xe6\xb3\x95\xe3\x81\xaf\xe3\x81\xa1\xe3\x82\x87\xe3\x81\xa3\xe3\x81\xa8\xe9\xa1\x9e\xe3\x81\xae\xe3\x81\xaa\xe3\x81\x84\xe3\x82\x84\xe3\x82\x8a\xe6\x96\xb9\xe3\x81\xa7\xe3\x81\x97\xe3\x81\xa6\xe3\x81\xad\xe3\x80\x81\xef\xbc\x88\xe7\x95\xa5\xef\xbc\x89'

t = b'\x95\xc2\x83\xc2\x82\xc3\x8c\xc2\x8b\xc2\xb3\xc2\x88\xc3\xa7\xc2\x96@\xc2\x82\xc3\x8d\xc2\x82\xc2\xbf\xc2\x82\xc3\xa5\xc2\x82\xc3\x81\xc2\x82\xc3\x86\xc2\x97\xc3\x9e\xc2\x82\xc3\x8c\xc2\x82\xc3\x88\xc2\x82\xc2\xa2\xc2\x82\xc3\xa2\xc2\x82\xc3\xa8\xc2\x95\xc3\xbb\xc2\x82\xc3\x85\xc2\x82\xc2\xb5\xc2\x82\xc3\x84\xc2\x82\xc3\x8b\xc2\x81A\xc2\x81i\xc2\x97\xc2\xaa\xc2\x81j'

t = b'\xc2\x80\xc2\xa0\xc2\xa0'

s = u'  µ£¢Ì«³¨ç¶@  ¢Í¢¿¢å¢Á¢Æ·Þ¢Ì¢È¢'
print(s.encode('iso-8859-1', 'ignore').decode("utf-8", 'ignore'))

#print(t.decode('iso-8859-1'))
"""

"""
t =  b'\xc2\xa2\xc2\xa2\xc3\xa2\xc2\xa2\xc3\xa8\xc2\xb5\xc3\xbb\xc2\xa2\xc3\x85\xc2\xa2\xc2\xb5\xc2\xa2\xc3\x84\xc2\xa2\xc3\x8b\xc2\xa1A\xe2\x82\xac\xc2\xa0\xc2\xa0\xc2\xa1i\xe2\x82\xac\xc2\xa0\xc2\xa0\xc2\xb7\xc2\xaa\xc2\xa1j|\xe2\x82\xac\xc2\xa0\xc2\xa0\xc2\xa1\xc2\xa2\xc3\xb0\xc2\xae\xc2\xbd\xc2\xa2\xc3\x81\xc2\xa2\xc3\x84\xc2\xa9B\xe2\x82\xac\xc2\xa0\xc2\xa0\xc2\xa2\xc3\xaa\xe2\x82\xac\xc2\xa0\xc2\xa0\xc2\xa2\xc3\x84\xc2\xa2\xc2\xa2\xc2\xa2\xc3\xa9\xc2\xa2\xc3\x8c\xc2\xa2\xc3\x85'

#t = b'\xe6\xb1\x89\xe8\xaf\xad / \xe6\xbc\xa2\xe8\xaa\x9e'
#print(t.decode('utf8').encode('utf8').decode('utf8'))

out = open('test.json', "w+", encoding='iso-8859-1')	
out.write(t.decode('iso-8859-1'))
out.close()
"""


"""
s = "'æˆ´æ£®ç¾Žå�‘é€\xa0åž‹å™¨å®Œæ•´ç‰ˆå¥—è£…Dyson Airwrap HS01ï¼ˆé“œé‡‘è‰²ç¤¼ç›’ç‰ˆï¼‰'"
s = "µû"

out = open('test.json', "w+", encoding='utf-8')	
out.write(s.encode('iso-8859-1', 'ignore').decode("utf-8", 'ignore'))
out.close()


"""
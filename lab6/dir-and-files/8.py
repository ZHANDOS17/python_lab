import os

f = 'testpp2.docx'

loc = '/Users/zandosmirbaj/Desktop' #сюда пишете локацию

p = os.path.join(loc, f)
if not os.path.exist(p):
    exit()
os.remove(p)

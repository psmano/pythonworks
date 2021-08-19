# Opening Files & Folders

f = open('practice.txt','w+')
f.write('This is a test string')
f.close()

import os

print(os.getcwd())
print(os.listdir('C:\\Users'))
print(os.listdir('C:\\Users\\PMANOHAR'))

import shutil

shutil.move('practice.txt','C:\\Users\PMANOHAR')

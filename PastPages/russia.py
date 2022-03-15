import re
import sys
f1 = open("itemlist.txt","r")
for line in f1:
    if (re.search(r'russia-today',line)):
        print(line,end='')



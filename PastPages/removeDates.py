import re
import sys

f1 = open("itemlist.txt","r")
sys.stdout = open("nodates.txt", "w")
for line in f1:
    if not(re.search(r'-\d\d\d\d-\d\d$',line)):
        print(line,end='')
    
    
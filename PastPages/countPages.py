import re
import sys

f1 = open("itemlist.txt","r")
l = set()
sys.stdout = open("countS.txt", "w")
for line in f1:
   m = re.search('[a-zA-Z-]*',line)
   l.add(m.group())

l2 = sorted(l)
for line in l2:
    print(line)
    
    
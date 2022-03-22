import re
import sys

f1 = open("itemlist.txt","r")
l = {}
sys.stdout = open("countS.txt", "w")
for line in f1:
   m = re.search('[a-zA-Z-]*',line)
   l[m.group()] = l.get(m.group(),0)+1

for i in l:
    
    print(i + " "+str(l.get(i)))
    
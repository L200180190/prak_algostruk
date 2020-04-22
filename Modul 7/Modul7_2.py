#Nomer 2

import re
f=open('IndonesiaWiki.txt','r')
baca = f.read()
f.close()
word = r"di\w+"
diPasif = re.findall(word,baca)
print(diPasif)

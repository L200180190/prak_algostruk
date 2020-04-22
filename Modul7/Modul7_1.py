#Nomer 1

import re
f=open('IndonesiaWiki.txt','r')
baca = f.read()
f.close()
a=r'me\w+'
kata = re.findall(a,baca)
print(kata)

#Nomer 4a

import re
print("Nomer 4 a menampilkan nama-nama Negara")
f=open('KEI.html','r', encoding='latin1')
teks = f.read()
f.close()
namaNegara=r'([\w+]+)</a></td>'
kata=re.findall(namaNegara,teks)
print(kata)


#Nomer 4b

print("Nomer 4 b menampilkan nama-nama Negara beserta Innovation Index nya")
f=open('KEI.html','r', encoding='latin1')
a = f.read()
f.close()
Negara = r'title="([\w+]+)">'
Index = r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>'
hasil = re.findall(Negara,a)
hasil = re.findall(Index,a)
p=[]
for x in hasil:
    p.append((x[0], float(x[1])))
print(p)

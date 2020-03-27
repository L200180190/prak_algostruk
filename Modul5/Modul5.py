#Kode untuk Soal Nomer 1 dan Nomer 2
class Manusia(object):
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n * 2

class Mahasiswa(Manusia):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + ', dan memiliki uang saku ' + selfuangSaku + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "Sambil belajar.")
        self.keadaan = 'kenyang'

class MhsTIF(Mahasiswa):
    def kataKanPy(self):
        print('Python is cool.')

a1=Mahasiswa("Anna",190,"Ngawi",250000)
a2=Mahasiswa("Noer",207,"Surakarta",550000)
a3=Mahasiswa("Kinan",167,"Ngawi",50000)
a4=Mahasiswa("Nafiza",104,"Jakarta",100000)
a5=Mahasiswa("Sari",132,"Jakarta",750000)
a6=Mahasiswa("Andri",209,"Sragen",650000)
a7=Mahasiswa("Fahrur",134,"Ngawi",8250000)
a8=Mahasiswa("Sia",202,"Salatiga",400000)
a9=Mahasiswa("Arif",213,"Ngawi",480000)
a10=Mahasiswa("Supri",160,"Sragen",950000)
a11=Mahasiswa("Erwan",215,"Salatiga",365000)

def urutkan(p):
    for i in range (len(p)-1, 0, -1):
        for k in range (i):
            if p[k] > p[k+1]:
                c = p[k]
                p[k] = p[k+1]
                p[k+1] = c

#Nomer 1
Daftar = [a1.NIM,a2.NIM,a3.NIM,a4.NIM,a5.NIM,a6.NIM,a7.NIM,a8.NIM,a9.NIM,a10.NIM,a11.NIM]

urutkan(Daftar)
print(Daftar)

#Nomer 2
A = [8,12,15,22,29,31,35]
B = [3,4,9,10,19,20,21,24]
C = A+B
urutkan(C)
print(C)

#Nomer 3
from time import time as detak
from random import shuffle as kocok

def BubbleSort(a):
    r = len(a)
    for x in range (r-1):
        for y in range (r-x-1):
            if a[y] > a[y+x]:
                tukar (a, y, y+1)

def SelectionSort(a):
    r = len(a)
    for x in range (r-1):
        indexKecil = mencariTerkecil(a, x, r)
        if indexKecil != x :
            tukar (a, x, indexKecil)

def InsertionSort(a):
    r = len(a)
    for x in range (1, r):
        n = a[x]
        pqr = x
        while pqr > 0 and n < a[pqr-1]:
            a[pqr] = a[pqr-1]
            pqr = pqr-1
        a[pqr] = n

def tukar (a, p, q):
    xyz = a[p]
    a[p] = a[q]
    a[q] = xyz

def mencariTerkecil(a, awal, nStop):
    terkecil = awal
    for x in range (awal+1, nStop):
        if a[x] < a[terkecil]:
            terkecil = x
    return terkecil

k = []
for x in range (1, 6001):
    k.append(x)

kocok(k)

u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak(); BubbleSort(u_bub); ak = detak(); print("Bubble : %g detik" %(ak-aw));
aw = detak(); SelectionSort(u_sel); ak = detak(); print("Selection : %g detik" %(ak-aw));
aw = detak(); InsertionSort(u_ins); ak = detak(); print("Insertion : %g detik" %(ak-aw));
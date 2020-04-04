#Nomer 6

class MhsTIF():
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.us = us

    def __str__(self):
        s = self.nama + ', NIM ' + str(self.nim) \
            + '. Tinggal di ' + self.kota \
            + '. Uang saku Rp. ' + str(self.us) \
            + ' tiap bulannya.'
        return s

    def ambilNama(self):
        return self.nama

    def ambilNim(self):
        return self.nim

    def ambilUangSaku(self):
        return self.us

a1=MhsTIF("Anna",190,"Ngawi",250000)
a2=MhsTIF("Noer",207,"Surakarta",550000)
a3=MhsTIF("Kinan",167,"Ngawi",50000)
a4=MhsTIF("Nafiza",104,"Jakarta",100000)
a5=MhsTIF("Sari",132,"Jakarta",750000)
a6=MhsTIF("Andri",209,"Sragen",650000)
a7=MhsTIF("Fahrur",134,"Ngawi",8250000)
a8=MhsTIF("Sia",202,"Salatiga",400000)
a9=MhsTIF("Arif",213,"Ngawi",480000)
a10=MhsTIF("Supri",160,"Sragen",950000)
a11=MhsTIF("Erwan",215,"Salatiga",365000)

Daftar = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]
A = []

for i in Daftar:
    A.append(i.nama)

def cetak():
    for i in A:
        print(i)

def quickSort(arr):
    kurang = []
    pivotList = []
    lebih = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                kurang.append(i)
            elif i > pivot:
                lebih.append(i)
            else:
                pivotList.append(i)
        kurang = quickSort(kurang)
        lebih = quickSort(lebih)
        return kurang + pivotList + lebih

print("Sebelum diurutkan")
cetak()
print("\nSetelah diurutkan")
quickSort(A)
cetak()

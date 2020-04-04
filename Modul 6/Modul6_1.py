#Nomer 1
#Merge Sort

class MhsTIF():
    def __init__(self, nim):
        self.nim = nim

    def __str__(self):
        return str(self.nim)
    
a0 = MhsTIF(13)
a1 = MhsTIF(4)
a2 = MhsTIF(6)
a3 = MhsTIF(7)
a4 = MhsTIF(24)
a5 = MhsTIF(15)
a6 = MhsTIF(29)
a7 = MhsTIF(23)
a8 = MhsTIF(11)
a9 = MhsTIF(1)
a10 = MhsTIF(3)

a0.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
a6.next = a7
a7.next = a8
a8.next = a9
a9.next = a10

def mergeSort(A):
    print("Membelah      ",A)
    if len(A) > 1:
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]
        mergeSort(separuhkiri)
        mergeSort(separuhkanan)
        i = 0;
        j = 0;
        k = 0
        while i < len(separuhkiri) and j < len(separuhkanan):
            if separuhkiri[i] < separuhkanan[j]:
                A[k] = separuhkiri[i]
                i = i + 1
            else:
                A[k] = separuhkanan[j]
                j = j + 1
            k = k + 1
        while i < len(separuhkiri):
            A[k] = separuhkiri[i]
            i = i + 1
            k = k + 1
        while j < len(separuhkanan):
            A[k] = separuhkanan[j]
            j = j + 1
            k = k + 1

def convert(arr, obj):
    hasil = []
    for x in range(len(arr)):
        for i in range(len(arr)):
            if arr[x] == obj[i].nim:
                hasil.append(obj[i])
    return hasil

Daftar = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
A = []

for x in Daftar:
    A.append(x.nim)

print("MERGE SORT")
mergeSort(A)
for x in convert(A, Daftar):
    print(x.nim)

#Quick Sort
def partisi(A, awal, akhir):
    nilaipivot = A[awal]
    penandakiri = awal + 1
    penandakanan = akhir
    selesai = False
    while not selesai:
        while penandakiri <= penandakanan and A[penandakiri] <= nilaipivot:
            penandakiri = penandakiri + 1
        while penandakanan >= penandakiri and A[penandakanan] >= nilaipivot:
            penandakanan = penandakanan - 1
        if penandakanan < penandakiri:
            selesai = True
        else:
            temp = A[penandakiri]
            A[penandakiri] = A[penandakanan]
            A[penandakanan] = temp
    temp = A[awal]
    A[awal] = A[penandakanan]
    A[penandakanan] = temp
    return penandakanan

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)

Daftar = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
A = []

def convert(arr, obj):
    hasil = []
    for x in range(len(arr)):
        for i in range(len(arr)):
            if arr[x] == obj[i].nim:
                hasil.append(obj[i])
    return hasil

for x in Daftar:
    A.append(x.nim)

print("QUICK SORT")
quickSort(A)
for x in convert(A, Daftar):
    print(x.nim)

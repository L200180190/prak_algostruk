from math import sqrt as sq
from random import randint

#No. 1.
def cetakSiku(x):
    a = 0
    while (a <= x):
        print(a * ('*'))
        a = a + 1
cetakSiku(5)

#No. 2.
def gambarlahPersegiEmpat(x, y):
    a = 0
    print(y * ('@'))
    while (a < x - 2):
        print('@' + (y - 2) * (' ') + '@')
        a = a + 1
    print(y * ('@'))
gambarlahPersegiEmpat(4, 5)

#No. 3. (a)
def jumlahHurufVokal(x):
    k = len(x)
    a = ('AEIOUaeiou')
    b = 0
    for c in x:
        if c in a:
            b = b + 1
    d = [k, b]
    print(d)
k=jumlahHurufVokal("Surakarta")
k

# No. 3. (b)
def jumlahHurufKonsonan(x):
    k = len(x)
    a = ('AEIOUaeiou')
    b = 0
    for c in x:
        if c not in a:
            b = b + 1
    d = [k, b]
    print(d)
k = jumlahHurufKonsonan("Surakarta")
k

#No. 4
def rerata(b):
    x = len(b)
    y = 0
    z = 0
    while (y < x):
        z = z + b[y]
        y = y + 1
    print (z / x)
rerata([1,2,3,4,5])
g = [3,4,5,4,3,4,5,2,2,10,11,23]
rerata(g)

#No. 5
def apakahPrima(n):
    n = int(n)
    assert n >= 0
    primaKecil = [2, 3, 5, 7, 11]
    bukanPrKecil = [0, 1, 4, 6, 8, 9, 10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2, int(sq(n)) + 1):
            if ((n % i) == 0):
                return False
            elif (i >= int(sq(n))):
                return True
            else:
                continue
apakahPrima(17)
apakahPrima(97)
apakahPrima(123)

#No. 6
def bilPrima():
    for i in range(2, 1000):
        q = True
        for y in range(2, i):
            if (i % y == 0):
                q = False
        if (q == True):
            print(i)
bilPrima()

#No. 7
def faktorPrima(w):
    w = int(w)
    assert w >= 0
    fakP = []
    q = 2
    while (q <= w):
        if (w % q == 0):
            w = w / q
            fakP.append(q)
        else:
            q = q + 1
    print(fakP)
faktorPrima(10)
faktorPrima(120)
faktorPrima(19)

#No. 8
def apakahTerkandung(a, b):
    a = a.lower()
    b = b.lower()
    if a in b:
        return True
    else:
        return False
h = "do"
k = "Indonesia tanah air beta"
apakahTerkandung(h,k)
apakahTerkandung("pusaka",k)

#No. 9
def tampilkan():
    for o in range(1, 100):
        if (o % 3 == 0):
            if (o % 5 == 0):
                print("Python UMS")
            else:
                print("Python")
        elif (o % 5 == 0):
            print("UMS")
        else:
            print(o)
tampilkan()

#No. 10
def selesaikanABC(r,s,t):
    r = float(r)
    s = float(s)
    t = float(t)
    D = (s ** 2) - (4 * r * t)
    if (D < 0):
        print("Determinannya negatif. Persamaan tidak mempunyai akar real")
    else:
        j1 = (-s + sq(D)) / (2 * r)
        j2 = (-s - sq(D)) / (2 * r)
        hasil = [j1, j2]
        print(hasil)
selesaikanABC(1,2,3)

#No. 11
def apakahKabisat(tahun):
    d = tahun
    if (d % 4 == 0):
        if (d % 100 == 0):
            if (d % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
apakahKabisat(1896)
apakahKabisat(1897)
apakahKabisat(1900)
apakahKabisat(2000)
apakahKabisat(2020)
apakahKabisat(2100)
#Hasil tidak ditampilkan karena nilai hanya dikembalikan dan tidak dicetak

#No. 12
#def gameTebakAngka():
 #   w = 1
  #  m = randint(1, 101)
   # n = input("Masukkan tebakkan ke-" + str(w) + " : ")
    #n = int(n)
 #   if (n == m):
  #      print("Ya anda benar")
   # if (n < m):
   #     print("Itu terlalu kecil")
   # elif (n > m):
   #     print("Itu terlalu besar")
   # while (n != m):
    #    w += 1
     #   n = input("Masukkan tebakkan ke-" + str(w) + " : ")
      #  n = int(n)
       # if (n < m):
        #    print("Itu terlalu kecil")
       # elif (n > m):
        #    print("Itu terlalu besar")
        #if (n == m):
         #   print("Ya anda benar")
#gameTebakAngka()

#No. 13
def katakan(angka):
    ejaan = ["","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    hasil = " "
    k = int(angka)
    if (k >= 0 and k <= 11) :
        hasil = hasil + ejaan[k]
    elif (k < 20) :
        hasil = katakan(k%10) + "Belas"
    elif (k < 100) :
        hasil = katakan(k/10) + "Puluh" + katakan(k%10)
    elif (k < 200) :
        hasil = "Seratus" + katakan(k-100)
    elif (k < 1000) :
        hasil = katakan(k/100) + "Ratus" + katakan(k%100)
    elif (k < 2000) :
        hasil = "Seribu" + katakan(k - 1000)
    elif (k < 10000) :
        hasil = katakan(k / 1000) + "Ribu" + katakan(k % 1000)
    elif (k < 20000) :
        hasil = "Sepuluh Ribu" + katakan(k - 10000)
    elif (k < 100000) :
        hasil = katakan(k / 10000) + "Puluh" + katakan(k % 10000)
    elif (k < 200000) :
        hasil = "Seratus Ribu" + katakan(k - 100000)
    elif (k < 1000000) :
        hasil = katakan(k / 100000) + "Ratus" + katakan(k % 100000)
    elif (k < 2000000) :
        hasil = "Satu Juta" + katakan(k - 1000000)
    elif (k < 10000000) :
        hasil = katakan(k / 1000000) + "Juta" + katakan(k % 1000000)
    elif (k == 10000000) :
        hasil = "Satu Milyar" + katakan(k % 10000000)
    else :
        hasil = "Angka hanya sampai satu milyar"
    return (hasil)
katakan(3125750)

#No. 14
def formatRupiah(tulisBil):
    t = str (tulisBil)
    if len(t) <= 3 :
         return ("Rp " + t)
    else :
         c = t[-3:]
         d = t[:-3]
         return (formatRupiah(d) + "." + c)
         print (("Rp ") + formatRupiah(d) + "." +c)
formatRupiah(1500)
formatRupiah(2560000)
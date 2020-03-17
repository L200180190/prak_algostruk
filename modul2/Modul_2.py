#Nomer 1

class Pesan(object):
    """Sebuah class bernama Pesan.
       Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimatku mempunyai', len(self.teks), 'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru

#a
    def apakahTerkandung(self, q):
        if q in self.teks:
            return True
        else :
            return False

#b
    def hitungKonsonan(self):
        a = 0
        x = self.teks
        Voc = "aiueoAIUEO"
        for i in x:
            if i not in Voc:
                a += 1
        return a

#c
    def hitungVokal(self):
        b = 0
        x = self.teks
        c = "aiueoAIUEO"
        for i in x:
            if i in c:
                b += 1
        return b

#Nomer 2

class Manusia(object):
    """class 'Manusia' dengan inisiasi 'nama'"""
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
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class manusia.
           Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan", s, "Sambil belajar.")
        self.keadaan = 'kenyang'

#a
    def ambilKotaTinggal(self):
        return self.kotaTinggal

#b
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal = ubah
        return ubah

#c
    def ambilUangSaku(self):
        return self.uangSaku

    def tambahUangSaku(self, tambah):
        self.uangSaku += tambah

#Nomer 4
    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)

#Nomer 5
    def hapusKuliah(self,kuliah):
        self.listKuliah.remove(kuliah)

#Nomer 6
class SiswaSMA(Manusia):
    def __init__(self, nama, sekolah, alamat, usia):
        self.nama = nama
        self.sekolah = sekolah
        self.alamat = alamat
        self.usia = usia
    def __str__(self):
        x = "Nama : " + str(self.nama) + '\n' \
            + "Sekolah : " + str(self.sekolah) + '\n' \
            + "Alamat : " + str(self.alamat) + '\n' \
            + "Usia : " + str(self.usia)
        return x

#Nomer 7
class MhsTIF(Mahasiswa):    
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def kataKanPy(self):
        print('Python is cool.')

# Apakah metode / state itu berasal dari class Manusia, Mahasiswa, atau MhsTIF?

# Jawab :

#Metoode atau state yang muncul berasal dari semua class baik Manusia, Mahasiswa, atau MhsTIF.
#Ini karena MhsTIF yang merupakan anak class dari Mahasiswa, dan itu membuat MhsTIF mewarisi
#semua properties dari Mahasiswa dan Manusia.


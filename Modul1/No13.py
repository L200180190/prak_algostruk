#No. 13
def katakan(angka):
    ejaan = ["","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    hasil = " "
    k = int(angka)
    if (k >= 0 and k <= 11) :
        hasil = hasil + ejaan[k]
    elif (k < 20) :
        hasil = katakan(k%10) + " Belas"
    elif (k < 100) :
        hasil = katakan(k/10) + " Puluh " + katakan(k%10)
    elif (k < 200) :
        hasil = "Seratus " + katakan(k-100)
    elif (k < 1000) :
        hasil = katakan(k/100) + " Ratus " + katakan(k%100)
    elif (k < 2000) :
        hasil = "Seribu " + katakan(k - 1000)
    elif (k < 10000) :
        hasil = katakan(k / 1000) + " Ribu " + katakan(k % 1000)
    elif (k < 20000) :
        hasil = "Sepuluh Ribu " + katakan(k - 10000)
    elif (k < 100000) :
        hasil = katakan(k / 10000) + " Puluh " + katakan(k % 10000)
    elif (k < 200000) :
        hasil = "Seratus Ribu " + katakan(k - 100000)
    elif (k < 1000000) :
        hasil = katakan(k / 100000) + " Ratus " + katakan(k % 100000)
    elif (k < 2000000) :
        hasil = "Satu Juta " + katakan(k - 1000000)
    elif (k < 10000000) :
        hasil = katakan(k / 1000000) + " Juta " + katakan(k % 1000000)
    elif (k == 10000000) :
        hasil = "Satu Milyar " + katakan(k % 10000000)
    else :
        hasil = "Angka hanya sampai satu milyar"
    return (hasil)


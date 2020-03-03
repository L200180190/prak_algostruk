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

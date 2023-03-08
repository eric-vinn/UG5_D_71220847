kalimat = str(input("Masukkan kalimat : "))
awal = str(input("Kata yang dicari : "))
setelah =  str(input("Diganti menjadi : "))
def ganti_kata(kalimat,awal,setelah):
    a = kalimat.split( )
    for i in range (len(a)):
        if a[i] == awal:
            a[i] = setelah
        else:
            continue
    print (" ".join(a))


ganti_kata(kalimat,awal,setelah)
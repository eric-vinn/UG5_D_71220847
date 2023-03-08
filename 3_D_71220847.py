import math
berhenti = False
while berhenti == False:
    awal = int(input("Masukkan jarak awal (dalam meter): "))
    ke5 = int(input("Masukkan sudut elevasi pada menit ke-5 (dalam derajat): "))
    ke6 = int(input("Masukkan sudut elevasi pada menit ke-6 (dalam derajat): "))
    t5 = awal*math.tan(math.radians(ke5))
    jarak = awal*(math.tan(math.radians(ke6))-math.tan(math.radians(ke5)))
    selisih = jarak*math.tan(math.radians(ke6))
    print(f"Ketinggian di menit 5 adalah {t5}")
    print(f"Selisih ketinggian drone saat menit ke-5 dan ke-8 adalah {selisih}")
    berhenti = False
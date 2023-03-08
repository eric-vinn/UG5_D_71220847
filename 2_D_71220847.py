def hitung_mobil():
    jumlahSol = 0
    jumlahSur = 0
    jumlahJog = 0
    jumlahMag = 0
    berhenti = False

    while berhenti == False:
        asal = input("Masukkan asal mobil atau ketik 'done' untuk keluar: ")
        if asal == "done":
            berhenti = True
        elif asal == "solo":
            jumlahSol += 1
        elif asal == "surabaya":
            jumlahSur += 1
        elif asal == "jogja":
            jumlahJog += 1
        elif asal == "magelang":
            jumlahMag += 1
        else:
            print("tidak valid")
    print(f"Jumlah Mobil Solo     : {jumlahSol}")
    print(f"Jumlah Mobil Surabaya : {jumlahSur}")
    print(f"Jumlah Mobil Jogja    : {jumlahJog}")
    print(f"Jumlah Mobil Magelang : {jumlahMag}")
hitung_mobil()
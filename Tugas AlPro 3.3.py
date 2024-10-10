usia = int(input("Masukkan usia Anda : "))
tekananDarah = int(input("Masukkan tekanan darah Anda : "))
if usia >= 60 and tekananDarah > 140:
    print("Status kesehatan : Tnggi")
elif usia >= 60 and tekananDarah <= 140:
    print("Status kesehatan : Normal")
elif usia < 60 and tekananDarah > 130:
    print("Status kesehatan : Tinggi")
elif usia < 60 and tekananDarah <= 130:
    print("Status kesehatan : Normal")
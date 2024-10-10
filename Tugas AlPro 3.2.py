nilai = int(input("Masukkan nilai ujian Anda (1-100) : "))
if 100 >= nilai >= 90:
    print ("Feedback : Sangat baik")
elif 80 >= nilai <= 89:
    print("Feedback : Baik")
elif 70 >= nilai <= 79:
    print("Feedback : Cukup")
elif 60 >= nilai <=69:
    print("Feedback : Kurang")
else:
    print("Feedback : Sangat kurang")

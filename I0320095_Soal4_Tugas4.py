usia = int(input("Berapa usia anda?"))
hasil_usia = (usia >= 21)

kelulusan = input("Apakah Anda sudah lulus ujian kualifikasi? (Y/T)")
hasil_kelulusan = (kelulusan == "Y")

if hasil_usia and hasil_kelulusan :
    print("Anda dapat mendaftar di kursus")
else :
    print("Anda tidak dapat mendaftar di kursus")
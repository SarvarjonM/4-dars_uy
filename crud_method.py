class MalumotlarBazasiJadvali:
    def __init__(self):
        self.malumotlar_bazasi = []

    def malumot_qoshish(self, malumot):
        self.malumotlar_bazasi.append(malumot)
        print("Malumot muvaffaqiyatli qo'shildi.")

    def malumotlarni_korsatish(self):
        if not self.malumotlar_bazasi:
            print("Malumotlar bazasi bo'sh.")
        else:
            for malumot in self.malumotlar_bazasi:
                print(malumot)

    def malumotni_yangilash(self, eski_malumot, yangi_malumot):
        if eski_malumot in self.malumotlar_bazasi:
            indeks = self.malumotlar_bazasi.index(eski_malumot)
            self.malumotlar_bazasi[indeks] = yangi_malumot
            print("Malumot muvaffaqiyatli yangilandi.")
        else:
            print("Malumot topilmadi.")

    def malumotni_ochirish(self, malumot):
        if malumot in self.malumotlar_bazasi:
            self.malumotlar_bazasi.remove(malumot)
            print("Malumot muvaffaqiyatli o'chirildi.")
        else:
            print("Malumot topilmadi.")

# Asosiy qo'llanma namunasi
if __name__ == "__main__":
    jadval = MalumotlarBazasiJadvali()

    # Ma'lumot qo'shish
    jadval.malumot_qoshish("Malumot 1")
    jadval.malumot_qoshish("Malumot 2")
    jadval.malumot_qoshish("Malumot 3")

    # Ma'lumotlarni ko'rsatish
    print("Barcha malumotlar:")
    jadval.malumotlarni_korsatish()

    # Ma'lumotni yangilash
    jadval.malumotni_yangilash("Malumot 2", "Yangilangan Malumot 2")

    # Ma'lumotni ochirish
    jadval.malumotni_ochirish("Malumot 3")

    # Yangilangan ma'lumotlarni ko'rsatish
    print("Yangilangan malumotlar:")
    jadval.malumotlarni_korsatish()

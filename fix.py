#TUGAS AKHIR MATA KULIAH SISTEM OPERASI 
#KELOMPOK 3
#TOPIK SJF PREEMPTIVE / SRTF (2)
#ANGGOTA KELOMPOK:
#71220854	David Arya Seta
#71220863	Diva Filemon Manik
#71220875	Hanli Febriano Galandjindjinay
#71220924	Giovanka Steviano Harry Premono



#Fungsi cari_sisa_waktu_terkecil
def cari_sisa_waktu_terkecil(waktu, n, waktu_sisa, waktu_datang):
    kurangi = float("inf")
    min_index = -1

    for i in range(n):
        if waktu_sisa[i] > 0 and waktu_datang[i] <= waktu and waktu_sisa[i] < kurangi:
            kurangi = waktu_sisa[i]
            min_index = i

    return min_index

# Input berapa banyak proses yang mau dihitung
n = int(input("Masukan Jumlah proses: "))

# Membuat matriks untuk menyimapan id proses, lama eksekusi, waktu datang, waktu tunggu, dan waktu tunggu proses selanjutnya.
hitung = [[0 for j in range(5)] for i in range(n)]
rata2waktutunggu, rata2waktutunggunext = 0, 0

print("Masukan waktu tiba dan lama eksekusi:")

# Ngambil waktu datang dan lama eksekusi lalu dihitung selisihnya.
for i in range(n):
    hitung[i][2] = int(input(f"Waktu kedatangan Proses ke {i + 1}: "))
    hitung[i][1] = int(input(f"Lama eksekusi proses ke {i + 1}: "))
    hitung[i][0] = i + 1

waktu_sisa = [hitung[i][1] for i in range(n)]
time = 0

# Sorting proses berdasarkan waktu tiba (Diurutkan dari paling cepat)
hitung.sort(key=lambda x: x[2])

print("Proses | Waktu_Datang |  Lama_Eksekusi |  Waktu_Tunggu |  Waktu Tunggu Selanjutnya |")

# Proses SJF preemptive nya.
while True:
    index = cari_sisa_waktu_terkecil(time, n, waktu_sisa, [hitung[i][2] for i in range(n)])
    
    if index == -1:
        break
    
    waktu_sisa[index] -= 1

    if waktu_sisa[index] == 0:
        hitung[index][4] = time + 1 - hitung[index][2]
        hitung[index][3] = hitung[index][4] - hitung[index][1]

    time += 1

#Mengeluarkan data 
for i in range(n):
    print(f" P{hitung[i][0]}\t\t{hitung[i][2]} \t\t{hitung[i][1]} \t\t{hitung[i][3]}\t\t\t{hitung[i][4]}")

# Menghitug rata2 waktu tunggu dan waktu tunggu proses selanjutnya.
rata2waktutunggu = sum(hitung[i][3] for i in range(n)) / n
rata2waktutunggunext = sum(hitung[i][4] for i in range(n)) / n

print("Rata-rata waktu tunggu proses  = %.3f" % rata2waktutunggu )
print("Rata-rata waktu tunggu proses selanjutnya = %.3f" % rata2waktutunggunext)

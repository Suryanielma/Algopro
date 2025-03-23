#https://www.spoj.com/problems/MAXROO
#n merupakan inisial untuk kanguru 
#MAXROO - Max dan peternakan kanguru
# Max adalah seorang petani kanguru di Stardew Valley. Setiap hari, dia bangun, minum susu kanguru, dan berangkat kerja. Rutinitasnya sehari-hari adalah memberi makan ayam jantan. Awalnya, peternakannya memiliki N kanguru, semuanya kelaparan. Setiap hari, Max mengurutkan semua ayam jantan yang lapar dan memberi nomor dari 1 sampai K (K adalah jumlah kanguru lapar, K ≤ N). Dia kemudian akan memberi makan semua ayam jantan yang bernomor genap. (yaitu Kanguru nomor 2, 4, 8, dst.) Jika hanya ada satu kanguru, maka dia akan memberi makan kanguru tersebut. Pekerjaan berlanjut sampai tidak ada lagi ayam lapar yang tersisa.
# Max ingin tahu berapa hari yang dibutuhkannya untuk menyelesaikan pekerjaannya. Rupanya, dia akan mulai memukulnya ketika mereka terlalu lapar, tapi itu bukan masalah kami. Bantu Max menemukan jawaban atas pertanyaannya.

# Memasukkan Satu bilangan bulat N yang merupakan jumlah kanguru di peternakan Max.

# (1 ≤ N ≤ 109)
# Keluaran
# - Bilangan bulat yang merupakan jawabannya



n = int(input())
days = 0
while n > 0:
    days += 1
    if n == 1:
        break
    n = (n + 1) // 2
print(days)
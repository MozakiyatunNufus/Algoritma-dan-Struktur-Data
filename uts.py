from collections import deque

class Produk:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"{self.kode}. {self.nama} : Rp {self.harga}"


class Minimarket:
    def __init__(self):
        #Penggunaan array/list (produk_list menyimpan daftar objek Produk)
        self.produk_list = [
            Produk("A", "Biskuit", 5000),
            Produk("B", "Sabun", 3000),
            Produk("C", "Minuman Soda", 7000),
            Produk("D", "Pasta Gigi", 10000),
            Produk("E", "Mie Instan", 3000),
        ]
        # Riwayat transaksi yang telah dilakukan (Stack)
        self.riwayat_transaksi = []
        # Keranjang belanja untuk menyimpan produk yang dipilih (Queue)
        self.keranjang_belanja = deque()

    def tampilkan_menu(self):
        print("===============================")
        print("          Minimarket           ")
        print("        Daftar Produk          ")
        print("===============================")
        #Penggunaan array/list (Iterasi melalui produk_list)
        for produk in self.produk_list:
            print(produk)
        print("===============================")

    def tampilkan_keranjang(self):
        print("\n--- Keranjang Belanja ---")
        total_semua = 0
        #Penggunaan array/list (Iterasi melalui keranjang belanja)
        for i, item in enumerate(self.keranjang_belanja, 1):
            produk = item["produk"]
            jumlah = item["jumlah"]
            total = item["total_bayar"]
            print(f"{i}. {produk.nama} x {jumlah} = Rp {total}")
            total_semua += total
        print(f"Total: Rp {total_semua}")
        print("------------------------\n")

    def hitung_total(self, jumlah, harga):
        total_harga = harga * jumlah
        diskon = int(total_harga * 0.1) if jumlah >= 5 else 0  # Diskon 10% jika jumlah >= 5
        total_bayar = total_harga - diskon 
        return total_harga, diskon, total_bayar

    def cari_produk(self, kode):
        #Penggunaan array/list (Pencarian dengan list comprehension)
        return next((p for p in self.produk_list if p.kode == kode), None)

    def tambah_ke_keranjang(self, produk, jumlah, total_bayar):
        #Penggunaan array/list (Menambahkan item ke keranjang (append))
        self.keranjang_belanja.append({
            "produk": produk,
            "jumlah": jumlah,
            "total_bayar": total_bayar
        })

    def simpan_transaksi(self):
        if self.keranjang_belanja:
            # Menyimpan keranjang belanja ke riwayat transaksi (Stack)
            self.riwayat_transaksi.append(self.keranjang_belanja.copy())
            self.keranjang_belanja.clear()  # Mengosongkan keranjang setelah transaksi disimpan
            print("Transaksi berhasil disimpan!")

    def tampilkan_riwayat(self):
        if not self.riwayat_transaksi:
            print("Belum ada riwayat transaksi.")
            return
            
        print("\n=== RIWAYAT TRANSAKSI ===")
        #Penggunaan array/list (Iterasi melalui riwayat transaksi)
        for i, transaksi in enumerate(self.riwayat_transaksi, 1):
            print(f"\nTransaksi #{i}:")
            total_transaksi = 0
            for item in transaksi:
                produk = item["produk"]
                jumlah = item["jumlah"]
                total = item["total_bayar"]
                print(f"- {produk.nama} x {jumlah} = Rp {total}")
                total_transaksi += total
            print(f"Total Transaksi: Rp {total_transaksi}")
        print("=========================\n")

    def undo_transaksi(self):
        if self.riwayat_transaksi:
            # Menghapus transaksi terakhir dari riwayat (Stack)
            last_transaction = self.riwayat_transaksi.pop()
            print("Transaksi terakhir telah di-undo.")
            print("Detail transaksi yang di-undo:")
            for item in last_transaction:
                print(f"- {item['produk'].nama} x {item['jumlah']} = Rp {item['total_bayar']}")
        else:
            print("Tidak ada transaksi untuk di-undo.")

    def transaksi(self):
        while True:   # Perulangan untuk proses transaksi
            self.tampilkan_menu()
            
            while True:   # Perulangan untuk pemesanan produk
                pesan = input("Masukkan list abjad produk (A/B/C/D/E) = ").upper()
                produk_terpilih = self.cari_produk(pesan)
                
                if produk_terpilih:
                    jumlah_pesan = int(input("Masukkan jumlah pesanan = "))
                    total_harga, diskon, total_bayar = self.hitung_total(jumlah_pesan, produk_terpilih.harga)

                    print("--------------------------")
                    print("          Minimarket      ")
                    print("--------------------------")
                    print("Produk :", produk_terpilih.nama)
                    print("Jumlah Pesan :", jumlah_pesan)
                    print("Harga :", total_harga)
                    print("Diskon :", diskon)
                    print("--------------------------")
                    print("Jumlah Bayar :", total_bayar)
                    print("--------------------------")

                    # Tambah ke keranjang (Queue)
                    self.tambah_ke_keranjang(produk_terpilih, jumlah_pesan, total_bayar)
                    self.tampilkan_keranjang()
                else:
                    print("Produk tidak tersedia, silahkan masukkan abjad produk yang tersedia.")

                tambah_lagi = input("Tambah produk lain ke keranjang? (Y/N) = ").lower()
                if tambah_lagi != 'y':
                    # Simpan transaksi (Stack)
                    self.simpan_transaksi()

                    # Tampilkan riwayat jika ingin melihatnya
                    lihat_riwayat = input("Lihat riwayat transaksi? (Y/N) = ").lower()
                    if lihat_riwayat == 'y':
                        self.tampilkan_riwayat()

                    # Tanya apakah ingin melakukan transaksi baru
                    break

            pilihan = input("Apakah Anda ingin order kembali? (Y/N) = ").lower()
            if pilihan != 'y':
                print("Terima kasih telah berbelanja di Minimarket!")
                break


if __name__ == "__main__":
    minimarket = Minimarket()
    minimarket.transaksi()
import time
import os

def load_data_csv(users_csv):
    data_user = {}
    
    lokasi_folder = os.path.dirname(__file__)

    path_lengkap = os.path.join(lokasi_folder, users_csv)
    
    try:
        with open(path_lengkap, "r") as file:
            baris_data = file.readlines()
            for baris in baris_data:
                akun = baris.strip().split(',')
                if len(akun) == 2:
                    data_user[akun[0]] = akun[1]
    except FileNotFoundError:
        print(f"Error: File '{users_csv}' tidak ditemukan di lokasi: {path_lengkap}")
    
    return data_user

def jalankan_login():
    users = load_data_csv("users.csv")
    
    if not users:
        print("Sistem dihentikan karena data user tidak tersedia.")
        return

    batas_percobaan = 3
    percobaan = 0

    while True:
        print("\n=== SISTEM LOGIN ===")
        input_username = input("Username: ")
        input_password = input("Password: ")

        if input_username in users and users[input_username] == input_password:
            print(f"\n[SUKSES] Login berhasil! Selamat datang, {input_username}.")
            break  
        else:
            percobaan += 1
            sisa = batas_percobaan - percobaan
            print(f"[GAGAL] Username atau password salah. Sisa percobaan: {sisa}")

            if percobaan >= batas_percobaan:
                print("\n[TERKUNCI] Anda telah gagal login 3 kali beruntun.")
                print("Sistem dikunci selama 5 menit. Harap tunggu...")
                
                waktu_tunggu = 300 
                
                # hitung mundur 
                while waktu_tunggu > 0:
                    menit = waktu_tunggu // 60
                    detik = waktu_tunggu % 60
                    # end="\r" membuat teks menimpa baris yang sama, tidak membuat baris baru
                    print(f"Waktu tersisa: {menit:02d}:{detik:02d} ", end="\r")
                    time.sleep(1)
                    waktu_tunggu -= 1
                    
                print("\n\n[TERBUKA] Waktu tunggu selesai. Silakan coba lagi.")
                percobaan = 0

jalankan_login()
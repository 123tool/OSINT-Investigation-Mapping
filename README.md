## SOURCE OSINT MAPPING INVESTIGATION

Platform investigasi digital terpadu yang dirancang untuk mengotomatisasi pengumpulan data dari berbagai sumber terbuka. Alat ini mengintegrasikan teknik **Deep Dorking** (fokus pada kebocoran data pemerintah Indonesia) dan **Social Media Enumeration** ke dalam satu dashboard interaktif.

---

## ⚡ Fitur

- **Deep Dorking Logic:** Mencari dokumen sensitif (PDF, XLSX, DOC) di domain `.go.id` dan `.ac.id`.
- **Social Scanner:** Melacak keberadaan profil target di platform populer secara paralel.
- **AI-Powered Analysis:** Menghasilkan prompt khusus yang siap dimasukkan ke Gemini/ChatGPT untuk analisis profil risiko otomatis.
- **Cyber-Forensic UI:** Dashboard dengan desain Glassmorphism untuk pengalaman investigasi profesional.

---

## Instalasi
​1. Konfigurasi API (Wajib)
​Dapatkan API Key dari Google Programmable Search. Setelah dapat, buat file .env di root folder :
```
GOOGLE_API_KEY=masukkan_api_key_disini
GOOGLE_CSE_ID=masukkan_cse_id_disini
```
2. Setup Backend
​Buka terminal dan jalankan :
## Install dependensi
```
pip install -r requirements.txt
```
## Jalankan backend
```
python -m app.main
```
3. Setup Frontend
​Buka terminal baru :
```
cd web
npm install
npm install axios
npm start
```

## Cara Penggunaan

1. ​Buka dashboard di http://localhost:3000.
​Masukkan nama target atau nomor HP pada kolom input.
2. ​Klik Start Investigation.
​Hasil dokumen publik dan akun sosial media akan muncul otomatis.
3. ​Tips : Gunakan tombol "Copy AI Prompt" (jika tersedia di UI) untuk menganalisis temuan secara mendalam menggunakan AI.

​🛡️ Disclaimer

**​Hanya untuk tujuan edukasi dan pertahanan siber. Pengembang tidak bertanggung jawab atas penyalahgunaan alat ini untuk kegiatan ilegal atau pelanggaran privasi (Doxing). Patuhi selalu hukum telekomunikasi yang berlaku di Indonesia.**

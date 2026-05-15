## SOURCE OSINT AGGREGATOR

![License](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)
![React](https://img.shields.io/badge/React-18.x-cyan.svg)
![OSINT](https://img.shields.io/badge/Intelligence-Unified-red.svg)

**SPY-SOURCE OSINT** adalah platform investigasi digital terpadu yang dirancang untuk mengotomatisasi pengumpulan data dari berbagai sumber terbuka (Open Source Intelligence). Alat ini mengintegrasikan teknik **Deep Dorking**, **Social Media Enumeration**, dan **Data Leak Analysis** ke dalam satu dashboard interaktif bergaya *Cyber-Forensics*.

---

## ⚡ Fitur Utama

- **🇮🇩 Localized Deep Dorking:** Algoritma khusus yang memprioritaskan pencarian pada domain pemerintah (`.go.id`) dan pendidikan (`.ac.id`) Indonesia untuk menemukan dokumen publik (PDF/XLSX) yang bocor.
- **📱 Social Media Presence Scanner:** Melacak jejak akun pada platform populer (Instagram, TikTok, Facebook, GitHub, dll) secara paralel.
- **🛡️ Glassmorphism Dashboard:** Antarmuka modern yang memudahkan analis untuk memvisualisasikan temuan data tanpa perlu menggunakan terminal secara manual.
- **🤖 AI-Ready Analysis:** Output data yang diformat khusus agar mudah dianalisis lebih lanjut menggunakan Large Language Models (LLM) seperti Gemini atau ChatGPT.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python) - High performance asynchronous processing.
- **Frontend:** React.js & Tailwind CSS - Glassmorphism UI Design.
- **Search Engine:** Google Custom Search API integration.
- **Networking:** HTTPX for fast, concurrent social media probing.

---

## 🚀 Panduan Instalasi

### 1. Prasyarat (Prerequisites)
Pastikan sistem Anda sudah terinstal:
- Python 3.10 atau lebih baru.
- Node.js & NPM.
- API Key dari [Google Programmable Search Engine](https://developers.google.com/custom-search/v1/overview).

### 2. Setup Backend
```bash
# Clone repository
git clone [https://github.com/username/spy-source-osint.git](https://github.com/username/spy-source-osint.git)
cd spy-source-osint

# Install dependensi Python
pip install -r requirements.txt

# Konfigurasi Environment Variables
# Buat file .env dan masukkan API Key Anda:
echo "GOOGLE_API_KEY=your_key_here" > .env
echo "GOOGLE_CSE_ID=your_cse_id_here" >> .env

# Jalankan server backend
uvicorn app.main:app --reload --port 8001

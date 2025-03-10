# Projek-Analisis-Data-Dengn-Python

## Setup Environment

Langkah-langkah untuk menyiapkan lingkungan agar dashboard bisa dijalankan.

### 1. Instal Python
- Unduh Python dari [python.org](https://www.python.org/downloads/).
- Instal dengan mencentang opsi "Add Python to PATH".
- Verifikasi instalasi:
  - Buka Command Prompt (CMD): `Win + R`, ketik `cmd`, Enter.
  - Ketik: `python --version`.
  - Harusnya muncul versi (misalnya, `Python 3.9.0`).

### 2. Unduh File Proyek
- Salin semua file (`day.csv`, `dashboard.py`, `requirements.txt`) ke folder lokal, misalnya: `C:\Proyek_Analisis_Data`.

## Setup Environment - Shell/Terminal

Instruksi spesifik untuk menyiapkan dependensi menggunakan shell/terminal (CMD di Windows).


1. **Buka Command Prompt**:
   - Tekan `Win + R`, ketik `cmd`, lalu tekan Enter.
   - Pastikan CMD terbuka.

2. **Navigasi ke Folder Proyek**:
   - Ketik perintah berikut untuk masuk ke folder proyek:
     
   - Cek Instalasi Ulang:
       -pip uninstall streamlit
       -pip install streamlit

   -Gunakan Virtual Environment (opsi bersih):
      1. Buat environment:
       python -m venv myenv
      2. Aktifkan:
       myenv\Scripts\activate
      3. Instal:
       pip install streamlit pandas matplotlib seaborn
      4. Jalankan:
         cd C:/Proyek_Analisis_Data-Dengn-Python
      5. Lanjutkan
         streamlit run dashboard.py
         

  3. **You can now view your Streamlit app in your browser**.
Local URL: http://localhost:8501

![ss1](https://github.com/user-attachments/assets/f000060c-fa03-4f43-b750-1cc404056c2d)
![ss2](https://github.com/user-attachments/assets/8a9e9fe3-b44c-435e-8e17-6673d5d69051)
![ss3](https://github.com/user-attachments/assets/0943bde0-7a64-4070-b278-90c66439fa61)


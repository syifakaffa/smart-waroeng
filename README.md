# LINKS

[Link menuju aplikasi smart_waroeng](https://smart-waroeng.adaptable.app) <br>

1. Cara mengimplementasikan setiap checklist:
    * Membuat sebuah proyek Django baru.
        - Pertama saya membuat direktori untuk tugas ini di laptop dengan nama TugasPBP. Lalu, saya menginisasi direktori lokal tersebut dengan git. 
        - Membuat repositori baru bernama smart-waroeng di github. Dan menghubungkan repositori github tersebut ke direktori lokal (TugasPBP) di laptop saya dengan perintah git remote add origin (url repo).
        - Setelah itu, saya membuat virtual environment di dalam direktori TugasPBP (lokal) dan membuat berkas requirements.txt dan menambahkan beberapa dependencies seperti yang ada di tutorial 0.
        - Lalu saya mulai membuat proyek baru django bernama “smart-waroeng” dan mengkonfigurasi proyek tersebut dengan menambahkan “*” pada ALLOWED_HOSTS di settings.py untuk keperluan deployment seperti yang ada di tutorial 0.
        - Membuat  file .gitignore di direktori lokal TugasPBP.
        - Mengunggah proyek django di atas ke repositori github smart-waroeng dengan add, commit, push.

    * Membuat aplikasi dengan nama main pada proyek tersebut.
        - Pertama, saya mengaktifkan virtual environment dengan perintah: env\Scripts\activate.bat di direktori TugasPBP.
        - Membuat aplikasi bernama main dengan menjalankan perintah: python manage.py startapp main.
        - Lalu, saya mendaftarkan aplikasi main tersebut ke dalam proyek smart_waroeng dengan menambahkan ‘main’ ke dalam variabel INSTALLED_APPS di berkas setting.py.

    * Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        - Saya melakukan routing dengan mendaftarkan aplikasi main tersebut ke dalam proyek smart_waroeng dengan menambahkan ‘main’ ke dalam variabel INSTALLED_APPS di berkas setting.py.

    * Membuat model pada aplikasi main dengan nama Item yang memiliki atribut name, amount, description, dan price.
        - Mengimport models dari django.db pada berkas models.py yang berada di direktori main.
        - Membuat class Item dan menginisiasi atribut:
            - name dengan tipe data CharField
            - amount dengan tipe data IntegerField
            - price dengan tipe data IntegerField
            - description dengan tipe data TextField
        - Membuat dan mengaplikasikan migrasi model  ke basis data lokal.
    
    * Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.
        - Dalam berskas views.py di direktori main, saya mengimpor render dari djago.shortcuts untuk merender tampilan HTML dari data yang digunakan. Lalu, sya menambahkan fungsi show_main yang akan mengatur HTTP, sehingga menampilkan tampilan yang sesuai. Di dalam fungsi show_main, saya menambahkan context yang berisi data-data nama aplikasi, nama, dan kelas yang nantinya akan terlihat di tampilan page.
        - Membuat direktori templates di dalam direktori main lalu membuat file main.html. Templates akan diisi oleh sintaks Django seperti {{name}}, {{app}}, dan {{class}} yang akan menampilkan nilai dari variabel yang ada di context.

    * Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        - Membuat berkas urls.py di dalam direktori main untuk mengatur rute URL yang terkait dengan aplikasi main.
        - Mengisi urls.py tersebut dengan menambahkan app_name dan mendefinisikan rute URL dengan meingimpor path dari django.urls.
        - Mengimport fungsi include dari django.urls ke dalam berkas urls.py di direktori smart_waroeng.
        - Menambahkan rute URL path('main/', include('main.urls')),  di dalam variabel urlpatterns yang ada di berkas urls.py tersebut.

    * Setelah selesai, saya melakukan deployment ke Adaptable agar aplikasi bisa diakses secara umum. Saya menggunakan Python App Template sebagai template deployment, PostgreeSQl sebagai tipe basis data, dan python yang digunakan oleh saya 3.11. Setelah itu, saya memasukkan perintah python manage.py migrate && gunicorn shopping_list.wsgi pada Start Command, lalu memulai proses deployment aplikasi.

    * Setelah itu, saya membuat file README.md di direktori lokal yang berisi jawaban setiap pertanyaan. Lalu, saya melakukan add, commit, push ke repository github. 


2. Soal ketiga



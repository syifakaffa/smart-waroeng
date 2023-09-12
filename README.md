# TUGAS 1

Nama    : Syifa Kaffa Billah

NPM     : 2206816430

Kelas   : PBP-C

[Link menuju aplikasi smart_waroeng](https://smart-waroeng.adaptable.app) <br>

1. Cara mengimplementasikan setiap checklist:
    * Membuat sebuah proyek Django baru.
        - Pertama saya membuat direktori untuk tugas ini di laptop dengan nama smart_waroeng. Lalu, saya menginisasi direktori lokal tersebut dengan git. 
        - Membuat repositori baru bernama smart-waroeng di github. Dan menghubungkan repositori github tersebut ke direktori lokal (smart_Wareong) di laptop saya dengan perintah git remote add origin (url repo).
        - Setelah itu, saya membuat virtual environment di dalam direktori smart_waroeng (lokal) dan membuat berkas requirements.txt dan menambahkan beberapa dependencies seperti yang ada di tutorial 0.
        - Lalu saya mulai membuat proyek baru django bernama “smart-waroeng” dan mengkonfigurasi proyek tersebut dengan menambahkan “*” pada ALLOWED_HOSTS di settings.py untuk keperluan deployment seperti yang ada di tutorial 0.
        - Membuat  file .gitignore di direktori lokal smart_wareong.
        - Mengunggah proyek django di atas ke repositori github smart-waroeng dengan add, commit, push.

    * Membuat aplikasi dengan nama main pada proyek tersebut.
        - Pertama, saya mengaktifkan virtual environment dengan perintah: env\Scripts\activate.bat di direktori utama smart_wareong.
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
        - Dalam berskas views.py di direktori main, saya mengimpor render dari djago.shortcuts untuk merender tampilan HTML dari data yang digunakan. Lalu, saya menambahkan fungsi show_main yang akan mengatur HTTP, sehingga menampilkan tampilan yang sesuai. Di dalam fungsi show_main, saya menambahkan context yang berisi data-data nama aplikasi, nama, dan kelas yang nantinya akan terlihat di tampilan page.
        - Membuat direktori templates di dalam direktori main lalu membuat file main.html. Templates akan diisi oleh sintaks Django seperti {{name}}, {{app}}, dan {{class}} yang akan menampilkan nilai dari variabel yang ada di context.

    * Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        - Membuat berkas urls.py di dalam direktori main untuk mengatur rute URL yang terkait dengan aplikasi main.
        - Mengisi urls.py tersebut dengan menambahkan app_name dan mendefinisikan rute URL dengan meingimpor path dari django.urls.
        - Mengimport fungsi include dari django.urls ke dalam berkas urls.py di direktori smart_waroeng.
        - Menambahkan rute URL path('main/', include('main.urls')),  di dalam variabel urlpatterns yang ada di berkas urls.py tersebut.

    * Setelah selesai, saya melakukan deployment ke Adaptable agar aplikasi bisa diakses secara umum. Saya menggunakan Python App Template sebagai template deployment, PostgreeSQl sebagai tipe basis data, dan python yang digunakan oleh saya 3.11. Setelah itu, saya memasukkan perintah *python manage.py migrate && gunicorn smart_waroeng.wsgi* pada Start Command, lalu memulai proses deployment aplikasi.

    * Setelah itu, saya membuat file README.md di direktori lokal yang berisi jawaban setiap pertanyaan. Lalu, saya melakukan add, commit, push ke repository github. 


2. Bagan Request Client:
<img width="571" alt="image" src="https://github.com/syifakaffa/smart-waroeng/assets/124903174/7a864266-f06d-4ca0-948d-98dec77997ae">


4. Virtual environment digunakan dalam membuat aplikasi web berbasis Django dengan alasan supaya ketika kita menggunakan versi package Django yang berbeda, bisa terhindar dari adanya konflik akibat dependensi antar versi package yang berbeda. *Virtual environment* sendiri merupakan tools yang digunakan untuk membuat lingkungan virtual python terisolasi (tertutup), dalam artian dunia luar tidak bisa mengaksesnya, sebab aplikasi yang menggunakan virtual environment memiliki modulnya sendiri. Selain itu, adanya virtual environment memudahkan kita untuk mengelola dependensi proyek secara independen, sehingga pengembang dapat menginstal, menghapus, atau memperbarui paket-paket dalam virtual environment tanpa mempengaruhi proyek lain. 

    Terkait pertanyaan kedua, kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*. Namun, alangkah baiknya setiap aplikasi yang dibuat menggunakan *virtual environment*, apalagi jika aplikasi yang dibuat berskala besar. Agar hal-hal terkait dependensi bisa dihindari.

5. Perbedaan MVC, MVT, dan MVVM:
    MVC, MVT, dan MVVM merupakan jenis dari arsitektur yang digunakan dalam pengembangan web yang bertujuan untuk memisahkan komponen-komponen utama aplikasi seperti logika aplikasi, tampilan, dan logika presentasi, sehingga pengelolaan kodenya lebih terstruktur dan mudah dipelihara. Perbedaan antara ketiganya terletak pada penempatan komponen logika presentasi dan penghubung antara View dan Model ditempatkan.
    *  **MVC (Model-View-Controller)**: 
        - Model: Bertanggung jawab dalam mengatur data dan logika aplikasi.
        - View: Mengatur logika presentasi kepada pengguna dengan menampilkan data yang diberikan oleh model.
        - Controller: Untuk mengatur interaksi antara Model dan View dan sebagai pengatur aliran aplikasi nya. 

    * **MVT (Model-View-Template)**:
        - Model: Sama seperti MVC, pengelolaan data dan logika aplikasi ada di Model.
        - View: Untuk menampilkan data dari model ke pengguna, namun logika presentasinya berada di template. Di MVT, pengatur aliran aplikasi ada di view.
        - Template: Untuk mengatur bagaimana data dari model bisa ditampilkan oleh view. Di MVT, template jugalah yang memisahkan kode HTML (untuk tampilan) dari logika presentasi.

    * **MVVM (Model-View-View Model)**:
        - Model: Bertanggung jawab dalam mengatur data dan logika aplikasi.
        - View: bertanggung jawab untuk menampilkan data kepada pengguna.
        - View Model: Sebagai penghubung antara View dan Model. ViewModel juga bertanggung jawab untuk merubah data dari model ke bentuk yang sesuai untuk tampilan pengguna.





# TUGAS 3

Nama    : Syifa Kaffa Billah

NPM     : 2206816430

Kelas   : PBP-C


1. Apa perbedaan antara form POST dan form GET dalam Django?
* Dari segi Metode Pengiriman Data:
    - Method POST tidak menampilkan data yang dikirim pada URL, tetapi langsung mengirimkan data atau nilai ke action untuk ditampung.
    - Sedangkan method GET akan menampilkan data/nilai pada URL (bisa dilihat semua orang yang mengakses), kemudian baru akan ditampung oleh action.
* Dari segi Kemampuan Pengiriman Data:
    - Method POST tidak memiliki batasan jumlah karakter/data yang ingin dikrimkan.
    - Method GET memiliki batasan maksimal karakter, yaitu 2047 karakter.
* Dari segi Preferensi Pengugunaan:
    - Method POST digunakan untuk mengirim data yang bersifat sensitif dan penting, seperti password. Biasanya data tersebut juga akan diperbaharui atau dihapus dari server.
    - Method GET bisa digunakan jika datanya bersifat public dan ingin tertampil di URL, misal ketika ingin melakukan pencarian (datanya diambil dari server).
* Dari segi Keamanan:
    - Method POST lebih aman karena dilindungi oleh token CSRF (Cross-Site Request Forgery) untuk mencegah serangan CSRF dan data tidak terlihat di URL.
    - Method GET kurang aman, karena datanya terlihat di URL.


2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
* Fungsi utama:
    - XML dan JSON digunakan untuk menyimpan dan mentransfer data (mengambil datanya dari server).
    - HTML digunakan untuk menjelaskan bagaimana suatu data ditampilkan dan juga untuk menentukan struktur suatu page, misal menampilkan konten di browser. Jadi, lebih kepada tampilan web.
* Human-Readability:
    - XML: Karena memiliki struktur yang kompleks, XML lebih sulit untuk dibaca manusia.
    - JSON: Lebih difokuskun pada representasi data yang mudah dibaca manusia dan lebih sederhana strukturnya (terdiri dari pasangan key-value).
    - HTML: Cukup mudah untuk dibaca oleh manusia karena penyusunannya berdasarkan hierarki dan menggunakan tag yang deskriptif, seperti '<p>' untuk paragraf.


3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- Representasi datanya lebih mudah dibaca oleh manusia karena strukturnya lebih sederhana (menggunakan pasangan key-value).
- JSON mendukung berbagai jenis data, seperti teks, angka, objek, dll.
- JSON lebih ringan strukturnya, penguraian servernya mudah dilakukan oleh berbagai bahasa pemrogaman khususnya JavaScript, dan memiliki overhead yang lebih rendah dibandingkan XML.
- Cocok untuk penggunaan di aplikasi web yang memanfaatkan JavaScript dan AJAX(Asynchronous JavaScript and XML).


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
* Membuat template dasar pada file base.html. Lalu, mengubah setting.py agar base.html terdeteksi sebagai template dengan add *'DIRS': [BASE_DIR / 'templates'],*. di bagian TEMPLATES. Setelah itu, saya menyesuaikan konten yang ada di main.html sesuai template yg ada di base.html. 
[ ] Membuat input form untuk menambahkan objek model pada app sebelumnya.
- Membuat file forms.py yang bisa menerima data produk baru dengan modelnya *Product* dan fieldsnya ada *name*, *available amount*, *price*, dan *description*.
- Pada file views.py di main, saya membuat fungsi *create_product* dengan request method nya POST, agar data otomatis tersimpan saat di submit formnya.
[ ] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
- Mengimport HttpResponse dan serializers.
-HTML: Fungsi show_main yang sebelumnya, saya tambahkan *products* pada *context* yang berisi semua object yang diinput pada form. Untuk mengambil semua objectnya, saya menggunakan *Product.objects.all()*.
- XML: membuat fungsi *show_xml* yang dapat menerima request dan akan mereturn HttpResponse dengan parameter seperti berikut: 
    ```def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")```
- JSON (show_json): sama seperti xml, hanya saja pada bagian serializers dan content_type diubah menjadi json.
- JSON dan XML by id: mirip seperti tanpa id, tetapi object yang dicari difilter berdasarkan id. Kodenya hanya berbeda di bagian *data = Product.objects.filter(pk=id)*. 
[ ] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
- Mengimpor 4 fungsi yang sebelumnya dibuat dan menambahkan 4 path URL (HTML sudah dilakukan di tugas 2) di urls.py bagian urlpatterns untuk keempat fungsi yang baru ditambahkan pada views.py sebelumnya.


5. Screenshot dari hasil akses URL pada Postman
* Format HTML
* Format JSON
* Format XML
* Format XML by Id
* Format JSON by Id


# TUGAS 2
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


3. Virtual environment digunakan dalam membuat aplikasi web berbasis Django dengan alasan supaya ketika kita menggunakan versi package Django yang berbeda, bisa terhindar dari adanya konflik akibat dependensi antar versi package yang berbeda. *Virtual environment* sendiri merupakan tools yang digunakan untuk membuat lingkungan virtual python terisolasi (tertutup), dalam artian dunia luar tidak bisa mengaksesnya, sebab aplikasi yang menggunakan virtual environment memiliki modulnya sendiri. Selain itu, adanya virtual environment memudahkan kita untuk mengelola dependensi proyek secara independen, sehingga pengembang dapat menginstal, menghapus, atau memperbarui paket-paket dalam virtual environment tanpa mempengaruhi proyek lain. 

    Terkait pertanyaan kedua, kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*. Namun, alangkah baiknya setiap aplikasi yang dibuat menggunakan *virtual environment*, apalagi jika aplikasi yang dibuat berskala besar. Agar hal-hal terkait dependensi bisa dihindari.

4. Perbedaan MVC, MVT, dan MVVM:
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
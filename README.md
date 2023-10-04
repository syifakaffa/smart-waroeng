Nama    : Syifa Kaffa Billah

NPM     : 2206816430

Kelas   : PBP-C

# TUGAS 5

1.  **Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.**

    - **Element Selector**: Untuk mengubah properti untuk semua elemen yang mempunya tag yang sama, misalnya heading (h1) ingin warna biru semuanya. Cocok digunakan saat ingin mengaplikasikan style umum ke semua elemen dengan tipe yang sama.
    - **ID Selector**: Untuk memilih elemen berdasarkan id nya. Id pada setiap elemen bersifat unik, jadi selector ini cocok digunakan saat ingin merubah style hanya pada elemen spesifik saja.
    - **Class Selector**: Digunakan untuk memilih atribut "class" dimana setiap elemen dapat memiliki banyak kelas. Cocok digunakan saat mengubah style pada sekelompok elemen yang memiliki karakteristik yang sama.

      
2.  **Jelaskan HTML5 Tag yang kamu ketahui.**

- &lt;p&gt; --> untuk membuat pargraf
- &lt;title&gt; --> untuk membuat judul sebuah page
- &lt;body&gt; ---> untuk membuat badan sebuah halaman
- &lt;h1&gt; sampai &lt;h6&gt; --> untuk membuat heading dengan ukuran yang berbeda sesuai angkanya.
- &lt;b&gt; --> untuk membuat teks yang bold
- &lt;style&gt; --> untuk mengatur style elemen menggunakan css


3.  **Jelaskan perbedaan antara margin dan padding.**

a. Margin:
- Mengosongkan area di sekitar border atau elemen.
- Merupakan ruang antara elemen dengan elemen lainnya.
- Hanya mengatur jarak dan tidak mengatur latar belakang atau warna.
- Mengatur tata letak dari sisi luarnya.

b. Padding:
- Mengosongkan area di sekitar konten.
- Ruang antara konten elemen dengan tepi elemennya.
- Mengatur latar belakang dan warna juga untuk elemennya.
- Mengatur tata letak dari sisi dalam.


4.  **Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**

a. Tailwind:
- Membangun tampilan dengan menggabungkan kelas-kelas utilitas yang udah didefinisikan sebelumnya.
- file CSS nya lebih kecil dan hanya akan memuat kelas-kelas utilitas yang ada.
- Memiliki memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek
- Lebih sulit untuk dipelajari, terrutama bagi pemula.

b. Bootstrap:
- Menggunakan style dan komponen yang sudah didefinisikan yang mana memiliki tampilan yang sudah jadi dan bisa langsung digunakan.
- Memiliki file CSS yang lebih besar dibandingkan dengan Tailwind CSS karena termasuk banyak komponen yang telah didefinisikan.
- Sering kali menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan komponen yang telah didefinisikan.
- Mudah dipelajari, khususnya untuk pemula karena sudah ada komponen yang telah didefinisikan.



5.  **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
- Menambahkan bootstrap ke aplikasi.
- Melakukan design pada halaman login. Disini saya membuat 1 card untuk loginnya, dimana ada header, body, dan footernya. Lalu baground color juga saya ubah.
- Membuat design halaman create product. Saya mengubah background color dan menambahkan margin bottom, up, right, dan left pada body nya.
- Membuat design halaman register. Saya menggunakan 1 card seperti pada halaman login, dimana pada card tersebut ada header dan bodynya. Saya tambahkan margin dan mengubah background color pada bagian tag body.
- Mmebuat design halaman main:
    - Membuat navigation bar yang diambil dari bootstrap. Di dalamnya terdapat nama brand (SmartWaroeng) pada ujung kiri atas, dan untuk navbar itemnya, ada logout dan add new product. Navbar ini saya buat dalam container fluid agar bisa menyesuaikan dengan layar konten nya.
    - Pada navbar tersebut, saya juga buat button navbar togler yang akan muncul saat ukuran tampilan layarnya kecil.
    - Saya buat class konten yang berisi konten2 pada inventori saya. Saya membuat card yang ada di dalam loop product, sehingga jumlah card product akan bertambah sesuai dengan jumlah barang yang dimiliki dalam inventori.
    - Untuk cardya, saya buat ada header untuk nama product, body untuk proce, deskripsi, dan jumlah serta beberapa button edit, serta footer cardnya untuk date addedd barangnya.
    - Saya juga mengubah baground color pada body dan membuat agar cardnya akan mengisi ke horizontal kanan dulu baru ke vertikal bawah.
  - Menambahkan tombol edit product dan membuat berkas html baru yaitu edit_product. Tampilannya saya design sama seperti create_product.
  - Mengerjakan readme dan melakukan add commit push ke github.    

# TUGAS 4

 1. **Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**

    --> UserCreationForm merupakan modul bawaan Django yang dapat membuat user baru pada suatu _web aplications_. yang mana di dalamnya ada field username, password1, dan password2 (_confirm password_).
    * **Kelebihan**: Mudah digunakan. Kita bisa langsung menggunakannya dan menyediakan fitur validasi otomatis, seperti format username yang benar, password yang sesuai dengan kebijakan keamanan, dan password konfirmasi yang harus sama dengan password sebelumnya.
    * **Kekurangan**: Tidak menyediakan field selain username, password1, dan password2. Sehingga jika ingin menambahkan field lain seperti email untuk verivikasi akun, _developer_ harus memodifikasi UserCreationForm atau membuat registration form baru dari awal.
    
 2. **Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**

    * **Autentikasi** : Lebih kepada proses verivikasi pengguna, apakah sesuai username dan password yang dimasukkan dengan yang ada di database. 
    * **Otorisasi**: Prose menentukan hal-hal apa saja yang bisa dilakukan oleh si user yang sudah terautentikasi tadi. Jadi, lebih kepada izin akses yang diberikan ke si pengguna tersebut.
    * **Kenapa penting?**: Tentu autentikasi dan otorisasi ini penting untuk menjaga kemanan web aplikasi yang dibuat agar tidak sembarang orang bisa masuk. Selain itu, adanya otorisasi membuat data yang dimiliki terjaga privasinya karena hanya user yang diautentikasi saja yang punya akses ke datanya masing-masing.
    
 3. **Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**

    Cookie adalah sepotong data (berupa teks) yang disimpan di sisi _client_ yang digunakan untuk mengelola informasi sesi pengguna (misalnya data login), sehingga HTTP bisa melakukan _holding_ state__. Cara kerjanya sendiri pertama-tama permintaan akan dikirim ke server oleh browser pengguna yang kemudian server tersebut akan merespons dengan memberikan satu atau lebih cookie ke browser. Setelah menerima cookie, browser akan menyimpannya, sehingga setiap kali _request_ dibuat ke server, browser akan mengirimkan cookie ke server sampai kadaluwarsanya habis. Saat sudah kadaluwarsa cookie tersebut akan dihapus dari browser.
    
    
 4. **Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**

    Pada umumnya, penggunaan cookies untuk mengelola data sesi pengguna kurang aman, sebab bisa saja informasi-informasi yang disimpan disalahgunakan. Beberapa porensial resiko yang haris diwaspadai, yaitu:
    - Melacak aktivitas pengguna dan menyimpan data pengguna tanpa izin.
    - _Session fixation_ dan _session hijacking_ yang mana memaksa pengguna untuk menggunakan _session id_ penyerang,
    - Menerima _cookies_ dari situs palsu atau sumber yang tidak kredibel: dapat terkena tindakan _phising_.
    - Memiliki _cookies_ dengan waktu kadaluwarsa yang panjang: berbahaya sebab dapat diretas oleh pihak ketiga.

    Jika ingin lebih aman, sebaiknya _cookies_ tidak digunakan secara langsung untuk mengelola semua informasi pengguna. Gunakan _session id_ yg unik sebagai data yang dikirim pada _cookies_ agar lebih aman.

**5. Cara pengimplementasian checklist:**
* Pertama saya membuat 3 fungsi baru, yaitu:
  - register untuk membuat akun. Di dalamnya menggunakan UserCreationForm Django untuk menangani pembuatan akun baru.
  - login_user untuk proses login. Di dalamnya saya menggunakan function _authenticate_ dan _login_ yang diimport dari Django untuk menghandle autentikasi dan login saat autentikasi berhasil.
  - logout_user untuk logout dari halaman utama.
* Membuat berkas register.html dan login.html untuk tampilan login dan registernya. Dan menambahkan tampilan tombol logout di berkas main.html.
* Membuat routing tampilan login, logout, dan register.
* Merestriksi akses halaman Main agar login terlebih dahulu dengan menambahkan kode @login_required(login_url='/login') di atas fungsi show_main.
* Setelah menjalankan runserver, saya membuat dua akun baru di section register. Berikut akunnya:
   - uname1: syifakaffa; pass: pbpsyifa
   - uname2: syifakaffa1; pass: pbpsyifa1

* Menghubungkan model Product dengan User:
  - Mengimport modul User dari django.contrib.auth.models, lalu menambahkan model user ke class Product dengan menggunakan code _user = models.ForeignKey(User, on_delete=models.CASCADE)_
  - Mengedit fungsi create_product agar Django tidak langsung menyimpan objek yg di buat ke database.
  - Mengubah fungsi show_main pada bagian 'name' agar yang muncul merupakan username yang sedang login.
  - Melakukan makemigration dan migrate.
* Mengimpor date time. Lalu di login_user membuat fungsi baru yang dapat menambahkan cookie.
  - Menambahkan _last_login_ pada show_main
  - Mengubah _logout_user_ untuk menghapus cookie setiap kali logout
  - Menambahkan teks last login pada main.html agar muncul di tampilan layar.

* Membuat Soal Bonus:
  - Membuat fungsi add_one dan dec_one di views.py yang tidak jauh berbeda kode nya. Pertama saya mencari product berdasarkan id yang tombolnya dipencet. Lalu menambahkan logika pengurangan atau pengurangan didalamnya.
  - Membuat routing url add_one dan dec_one.
  - Membuat tampilan tombolnya di main.html
  - Membuat fungsi delete_product di views.py yang tidak jauh berebeda dengan add_one dan dec_one. Hanya berbeda di bagian product.save() tidak dibuat pada delete product.
  - Membuat routing url delete_product di urls.py dan membuat tampilan tombolnya di main.html.
 
    
# TUGAS 3

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
* Saya juga sedikit mengedit main.html agar tampilan tabel diberi border untuk setiap selnya. Bagian ini saya tambahkan di bagian style. 
* Membuat input form untuk menambahkan objek model pada app sebelumnya.
    - Membuat file forms.py yang bisa menerima data produk baru dengan modelnya *Product* dan fieldsnya ada *name*, *available amount*, *price*, dan *description*.
    - Pada file views.py di main, saya membuat fungsi *create_product* dengan request method nya POST, agar data otomatis tersimpan saat di submit formnya.
* Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
    - Mengimport HttpResponse dan serializers.
    -HTML: Fungsi show_main yang sebelumnya, saya tambahkan *products* pada *context* yang berisi semua object yang diinput pada form. Untuk mengambil semua objectnya, saya menggunakan *Product.objects.all()*.
    - XML: membuat fungsi *show_xml* yang dapat menerima request dan akan mereturn HttpResponse dengan parameter seperti berikut: 
    ```def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    - JSON (show_json): sama seperti xml, hanya saja pada bagian serializers dan content_type diubah menjadi json.
    - JSON dan XML by id: mirip seperti tanpa id, tetapi object yang dicari difilter berdasarkan id. Kodenya hanya berbeda di bagian *data = Product.objects.filter(pk=id)*. 
* Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
    - Mengimpor 4 fungsi yang sebelumnya dibuat dan menambahkan 4 path URL (HTML sudah dilakukan di tugas 2) di urls.py bagian urlpatterns untuk keempat fungsi yang baru ditambahkan pada views.py sebelumnya.


5. Screenshot dari hasil akses URL pada Postman
* Format HTML
  <img width="960" alt="Screenshot 2023-09-18 153053" src="https://github.com/syifakaffa/smart-waroeng/assets/124903174/b19c31bc-5c78-4bba-8845-59d56b772b07">

* Format JSON
  <img width="960" alt="Screenshot 2023-09-16 235358" src="https://github.com/syifakaffa/smart-waroeng/assets/124903174/078abe84-96f5-41c5-9c4c-4bcab1e484e8">

* Format XML
  <img width="960" alt="Screenshot 2023-09-16 235350" src="https://github.com/syifakaffa/smart-waroeng/assets/124903174/8a9acd1c-eb4c-48d1-8122-25c55d265fa0">

* Format XML by Id
  <img width="960" alt="Screenshot 2023-09-16 235425" src="https://github.com/syifakaffa/smart-waroeng/assets/124903174/20df171f-e1d4-4da8-93ce-5ed3ac2ceee3">

* Format JSON by Id
  <img width="960" alt="Screenshot 2023-09-16 235411" src="https://github.com/syifakaffa/smart-waroeng/assets/124903174/d877e23c-5b97-4563-800a-ed983f371c9b">



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

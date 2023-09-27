TUGAS 4
1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Jawab:
UserCreationForm adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web Anda tanpa harus menulis kode dari awal.

Kelebihan:
- Mudah digunakan dan cepat diimplementasikan.
- Validasi otomatis untuk mengurangi kesalahan input.
- Dukungan untuk integrasi dengan sistem otentikasi Open Authorization.
- Fleksibilitas untuk penyesuaian tampilan dan perilaku.

Kekurangan:
- Keterbatasan kustomisasi untuk proyek yang lebih kompleks.
- Bergantung pada model User bawaan Django.
- Tampilan bawaan mungkin memerlukan penyesuaian desain.
- Mungkin memerlukan penyesuaian tambahan untuk UI atau logika bisnis yang kompleks.

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Jawab:
Autentikasi di Django adalah proses verifikasi identitas pengguna, memastikan bahwa mereka adalah siapa yang mereka klaim. Sementara otorisasi adalah tentang mengendalikan izin akses pengguna terhadap berbagai sumber daya dan fitur dalam aplikasi. Autentikasi melindungi akun pengguna, sementara otorisasi melindungi data dan fitur dari akses yang tidak diizinkan. Kedua konsep ini bersama-sama menciptakan sistem keamanan yang kokoh dalam aplikasi Django, memastikan bahwa hanya pengguna yang sah dengan izin yang sesuai yang dapat mengakses dan berinteraksi dengan sumber daya aplikasi.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Jawab:
Cookie HTTP (juga disebut cookie web, cookie Internet, cookie browser, atau cookie sederhana) adalah sepotong kecil data yang dikirim dari situs web dan disimpan di komputer pengguna oleh browser web pengguna saat pengguna berselancar.

Teknologi ini dirancang untuk menjadi mekanisme andal bagi situs web untuk mengingat informasi stateful (seperti barang yang ditambahkan dalam keranjang belanja di toko online) atau untuk merekam aktivitas penelusuran pengguna.

Mereka juga dapat digunakan untuk mengingat potongan informasi dan data yang sebelumnya dimasukkan pengguna ke dalam bidang formulir seperti nama, alamat, kata sandi, dan nomor kartu kredit.

Sebuah situs biasanya akan memberikan notifikasi terkait penggunaan cookie ketika pengguna baru mengunjungi web tersebut. Pengguna bisa mengelola cookie sesuai dengan keinginannya melalui pengaturan browser.

Berikut adalah beberapa kegunaan & fungsi cookies :
- Menyimpan informasi login
- Menyimpan pengaturan website
- Menyediakan konten lebih personal
- Menampilkan iklan
  
Langkah-langkah Django menggunakan cookies untuk mengelola sesi pengguna:
- Konfigurasi Settings: Pada settings.py, pastikan 'django.contrib.sessions.middleware.SessionMiddleware' sudah ada dalam daftar middleware.
- Cookies Sesi: Ketika pengguna pertama kali mengunjungi situs web Django Anda, server akan menghasilkan cookie sesi khusus yang akan dikirim ke peramban pengguna. Cookie ini berisi identifikasi unik sesi pengguna, biasanya berupa string panjang.
- Penyimpanan Data Sesi: Data sesi pengguna sebenarnya disimpan di sisi server, biasanya dalam database atau dalam penyimpanan cache yang dapat dikonfigurasi. Django memiliki pengaturan untuk mengonfigurasi penyimpanan sesi.
- Penggunaan Cookies: Setiap kali pengguna membuat permintaan selanjutnya ke server, cookie sesi akan dikirim bersama permintaan. Server kemudian akan mengidentifikasi sesi pengguna berdasarkan nilai unik dalam cookie tersebut.
- Mengakses Data Sesi: Kita dapat mengakses dan memanipulasi data sesi pengguna dengan mudah di tampilan Django menggunakan objek request.session. Ini adalah cara yang aman untuk menyimpan data sesi pengguna karena data sesi sebenarnya tidak ada di sisi klien.
- Kadaluwarsa Sesi: Django akan mengatur masa berlaku sesi secara otomatis. Kita dapat mengkonfigurasi berapa lama sesi akan berlangsung dengan mengatur SESSION_COOKIE_AGE dalam pengaturan (settings.py).

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Jawab:
Penggunaan cookies dalam pengembangan web bisa aman, tetapi ada risiko yang perlu diwaspadai. Berikut adalah beberapa risiko potensial yang perlu diwaspadai saat menggunakan cookies:
- Pelanggaran Privasi: Cookies dapat digunakan untuk melacak perilaku pengguna di situs web, dan jika data pribadi atau sensitif disimpan dalam cookies, ada potensi pelanggaran privasi. Oleh karena itu, sangat penting untuk melindungi data pribadi pengguna dan hanya menyimpan data yang diperlukan.
- Cross-Site Scripting (XSS): Jika cookies digunakan untuk menyimpan data yang diambil dari input pengguna tanpa penyaringan yang tepat, maka aplikasi Anda dapat rentan terhadap serangan XSS. Dalam serangan XSS, penyerang dapat mencoba mencuri cookies pengguna atau menjalankan kode berbahaya di perangkat pengguna.
- Session Hijacking: Cookies yang digunakan untuk mengidentifikasi sesi pengguna (session cookies) harus dijaga dengan baik. Jika sesi pengguna dapat diambil alih (hijacked), penyerang dapat mengakses akun pengguna tanpa izin.
- Cookies yang Tidak Aman: Pengaturan cookie yang tidak aman, seperti mengizinkan cookie berjalan melalui HTTP tanpa enkripsi SSL/TLS, dapat membuka peluang bagi penyerang untuk mengambil alih atau mencuri cookies.
- Penyimpanan Berlebihan: Penyimpanan berlebihan atau penggunaan cookies yang tidak perlu dapat memperlambat kinerja situs web dan membebani pengguna.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab:
Saya membaca dan mempelajari tutorial 3 lalu sayaa juga mencari tahu lebih lanjut tentang register, login dan logout dan membaca laman web https://ordinarycoders.com/blog/article/django-user-register-login-logout, kemudian saya juga membaca penjelasan-penjelasan tentaang Cookies dan Session https://www.dcs.gla.ac.uk/~leif/di/tutorial/cookie.html, emudian barulah saya mengimplementasikannya pada tugas 4 PBP ini.

   
TUGAS 3
1. Apa perbedaan antara form POST dan form GET dalam Django?
   POST akan mengirimkan data/nilai langsung ke file lain untuk ditampung tanpa menampilkan pada URL (umumnya digunakan untuk mengirimkan data penting seperti password dan data pribadi), sementara GET akan menampilkan data/nilai pada URL, kemudian ditampung oleh file lain
   
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- XML adalah adalah bahasa markup yang digunakan untuk mendefinisikan struktur data secara hierarkis. XML sering digunakan untuk pertukaran data antara aplikasi dan sistem yang berbeda, terutama dalam lingkungan yang lebih kompleks seperti aplikasi bisnis dan web services.
  
- JSON adalah format pertukaran data ringan yang terinspirasi oleh sintaksis objek JavaScript. SON lebih mudah dibaca oleh manusia daripada XML karena memiliki sintaksis yang lebih sederhana dan mirip dengan bahasa pemrograman.
  
- HTML adalah bahasa markup yang digunakan untuk membuat halaman web dan menampilkan konten di browser web. HTML memiliki sejumlah elemen bawaan yang digunakan untuk mendefinisikan struktur konten, seperti paragraf, heading, daftar, tabel, dan lainnya. 

Perbedaan utama ketiganya : XML digunakan untuk mendefinisikan struktur data dan pertukaran data antar aplikasi. JSON digunakan untuk pertukaran data ringan antar aplikasi, terutama di lingkungan web. Sementara HTML digunakan untuk membuat tampilan dan konten halaman web yang dapat diakses oleh pengguna melalui browser.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
   JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki banyak kelebihan sebagai berikut:
   - JSON memiliki format teks yang sederhana, yang membuatnya mudah dibaca oleh manusia dan mudah dipahami oleh mesin.
   - JSON mendukung berbagai jenis data, termasuk objek dan array, sehingga dapat digunakan untuk merepresentasikan data yang kompleks.
   - Dalam aplikasi web modern, seringkali hanya sebagian kecil data yang perlu diperbarui, bukan seluruh halaman. JSON memungkinkan pembaruan parsial dengan mudah, yang membantu mengurangi beban server dan meningkatkan responsivitas aplikasi.
   - JSON tidak hanya digunakan dalam lingkungan JavaScript, tetapi juga dapat diakses dan dimengerti oleh banyak bahasa pemrograman lainnya.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   - Membuat input form untuk menambahkan objek model pada app sebelumnya.
   Jawab:
   Saya membaca dan memahami materi yang ada pada tutorial kemudian saya juga mempelajari mengenai form dari https://docs.djangoproject.com/en/4.2/topics/forms/ kemudian setelah saya mengerti, baru saya tambahkan pada projek tugas saya

   - Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
   Jawab:
   Saya membaca dan memahami materi yang ada pada tutorial kemudian saya juga mempelajari mengenai form dari https://docs.djangoproject.com/en/4.2/topics/http/views/ kemudian setelah saya mengerti, baru saya tambahkan pada projek tugas saya

   - Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
   Jawab:
   Saya membaca dan memahami materi yang ada pada tutorial kemudian saya juga mempelajari mengenai form dari https://docs.djangoproject.com/en/4.2/topics/http/urls/ kemudian setelah saya mengerti, baru saya tambahkan pada projek tugas saya

5. Screenshot Postman
   ![Alt text](Markdown/main.png)
   ![Alt text](Markdown/xml.png)
   ![Alt text](Markdown/json.png)
   ![Alt text](Markdown/xml:1.png)
   ![Alt text](Markdown/xml:2.png)
   ![Alt text](Markdown/json:1.png)
   ![Alt text](Markdown/json:2.png)
   
TUGAS 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab:
Saya membaca dan memahami terlebih dahulu berkas tutorial, saya juga mencari tahu hubungan antara tiap file pada project Django (seperti urls.py, view.py, models.py, dll.), kemudian baru saya mengimplementasikan apa yang sudah saya pelajari ke dalam aplikasi Inventory ini untuk Tugas 2 PBP

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 
Jawab:
![Alt text](Markdown/bagan.png)
- Client mengirimkan permintaan HTTP ke server Django
- urls.py (routing)
   Permintaan dari client masuk ke dalam berkas urls.py dan kemudian URL yang diterima dihubungkan dengan fungsi tampilan yang sesuai
- view.py (controller)
   Pada file views.py berisi logika aplikasi untuk memproses permintaan. Fungsi views ini berinteraksi dengan models.py untuk memodifikasi data dalam database
- models.py (Model)
   Pada models.py terdapat struktur data aplikasi dan tersedia metode untuk berinteraksi dengan database.
- HTML (template)
   Jika berupa respon, File HTML akan di-render sebagai tampilan yang akan diberikan kepada client.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab:
Virtual environment adalah sebuah tool untuk membuat suatu lingkungan virtual untuk project python yang terisolasi dari project lainnya. Misalnya kita mempunyai 2 project python dan masing-masing membutuhkan suatu paket yang sama dengan versi yang berbeda. Kita dapat membuat aplikasi Django tanpa menggunakan virtualenv tetapi dengan memakai virtual environment, kita bisa mengisolasi environment development kita dan menginstall paket yang dibutuhkan suatu project tanpa bentrok dengan project lainnya.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Jawab:
- MVC (Model-View-Controller) 
    Model -> Berisi logika bisnis & status data yang ada dalam aplikasi. Bertugas mendapatkan dan memanipulasi data, berkomunikasi dengan Controller dan database, dll.

    View -> Tampilan grafis dari data yang diberikan oleh Model. View bekerja sama dengan Controller untuk menciptakan tampilan dinamis pada aplikasi.

    Controller -> Komunikasi antara View dan Model. Menangani inpuy pengguna, memproses permintaan, dll.

- MVT (Model-View-Template)
    Model -> Sama seperti Model pada MVC

    View -> Tampilan yang menggambarkan data dari Model, tetapi dalam konteks Django, View dalam MVT lebih mirip Controller pada MVC

    Template -> Tampilan HTML yang memiliki kode template Django yang digunakan untuk mengisi kontennya dengan data dari Model. Mirip View pada MVC.

- MVVM (Model-View-ViewModel)
    Model -> Sama seperti MVC dan MVT

    View -> Antarmuka grafis antara penggunaa & pola desain serta menampilkan output dari data yang telah diproses.

    ViewModel -> Berisi logika bisnis serta tampilan data yang akan ditampilkan View. Menghubungkan Model dengan View.

    Perbedaan antara ketiganya : MVC adalah pola desain yang lebih umum & fleksibel, MVT modifikasi MVC yang menggunakan template Django, sementara MVVM adalah pola desain yang lebih fokus kepada UI yang kompleks dan menggunakan ukuran kode yang besar.
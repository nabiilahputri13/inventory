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
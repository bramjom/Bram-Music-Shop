## Tugas 2
# Nama Repository : Bram-Music-Shop

**Abraham Jordy Ollen**
**NPM : 2306275102**
**----------------------------------------------------------------------------------------------------------------------------------------**

### 1) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

##### Checkpoint 1 : Membuat sebuah proyek Django baru

1. Awal-awal, saya membuat  _repository_ baru di Github bernama sama yaitu `Bram-Music Shop` dengan visibility _public_.
2. Buatlah sebuah direktory lokal baru bernama `Bram-Music Shop`, sesuai nama repo, di komputer
3. Dalam direktory baru tersebut, buka _command prompt_ (Windows)
4. Buatlah _virtual enviroment_ menggunakan python dengan command :
   ```bash
   python -m venv env
   ```
5. Lalu, aktifkan _virtual environement_ dengan command :
   ```bash
   env\Scripts\activate
   ```
6. _Virtual environment_ akan aktif yang ditandai (env) di awal baris input terminal
7. Buatlah file dengan nama `requirements.txt` di dalam direktori yang sama dan tambahkan beberapa _dependencies_ berikut di file tersebut :
   ```text
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```
8. Melakukan instalansi _dependencies_ pada `requirements.txt` dengan command :
   ```python
   pip install -r requirements.txt
   ```
9. Buatlah proyek Django baru dengan nama `bram_music_shop` dengan command :
   ```bash
   django-admin startproject bram_music_shop .
   ```

- Note : Pastikan `.` tertulis dalam baris command

10. Ubahlah isi variabel `ALLOWED_HOSTS` di file `settings.py` dengan menambahkan kode berikut :
    ```python
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ...
    ```
11. Pastikan terdapat file `manage.py` pada direktori yang aktif pada terminal kamu saat ini. Lalu, jalankan _server_ Django dengan command berikut :
    ```bash
    python manage.py runserver
    ```
12. Buka link [http://localhost:8000](http://localhost:8000/) pada browser dan pastikan muncul gambar roket yang menandakan bahwa Django berhasil diinstal. 
13. Hentikan server dengan cara menekan `Ctrl+C` pada cmd.
14. Non aktifkan virtual environment (env) dengan command :
    ```bash
    deactivate
    ```

##### Checkpoint 2 : Membuat aplikasi dengan nama `main` pada proyek tersebut.

15. Buatlah aplikasi baru dengan nama **main** dengan menjalankan perintah berikut :
    ```bash
    python manage.py startapp main
    ```
16. Buka berkas `settings.py` di dalam direktori proyek `Bram_Music_Shop`.
17. Tambahkanlah `'main'` ke dalam variabel `INSTALLED_APPS` seperti contoh berikut :
    ```python
    INSTALLED_APPS = [
        ...,
        'main'
    ]
    ```

##### Checkpoint 3 : Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`

18. Bukalah berkas `urls.py` di dalam direktori proyek `Bram_Music_Shop`
19. Lakukan perubahan pada isi berkas tersebut seperti kode berikut:

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```

##### Checkpoint 4 : Membuat model pada aplikasi `main` dengan nama Product dan memiliki atibut wajib.

20. Di direktori `main`, bukalah berkas `models.py`
21. Isilah berkas `models.py` dengan kode berikut :

    ```python
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        description = models.TextField()
        price = models.IntegerField()
        quantity = models.IntegerField()

        @property
        def is_available(self):
            return self.quantity > 0
    ```

22. Melakukan migrasi model dengan menjalankan perintah berikut.
    ```bash
    python manage.py makemigrations
    ```
23. Menerapkan migrasi ke dalam basis data lokal dengan menjalankan perintah berikut.
    ```bash
    python manage.py migrate
    ```

##### Checkpoint 5 : Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ html yang menampilkan nama aplikasi serta nama dan kelas kamu.

24. Bukalah berkas `views.py` yang terletak pada direktori `main`.
25. Gantilah isi berkas tersebut dengan kode berikut :

    ```python
    from django.shortcuts import render

    def show_main(request):
    context = {
        'npm' : '2306275102',
        'name': 'Abraham Jordy Ollen',
        'class': 'PBP C'
    }

        return render(request, "main.html", context)
    ```

26. Buatlah direktori baru bernama `templates` dalam direktori `main`.
27. Di dalam direktori `templates`, buatlah berkas baru dengan nama `main.html`. Isi berkas `main.html` dengan kode berikut :

    ```html
    <h1>{{ app }}</h1>

    <h5>Name:</h5>
    <p>{{ name }}</p>
    <p></p>
    <h5>Class:</h5>
    <p>{{ class }}</p>
    <p></p>
    ```

##### Checkpoint 6 : Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

28. Buatlah berkas baru bernama `urls.py` di dalam direktori main.
29. Isi berkas tersebut dengan kode berikut :

    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

##### Checkpoint 7: Membuat _deployment_ ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-teman.

###### Untuk add, commit dan push ke GITHUB :

30. Lakukan inisiasi direktori lokal `Bram-Music Shop` sebagai repositori git dengan menjalankan perintah berikut pada terminal :
    ```bash
    git init
    ```
31. Kemudian, tandai semua _file_ yang berada pada direktori tersebut sebagai _file_ yang akan di-_commit (tracked)_ dengan perintah berikut :
    ```bash
    git add .
    ```
32. Lanjutkan membuat pesan _commit_ yang sesuai dengan perubahan atau pembaharuan dengan perintah berikut :
    ```bash
    git commit -m "<PESAN KAMU>"
    ```
33. Pastikan saat ini kamu berada pada branch _main_ dengan menjalankan perntah berikut :
    ```bash
    git branch -M main
    ```
34. Hubungkan repositori lokal (direktori saat ini) dengan repositori di Github kamu dengan perintah berikut :
    ```bash
    git remote add origin <URL_REPO>
    ```

- Note : ubah `<URL_REPO>` dengan url github yang baru kamu buat.

35. Kemudian, push seluruh berkas ke repositori github dengan perintah berikut :
    ```bash
    git push -u origin main
    ```

###### Untuk proses PWSnya:

36. Akses halaman PWS di https://pbp.cs.ui.ac.id/ , lalu buat akun baru atau daftar dengan menggunakan akun SSO kamu.
37. Setelah membuat akun baru, lakukan _login_ menggunakan akun yang baru saja kamu buat.
38. Buatlah proyek baru dengan mengklik tombol `Create New Project`. Kamu akan berpindah ke halaman untuk membuat proyek baru. Masukkan `Project Name` dengan "brammusicshop". Setelah itu, tekan tombol `Create New Project` 
39. Simpan informasi _Project Credentials_ dengan aman dan jangan sampai hilang karena digunakan di langkah selanjutnya. 
40. Perbarui berkas `settings.py` di proyek Django kamu, tambahkan URL _deployment PWS_ pada variabel `ALLOWED_HOSTS` seperti kode berikut :
    ```python
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", <NAMA DEPAN>-<NAMA TENGAH>-brammusicshop.pbp.cs.ui.ac.id]
    ...
    ```

- Note : ganti `<NAMA DEPAN>` dan `<NAMA TENGAH>` sesuai akun SSO kamu. Dalam kasus saya : abraham-jordy-brammusicshop.pbp.cs.ui.ac.id .

41. Jalankan perintah berikut untuk melakukan push repositori lokal ke PWS kamu (jalankan satu per satu tiap baris) :

    ```bash
    git remote add pws http://pbp.cs.ui.ac.id/<USERNAME PWS>/brammusicshop

    git branch -M master

    git push pws master
    ```

42. Setelah menjalankan perintah tersebut, kamu akan diminta `username` dan `password`. Gunakan _Project Credentials_ yang telah kamu simpan (ingat kembali langkah 45).
43. Setelah menjalankan perintah tersebut, silahkan kembalikan branch ke main dengan perintah berikut :
    ```bash
    git branch -M main
    ```
44. Cari proyek kamu di laman PWS, kemudian cek statusnya. Jika status `Building` maka tunggu beberapa saat hingga status berubah menjadi `Running`.
45. Jika sudah `Running`, silahkan tekan tombol `View Project` lalu copy linknya dan buka di aplikasi Google Chrome. Pastikan https:// diganti dengan http:// pada link tersebut.

### 2) Bagan _request client_ ke web pada Django

![Bagan request & response Django](https://cdn.discordapp.com/attachments/1282940035523412013/1282940064686669865/image.png?ex=66e12e8b&is=66dfdd0b&hm=ea5452752c20044eb35237c588e15d8ca7f1792af8621bbb4d3757590ed12742&)

Diagram di atas menunjukkan alur request-response dalam sebuah aplikasi web berbasis Django. Berikut penjelasan mengenai hubungan antara urls.py, views.py, models.py, dan file HTML dalam proses ini:

Permintaan dari Klien: Proses dimulai dengan klien (misalnya, browser atau aplikasi lain) yang mengirimkan permintaan ke server Django.
urls.py: File ini berfungsi sebagai pengatur rute (routing) dalam aplikasi Django. urls.py menentukan URL mana yang perlu dipanggil dan tampilan (view) mana yang bertanggung jawab. Saat permintaan diterima, Django mencocokkan URL tersebut dengan pola yang ada di urls.py.
views.py: Setelah URL yang sesuai ditemukan, kontrol diberikan kepada fungsi atau kelas di views.py. Tugas view adalah memproses data yang diterima dan mengirimkan respons yang tepat kepada klien, yang sering kali melibatkan pengambilan data dari database melalui model.
models.py: View dapat berinteraksi dengan models.py untuk mendapatkan data dari basis data. File model ini berperan dalam mendefinisikan struktur data dan menyediakan alat untuk mengelola database, seperti mengakses, menambah, atau memodifikasi data.
Database: Database digunakan untuk menyimpan informasi yang dapat diakses, ditambahkan, atau diperbarui berdasarkan kebutuhan.
models.py: Data yang diambil dari database kemudian dikembalikan ke models.py, yang akan meneruskannya kembali ke view di views.py.
views.py: Setelah menerima data dari model, view mengolah informasi tersebut dan mempersiapkan respons (biasanya berupa file HTML) untuk dikirim ke klien.
Template HTML: Template HTML diisi dengan data yang diberikan oleh view dan diubah menjadi HTML yang lengkap dan siap dikirimkan ke klien.
Respon ke Klien: HTML yang telah diproses kemudian dikirim kembali ke klien sebagai tanggapan atas permintaan yang diajukan sebelumnya.

### 3) Jelaskan fungsi git dalam pengembangan perangkat lunak
Git adalah sistem kontrol versi terdistribusi yang sangat penting dalam pengembangan perangkat lunak. Fungsi utamanya adalah membantu tim atau individu dalam melacak perubahan yang terjadi pada kode sumber proyek selama siklus pengembangan. Berikut beberapa fungsi utama Git dalam pengembangan perangkat lunak:

**1. Pelacakan Perubahan (Version Control)**
Git memungkinkan pengembang melacak setiap perubahan yang dilakukan pada file proyek, seperti penambahan, penghapusan, atau modifikasi. Setiap perubahan disimpan dalam bentuk komit yang dapat dirujuk kembali. Ini memungkinkan pengembang untuk melihat versi lama dari proyek, membandingkan perubahan, dan mengembalikan versi sebelumnya jika diperlukan.

**2. Kolaborasi Tim (Collaborative Development)**
Git memungkinkan banyak pengembang untuk bekerja pada proyek yang sama secara bersamaan. Dengan sistem kontrol versi terdistribusi, setiap pengembang dapat bekerja di cabang (branch) yang terpisah dan menggabungkan (merge) perubahan mereka ke cabang utama. Ini membantu menghindari konflik ketika banyak pengembang bekerja pada file yang sama.

**3. Branching dan Merging**
Fitur branching pada Git memungkinkan pengembang membuat cabang yang terisolasi dari cabang utama untuk mengerjakan fitur baru, memperbaiki bug, atau bereksperimen tanpa mempengaruhi kode produksi. Setelah selesai, mereka bisa menggabungkan perubahan mereka ke cabang utama menggunakan merging, yang membantu menjaga integritas dan stabilitas kode utama.

**4. Manajemen Proyek**
Git juga mendukung manajemen proyek dengan menyediakan alat untuk pengembang mengelola tugas-tugas pengembangan seperti issue tracking dan code review. Misalnya, pada platform seperti GitHub atau GitLab, pengembang dapat menghubungkan perubahan kode dengan masalah tertentu, mempermudah pengelolaan fitur dan bug.

**5. Backup dan Pemulihan (Backup and Recovery)**
Karena Git menyimpan riwayat lengkap dari setiap perubahan dalam proyek, ia juga berfungsi sebagai cadangan (backup) yang komprehensif. Jika ada kesalahan atau perubahan yang tidak diinginkan, pengembang dapat mengembalikan proyek ke keadaan yang benar sebelumnya.

**6. Distribusi Kode (Distributed System)**
Git bersifat terdistribusi, yang berarti setiap pengembang memiliki salinan lengkap dari repositori di komputer mereka. Hal ini memungkinkan pengembang untuk bekerja secara offline dan melakukan komit lokal, kemudian mensinkronisasikan perubahan dengan repositori utama ketika koneksi tersedia.

**7. Continuous Integration dan Deployment (CI/CD)**
Git sering diintegrasikan dengan alat CI/CD untuk memungkinkan otomatisasi dalam pengujian, kompilasi, dan penerapan perangkat lunak. Setiap kali ada komit yang masuk ke repositori, alat CI/CD dapat memicu pengujian otomatis, membangun aplikasi, dan bahkan menerapkan aplikasi ke server produksi.

**8. Auditing dan Pelacakan Kode**
Dengan Git, pengembang dapat melihat siapa yang membuat perubahan tertentu pada kode dan kapan perubahan tersebut dilakukan. Ini sangat penting dalam audit dan analisis sejarah proyek untuk memastikan kualitas dan keamanan kode.

**Kesimpulan**
Secara keseluruhan, Git adalah alat yang sangat penting dalam pengembangan perangkat lunak modern. Dengan fitur version control, kemampuan kolaborasi, dan manajemen proyek, Git memberikan fleksibilitas dan efisiensi yang besar bagi pengembang dan tim perangkat lunak, baik dalam proyek kecil maupun proyek skala besar.

### 4) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Bagi saya, Django sering dipilih sebagai framework awal dalam pembelajaran pengembangan perangkat lunak karena menawarkan banyak keunggulan. Django hadir dengan banyak fitur bawaan yang memungkinkan pemula langsung memulai tanpa harus melakukan konfigurasi rumit. Struktur arsitektur Model-View-Template (MVT) yang terorganisir dengan baik memudahkan pemula memahami bagaimana logika, data, dan tampilan dipisahkan dalam pengembangan aplikasi. Selain itu, Django menggunakan bahasa Python yang dikenal mudah dipelajari, menjadikannya pilihan tepat untuk pengembang baru. Dokumentasi Django sangat lengkap dan ramah bagi pemula, sehingga membantu mereka memahami konsep-konsep pengembangan dengan lebih cepat. Django juga mengajarkan praktik terbaik, seperti prinsip Don’t Repeat Yourself (DRY), yang mendorong efisiensi dan kode yang bisa digunakan kembali. Keamanan aplikasi juga dijaga dengan fitur bawaan yang melindungi dari berbagai jenis serangan umum. Dengan komunitas besar dan aktif, Django menawarkan dukungan yang kuat, sehingga pemula dapat dengan mudah mengakses berbagai sumber pembelajaran tambahan. Semua ini menjadikan Django pilihan ideal bagi mereka yang baru memulai perjalanan dalam pengembangan perangkat lunak.

## 5) Mengapa model pada Django disebut sebagai ORM?
Fungsi model ORM (Object-Relational Mapping) pada Django adalah untuk menghubungkan tabel-tabel di basis data relasional dengan objek-objek dalam kode Python. Ini memungkinkan pengembang bekerja dengan data dalam bentuk objek Python tanpa menulis kueri SQL untuk mengelola basis data.

ORM pada Django secara teknis menerjemahkan tindakan atau operasi dari model (seperti menyimpan, mengambil, memperbarui, atau menghapus data) ke dalam perintah SQL yang sesuai untuk berinteraksi dengan database, memungkinkan pengembang mengelola database menggunakan bahasa pemrograman yang mereka gunakan (Python), tanpa harus mempelajari atau menangani detail SQL. Dengan kata lain, ORM memberikan abstraksi antara kode program dan database.


**----------------------------------------------------------------------------------------------------------------------------------------**
## Tugas 2

### 1) Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena data merupakan bagian penting dari interaksi, proses, dan layanan yang disediakan oleh platform, pengiriman data sangat penting untuk pengoperasian platform. Berikut adalah beberapa alasan mengapa pengiriman data penting:

**Aksesibilitas Pengguna**: Pengiriman data memungkinkan pengguna mengakses layanan atau informasi yang mereka butuhkan dari platform secara cepat dan tepat waktu, tanpa adanya keterlambatan atau jeda.

**Keputusan Berbasis Data**: Pengiriman data yang cepat dan andal membantu pengambilan keputusan yang akurat berdasarkan data real-time; banyak platform, seperti platform media sosial atau e-commerce, bergantung pada analitik dan pengolahan data untuk memberikan wawasan yang lebih baik.

**Pengalaman Pengguna**: Kecepatan pengiriman data platform sangat penting untuk pengalaman pengguna yang baik; pengiriman data yang lambat pada platform streaming video akan menyebabkan buffering dan pengalaman pengguna yang buruk.

**Konektivitas Antar Komponen**: Dalam arsitektur platform yang terdistribusi, seperti cloud atau microservices, setiap komponen platform bergantung pada data yang dikirim oleh layanan lain. Pengiriman data yang handal menjamin integritas sistem dan kelancaran operasional seluruh komponen.

**Keamanan dan Kepatuhan**: Pengiriman data yang aman memastikan bahwa data sensitif dikirim dengan enkripsi dan metode perlindungan lainnya, mengurangi risiko kebocoran data, dan mematuhi peraturan seperti GDPR.

Platform tidak dapat beroperasi dengan baik tanpa data pengiriman yang baik, yang mengakibatkan kegagalan layanan dan ketidakpuasan pengguna.

### 2) Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Untuk beberapa tujuan, terutama dalam pengembangan web dan pertukaran data antara klien dan server, JSON (JavaScript Object Notation) dianggap lebih baik daripada XML. Ada beberapa poin keunggulan yang dapat saya rangkum dari JSON:

**Lebih Mudah Dibaca**: Data dalam JSON ditulis dalam format pasangan nilai kunci, mirip dengan objek JavaScript, sehingga lebih mudah dipahami oleh manusia.

**Ukuran Lebih Kecil**: JSON tidak memiliki tag pembuka dan penutup seperti XML, sehingga datanya lebih kecil dan lebih efisien untuk dikirim melalui jaringan.

**Integrasi dengan JavaScript**: Karena JSON merupakan subset dari JavaScript itu sendiri, sangat terintegrasi dengan JavaScript, sehingga pengembang web dapat bekerja dengan data JSON di browser tanpa perlu melakukan parsing manual.

**Parsing Lebih Cepat**: Banyak bahasa pemrograman dapat langsung parsing JSON dengan library bawaan, tetapi parser XML biasanya lebih kompleks, yang dapat memperlambat kinerja.

**Struktur Sederhana**: Format JSON lebih sederhana dan strukturnya lebih sederhana dibandingkan dengan XML yang bergantung pada hierarki tag, sehingga lebih mudah diolah dan digunakan untuk menyimpan data terstruktur.

### 3) Jelaskan fungsi dari method 'is_valid()' pada form Django dan mengapa kita membutuhkan method tersebut?
Pada form Django, metode is_valid() digunakan untuk memastikan bahwa data yang dimasukkan ke dalam form memenuhi semua validasi yang telah ditentukan. Untuk alasan berikut, peran ini sangat penting dalam proses penanganan form:

**Memeriksa Validitas Input**: Metode is_valid() menjalankan semua validasi yang ditetapkan di kolom formulir untuk memastikan bahwa data sesuai dengan tipe yang diharapkan (seperti email valid, angka dalam rentang yang diperbolehkan, dll.). Jika semua validasi berhasil dilewati, metode ini mengembalikan nilai True, yang menunjukkan bahwa data formulir valid.

**Menangani Data yang Divalidasi**: Jika form valid, is_valid() juga menyiapkan dan membersihkan data yang telah divalidasi. Anda dapat mengakses data yang telah divalidasi ini melalui atribut cleaned_data, yang menyimpan versi "bersih" input formulir, siap untuk digunakan untuk tujuan lain, seperti disimpan ke database atau diproses.

**Mengumpulkan Kesalahan**: Jika validasi gagal, is_valid() mengembalikan False, dan kesalahan validasi yang terjadi dapat diakses melalui atribut kesalahan. Ini memungkinkan pengembang untuk memberi umpan balik kepada pengguna tentang kesalahan input yang harus diperbaiki.

#### Untuk alasan apa metode is_valid() diperlukan?
**Validasi Form**: Validasi form sangat penting untuk memastikan bahwa data yang diterima aman dan sesuai dengan harapan aplikasi. Tanpa memanggil is_valid(), form tidak akan divalidasi, dan input pengguna mungkin mengandung data yang tidak valid atau berbahaya.

**Error Handling**: Metode is_valid() dapat secara efektif menangani kesalahan input, memastikan bahwa pengguna menerima pesan kesalahan yang relevan, dan form hanya diproses ketika inputnya valid.

### 4) Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Untuk melindungi aplikasi dari serangan *Cross-Site Request Forgery (CSRF)*, csrf_token diperlukan pada form Django. CSRF adalah jenis serangan di mana penyerang mencoba menipu pengguna untuk mengirimkan permintaan yang tidak sah ke server aplikasi tanpa pengetahuan pengguna.

#### Mengapa csrf_token diperlukan?
Token khusus yang disebut csrf_token dibuat untuk setiap sesi pengguna dan dimasukkan ke dalam formulir sebagai bagian dari proses validasi. Ketika formulir dikirimkan, token ini diverifikasi oleh server untuk memastikan bahwa permintaan berasal dari sumber yang sah, dalam hal ini dari pengguna yang sebenarnya melalui situs web yang sah.

#### Apa yang akan terjadi jika tidak ada csrf_token?
Tanpa csrf_token, aplikasi tidak dapat membedakan permintaan pengguna yang sah dari yang dibuat oleh pihak ketiga. Ini memungkinkan pencuri untuk mengirimkan permintaan palsu ke aplikasi yang berpotensi berbahaya melalui situs web lain, yang dapat menyebabkan perubahan data atau tindakan tidak diinginkan, seperti mengubah pengaturan pengguna atau melakukan transaksi tanpa izin.

#### Bagaimana Peretas Dapat Memanfaatkannya?
Karena browser korban secara otomatis mengirimkan cookies otentikasi ke server, penyerang dapat mengirimkan link atau kode berbahaya ke korban tanpa disadari jika form tidak dilindungi oleh csrf_token. 
Contoh serangan mungkin termasuk:

1. Transfer uang melalui aplikasi bank online tidak sah.
2. Mengubah profil data di aplikasi sosial.
3. Menghapus data atau melakukan operasi sensitif lainnya yang tidak diinginkan korban

Oleh karena itu, csrf_token sangat penting untuk melindungi form aplikasi Django dari serangan CSRF dan untuk menjaga keamanan form.


### 5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
##### Checkpoint 1 : Membuat input form untuk menambahkan objek model pada app sebelumnya 
Menambah line "from main.models import Product"
Jadi, keseluruhan program forms.py sebagai berikut:

    ```python
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description", "quantity"]
    ```

##### Checkpoint 2 : Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Menambahkan 4 fungsi pada views.py sebagai berikut :

    ```python
    def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type= "application/xml" )

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type= "application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

##### Checkpoint 3 : Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Menambah urlpatterns pada urls.py sebagai berikut:

    ```python
    path('json/', show_json, name = "show_json"),
    path('xml/', show_xml, name = "show_xml"),
    path('json/<int:id>/', show_json_by_id, name = "show_json_by_id"),
    path('xml/<int:id>/', show_xml_by_id, name = "show_xml_by_id"),
    ```

### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman
1.) xml/
(https://media.discordapp.net/attachments/817255852259672094/1285502956006936618/localhost8000_xml.png?ex=66ea816c&is=66e92fec&hm=69edfd1193c9f8f95ba30c7ac52fcc0dcdf06c55a2979702f5a3213c19e6803e&=&format=webp&quality=lossless&width=1314&height=655)

2.) json/
(https://media.discordapp.net/attachments/817255852259672094/1285503403627384886/localhost8000_json.png?ex=66ea81d6&is=66e93056&hm=32e3cdc1442a4b33e199ef1f99c12f8ca15951222f14a6f0592a80e7560b323a&=&format=webp&quality=lossless&width=1330&height=655)

3.) xml/<str:id>/
(https://media.discordapp.net/attachments/817255852259672094/1285503627561144353/localhost8000_xmlbyid.png?ex=66ea820c&is=66e9308c&hm=5be11402e8ea5f24be84c3cda7956d911cb5a1ea19da71a2e0eb205f717ecba0&=&format=webp&quality=lossless&width=1440&height=514)

4.) json/<str:id>/
(https://media.discordapp.net/attachments/817255852259672094/1285503764630868019/localhost8000_jsonbyid.png?ex=66ea822c&is=66e930ac&hm=860bc5659d994721a12c6b8854da0cb61ccdc7ebff59c55867938b1e1aae49eb&=&format=webp&quality=lossless&width=1341&height=655)











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
## Tugas 3

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



**----------------------------------------------------------------------------------------------------------------------------------------**
## Tugas 4

### 1) Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
`HttpResponseRedirect()` dan `redirect()` sama-sama digunakan di Django untuk mengarahkan pengguna ke URL lain, tetapi ada beberapa perbedaan antara keduanya:

**a. HttpResponseRedirect():**
- Ini adalah kelas respons HTTP yang secara eksplisit mengirimkan respons pengalihan (HTTP status code 302) ke URL yang diberikan.
- Penggunaannya mengharuskan kita untuk memberikan URL sebagai argumen, yang bisa berupa string URL absolut atau relatif.

    ```python
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect('/some-url/')
    ```
**b. redirect():**
- Ini adalah shortcut yang lebih fleksibel di Django, yang secara internal menggunakan 'HttpResponseRedirect()'.
- redirect() lebih pintar karena kita bisa memberikannya beberapa jenis argumen: URL string, model, atau bahkan nama pola URL (dengan atau tanpa argumen), dan Django akan menangani konversi ini menjadi URL.

    ```python
    from django.shortcuts import redirect
    return redirect('/some-url/')
    ```
**Kesimpulan** : `HttpResponseRedirect()` hanya menerima URL string, sedangkan `redirect()` lebih fleksibel dan bisa menerima pola URL, model, atau URL string.

### 2) Jelaskan cara kerja penghubungan model 'Product' dengan 'User'!

a.) Mengimpor model 'User'
    Pada file, `models.py` kita impor model `User` dari Django :
```python
from django.contrib.auth.models import User
```
    Nah, model `User` ini akan digunakan untuk mengasosiasikan setiap objek `Product` dengan seorang pengguna.

b.) Menambahkan relasi pada Model `Product`
```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
    - **ForeignKey(User, on_delete=models.CASCADE)** menyatakan bahwa setiap produk akan berhubungan dengan satu pengguna.
    - **on_delete=models.CASCADE** berarti jika pengguna dihapus, semua produk yang berhubungan dengan pengguna tersebut juga akan dihapus. 

c.) Menambahkan User pada Saat Menyimpan Produk
    Di `views.py`, ketika membuat produk baru, kita perlu memastikan bahwa produk tersebut terhubung dengan pengguna yang sedang login. Berikut adalah bagaimana kita melakukan modifikasi pada fungsi untuk menyimpan produk:
```python
def create_product(request):
form = ProductForm(request.POST or None)

if form.is_valid() and request.method == "POST":
    product = form.save(commit=False)
    product.user = request.user  # Menghubungkan produk dengan user yang login
    product.save()
    return redirect('main:show_main')

context = {'form': form}
return render(request, "create_product.html", context)
```
    
    - **form.save(commit=False)** menghentikan penyimpanan langsung ke database agar kita bisa menambahkan data lebih lanjut (dalam hal ini, menambahkan pengguna).
    - **product.user** = request.user menghubungkan produk dengan pengguna yang sedang login.

d.) Menampilkan Produk Berdasarkan Pengguna
    Untuk menampilkan produk yang dimiliki oleh pengguna yang sedang login, kita bisa menggunakan `filter` di fungsi `show_main`:
```python
def show_main(request):
    # Program lain ...
    product_entries = Product.objects.filter(user = request.user)
    context = {
        'name': request.user.username,
        'product_entries': product_entries,
        # Program lain ...
    }
```
    - **Product.objects.filter(user=request.user)** menyaring produk yang hanya terasosiasikan dengan pengguna yang sedang login.
    - Ini memastikan pengguna hanya melihat produk mereka sendiri, bukan produk dari pengguna lain.

e.) Menyimpan Perubahan dan Melakukan Migrasi
    Setelah mengubah model, kita perlu menjalankan migrasi untuk menerapkan perubahan ke database:
```python
python manage.py makemigrations
python manage.py migrate
```
    - Ketika diminta untuk memilih default value untuk field user yang baru, kita bisa memilih untuk mengatur pengguna default, misalnya user dengan ID 1.

f.) Mengubah Pengaturan `DEBUG` untuk Production
    Untuk mempersiapkan aplikasi untuk lingkungan produksi, tambahkan ini ke file `settings.py`:
```python
import os
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```
    - Ini mengaktifkan mode produksi jika variabel lingkungan `PRODUCTION` disetel ke `True`, yang umumnya digunakan saat aplikasi sudah dijalankan di server live.

Dengan langkah-langkah ini, kita berhasil menghubungkan model `Product` dengan `User`, memungkinkan produk dikaitkan dengan pengguna tertentu dan ditampilkan sesuai dengan pengguna yang login.

### 3) Apa perbedaan antara *authentication* dan *authorization*, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

**Perbedaan Utama:**
Autentikasi: **Memastikan bahwa pengguna adalah siapa** yang mereka klaim (identifikasi pengguna).
Autorisasi: **Menentukan apa yang diizinkan** pengguna lakukan setelah terautentikasi (hak akses).

**Apa yang terjadi setelah pengguna login?**
- Autentikasi : Saat pengguna login, sistem akan melakukan autentikasi terhadap pengguna. Jika pengguna memasukkan username dan password yang benar, mereka dianggap terautentikasi, dan sesi (session) biasanya dibuat untuk menjaga status login mereka.

- Autorisasi : Setelah autentikasi berhasil, autorisasi memutuskan apa yang diizinkan pengguna lakukan. Misalnya, seorang pengguna biasa mungkin dapat melihat dan mengedit profil mereka, tetapi hanya pengguna dengan peran admin yang bisa mengelola pengguna lain atau mengubah pengaturan penting.

**Implementasi Django**
a.) Autentikasi di Django
- Django menggunakan middleware session untuk mengelola autentikasi pengguna. Saat pengguna login menggunakan form login bawaan Django (`LoginView`), Django memeriksa kredensial pengguna melalui model User yang tersedia di `django.contrib.auth.models.User`.

- Django menggunakan metode authenticate() untuk memeriksa kredensial pengguna, dan jika cocok, `login()` digunakan untuk membuat sesi yang menandakan bahwa pengguna sudah berhasil terautentikasi.

Contoh :
```python
from django.contrib.auth import authenticate, login

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Pengguna berhasil login
    else:
        # Kredensial tidak valid
```

b.) Autorisasi di Django
- Django memiliki sistem permissions dan groups bawaan yang digunakan untuk mengelola autorisasi pengguna. Permission mengatur hak akses apa saja yang dimiliki oleh pengguna terhadap objek di sistem.
- Setiap model di Django dapat dikaitkan dengan permissions (seperti tambah, edit, hapus, atau lihat) yang menentukan apa yang boleh dilakukan oleh pengguna terhadap model tersebut.
- Django juga mendukung user roles melalui konsep groups, di mana sekelompok pengguna dapat diberikan hak akses tertentu.

Contoh:
```python
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('app_name.add_model_name', raise_exception=True)
def add_object(request):
    # Hanya pengguna yang terautentikasi dan memiliki izin untuk menambah objek yang dapat mengakses fungsi ini
```
- `@login_required`: Membatasi akses hanya kepada pengguna yang sudah login (terautentikasi).
- `@permission_required`: Membatasi akses berdasarkan izin tertentu (otorisasi). Misalnya, pengguna harus memiliki izin untuk menambah objek tertentu.

### 4) Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django menggunakan `session management` dan `cookies` untuk mengingat pengguna yang telah login.

a. Session (Sesi) Django:
- Setelah pengguna masuk, Django membuat sesi untuk mereka. Session adalah cara Django melacak informasi pengguna di antara berbagai permintaan HTTP. 
- Django secara otomatis menggunakan middleware session yang aktif secara default untuk membuat dan mengelola session. ID sesi disimpan dalam cookie pengguna browser.

b. Cookie :
- Django menggunakan cookie untuk menyimpan ID session pengguna di browser, yang berisi informasi yang menghubungkan pengguna dengan data session yang disimpan di server.

- Cookie default adalah sessionid, dan dikirim kembali ke server ketika pengguna membuat permintaan HTTP berikutnya.

- Django akan menggunakan cookie sessionid ini untuk mengambil data session yang sesuai dari server dan mengidentifikasi

- Dalam contoh sederhana : pengguna login ke Django dan membuat sesi → Django mengirimkan ID sesi ke browser sebagai cookie → browser menyimpan cookie tersebut. 

- Setiap kali pengguna mengakses halaman lain, cookie ID sesi dikirim bersama permintaan HTTP dan Django mengidentifikasi pengguna berdasarkan ID sesi tersebut.

**Kegunaan lain dari Cookies**
1. Menyimpan Preferensi Pengguna: Kita dapat menggunakan cookies untuk menyimpan preferensi pengguna seperti bahasa yang dipilih, tema (misalnya, gelap atau terang), atau item di keranjang belanja (misalnya, shopping cart).

2. Membuat Pengalaman Pengguna yang Lebih Baik: Situs web dapat memperbaiki pengalaman pengguna dengan menyimpan informasi pengguna di cookies. Jika cookie autentikasi masih berlaku, pengguna tidak perlu login setiap kali mereka mengunjungi situs web.

3. Pelacakan Aktivitas Pengguna (Tracking): Pengiklan sering menggunakan cookies untuk melacak aktivitas pengguna di berbagai situs web, memungkinkan mereka untuk menargetkan iklan berdasarkan perilaku pengguna. Cookies ini biasanya disebut sebagai cookies pihak ketiga karena dikelola oleh pihak ketiga (pengiklan) yang bukan bagian dari situs web yang dikunjungi oleh pengguna.

4. Mempertahankan Token Autentikasi: Selain itu, cookie dapat digunakan untuk menyimpan token autentikasi yang diberikan oleh server setelah login, seperti JWT—JSON Web Token, yang digunakan sebagai metode tambahan untuk memverifikasi identitas pengguna tanpa bergantung pada session.

**Apakah semua cookies Aman?**
1. Cookie Aman: Properti Secure memastikan bahwa cookie hanya dikirim melalui koneksi HTTPS yang aman, bukan HTTP yang tidak terenkripsi. Ini mencegah cookie dari bocor melalui koneksi yang tidak aman.

2. Cookie HttpOnly: Cookie dengan atribut HttpOnly tidak dapat diakses melalui JavaScript, sehingga mencegah serangan Cross-Site Scripting (XSS), di mana script berbahaya dapat mencoba mencuri cookie pengguna di situs web.

3. Cookie SameSite: Properti SameSite mengatur apakah cookie harus dikirim bersama permintaan dari domain yang berbeda untuk melindungi dari Cross-Site Request Forgery (CSRF). Sebagai contoh, pengaturan SameSite=Strict mencegah cookie dikirim ketika permintaan berasal dari domain luar.

4. Expiration/Max-Age: Cookies harus memiliki waktu kedaluwarsa atau usia maksimal untuk mencegah penyalahgunaan. Cookie yang tidak memiliki batas waktu yang jelas dapat tetap ada di browser pengguna untuk waktu yang lama, meningkatkan kemungkinan mereka jatuh ke tangan orang yang tidak bertanggung jawab.

5. Cookie Third-Party: Pengiklan sering menggunakan cookie third-party, yang merupakan cookie yang dibuat oleh domain yang berbeda dari situs yang sedang dikunjungi. Penyalahgunaan cookie jenis ini termasuk pelacakan pengguna tanpa izin, yang mengancam privasi mereka.

### 5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

a.)Registrasi Pengguna:
- Membuat fungsi `register` yang menghasilkan formulir pendaftaran menggunakan `UserCreationForm`.
- Setelah formulir di-submit dan valid, pengguna baru dibuat dan disimpan dalam database.
- Pesan sukses dikirimkan menggunakan messages, dan pengguna diarahkan ke halaman login.
- Menambahkan template `register.html` untuk menampilkan form registrasi.

b.)Login Pengguna:
- Membuat fungsi `login_user` yang menggunakan `AuthenticationForm` untuk mengautentikasi pengguna berdasarkan kredensial yang diberikan.
- Jika login berhasil, sesi pengguna dibuat menggunakan login(request, user) dan pengguna diarahkan ke halaman utama.
- Menambahkan template `login.html` untuk menampilkan form login, serta link ke halaman registrasi.

c.)Logout Pengguna:
- Membuat fungsi `logout_user` yang menggunakan logout(request) untuk menghapus sesi pengguna.
- Setelah logout, pengguna diarahkan kembali ke halaman login.
- Menambahkan tombol logout di halaman utama dan rute URL logout dalam `urls.py`.

Dengan langkah-langkah ini, sistem autentikasi lengkap termasuk registrasi, login, dan logout telah diimplementasikan dalam proyek Django.

#### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

a.) Mendaftar 2 akun dengan memencet tombol `register` di halaman main, dan menambah `Add new Product` sebanyak 3 models
Akun 1 :
username = bramjo
password = mungkin-iya
(https://media.discordapp.net/attachments/817255852259672094/1287778573838585856/image_2024-09-23_21-07-01_-.png?ex=66f2c8c1&is=66f17741&hm=a8dab3660b5d016f358c0df5b3b03ba0acf62eeed58cbfe34171b34b361eb5b4&=&format=webp&quality=lossless&width=643&height=655)


Akun 2 :
username = bramjo2
password = mungkin-tidak
(https://media.discordapp.net/attachments/817255852259672094/1287778574153027616/photo_2024-09-23_21-11-19.jpg?ex=66f2c8c1&is=66f17741&hm=727dac081d0e0cbe254d3c1d935f6609ba2396a7c47c6205d0144fa5af093694&=&format=webp&width=684&height=655)

#### Menghubungkan model `Product` dengan `User`.
1. Mengimpor Model `User`:
- Impor model `User` dari Django menggunakan:
```python
from django.contrib.auth.models import User
```

2. Menambahkan Relasi pada Model `Product`:
- Tambahkan `ForeignKey` pada model `Product` untuk menghubungkan setiap produk dengan seorang pengguna:
```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
``` 
- Relasi ini memastikan bahwa setiap produk terkait dengan satu pengguna, dan produk akan dihapus jika pengguna dihapus.

3. Menambahkan User pada Saat Menyimpan Produk:
- Pada `views.py`, modifikasi fungsi untuk menyimpan produk dengan menambahkan pengguna yang sedang login:
```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product.html", context)
```

4. Menampilkan Produk Berdasarkan Pengguna:
- Gunakan `filter` untuk hanya menampilkan produk milik pengguna yang login:
```python
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'product_entries': product_entries,
    }
```

5. Menyimpan Perubahan dan Melakukan Migrasi:
- Jalankan perintah berikut untuk menerapkan perubahan ke database:
```python
python manage.py makemigrations
python manage.py migrate
```

6. Pengaturan `DEBUG` untuk Production:
- Tambahkan pengaturan `PRODUCTION` di `settings.py` untuk mempersiapkan aplikasi di lingkungan live:
```python
import os
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```

#### Menampilkan detail informasi pengguna yang sedang *logged in* seperti *username* dan menerapkan *cookies* seperti last login pada halaman utama aplikasi.

Buka di *Inspect* pada browser, lalu buka tab *Application* kemudian Cookies

Berikut lampiran informasi kedua pengguna yang saya buat dan cookies yang ditampilkan :

(https://media.discordapp.net/attachments/817255852259672094/1287781781092696094/image.png?ex=66f2cbbe&is=66f17a3e&hm=e8ace3f4c32e0f3c93335b016396b206e754cecca9fee5b4b6276d9dd1f36105&=&format=webp&quality=lossless&width=1440&height=610)

(https://media.discordapp.net/attachments/817255852259672094/1287781960470495243/image.png?ex=66f2cbe9&is=66f17a69&hm=0aa3fc04d191c4952188f17c1ab926dcb70a9c223abda62af24fc7c91b9f713b&=&format=webp&quality=lossless&width=1440&height=613)


**----------------------------------------------------------------------------------------------------------------------------------------**
## Tugas 5

### 1)  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Dalam CSS, ketika terdapat beberapa selector yang berlaku pada elemen yang sama, urutan prioritas pengambilan CSS selector ditentukan oleh **spesifisitas** dan **aturan penting**. Berikut adalah urutan prioritas CSS selector dari yang terendah hingga yang tertinggi:

1. **Elemen Inline**: Jika style diterapkan langsung pada elemen HTML menggunakan atribut `style`, maka ini memiliki prioritas tertinggi kecuali ada aturan `!important`.

```html
<p style="color: red;">Text in red</p>
```

2. **Selector Tag/Elemen (Spesifisitas Rendah)**: Selektor yang langsung merujuk pada nama tag HTML, seperti `div`, `p`, atau `h1`.

```css
p { color: blue; }
```

3. **Selector Class (Spesifisitas Menengah)**: Selektor yang merujuk pada class tertentu dengan tanda titik (`.`), contohnya `.class-name`.

```css
.example { color: green; }
```

**Rumus Spesifisitas**
Spesifisitas dihitung menggunakan angka dengan urutan:

- *Inline style*: 1000
- *ID selector*: 100
- *Class, pseudo-class, attribute selector*: 10
- *Tag selector dan pseudo-element*: 1

CSS dengan spesifisitas lebih tinggi akan mengalahkan CSS dengan spesifisitas lebih rendah. Jika spesifisitasnya sama, aturan yang didefinisikan paling terakhir di dalam stylesheet akan digunakan.

### 2) Mengapa *responsive design* menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan *responsive design*!
*Responsive design* adalah salah satu konsep yang sangat penting dalam pengembangan aplikasi web adalah desain responsif, yang memungkinkan antarmuka web menyesuaikan diri secara otomatis dengan berbagai ukuran layar dan perangkat, seperti tablet dan perangkat seluler. Karena penggunaan berbagai ukuran layar semakin meningkat di perangkat ini, desain responsif memastikan pengalaman pengguna yang optimal di semua perangkat yang digunakan. Untuk beberapa alasan, responsif desain sangat penting karena :

1. **Peningkatan Pengalaman Pengguna (User Experience)**
Situs web dapat diakses dari berbagai perangkat dan ukuran layar. Tampilan web yang responsif tetap mudah digunakan dan nyaman dibaca baik di desktop maupun ponsel. Pengguna tidak perlu menggulir secara horizontal atau *zoom in/out* untuk melihat konten.

2. **Optimasi SEO (Search Engine Optimization)**
Mesin pencari, seperti Google, memprioritaskan situs yang responsif karena menawarkan pengalaman pengguna seluler yang lebih baik dan memiliki peringkat hasil pencarian yang lebih tinggi, meningkatkan visibilitas web.

3. **Efisiensi Pengembangan dan Pemeliharaan**
Pengembang dapat membuat situs yang responsif untuk berbagai perangkat daripada harus membuat situs desktop dan seluler terpisah. Ini menghemat waktu dan sumber daya selama pembangunan dan pemeliharaan.

#### Contoh Aplikasi yang Sudah Menerapkan Responsive Design:
- **Airbnb** : Airbnb menyediakan tampilan yang konsisten dan nyaman di berbagai perangkat, mulai dari desktop hingga ponsel. Pengguna dapat dengan mudah mencari akomodasi, membaca ulasan, dan memesan kamar dengan pengalaman yang mulus terlepas dari perangkat yang digunakan.

- **Spotify** : Spotify menggunakan responsive design untuk memberikan pengalaman pengguna yang optimal di browser web. Tata letak dan navigasi berubah secara otomatis sesuai dengan ukuran layar, baik di desktop maupun di ponsel.

#### Contoh Aplikasi yang Belum Menerapkan Responsive Design:
- **Situs Web Lama (Korporasi Kecil atau Situs Web Lama)** : Beberapa situs web bisnis kecil atau situs web lama yang belum diperbarui masih menggunakan desain tetap *(fixed layout)* yang tidak menyesuaikan dengan ukuran layar perangkat. Pengguna di perangkat seluler sering kali harus melakukan zoom atau menggulir secara horizontal, yang mengurangi kenyamanan.

- **Beberapa Portal Pemerintah Lama** :  Beberapa situs pemerintah yang belum diperbarui ke standar modern sering kali tidak responsif. Pengguna di perangkat seluler mengalami kesulitan dalam membaca informasi dan melakukan interaksi seperti mengisi formulir.

### 3) Jelaskan perbedaan antara *margin*, *border*, dan *padding, serta cara untuk mengimplementasikan ketiga hal tersebut!*
Dalam CSS, margin, border, dan padding adalah tiga properti yang digunakan untuk mengatur ruang di sekitar elemen. Berikut adalah penjelasan tentang masing-masing properti, serta bagaimana masing-masing digunakan:

1. **Padding**
- Definisi: Padding adalah ruang di dalam elemen, antara konten elemen dan tepi dalam border. Padding memberikan ruang antara konten dan batas elemen.
- Implementasi: Padding dapat diatur secara keseluruhan atau secara spesifik untuk setiap sisi elemen (atas, kanan, bawah, kiri)
- Contoh Implementasinya:
```css
.box {
  padding: 20px; /* Padding untuk semua sisi */
  padding-top: 10px;    /* Padding atas */
  padding-right: 15px;  /* Padding kanan */
  padding-bottom: 10px; /* Padding bawah */
  padding-left: 5px;    /* Padding kiri */
}
```

2. **Border**
- Definisi: Border adalah garis di sekitar padding dan konten elemen. Border berfungsi sebagai pembatas visual dari elemen.
- Implementasi: Border dapat diatur dengan warna, ketebalan, dan gaya (solid, dashed, dll.). Seperti padding, border juga bisa diatur untuk setiap sisi elemen.
- Contoh Implementasinya:
```css
.box {
  border: 2px solid black; /* Border di semua sisi */
  border-top: 3px dotted red;    /* Border atas dengan gaya dotted */
  border-right: 4px dashed blue; /* Border kanan dengan gaya dashed */
}
```
3. **Margin**
- Definisi: Margin adalah ruang di luar border elemen, yang digunakan untuk mengatur jarak antara elemen tersebut dengan elemen lain di sekitarnya. Margin memberikan ruang di luar elemen untuk memastikan elemen tidak terlalu rapat satu sama lain.
- Implementasi: Sama seperti padding dan border, margin juga dapat diatur untuk setiap sisi elemen.
- Contoh Implementasinya:
```css
.box {
  margin: 10px; /* Margin untuk semua sisi */
  margin-top: 20px;    /* Margin atas */
  margin-right: 15px;  /* Margin kanan */
  margin-bottom: 10px; /* Margin bawah */
  margin-left: 5px;    /* Margin kiri */
}
```

### 4) Jelaskan konsep *flex box* dan *grid layout* beserta kegunaannya!
Dua metode tata letak CSS modern, *Flexbox* dan *Grid Layout*, digunakan untuk merancang tampilan halaman web yang fleksibel dan efisien. Meskipun masing-masing menawarkan fokus yang berbeda, keduanya mempermudah pengaturan elemen pada halaman. Berikut ini adalah penjelasan dari masing-masing ide dan manfaatnya:

1. **Flexbox (Flexible Box Layout)**
Konsep: Flexbox adalah model tata letak satu dimensi yang digunakan untuk menyusun elemen dalam satu baris atau satu kolom. Model ini mengutamakan fleksibilitas elemen anak dalam wadah, yang memungkinkan mereka beradaptasi secara dinamis dengan ruang yang tersedia.

- **Fitur Utama:**
-- *Arah Utama (Main Axis)*: Elemen dapat diatur dalam satu baris atau satu kolom.
Pembagian Ruang Otomatis: Elemen akan secara otomatis mengambil ruang yang tersedia, baik dengan memperluas atau mengecil sesuai ukuran kontainer.
-- *Pengaturan Alignment dan Distribusi*: Flexbox memungkinkan pengaturan posisi elemen (alignment) dan distribusi ruang antar elemen (spacing) secara dinamis tanpa perlu menggunakan margin atau padding secara manual.
-- *Urutan Fleksibel*: Elemen dapat diatur urutannya dalam dokumen tanpa mengubah urutan sebenarnya di dalam HTML.

- **Kegunaan**:
-- Flexbox sangat ideal untuk tata letak yang sederhana dan responsif dalam satu dimensi, seperti membuat menu navigasi horizontal, baris produk, atau kolom artikel.
-- Cocok untuk tata letak yang perlu dirancang secara fleksibel tanpa ketergantungan pada ukuran tetap

2. **Grid Layout**
Konsep: Tata letak grid CSS adalah sistem tata letak dua dimensi yang memungkinkan elemen diatur secara bersamaan dalam baris dan kolom. Tata letak grid memberi pengembang kemampuan untuk membuat tata letak yang kompleks dengan pembagian ruang yang lebih tepat.

- **Fitur Utama:**
-- *Baris dan Kolom*: Grid memungkinkan Anda membuat tata letak dengan berbagai baris dan kolom yang dapat diatur ukurannya.
-- *Grid Template*: Anda dapat menentukan template grid yang terdiri dari jumlah dan ukuran kolom serta baris secara eksplisit.
-- *Alignment dan Positioning*: Grid memungkinkan penempatan elemen secara eksplisit pada posisi tertentu di dalam grid (misalnya, elemen bisa ditempatkan pada kolom 2 dan baris 1).
-- *Responsivitas Lebih Baik*: Grid mempermudah penyesuaian tampilan halaman saat berpindah dari ukuran layar besar (desktop) ke ukuran layar kecil (ponsel).

### 5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Framework CSS yang saya pakai adalah **Tailwind**.
1. Menambah Tailwind ke Aplikasi dan menambah `global.css` lewat `base.html`
```html
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
```

2. Menambah 3 fungsi pada `views.py`
a.) Edit product
```python
def edit_product(request, id):
    # Get product entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:products'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```

b.) Delete product
```python
def delete_product(request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:products'))
```

c.) Show product cards di navbar "Product"
```python
def product_page(request):
    product_entries = Product.objects.all()  # Ambil semua produk dari database
    return render(request, 'products.html', {'product_entries': product_entries})
```

3. Menambahkan Navigation Bar (`navbar.html` di direktori root folder/templates) pada Aplikasi
Navbar saya sebagai berikut :
(https://media.discordapp.net/attachments/817255852259672094/1290586995701055550/image.png?ex=66fd004d&is=66fbaecd&hm=6670550e68d85522f72733b31dc8964476d2b2cc7e2a91639dde9ed9213795b0&=&format=webp&quality=lossless&width=1440&height=66)

Saya mengganti tema warna yang sesuai dengan foto dan kostumisasi tailwind nya.

4. Menambahkan `global.css` di direktori `static/css/global.css` untuk tema keseluruhan program
```css
.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}
.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #ef4444;
    box-shadow: 0 0 0 3px #ef4444;
}
@keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}
.animate-shine {
    background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
    background-size: 200% 100%;
    animation: shine 3s infinite;
}
```

5. Memisahkan tampilan cards product dari `main.html` dengan menggunakan html baru di main/templates yaitu `products.html`

```html
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Products - Bram Music Shop</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-gray-900 flex flex-col">
    <div class="flex justify-end mb-6">
        <a href="{% url 'main:create_product' %}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
            Add New Product
        </a>
    </div>
    
    {% if not product_entries %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
        <p class="text-center text-gray-300 mt-4">Belum ada data produk.</p>
    </div>
    {% else %}
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full">
        {% for product_entry in product_entries %}
            {% include 'card_product.html' with product_entry=product_entry %}
        {% endfor %}
    </div>
    {% endif %}
</div>
{% endblock content %}
```

6. Menambahkan styling css ke beberapa html, di antaranya : 
- card_info.html
- card_product.html
- create_product.html
- edit_product.html
- login.html
- main.html
- products.html
- register.html

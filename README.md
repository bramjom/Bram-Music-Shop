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

ORM pada Django secara teknis menerjemahkan tindakan atau operasi dari model (seperti menyimpan, mengambil, memperbarui, atau menghapus data) ke dalam perintah SQL yang sesuai untuk berinteraksi dengan database, memungkinkan pengembang mengelola database menggunakan bahasa pemrograman yang mereka gunakan (Python), tanpa harus mempelajari atau menangani detail SQL. Dengan kata lain, ORM memberikan abstraksi antara kode program dan database, sehingga


# ubuntu

1. Deploy MHN terlebih dahulu : https://github.com/pwnlandia/mhn
2. Masuk ke alamat IP MHN, misal 10.33.109.126
![alt text](https://github.com/andri-x99/ubuntu/blob/master/picture/3-mhn.png)
3. Pilih Menu Deploy, kemudian cari Honeypot yang diinginkan, misal Dionaea
![alt text](https://github.com/andri-x99/ubuntu/blob/master/picture/4-raspi-deploy.png)
4. Copy "Deploy Command" menuju perangkat yang ingin dijadikan sebagai Honeypot
![alt text](https://github.com/andri-x99/ubuntu/blob/master/picture/5-raspi-deploy.png)
5. Pastikan service Honeypot telah berjalan menggunakan perintah "lsof -i -n -P" atau "netstat -tlpn"
![alt text](https://github.com/andri-x99/ubuntu/blob/master/picture/6-dionaea-services.png)

6. Edit pada bagian /opt/dionaea/lib/dionaea/python/dionaea/log_db_sql/model.py, agar ketika membuat database sudah ada AUTO_INCREMENT, sehingga ketika data dihapus, maka hanya perlu melanjutkan angka setelahnya, tidak kembali ke angka 1 (mencegah data yang tertumpuk)

![alt text](https://github.com/andri-x99/ubuntu/blob/master/picture/0-edit_dionaea_auto_increment_base_in_model.png)

7. Edit pada bagian /opt/dionaea/lib/dionaea/python/dionaea/logsql.py, pastikan ketika mengupdate tabel baru, menggunakan AUTO_INCREMENT, ini bertujuan agar ketika dihapus tabelnya, maka akan melanjutkan proses penomoran secara otomatisnya, sehingga tidak terjadi penumpukan id yang sama

![alt text](https://github.com/andri-x99/ubuntu/blob/master/picture/1-edit_dionaea_auto_increment_update_in_logsql.png)

8. (OPTIONAL) Edit pada bagian /opt/dionaea/etc/dionaea/ihandlers-available/log_sqlite.yaml, karena LOG pada honeypot akan dihapus, apabila masih ingin memanfaatkan datanya, dapat melakukan duplikasi database, defaultnya dionaea.sqlite, bisa menambahkan dibawah command tersebut, menjadi dionaea-duplicate.sqlite

![alt text](https://github.com/andri-x99/ubuntu/blob/master/picture/3-optional-logsqlite-yaml.png)

9. Install git, lalu clone repository https://github.com/andri-x99/ubuntu.git
10. Masuk ke folder 03-proyekakhir, copy api.py ke /opt/dionaea/var/lib/dionaea/

![alt text](https://github.com/andri-x99/ubuntu/blob/master/picture/14-copy-opt.png)

11. Jalankan menggunakan perintah python3 api.py, apabila library tidak ditemukan, install pip terlebih dahulu, kemudian install paketnya menggunakan pip
12. Kemudian sebagai tempat penampungan log dari honeypot, membutuhkan server yang sudah terinstall mongodb
13. Install git pada server, lalu clone repository https://github.com/andri-x99/ubuntu.git
14. Masuk ke foler 03-proyekakhir, jalankan python3 update_data.py


# Praktikum Teori Graf Kelompok 14
---
|Nama     |NRP     |
|---      |---     |
| Jeihan Shawmy Prasetya | 5025241132 |
| Kineisha Rana Salsabila | 5025241149 |
| Shifa Alya Dewi | 5025241176 |


## Praktikum 1 - The Knight's Tour

#### Soal:
Jika sebuah bidak kuda diletakkan pada sebarang kotak untuk kemudian melakukan perjalanan (dengan cara pergerakan kuda) mengunjungi ke semua (8 x 8) kotak papan catur.

![Image](https://github.com/user-attachments/assets/12a9e983-9602-4c70-9a55-bdb75c9db6fe)

Jika diinginkan situasi bahwa kuda tersebut dapat:
a. Mengakhiri perjalanan di sebarang kotak (open tour)
b. Mengakhiri perjalanan pada attacking square (closed tour)
Maka aplikasikan algoritma untuk menyelesaikan masalah di atas ke dalam sebuah program dengan menunjukkan rute perjalanan seperti gambar di bawah.

![Image](https://github.com/user-attachments/assets/9e8e2ccc-c2d1-4479-a13b-9256356e3da9)

#### Penjelasan Program:

Program membuat papan catur 8 x 8, tiap kotaknya ditandai -1 yang berarti belum dikunjungi dan akan berubah menjadi 0 jika sudah dikunjungi. Kuda diletakkan di posisi awal (start_x, start_y) dan setiap langkah berikutnya ditentukan dengan mencari kotak-kotak yang dapat dicapai kuda dengan pergerakan L. Dari kotak-kotak tersebut dipilih yang memiliki degree paling kecil atau jumlah langkah valid dari kotak tersebut (Warnsdorff). Proses terus diulang, jika menemukan kebuntuan akan melakukan backtrack. 
Tur dianggap berhasil jika semua 64 kotak telah dikunjungi. Terdapat 2 jenis tur; open dan closed (ini dapat diubah pada bagian mode). Tur dapat berhenti di kotak manapun pada open tour, sedangkan pada closed tour harus berhenti di kotak posisi awal kuda.

Contoh Input
```sh
start_x, start_y = 1, 2
mode = "open"
```

Contoh Output
```sh
Knight's Tour (OPEN):

[1, 22, 3, 18, 43, 38, 13, 16]
[4, 19, 0, 39, 14, 17, 44, 37]
[23, 2, 21, 42, 45, 50, 15, 12]
[20, 5, 58, 49, 40, 47, 36, 51]
[61, 24, 41, 46, 57, 52, 11, 32]
[6, 27, 62, 59, 48, 33, 54, 35]
[25, 60, 29, 8, 53, 56, 31, 10]
[28, 7, 26, 63, 30, 9, 34, 55]
```

## Praktikum 2 - Largest Monotonically Increasing Subsequence

#### Soal:
Implementasikan sebuah program untuk menyelesaikan permasalahan Largest Monotonically Increasing Subsequence.

![Image](https://github.com/user-attachments/assets/96ffa51c-0555-4a63-b398-10f13e51f5fe)
Aplikasi tree untuk mencari Largest Monotonically Increasing Subsequence dari urutan bilangan :
4, 1, 13, 7, 0, 2, 8, 11, 3

#### Penjelasan Program:

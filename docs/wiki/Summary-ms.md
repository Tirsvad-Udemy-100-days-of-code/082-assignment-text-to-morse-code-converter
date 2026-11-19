[English](Summary) · [Dansk](Summary-da) · **Bahasa Malaysia**

# Apa yang diajar oleh langkah-langkah ini

- Mulakan projek dengan kes guna dan reka bentuk, kemudian tulis kod daripada reka bentuk itu.
- Sebuah `.venv`, `python -m pip install --upgrade pip` dan pemasangan boleh suntingan memberi persediaan yang boleh diulang.
- Kamus memetakan aksara kepada kod Morse; `str.upper()`, `str.split()` dan `str.join()` melakukan penukaran.
- Pengecualian khusus (`UnsupportedCharacterError`) memberitahu pemanggil apa yang salah, dan `raise ... from` mengekalkan puncanya.
- `python -m morse_converter` menerima argumen atau gesaan, dan memulangkan kod keluar 0 atau 1.
- pytest menguji unit dan menjalankan atur cara sebagai subproses; buku nota menjalankan langkah yang sama.

Contoh: `SOS` ialah `... --- ...`; `Hello World` ialah `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`; `~` tidak disokong dan memberi kod keluar 1.

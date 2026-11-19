[English](Step-4-Command-Line) · [Dansk](Step-4-Command-Line-da) · **Bahasa Malaysia**

# Langkah 4: Jalankan dari baris perintah

**Soalan:** Bagaimanakah pengguna menjalankan atur cara, dan bagaimanakah ia memberitahu bahawa ada yang tidak kena?

![Langkah 4: baris perintah](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/raw/branch/main/docs/images/step-4-command-line.png)

## Apa yang kod lakukan

`python -m morse_converter Hello World` menjalankan `__main__.py`. Perintah ini menyambung argumen dengan satu ruang; tanpa argumen, ia meminta teks dengan `input()`. Ia mencetak kod Morse dan keluar dengan 0. Bagi aksara yang tidak disokong, seperti `~`, ia mencetak aksara itu pada aliran ralat dan keluar dengan 1, seperti yang ditunjukkan oleh tangkapan skrin.

## Apa yang anda perolehi

- `python -m pakej` menjalankan `__main__.py` sesebuah pakej.
- `sys.argv` menyimpan argumen dan `input()` membaca satu baris.
- Kod keluar 0 bermaksud berjaya; output untuk pengguna pergi ke output standard dan ralat ke ralat standard.
- Ujian boleh menjalankan atur cara sebagai subproses dan menyemak output serta kod keluarnya.

Sebelum: [Step-3-Convert-Text](Step-3-Convert-Text-ms) · Seterusnya: [Summary](Summary-ms)

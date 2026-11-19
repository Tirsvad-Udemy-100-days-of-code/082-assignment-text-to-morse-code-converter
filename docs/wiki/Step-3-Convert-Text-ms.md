[English](Step-3-Convert-Text) · [Dansk](Step-3-Convert-Text-da) · **Bahasa Malaysia**

# Langkah 3: Tukar teks kepada kod Morse

**Soalan:** Bagaimanakah satu ayat penuh menjadi kod Morse?

![Langkah 3: menukar teks](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/raw/branch/main/docs/images/step-3-convert-text.png)

## Apa yang kod lakukan

`text_to_morse` memecahkan teks kepada perkataan dengan `text.split()`, menyambung corak isyarat satu perkataan dengan satu ruang dan perkataan dengan ` / `. `SOS` memberi `... --- ...` dan `Hello World` memberi `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`. Teks kosong atau teks yang hanya berisi ruang memberi rentetan kosong. Aksara tanpa corak menimbulkan `UnsupportedCharacterError`, dan tiada apa yang ditukar ([ADR-0001](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/src/branch/main/docs/adr/adr-0001-unsupported-characters-are-rejected.md)).

## Apa yang anda perolehi

- `str.split()` memisahkan pada sebarang ruang kosong dan membuang bahagian kosong.
- `str.join()` dengan ungkapan penjana membina hasil tanpa pemboleh ubah gelung.
- Kes tepi (teks kosong, ruang tambahan, aksara tidak dikenali) ialah sebahagian daripada reka bentuk, jadi putuskan dahulu.

Sebelum: [Step-2-Morse-Table](Step-2-Morse-Table-ms) · Seterusnya: [Step-4-Command-Line](Step-4-Command-Line-ms)

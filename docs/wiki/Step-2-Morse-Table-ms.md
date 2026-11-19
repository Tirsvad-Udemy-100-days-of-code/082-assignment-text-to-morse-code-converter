[English](Step-2-Morse-Table) · [Dansk](Step-2-Morse-Table-da) · **Bahasa Malaysia**

# Langkah 2: Jadual Morse

**Soalan:** Dari manakah atur cara mendapat titik dan sengkang bagi setiap aksara?

![Langkah 2: jadual Morse](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/raw/branch/main/docs/images/step-2-morse-table.png)

## Apa yang kod lakukan

`MORSE_CODE_DICT` dalam `domain/constants.py` memetakan **54** aksara (huruf A hingga Z, digit 0 hingga 9 dan 18 tanda baca) kepada corak isyaratnya, contohnya `S` kepada `...` dan `0` kepada `-----`. `signal_pattern_for` mencari aksara selepas menukarnya kepada huruf besar, jadi `s` dan `S` memberi corak yang sama.

## Apa yang anda perolehi

- Kamus ialah jadual carian: satu kunci memberi satu nilai dalam satu langkah.
- Pemalar disimpan dalam satu modul (`constants.py`) dan ditulis sekali.
- `str.upper()` menjadikan carian tidak bergantung pada huruf besar atau kecil.

Sebelum: [Step-1-The-Road](Step-1-The-Road-ms) · Seterusnya: [Step-3-Convert-Text](Step-3-Convert-Text-ms)

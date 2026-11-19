[English](Step-3-Convert-Text) · **Dansk** · [Bahasa Malaysia](Step-3-Convert-Text-ms)

# Trin 3: Omsæt tekst til morsekode

**Spørgsmål:** Hvordan bliver en hel sætning til morsekode?

![Trin 3: omsætning af tekst](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/raw/branch/main/docs/images/step-3-convert-text.png)

## Hvad koden gør

`text_to_morse` deler teksten i ord med `text.split()`, sætter signalmønstrene i et ord sammen med ét mellemrum og ordene med ` / `. `SOS` giver `... --- ...`, og `Hello World` giver `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`. En tom tekst eller en tekst med kun mellemrum giver en tom streng. Et tegn uden mønster udløser `UnsupportedCharacterError`, og intet bliver omsat ([ADR-0001](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/src/branch/main/docs/adr/adr-0001-unsupported-characters-are-rejected.md)).

## Hvad du fik ud af det

- `str.split()` deler ved enhver form for blanktegn og fjerner tomme dele.
- `str.join()` med et generatoruttryk bygger resultatet uden en løkkevariabel.
- Grænsetilfælde (tom tekst, ekstra mellemrum, ukendte tegn) er en del af designet, så beslut dem først.

Forrige: [Step-2-Morse-Table](Step-2-Morse-Table-da) · Næste: [Step-4-Command-Line](Step-4-Command-Line-da)

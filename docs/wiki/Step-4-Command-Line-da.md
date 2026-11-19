[English](Step-4-Command-Line) · **Dansk** · [Bahasa Malaysia](Step-4-Command-Line-ms)

# Trin 4: Kør det fra kommandolinjen

**Spørgsmål:** Hvordan kører en bruger programmet, og hvordan fortæller det, at noget gik galt?

![Trin 4: kommandolinjen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/raw/branch/main/docs/images/step-4-command-line.png)

## Hvad koden gør

`python -m morse_converter Hello World` kører `__main__.py`. Kommandoen sætter argumenterne sammen med ét mellemrum; uden argumenter spørger den efter teksten med `input()`. Den skriver morsekoden og afslutter med 0. Ved et tegn, der ikke understøttes, for eksempel `~`, skriver den tegnet på fejlstrømmen og afslutter med 1, som skærmbilledet viser.

## Hvad du fik ud af det

- `python -m pakke` kører `__main__.py` i en pakke.
- `sys.argv` indeholder argumenterne, og `input()` læser en linje.
- Exitkode 0 betyder succes; output til brugeren går til standard output og fejl til standard error.
- En test kan køre programmet som en delproces og kontrollere dets output og exitkode.

Forrige: [Step-3-Convert-Text](Step-3-Convert-Text-da) · Næste: [Summary](Summary-da)

[English](Step-2-Morse-Table) · **Dansk** · [Bahasa Malaysia](Step-2-Morse-Table-ms)

# Trin 2: Morsetabellen

**Spørgsmål:** Hvor henter programmet prikker og streger for hvert tegn?

![Trin 2: morsetabellen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/raw/branch/main/docs/images/step-2-morse-table.png)

## Hvad koden gør

`MORSE_CODE_DICT` i `domain/constants.py` knytter **54** tegn (bogstaverne A til Z, cifrene 0 til 9 og 18 tegnsætningstegn) til deres signalmønstre, for eksempel `S` til `...` og `0` til `-----`. `signal_pattern_for` slår et tegn op, efter at det er gjort til stort bogstav, så `s` og `S` giver samme mønster.

## Hvad du fik ud af det

- En ordbog er en opslagstabel: en nøgle giver en værdi i ét trin.
- Konstanter ligger i ét modul (`constants.py`) og er skrevet én gang.
- `str.upper()` gør opslaget uafhængigt af store og små bogstaver.

Forrige: [Step-1-The-Road](Step-1-The-Road-da) · Næste: [Step-3-Convert-Text](Step-3-Convert-Text-da)

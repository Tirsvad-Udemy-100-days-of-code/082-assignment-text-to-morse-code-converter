[English](Summary) · **Dansk** · [Bahasa Malaysia](Summary-ms)

# Hvad trinene lærte

- Start et projekt med en use case og et design, og kod så ud fra designet.
- Et `.venv`, `python -m pip install --upgrade pip` og en redigerbar installation giver en gentagelig opsætning.
- En ordbog knytter tegn til morsekode; `str.upper()`, `str.split()` og `str.join()` står for omsætningen.
- En specifik undtagelse (`UnsupportedCharacterError`) fortæller kalderen, hvad der er galt, og `raise ... from` bevarer årsagen.
- `python -m morse_converter` tager argumenter eller en prompt og giver exitkode 0 eller 1.
- pytest tester enhederne og kører programmet som en delproces; en notebook kører de samme trin.

Eksempler: `SOS` er `... --- ...`; `Hello World` er `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`; `~` understøttes ikke og giver exitkode 1.

# Google Docs → Gmail

Proste narzędzie: wklejasz treść z Google Docs, a ono oddaje czysty HTML gotowy
do wklejenia w okno nowej wiadomości w Gmailu (z zachowanym formatowaniem —
pogrubienia, nagłówki, listy, linki).

Całą robotę wykonuje przeglądarka. Streamlit służy tu tylko jako hosting.

## Pliki

| plik | do czego |
|------|----------|
| `app.py` | aplikacja Streamlit (wczytuje i osadza `index.html`) |
| `index.html` | właściwe narzędzie (edytor + czyszczenie + kopiowanie) |
| `requirements.txt` | zależności (`streamlit`) |

## Wdrożenie przez GitHub + Streamlit Community Cloud

1. **Utwórz repozytorium na GitHub** (może być prywatne) i wrzuć do niego
   wszystkie trzy pliki: `app.py`, `index.html`, `requirements.txt`.
   Przez stronę GitHuba: *Add file → Upload files* → przeciągnij pliki → *Commit*.
2. Wejdź na **https://share.streamlit.io** i zaloguj się kontem GitHub.
3. Kliknij **Create app → Deploy a public app from GitHub**.
4. Wskaż swoje repozytorium, gałąź `main` i plik główny **`app.py`**.
5. **Deploy**. Po chwili dostaniesz stały adres `...streamlit.app`, który możesz
   zapisać w zakładkach i podesłać zespołowi.

Każdy push do repo automatycznie zaktualizuje aplikację.

## Jak używać

1. W Google Docs zaznacz treść i skopiuj (Ctrl/Cmd + C).
2. Wklej w pole w aplikacji (Ctrl/Cmd + V) — formatowanie zostanie oczyszczone.
3. (Opcjonalnie) popraw tekst bezpośrednio w polu.
4. **Kopiuj do Gmaila** → w nowej wiadomości wklej (Ctrl/Cmd + V).

Przycisk **Kopiuj HTML (źródło)** kopiuje sam kod HTML, gdyby przydał się gdzie
indziej.

## Uruchomienie lokalnie (opcjonalnie)

```bash
pip install -r requirements.txt
streamlit run app.py
```

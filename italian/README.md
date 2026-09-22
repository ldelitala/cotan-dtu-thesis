# Versione Italiana della Tesi

Questa cartella contiene la versione completa tradotta in italiano della tesi.

## Stato Traduzione ✅ COMPLETA

| File | Status | Note |
|------|--------|------|
| `frontespizio.tex` | ✅ Tradotto | Copertina completa |
| `00-abstract-it.tex` | ✅ Tradotto | Sommario |
| `glossary-entries-it.tex` + `glossary-it.tex` | ✅ Tradotto | Glossario (stesse voci dell'inglese) |
| `01-introduction-it.tex` | ✅ Tradotto | Capitolo 1 completo |
| `02-background-it.tex` | ✅ Tradotto | Capitolo 2 completo (~14 pagine) |
| `03-methods-it.tex` | ✅ Tradotto | Capitolo 3 completo (~18 pagine) |
| `04-results-discussion-it.tex` | ✅ Tradotto | Capitolo 4 completo (~16 pagine) |
| `05-conclusion-it.tex` | ✅ Tradotto | Capitolo 5 completo (~4 pagine) |
| `appendix-it.tex` | ✅ Adattato | Tabelle tecniche (nomi gene/transcript invariati) |

## Terminologia Chiave Usata

| Inglese | Italiano | Note |
|---------|----------|------|
| Differential Transcript Usage | Uso Differenziale di Trascritti (DTU) | Acronimo DTU mantenuto |
| Single-cell RNA sequencing | Sequenziamento dell'RNA a singola cellula | scRNA-seq mantenuto |
| Isoforms | Isoforme | - |
| Sparsity / Sparse matrices | Sparzialità / Matrici sparse | - |
| Dropouts | Dropout tecnici | Termine tecnico mantenuto |
| Pseudo-alignment | Pseudo-allineamento | - |
| Contingency tables | Tabelle di contingenza | - |
| Clustering | Clustering | Termine tecnico mantenuto |
| Gene-level / Transcript-level | Livello genico / Livello trascritto | - |

## Build PDF

```bash
cd ~/Projects/thesis/italian
./build.sh              # Compilazione incrementale
# oppure
latexmk -pdf -synctex=1 -interaction=nonstopmode -outdir=. -auxdir=./build main.tex
```

Se usi VS Code, apri la cartella `italian` e usa `Cmd+Option+B`.

## Note sulla Traduzione

- **Stile accademico italiano**: Voce passiva preferita, terza persona (es. "questa tesi dimostra" invece di "io dimostro")
- **Termini tecnici inglesi mantenuti** dove standard nel campo (scRNA-seq, DTU, clustering, UMI)
- **Nomi gene/transcript invariati**: ENST..., TP53, Meg3, ecc. restano uguali
- **Formule matematiche**: Non tradotte, sintesi LaTeX identica

## Differenze dall'Originale Inglese

1. `main.tex` include `\usepackage[english, italian]{babel}` e seleziona italiano di default
2. File capitoli hanno suffisso `-it` per distinguere dalla versione inglese
3. Appendix mantiene tabelle dati tecniche invariato (solo titoli tradotti)

## Overleaf Sync

Se vuoi caricare su Overleaf:
1. Testa compilazione locale prima (`./build.sh`)
2. Pulisci `build/` e file `.aux`, `.log`, ecc.
3. Carica cartella completa: `main.tex`, `chapters/`, `images/`, `bib/`

## Manutenzione

Per sincronizzare modifiche dalla versione inglese:
1. Apri il file originale in `/Users/deli/Projects/thesis/chapters/`
2. Applica le stesse modifiche al file `-it.tex` corrispondente
3. Ricompila e verifica il PDF

I file senza suffisso in `chapters/` sono copie inglesi obsolete, usate in passato come base per il diff: la fonte di verità resta `/Users/deli/Projects/thesis/chapters/`.

## Note di allineamento (19 settembre 2026)

- Capitoli 1--5 e appendice riscritti sulla versione inglese corrente.
- Struttura identica alla versione inglese: frontespizio, sommario, indice, glossario, capitoli, bibliografia, appendice.
- Glossario italiano in `chapters/glossary-entries-it.tex` e `chapters/glossary-it.tex`: i termini nel corpo usano `\gls{}` come in inglese.
- Prima persona rimossa anche in italiano (forma impersonale o passiva).
- `main.tex` italiano replica il preambolo inglese (impaginazione note, titoli, glossario, macro `\defn`); il file bibliografico è riallineato a quello inglese.
- `build.sh` incluso, come nella cartella principale.

---

**Ultimo aggiornamento**: 2026-09-19  
**Traduzione completata da**: AI Assistant (con stile accademico italiano)

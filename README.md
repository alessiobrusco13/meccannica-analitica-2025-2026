# Appunti di Meccanica Analitica

Raccolta di appunti redatti in LaTeX durante il corso di Meccanica Analitica, tenuto dal Prof. Maurizio Gentile per il secondo anno del Corso di Laurea in Fisica (Gruppo 1) presso l'Università degli Studi di Napoli Federico II.

> **Avvertenza:** Il presente materiale non costituisce documentazione ufficiale del corso. Trattandosi di una trascrizione personale e attualmente in fase di stesura, il testo è soggetto a revisioni e potrebbe presentare errori, imprecisioni o parti incomplete. Contributi sotto forma di segnalazioni (Issues) o correzioni (Pull Requests) sono incoraggiati e benvenuti.

---

## Download degli Appunti (PDF)

Per consultare gli appunti **non è necessario scaricare o compilare il codice sorgente**. 

L'ultima versione precompilata del documento, pronta per la lettura e la stampa, è sempre disponibile per il download:

**[Scarica l'ultimo PDF aggiornato dalle Releases](https://github.com/alessiobrusco13/meccannica-analitica-2025-2026/releases/latest)**

*(Il file allegato alle release viene aggiornato periodicamente seguendo l'avanzamento delle lezioni).*

---

## Indice degli Argomenti

Il testo si propone di trattare i seguenti argomenti (elenco parziale e in aggiornamento):

- Principi fondamentali della meccanica analitica
- Equazioni di Lagrange e principi variazionali
- Equazioni di Hamilton
- Teoria di Hamilton-Jacobi

---

## Struttura del Repository

Il progetto è organizzato in modo modulare per facilitare la stesura e la manutenzione del codice sorgente LaTeX:
```text
.
├── main.tex       # File principale (root) del documento
├── Sections/      # Directory contenente i file sorgente dei singoli capitoli
└── Setup/         # Directory dedicata a preambolo, pacchetti, comandi custom e stili
```

---

## Istruzioni per Compilazione e Contributi

Se desideri modificare gli appunti, proporre correzioni o compilare il documento in autonomia, puoi farlo comodamente online o in locale. I file binari generati dalla compilazione (incluso `main.pdf`) sono intenzionalmente ignorati dal versionamento per mantenere la cronologia di Git pulita.

### Compilazione in Locale

È richiesta una distribuzione TeX locale funzionante (es. TeX Live o MacTeX). 

Il metodo consigliato prevede l'utilizzo di `latexmk`, che si occupa automaticamente di gestire le dipendenze e i cicli di compilazione:
```bash
latexmk -pdf main.tex
```

In alternativa, è possibile ricorrere alla compilazione manuale tramite `pdflatex`. In tal caso, sono necessarie due esecuzioni consecutive per garantire la corretta risoluzione dei riferimenti incrociati e la generazione dell'indice:
```bash
pdflatex main.tex
pdflatex main.tex
```

### Utilizzo tramite Overleaf

Se si preferisce evitare l'installazione di un ambiente in locale, è possibile utilizzare [Overleaf](https://www.overleaf.com/):

1. Scaricare il codice sorgente di questo repository come archivio `.zip` (tasto "Download ZIP").
2. Su Overleaf, creare un nuovo progetto selezionando **Upload Project** e caricare l'archivio.
3. Nelle impostazioni del progetto, verificare che `main.tex` sia impostato come *Main document*.
4. (Opzionale) Se si possiede un account premium collegato a GitHub, è possibile importare il repository direttamente tramite l'opzione **Import from GitHub**.
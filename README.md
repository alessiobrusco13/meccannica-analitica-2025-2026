# Appunti di Meccanica Analitica

**Stato del progetto:** Lavori in corso (Work in Progress)

Raccolta di appunti redatti in LaTeX durante il corso di Meccanica Analitica, tenuto dal Prof. Gentile per il secondo anno del Corso di Laurea in Fisica (Gruppo 1) presso l'Università degli Studi di Napoli Federico II.

> **Avvertenza:** Il presente materiale non costituisce documentazione ufficiale del corso. Trattandosi di una trascrizione personale e attualmente in fase di stesura, il testo è soggetto a revisioni e potrebbe presentare errori, imprecisioni o parti incomplete. Contributi sotto forma di segnalazioni (Issues) o correzioni (Pull Requests) sono incoraggiati e benvenuti.

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

## Utilizzo tramite Overleaf

Se si preferisce evitare l'installazione di un ambiente di sviluppo in locale, è possibile compilare e visualizzare gli appunti direttamente online utilizzando [Overleaf](https://www.overleaf.com/). 

Per importare il progetto:
1. Scaricare il codice sorgente di questo repository sotto forma di archivio `.zip` (tramite il tasto "Download ZIP").
2. Su Overleaf, creare un nuovo progetto selezionando l'opzione **Upload Project** e caricare l'archivio precedentemente scaricato.
3. Se necessario, verificare nelle impostazioni del progetto (Menu in alto a sinistra) che `main.tex` sia selezionato come *Main document*.
4. (Opzionale) Se si possiede un account premium collegato a GitHub, è possibile importare il progetto direttamente dal repository tramite l'opzione **Import from GitHub**.

---

## Compilazione in Locale

Per generare il documento in formato PDF sul proprio computer, è richiesta una distribuzione TeX locale funzionante (es. TeX Live o MacTeX). 

Il metodo consigliato prevede l'utilizzo di `latexmk`, che si occupa automaticamente di gestire le dipendenze e i cicli di compilazione:
```bash
latexmk -pdf main.tex
```

In alternativa, è possibile ricorrere alla compilazione manuale tramite `pdflatex`. In tal caso, sono necessarie due esecuzioni consecutive per garantire la corretta risoluzione dei riferimenti incrociati e la generazione dell'indice:
```bash
pdflatex main.tex
pdflatex main.tex
```

---

## Consultazione del PDF

Al fine di mantenere pulita la cronologia del sistema di versionamento, i file binari e i log di compilazione (incluso il file `main.pdf`) sono ignorati e non tracciati all'interno del repository.

Per consultare gli appunti senza dover compilare i sorgenti, è possibile scaricare l'ultima versione del documento precompilato dalla sezione **Releases** di questo repository. Il PDF allegato alle release verrà aggiornato periodicamente in concomitanza con i progressi nella stesura dei capitoli.
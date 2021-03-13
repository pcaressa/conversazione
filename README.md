# Conversazione con un pazzo

Semplice applicazione di un modello markoviano per conversare con un pazzo che si crede Gramsci... Si tratta di un programmino dimostrativo che uso nelle mie conferenze o che mostro come esempio di programmazione Python nei miei corsi introduttivi. Non originale e perfettibile, ma funzionante:-) La cosa sorprendente del programma è che produce frasi grammaticalmente corrette, sebbene di dubbio senso, partendo da esmepi di frasi prese come input dal modello markoviano.

Per farlo funzionare basta scaricare i file in una cartella e dare in pasto all'interprete Python il file conversazione.py. In questo file sono definite tre variabili

```python
NOME = "Gramsci"
NOME_FILE = "gramsci.txt"
ENC = "latin-1"
```

che definiscono il nome del personaggio col quale conversare, un file di testo che contiene frasi, testi, libri e altro del personaggio in formato test (no html, no xml, etc.) e la codifica del carattere del file di testo (per le lettere accentate, etc.).

L'idea del programma è di scandire tutte le parole del testo e di annotare per ciascuna parola tutte le parole che la seguono in qualche frase e quante volte la seguono. Si ottiene così, per ogni parola del testo, una distribuzione probabilistica empirica delle parole che la seguono, dalla quale fare sampling per generare, data una parola, quella seguente, e poi quella seguente a essa, e così via fino a formare una frase.

Per svolgere la conversazione il programma lascia introdurre all'utente una frase e prende l'ultima parola, usandola come origine per generare la risposta.

Il programma cerca una versione binaria (pkl) del file di esempio e se la trova la carica, altrimenti la produce e la salva prima di far partire la conversazione.

Enjoy,
P

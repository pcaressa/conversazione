# Conversazione con un pazzo che si crede Gramsci

Semplice applicazione di un modello markoviano per conversare con un pazzo che si crede Gramsci... Si tratta di un semplice programmino dimostrativo che uso nelle mie conferenze o che mostro come esempio di programmazione Python nei miei corsi introduttivi. Non originale e perfettibile, ma funzionante:-)

Basta scaricare i file in una cartella e dare in pasto all'interprete Python il file gramsci.py. Volendo conversare con altri, basta sostituire il contenuto del file gramsci.txt con un testo altrui, per esempio la Divina Commedia...

L'idea del programma è di scandire tutte le parole del testo (un volume delle opere di Gramsci), e di annotare per ciascuna parola tutte le parole che la seguono in qualche frase, e quante volte la seguono. Si ottiene così, per ogni parola del testo, una distribuzione probabilistica empirica delle parole che la seguono, dalla quale fare sampling per generare, data una parola, quella seguente, e poi quella seguente a essa, e così via fino a formare una frase.

Il programma salva in formato binario i suoi dati per riusarli la prossima volta senza dover nuovamente analizzare il testo.

Enjoy,
P

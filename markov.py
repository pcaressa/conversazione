# -*- coding: utf-8 -*-
import random

def analizza_testo(testo):
    """Tokenizza il testo dato e torna una lista che contiene i token estratti
        nell'ordine con cui si presentano. Come singolo token intendiamo:
            * una sequenza contigua di lettere
            * una sequenza contigua di cifre
            * un singolo carattere non bianco."""
    accentate = "èéàìòùÈÀÌÒÙÉ"
    token = []
    i = 0
    while i < len(testo):
        while i < len(testo) and testo[i].isspace():
            i += 1
        if i == len(testo):
            break
        # i = inizio della prossima parola; ne cerca la fine
        i0 = i
        i += 1
        if testo[i0].isdigit():
            # Sequenza di cifre
            while i < len(testo) and testo[i].isdigit():
                i += 1
        elif testo[i0].isalpha() or testo[i0] in accentate:
            # Parola
            while i < len(testo) and (testo[i].isalpha() or testo[i] in accentate):
                i += 1
        # i = fine del token + 1
        # Se singolo carattere ha già incrementato di 1 i.
        token.append(testo[i0:i])
    return token
    

def analizza(nome_file, enc="utf-8"):
    """Legge un file di testo, estrae la successione dei token e la scrive su
        un altro file con estensione ".tok"."""
    with open(nome_file, encoding=enc) as file_in,  \
            open(nome_file + ".tok", "w") as file_out:
        for riga in file_in:
            token = analizza_testo(riga)
            for t in token:
                file_out.write(t + "\n")

def dizionario(d, file_tok, N):
    """Considera un dizionario e un file che contiene una parola in ciascuna
        riga, e aggiunte al dizionario come chiavi le parole e come valori
        le sequenze di N parole che seguono la parola chiave, ciascuna contata
        per il numero di volte che appare di seguito alla parola chiave stessa.
        Il valore è quindi una lista di liste [[freq, lista-N-parole], ...].
        Se ci sono meno di N parole precedenti riempie i "buchi" con ""."""
    Ngramma = [""]*(N + 1)
    with open(file_tok) as file_in:
        # legge N+1 parole dal file (riempie con "" se il file è finito)
        i = 0
        while i < N+1 and file_in.readable():
            Ngramma[i] = file_in.readline()[:-1]
            i += 1
        while i < N+1:
            Ngramma[i] = ""
            i += 1
        while Ngramma[0] != "":
            p = Ngramma[0]
            if p not in d:
                d[p] = [[1, Ngramma[1:]]]
            else:
                # Cerca l'Ngramma nella lista
                i = 0
                while i < len(d[p]):
                    if d[p][i][1] == Ngramma[1:]:
                        d[p][i][0] += 1
                        break
                    i += 1
                if i == len(d[p]):
                    d[p].append([1, Ngramma[1:]])
            # finito con questa parola: passa alle seguenti
            Ngramma.pop(0)
            if file_in.readable():
                Ngramma.append(file_in.readline()[:-1])
            else:
                Ngramma.append("")

def genera(dizionario, testo):
    """Dato un dizionario di frequenze di frasi che seguono una data parola
        e un testo, genera un testo in output."""
    token = analizza_testo(testo)
    output = ""
    if len(token) == 0:
        last = ""
    else:
        last = token[-1]
    while last in dizionario:
        # Sceglie a caso una lista di parole seguenti last
        casi = dizionario[last]
        # Calcola in n_casi il numero di liste di parole seguenti
        # contato con la propria frequenza
        n_casi = 0
        for e in casi:
            n_casi += e[0]
        caso = random.randrange(n_casi)
        i = 0
        x = 0   # quando x > caso scegliamo la lista di parole i-esima
        while i < len(casi):
            x += casi[i][0]
            if x > caso:
                for e in casi[i][1]:
                    if e[0].isalnum():
                       output += " " 
                    output += e
                    if e == "" or e == ".":
                        last = ""
                        break
                    last = e
                i = len(casi)   # per uscire dal while
            i += 1
    return output

import pickle
import markov

NOME = "gramsci.txt"
# Se il file NOME.pkl esiste lo carica, se no lo crea e lo salva
try:
    with open(NOME + ".pkl", "rb") as f:
        gramsci_dixit = pickle.load(f)
except:
    markov.analizza(NOME)
    gramsci_dixit = {}
    markov.dizionario(gramsci_dixit, NOME + ".tok", 5)
    with open(NOME + '.pkl', 'wb') as f:
        pickle.dump(gramsci_dixit, f, pickle.HIGHEST_PROTOCOL)

print("Conversazione con un pazzo che si crede Gramsci:")
while True:
    domanda = input(">")
    if domanda == "":
        break
    if domanda[-1] in [".", "?", "!"]:
        domanda = domanda[:-1]
    risposta = markov.genera(gramsci_dixit, domanda)
    print(risposta)

import pickle
import markov

NOME = "Gramsci"
NOME_FILE = "gramsci.txt"
ENC = "utf-8"

# Se il file NOME.pkl esiste lo carica, se no lo crea e lo salva
try:
    with open(NOME_FILE + ".pkl", "rb") as f:
        dixit = pickle.load(f)
except:
    markov.analizza(NOME_FILE, enc=ENC)
    dixit = {}
    markov.dizionario(dixit, NOME_FILE + ".tok", 5)
    with open(NOME_FILE + '.pkl', 'wb') as f:
        pickle.dump(dixit, f, pickle.HIGHEST_PROTOCOL)

print("Conversazione con un pazzo che si crede", NOME)
while True:
    domanda = input("Tu - ")
    if domanda == "":
        break
    if domanda[-1] in [".", "?", "!", ";", ","]:
        domanda = domanda[:-1]
    risposta = markov.genera(dixit, domanda)
    print(NOME, "-", risposta)

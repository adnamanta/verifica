# PROPOSTA MAGAZZINO

# Utilizzo  una classe per ogni funzione dell'esercizio precedente.
# Ogni classe rappresenta un parametro della classe Prodotto.
# Le classi Nome, Codice, Prezzo e Quantità contengono al loro interno le funzioni per gestire l'inserimento e la modifica delle
#proprietà

#creiamo una classe magazzino ed una classe prodotto che ha come proprietà 
#nella classe magazzino ci mettiamo una lista che contiene prodotti 
#prodotto che ha quantita prezzo codice e nome 

#iniazializziamo i quattro attributi 
#associamo a ciascuna di essi una funzione un metodo 
# che controllera la validità del valore 
#avremo quatto metodi che oltrte a modificare il prezzo lo cerchiamo anche
#fatto cio andiamo ad aggiungere il valore alla lista 
#per il contenuto di ciascun metoto prodotto. prezzo 
#fare una funzione che ricerca i prodotti e una funzione che ricerca il magazzino 
#la funzione che ricerca il prodotto ributta direttamente il prodotto 
#se esiste  
#ci sara sempre l'opzione per uscire pero non è all'interno della classe


class Prodotto():
    def __init__(self, nome="", codice="", prezzo=0.0, quantita=0):
        self.nome = Nome(nome)
        self.codice = Codice(codice)
        self.prezzo = Prezzo(prezzo)
        self.quantita = Quantita(quantita)
class Nome:
    def __init__(self, nomeprodotto):
        self.valore = nomeprodotto

    def modifica(self):
        if not self.nomeprodotto:
            self.nomeprodotto = input("Inserisci il nome del prodotto: ")
        else:
            print(f"Nome del prodotto: {self.nomeprodotto}")
            modifica = input("Vuoi modificare il nome? (s/n): ")
            if modifica.lower() == 's':
                self.nomeprodotto = input("Inserisci il nuovo nome del prodotto: ")
                print(f"Nome aggiornato a: {self.nomeprootto}")
        input("Premi invio per continuare")


class Codice:
    def __init__(self, codiceprodotto):
        self.codiceprodotto = codiceprodotto

    def modifica(self):
        print(f"Codice attuale: {self.codiceprodotto}")
        modifica = input("Vuoi modificare il codice? (s/n): ")
        if modifica.lower() == 's':
            self.codiceprodotto = input("Inserisci il nuovo codice: ")
            print(f"Codice aggiornato a: {self.codiceprodotto}")
        input("Premi invio per continuare")


class Prezzo:
    def __init__(self, prezzoprodotto):
        self.prezzoprodotto = prezzoprodotto

    def modifica(self):
        if self.prezzoprodotto == 0:
            while True:
                nuovo_prezzo = input("Inserisci il prezzo del prodotto: ")
                try:
                    nuovo_prezzo_float = float(nuovo_prezzo)
                    if nuovo_prezzo_float >= 0:
                        self.prezzoprodotto = nuovo_prezzo_float
                        print(f"Prezzo inserito: {self.prezzoprodotto:.2f}")
                        break
                    else:
                        print("Il prezzo non può essere negativo.")
                except ValueError:
                    print("Prezzo non valido. Inserisci solo numeri.")
        else:
            print(f"Prezzo attuale: {self.prezzoprodotto:.2f}")
            modifica = input("Vuoi modificare il prezzo? (s/n): ")
            if modifica.lower() == 's':
                while True:
                    nuovo_prezzo = input("Inserisci il nuovo prezzo: ")
                    try:
                        nuovo_prezzo_float = float(nuovo_prezzo)
                        if nuovo_prezzo_float >= 0:
                            self.valore = nuovo_prezzo_float
                            print(f"Prezzo aggiornato a: {self.valore:.2f}")
                            break
                        else:
                            print("Il prezzo non può essere negativo.")
                    except ValueError:
                        print("Prezzo non valido. Inserisci solo numeri.")
        input("Premi invio per continuare")


class Quantita:
    def __init__(self, quantita_prodotto):
        self.quantita_prodotto = quantita_prodotto

    def modifica(self):
        if self.valore == 0:
            nuova_quantita = int(input("Inserisci la quantità del prodotto: "))
            self.valore = nuova_quantita
            print(f"Quantità inserita: {self.quantita_prodotto}")
        else:
            print(f"Quantità attuale: {self.quantita_prodotto}")
            modifica = input("Vuoi modificare la quantità? (s/n): ")
            if modifica.lower() == 's':
                nuova_quantita = int(input("Inserisci la nuova quantità: "))
                self.quantita_prodotto = nuova_quantita
                print(f"Quantità aggiornata a: {self.quantita_prodotto}")
        input("Premi invio per continuare")


class Magazzino:
    def __init__(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)

    def mostra_magazzino(self):
        print("Oggetti nel magazzino:")
        for prodotto in self.prodotti:
            prodotto.mostra_info()

    def ricerca_prodotto(self, nome):
        for prodotto in self.prodotti:
            if prodotto.nome.valore.lower() == nome.lower():
                return prodotto
        print("Prodotto non esistente.")
        input("Premi invio per continuare")
        return None

    def gestione_magazzino(self):
        while True:
            scelta = input("""
Invia 1 se vuoi inserire un nuovo prodotto
Invia 2 se vuoi modificare il prezzo di un prodotto
Invia 3 se vuoi modificare la quantità di un prodotto
Invia 4 se vuoi modificare il nome di un prodotto
Invia 5 se vuoi modificare il codice di un prodotto
Invia 6 se vuoi vedere tutto l'inventario
Invia 7 se vuoi uscire dal programma
>>> """)
            if scelta == "1":
                nuovo_prodotto = Prodotto()
                nuovo_prodotto.nome.modifica()
                nuovo_prodotto.codice.modifica()
                nuovo_prodotto.prezzo.modifica()
                nuovo_prodotto.quantita.modifica()
                self.aggiungi_prodotto(nuovo_prodotto)

            elif scelta in ["2", "3", "4", "5"]:
                nome_prodotto = input("Inserisci il nome del prodotto da modificare: ")
                prodotto = self.ricerca_prodotto(nome_prodotto)
                if prodotto:
                    if scelta == "2":
                        prodotto.prezzo.modifica()
                    elif scelta == "3":
                        prodotto.quantita.modifica()
                    elif scelta == "4":
                        prodotto.nome.modifica()
                    elif scelta == "5":
                        prodotto.codice.modifica()

            elif scelta == "6":
                self.mostra_magazzino()

            elif scelta == "7":
                print("Programma in chiusura.")
                break

            else:
                print("Scelta non valida. Riprova.")


magazzino = Magazzino()
magazzino.gestione_magazzino()

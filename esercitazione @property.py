

#esercitazione @property


class Persona:
    def __init__(self, nome, età,sesso,indirizzo):
        self.nome = nome
        self._età = None #questo undercore si mette perche retituisce 
        self.età = età  # usa il setter per la validazione
        self._sesso=None
        self.sesso=sesso
        self._indirizzo=None
        self.indirizzo=indirizzo
        
        

    # Getter per l'attributo "età"
    @property #decoratore 
    def età(self):
        return self._età
    # Setter per l'attributo "età" con validazione
    @età.setter
    def età(self, valore):
        if valore >= 0:
            self._età = valore
        else:
            raise ValueError("L'età non può essere negativa")

    @property
    def sesso(self):
        return self._sesso
    
    @sesso.setter
    def sesso(self,valore):
        if valore =="SHE":
            self.sesso = valore
        elif valore == "HER":
            self.sesso= valore
        elif valore == "THEY":
            self.sesso= valore
        else:
            raise ValueError("")
        
class Persona:
    def __init__(self, nome, età, sesso, indirizzo):
        self.nome = nome
        self._età = None  # Questo underscore si usa per indicare che è privato
        self.età = età  # Usa il setter per la validazione
        self._sesso = None
        self.sesso = sesso
        self._indirizzo = None
        self.indirizzo = indirizzo

    # Getter per l'attributo "età"
    @property
    def età(self):
        return self._età

    # Setter per l'attributo "età" con validazione
    @età.setter
    def età(self, valore):
        if valore >= 0:
            self._età = valore
        else:
            raise ValueError("L'età non può essere negativa")

    @property
    def sesso(self):
        return self._sesso

    @sesso.setter
    def sesso(self, valore):
        if valore == "SHE":
            self._sesso = valore
        elif valore == "HER":
            self._sesso = valore
        elif valore == "THEY":
            self._sesso = valore
        else:
            raise ValueError("Valore di sesso non valido")





#esercizio trovare l'area del quadrato


import math

class Quadrato:
    def __init__(self,lato):
        self._lato = None
        self.lato = lato
    
    @property
    def lato(self):
        return self._lato
    
    @lato.setter
    def lato(self,valore):
        if valore < 0:
            raise ValueError("il lato non può essere negativo")
        self._lato = valore
        
    @property
    def area(self):
        return math.pi* (self._lato*2)
    
quadrato =Quadrato(4)
print ("lato",quadrato.lato)
print("area",quadrato.area)
    
#titolo numero di pagine attributi privati
#classe di libri 
#autore di libri attributi privati
#protetto titolo

class Libri:
    def __init__(self,titolo,autore,numeroPagine):
        self._titolo = titolo
        self.__autore = autore
        self._numeroPagine = numeroPagine
    
libro = Libri("Espiazione","IanMcEwan",388)
print (libro._titolo)


#decoratori delle funzioni esercizio

def decoratore(func): #decoratore 
    def wrapper(*args, **kwargs):
        print("Inizio del' esercizio...") #
        result = func(*args, **kwargs)
        print("Fine del'esercizio...")
        return result
    return wrapper

# Usare il decoratore
@decoratore
def saluta():
    print("Halo!")

# Eseguire la funzione decorata
saluta()


import pandas as pd  # Importa la libreria Pandas per la gestione dei DataFrame
import time  # Importa il modulo time per misurare il tempo di esecuzione

# Definizione del decoratore per misurare il tempo di esecuzione
def timer_decorator(func):  # Definisce un decoratore che prende una funzione come argomento
    def wrapper(*args, **kwargs):  # Funzione interna che agirà come wrapper attorno alla funzione originale
        start_time = time.time()  # Registra il tempo di inizio dell'esecuzione
        result = func(*args, **kwargs)  # Chiama la funzione originale e memorizza il risultato
        end_time = time.time()  # Registra il tempo di fine dell'esecuzione
        # Stampa il tempo di esecuzione della funzione
        print(f"Tempo di esecuzione di {func.__name__}: {end_time - start_time} secondi")
        return result  # Restituisce il risultato della funzione originale
    return wrapper  # Restituisce il wrapper come nuova funzione decorata

# Applicazione del decoratore a una funzione che effettua una semplice operazione con Pandas
@timer_decorator  # Utilizza il decoratore sopra definito
def process_dataframe(df):  # Definisce una funzione che accetta un DataFrame come argomento
    # Esempio di operazione: calcolo della somma delle colonne
    return df.sum()  # Restituisce la somma di ogni colonna del DataFrame

# Creazione di un DataFrame di esempio
data = {  # Dizionario che contiene i dati da inserire nel DataFrame
    'A': [1, 2, 3, 4, 5],  # Colonna A con valori da 1 a 5
    'B': [6, 7, 8, 9, 10],  # Colonna B con valori da 6 a 10
    'C': [11, 12, 13, 14, 15]  # Colonna C con valori da 11 a 15
}
df = pd.DataFrame(data)  # Crea un DataFrame Pandas dai dati forniti

# Chiamata alla funzione decorata
result = process_dataframe(df)  # Chiama la funzione process_dataframe con il DataFrame df
print("Risultato:", result)  # Stampa il risultato della somma delle colonne

# In questo esempio, abbiamo definito un decoratore chiamato timer_decorator 
# che misura il tempo di esecuzione di una funzione. Questo decoratore può 
# essere applicato a qualsiasi funzione, incluso un'operazione che coinvolge 
# Pandas come nel nostro caso.

# Quando chiamiamo process_dataframe(df), il decoratore viene applicato 
# automaticamente alla funzione process_dataframe. Il decoratore registra
# il tempo di inizio prima di chiamare la funzione e il tempo di fine dopo 
# che la funzione è stata eseguita. Infine, calcola la differenza tra questi
# tempi per determinare il tempo di esecuzione effettivo della funzione e 
# lo stampa a schermo.

#matrice e prodotto matriciale 
#algebra lineare e trigonometria 
#mtrice inversa 
#logaritmo

#
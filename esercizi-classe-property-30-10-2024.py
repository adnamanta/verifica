


#esercitazione lezione classi e proprietà 30-10-2024


class Libri:
    genere = "Fantasy"  # Attributo di classe

    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    @classmethod
    def descrivi_genere(cls):
        print(f"Tutti i libri sono {cls.genere}")
        #una creazione all'interno della stessa classe senza un costruttore con un metodo di clasee

    @classmethod     #oggetto lo andiamo a creare attraverso il copstruttore i una classe #
    def crea_libro(cls, titolo):  #l'istanza della classe è comunque l'oggetto istanza(DERIVA DA - DALLA CLASSE)
        return cls(titolo, autore= "Tolkien")  # Crea un'istanza della classe con autore  = Tolkien 

# è UN ABBREVIAZIONE di un oggetto
# non sempre dobbiamo crere oggetti attraverso il 
#costruttore ma possiamo farlo attraverso lì'istanza di una classe 

# Uso di @classmethod
Libri.descrivi_genere()  # Output: Tutte le persone appartengono alla specie Homo sapiens
libro = Libri.crea_libro("Il Signore degli Anelli")  #stiamo creando un istanza senza un oggetto 
print(libro.titolo, libro.autore) 


class Automobile: 

    @staticmethod
    def accelera(a, b):
        return a * b 

    @staticmethod
    def rallenta(a, b):
        return a % b

# Uso di @staticmethod
print(Automobile.accelera(5, 3))         # Output: 8
print(Automobile.rallenta(10, 7))    # Output: 3

#creare una classe astratta sfruttando il concetto di animale 

#obbligare le classi figlie 

from abc import ABC, abstractmethod

class Animale(ABC):
    @abstractmethod
    def movimento(self):
        pass

class Cavallo(Animale):
    def movimento(self):
        return "va al Galoppo!"

class Coniglio(Animale):
    def movimento(self):
        return "salta!"

# Non si può istanziare una classe astratta
# animale = Animale()  # Errore: non si può istanziare una classe astratta

cavallo = Cavallo()
print(f'Il Cavallo  {cavallo.movimento()}')  # Output: Il cane dice: Bau!

coniglio = Coniglio()
print(f'Il Coniglio {coniglio.movimento()}')  # Output: Il gatto dice: Miao!


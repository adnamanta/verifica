"""
Verifica finale 
Realizzare un gioco in python 
utilizzando quanti più costrutti possibili studiati fino ad ora,
con commenti dettagliati e sintetici, 
possibilmente motivando quindi le scelte dei vari costrutti 
ed infine realizzare un' essenziale, grezza interfaccia utente 
per le interazioni con l'utente. 
"""

import random

# Classe base che rappresenta un combattente
class Combattente:
    def __init__(self, nome, vita, forza_attacco, abilita_speciale):
        self.nome = nome
        self.vita = vita
        self.forza_attacco = forza_attacco
        self.abilita_speciale = abilita_speciale
        self.abilita_usata = False  # Aggiunto per tracciare se l'abilità è stata usata

    def attacca(self):
        danno = self.forza_attacco + random.randint(5, 15)
        print(f"{self.nome} infligge {danno} danni!")
        return danno

    def subisci(self, danno, difesa=False):
        if difesa:
            danno = int(danno * 0.5)  # Riduce il danno subito se si difende (50%)
            print(f"{self.nome} si difende, riducendo i danni!")
        self.vita -= danno
        if self.vita <= 0:
            self.vita = 0
        print(f"{self.nome} ha {self.vita} punti vita rimasti.")

    def usa_abilita(self, avversario):
        if not self.abilita_usata:  # Controllo se l'abilità è già stata usata
            self.abilita_speciale(avversario)
            self.abilita_usata = True
        else:
            print(f"{self.nome} ha già usato la sua abilità speciale!")

# Funzione abilità speciale per Spadaccino
def abilita_spadaccino(avversario):
    danno_extra = random.randint(25, 40)
    avversario.subisci(danno_extra)
    print(f"Lo Spadaccino infligge {danno_extra} danni extra con l'abilità speciale!")

# Funzione abilità speciale per Lanciere
def abilita_lanciere(avversario):
    danno_extra = random.randint(20, 35)
    avversario.subisci(danno_extra)
    print(f"Il Lanciere infligge {danno_extra} danni extra con l'abilità speciale!")

# Funzione abilità speciale per Berserker
def abilita_berserker(avversario):
    cura = random.randint(20, 40)
    print(f"Il Berserker si rigenera di {cura} punti vita!")
    avversario.subisci(cura)
    print(f"Il Berserker infligge {cura} danni all'avversario con l'abilità speciale!")

# Classi per i combattenti
class Lanciere(Combattente):
    def __init__(self, nome):
        vita = 120
        forza_attacco = 18
        super().__init__(nome, vita, forza_attacco, abilita_lanciere)

class Spadaccino(Combattente):
    def __init__(self, nome):
        vita = 110
        forza_attacco = 20
        super().__init__(nome, vita, forza_attacco, abilita_spadaccino)

class Berserker(Combattente):
    def __init__(self, nome):
        vita = 150
        forza_attacco = 25
        super().__init__(nome, vita, forza_attacco, abilita_berserker)

# Classe per la gestione dello scontro
class Battaglia:
    def __init__(self, combattente1, combattente2):
        self.combattente1 = combattente1
        self.combattente2 = combattente2
        self.turno = 1

    def inizia(self):
        print("\n--- Inizia il combattimento! ---")
        
        # Ciclo per 3 turni o fino alla morte di un combattente
        while self.combattente1.vita > 0 and self.combattente2.vita > 0 and self.turno <= 3:
            print(f"\n--- Turno {self.turno} ---")
            
            # Turno del combattente 1
            self.turno_combattente(self.combattente1, self.combattente2)
            if self.combattente2.vita <= 0:
                break  # Se il secondo combattente è morto, termina il combattimento

            # Turno del combattente 2
            self.turno_combattente(self.combattente2, self.combattente1)
            if self.combattente1.vita <= 0:
                break  # Se il primo combattente è morto, termina il combattimento

            self.turno += 1

        # Risultato della battaglia
        self.risultato()

    def turno_combattente(self, combattente, avversario):
        print(f"\n{combattente.nome}, è il tuo turno!")
        print("Scegli la tua mossa:")
        print("1: Attaccare normalmente")
        print("2: Difendersi (riduce i danni subiti)")
        print("3: Usare abilità speciale (una volta per battaglia)")

        scelta = input("Cosa vuoi fare? (1/2/3): ")

        if scelta == "1":
            danno = combattente.attacca()
            avversario.subisci(danno)
        elif scelta == "2":
            danno_avversario = avversario.attacca()
            combattente.subisci(danno_avversario, difesa=True)
        elif scelta == "3":
            combattente.usa_abilita(avversario)
        else:
            print("Scelta non valida! Usa 1, 2 o 3.")
            self.turno_combattente(combattente, avversario)  # Riprova il turno

    def risultato(self):
        if self.combattente1.vita > 0 and self.combattente2.vita <= 0:
            print(f"{self.combattente1.nome} ha vinto!")
        elif self.combattente2.vita > 0 and self.combattente1.vita <= 0:
            print(f"{self.combattente2.nome} ha vinto!")
        else:
            print("La battaglia è terminata in pareggio!")

# Funzione che avvia il gioco
def avvia_partita():
    print("Benvenuto al gioco di battaglia!")
    nome = input("Inserisci il nome del tuo combattente: ")

    # Selezione del combattente
    while True:
        scelta = input("Scegli il tuo guerriero: (1 per Spadaccino, 2 per Lanciere, 3 per Berserker): ")
        if scelta == "1":
            combattente = Spadaccino(nome)
            break
        elif scelta == "2":
            combattente = Lanciere(nome)
            break
        elif scelta == "3":
            combattente = Berserker(nome)
            break
        else:
            print("Scelta non valida! Devi scegliere 1, 2 o 3. Ripeti.")

    # Inserimento del nome dell'avversario
    nome_avversario = input("Inserisci il nome del tuo avversario: ")

    # Selezione dell'avversario
    while True:
        scelta_avversario = input("Scegli il tipo di avversario: (1 per Spadaccino, 2 per Lanciere, 3 per Berserker): ")
        if scelta_avversario == "1":
            avversario = Spadaccino(nome_avversario)
            break
        elif scelta_avversario == "2":
            avversario = Lanciere(nome_avversario)
            break
        elif scelta_avversario == "3":
            avversario = Berserker(nome_avversario)
            break
        else:
            print("Scelta non valida! Devi scegliere 1, 2 o 3. Ripeti.")

    # Crea e avvia la battaglia
    battaglia = Battaglia(combattente, avversario)
    battaglia.inizia()

# Avvia il gioco
avvia_partita()

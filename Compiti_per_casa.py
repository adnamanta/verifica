#COMPITI PER CASA

"""Uno switch-case in Java 
è una struttura di controllo che permette di eseguire diverse parti
di codice in base al valore di una variabile. È utile quando hai
più condizioni da controllare e vuoi evitare un lungo elenco di if-else."""


# MATRIX

print("MATRIX")

scelta = input("È la tua ultima occasione: se rinunci, non ne avrai altre....scegli tra pilloa azzurra o rossa")


if scelta.lower() == "pillola azzurra":
    print("Fine della storia, domani ti sveglierai in camera tua e crederai a quello che vorrai.")
elif scelta.lower() == "pillola rossa":
    print("Resti nel paese delle meraviglie e vedrai quant'è profonda la tana del bianconiglio.")
else:
    print("Ti sto offrendo solo la verità.")


#FRIENDSHIP 
print("Friendship")

amici = input("Mi vuoi bene? (Rispondi 'si', 'no' o 'forse'): ").lower()

if amici in {"si"}:
    print("(o￣∇￣o)/")
elif amici in {"no"}:
    print("(╥﹏╥)")
elif amici in {"forse"}:
    print("(｡◕‿◕｡)")
else:
    print("(￣口￣) - Risposta non valida!")


#DO WHILE IN PYTHON 

"""In Python non esiste un costrutto do while nativo come in altri linguaggi,
ma puoi simularlo usando un ciclo while. Il ciclo do while esegue il blocco 
di codice almeno una volta prima di controllare la condizione."""


# verifica IN CLASSE 



voti = []


materie = ["italiano", "matematica", "inglese", "geografia", "arte", "scienze", "educazione fisica"]


for materia in materie:
    voto = float(input("Inserire il voto per", materia))  
    voti.append(voto)


somma_voti = sum(voti)


media_voti = somma_voti / len(voti)

voto_piu_alto = max(voti)
voto_piu_basso = min(voti)


print("La media dei voti è:", media_voti)
print("Il voto più alto è:" ,voto_piu_alto)
print("Il voto più basso è:", voto_piu_basso)

def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b != 0:
        return a / b
    else:
        return "Errore: divisione per zero!"

operazione = input("Che operazione vuoi svolgere? (+, -, *, /): ")

numero_a = float(input("Inserisci il primo numero: "))
numero_b = float(input("Inserisci il secondo numero: "))

if operazione == "+":
    risultato = somma(numero_a, numero_b)
elif operazione == "-":
    risultato = sottrazione(numero_a, numero_b)
elif operazione == "*":
    risultato = moltiplicazione(numero_a, numero_b)
elif operazione == "/":
    risultato = divisione(numero_a, numero_b)
else:
    risultato = "Operazione non valida!"

print("Il risultato è:", risultato)

"""si può creare  anche un  dizionario """


""" realizzare in un unica funzione chiamata geometra
la possibilità di chiedere all'utente alcuni dati 
come per esempio una figura geometrica e le sue dimensioni, 
affinche si svolgano i calcoli relativi alla figura scelta """


def geometra():
    figura_geometrica = input("Scegli una forma geometrica (triangolo, quadrato, cerchio, rettangolo): ").lower()

    if figura_geometrica == "triangolo":
        base_t = float(input("Inserisci valore base triangolo: "))
        altezza_t = float(input("Inserisci valore altezza triangolo: "))
        area = base_t * altezza_t / 2
        print("L'area del triangolo è:" , area )

    elif figura_geometrica == "quadrato":
        lato = float(input("Inserisci valore lato quadrato: "))
        area = lato * lato
        print("L'area del quadrato è:", area )

    elif figura_geometrica == "cerchio":
        raggio = float(input("Inserisci valore raggio: "))
        p_greco = 3.14
        area = p_greco * raggio ** 2
        print("L'area del cerchio è:", area )

    elif figura_geometrica == "rettangolo":
        base_rettangolo = float(input("Inserisci valore base rettangolo: "))
        altezza_rettangolo = float(input("Inserisci valore altezza rettangolo: "))
        area = base_rettangolo * altezza_rettangolo
        print("L'area del rettangolo è:", area )

    else:
        print("Forma geometrica non riconosciuta. Riprova.")


geometra()
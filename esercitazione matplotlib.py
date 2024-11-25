

import matplotlib.pyplot as plt

#dati da plottare 

x= [1,2,3,4,5]
y= [1,4,9,16,25]

#creazione del grafico 
plt.plot(x,y)

#plt la classe plt è una funzione x,y sono i parametri delle funzioni 

#etichette per gli assi

plt.xlabel('X axis Label')
plt.ylabel('Y axis Label')

#titolo del grafico
plt.title('simpleLine Graph')

#mostra il grafico
plt.show()

#metodi statici non hanno bisogno dell'oggetoo

#lista di stringhe e lista di numeri

x= ['Giorno','Mese','Anno','Numero']
y=[12,6,2020,36]

#grafico a barre 
plt.bar(x,y)

#etichette e titolo
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.title('Statistiche')

#mosta il grafico

plt.show()


#un grafico a dispersione - utile per una serie di dati 
#i programmi vanno scritti iniziando con le variabili
"""
x=[10,20,30,40,50,60,70,80]
y=[1,2,3,4,5,6,7,8]

plt.scatter(x,y)

#etichette e titolo
plt.xlabel()

plt.show()
"""

#dati
oggetti=['cd','libri','dvd','quadri']
quantita=[30,100,40,10]

plt.pie(quantita, labels=oggetti,autopct='%1.1f%%')

plt.title('grafico a torta')

plt.show()


#creare un istogramma 

#dati es. voti di un esame 
data=[18,30,64,87,90,56,22,11,37,65,98,100,39]

#creazione dell'istogramma 
plt.hist(data,bins=5,edgecolor='black')

#etichette e titolo
#etichette e titolo 

plt.xlabel('voti')
plt.ylabel('valore')
plt.title('studente 1')

plt.show()

#dati per due linee 
x=[1,2,3,4,5]
y1=[1,24,9,10,25]
y2=[25,16,9,4,1]

#grafico per la prima linea
plt.plot(x,y1,label='Line1')

#grafico per la seconda linea 
plt.plot(x,y2,label= 'Line2')

#aggiungere una leggenda 
plt.legend()

#Ertichette e citolo

plt.show()


#grafico personalizzato
x=[1,2,3,4,5,6,7,8,9,10]
y=[10,20,30,40,50,60,70,80,90,100]
#grafico con linea rossa tratteggiata e spessore della linea 
plt.plot(x,y, color='red',linestyle='--', linewidth=2)



#perch usare matplotlib


armi=['spada','lancia','spadone','arco','catalizzatore']
danno=[26,18,39,21,36]

import os 
current_directory


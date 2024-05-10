import pandas as pd


#parametro della series un array
grades=pd.Series([87, 100, 94])
print(grades)
#array che ripete tre volte lo stesso valore
g2=pd.Series(98.6, range(3))
print(g2)
#visualizzazione dell'array nella posizione 1
print(grades[1])
#operatori di conteggio
print(grades.count())
print(grades.mean())
print(grades.min())
print(grades.max())
#visualizza tutti gli operatori di conteggio
print(grades.describe())
#possibilità di creare indici diversi dagli interi, come le stringhe
grad=pd.Series([87, 100, 94], index=['Wally', 'Eva', 'Sam'])
print(grad)
#argomento della series un dizionario, in cui le chiavi diventano indici
g=pd.Series({'Wally': 87, 'Eva': 100, 'Sam':94})
print(g)
#leggere il contenuto di un elemento della serie con indice personalizzato
print(g['Eva'])
#leggere l'elemento dell'array utilizzando il punto 
print(g.Wally)
#conoscere il tipo dei dati dell'array
print(g.dtype)
#visualizza tutto l'array
print(g.values)
#creare serie di oggetti di tipo stringa
hardware=pd.Series(['Tenaglia', 'Sega', 'Martello'])
print(hardware)
#verifica se le stringhe della serie contengono la lettera g
print(hardware.str.contains('g'))
#crea una nuova serie in cui tutte le stringhe contenute nella serie in lettere maiuscole
print(hardware.str.upper())

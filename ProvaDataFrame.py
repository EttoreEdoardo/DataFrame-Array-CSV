#DataFrame array bidimensionale potenziato, possono avere indici personaloizzati per righe e per colonne, 
#offrono operazioni e funzionalità aggiuntive che li rendono utili per il data science. 
#Ogni colonna di un oggetto Dataframe è un oggetto Series

import pandas as pd

#Creare oggetti DataFrame a partire da un dizionario

grades_dict={'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie':[100, 81, 82], 'Bob': [83, 65, 85]}
grades= pd.DataFrame(grades_dict)
print(grades)
print()

#personalizzazione degli indici
pd.DataFrame(grades_dict, index=['Test1', 'Test2', 'Test3'])
grades.index=['Test1', 'Test2', 'Test3']
#Accesso alle colonne di un dataFrame

print(grades['Eva'])
print()
#visualizzare i voti di Sam si può usare come atrributo
print(grades.Sam)
print()
#selezionare righe con gli attributi loc e iloc,
#grazie all'attributo loc si può accedere ad una riga usando la sua etichetta
#elencare tutti i voti della riga Test1
print(grades.loc['Test1'])
print()
#accedere alle righe con indici interi a partire da 0 con l'attributo iloc
print(grades.iloc[1])
print()
#selezionare righe con gli attributi loc e iloc usando il porzionamento e liste
#elencare i voti della seconda riga

print(grades.loc['Test1': 'Test3'])
print()
#quando si usano porzioni di interi con iloc, l'intervallo specificato esclude l'indice più alto
print(grades.iloc[0:2])
print()
#per selezionare righe specifiche, si utilizzi una lista piuttosto che la notazione delle porzioni con loc o iloc:

print(grades.loc[['Test1', 'Test3']])
print()
print(grades.iloc[[0,2]])
print()
#selezionare sottoinsiemi di righe e colonne: vedere solo i voti del Test1 e delTest2 di Eva e Katie

print(grades.loc['Test1': 'Test2', ['Eva', 'Katie']])
print()
#usare iloc per selezionare il prmo e il terzo test e le prime tre colonne

print(grades.iloc[[0,2], 0:3])
print()

#Indicizzazione booleana: selezionare tutti i voti maggiori di 90, tutti quelli che non esistono sono Not a Number(valori mancanti)
print(grades[grades>=90])
print()
 #selezionare voti tra 80 e 90
print(grades[(grades>=80)&(grades<98)])
print()
#Accedere ad una determinata cella del dataframe

print(grades.at['Test2', 'Eva'])
print()

#assegnare nuovi valori a elementi specifici, cambiare il voto di Eva nel Test2 a 100 usando at

grades.at['Test2', 'Eva']=100
print(grades.at['Test2', 'Eva'])

#statistiche descrittive

print(grades.describe())
print()

#modificare la precisione e altri parametri predefiniti 
pd.set_option('precision', 2)

print(grades.describe())
print()
#trasporre righe con colonne T restituisce una vista trasposta

print(grades.T)
print()
#per ottenere le statistiche per test anzichè per studente

print(grades.T.describe())
print()
#media di tutti i voti degli studenti su ogni test
print(grades.T.mean())
print()
#ordinare per gli indici delle righe

print(grades.sort_index(ascending=False))
print()

#ordinare per gli indici delle colonne axis=1 si indica di ordinare gli indici delle colonne, per default axis=0 ordina indice righe

print(grades.sort_index(axis=1))
print()

#ordinare per i valori delle colonne

print(grades.sort_values(by='Test1', axis=1, ascending=False))
print()

print(grades.T.sort_values(by='Test1', ascending=False))
print()

#combinazione la selezione con l'ordinamento

print(grades.loc['Test1'].sort_values(ascending=False))
print()

#i metodi sort_index e sort_values restituiscono una copia del dataframe originale 
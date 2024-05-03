import csv
import pandas as pd
#import Matplotlib

#Creare file csv: file creato 'account.csv', 
#si raccomanda l'apertura del file con newline='' per avere i correttori di fine riga
with open('account.csv', mode='w', newline='') as accounts:
    writer=csv.writer(accounts)
    writer.writerow([100, 'Jones', 24.98])
    writer.writerow([200, 'Doe', 345.67])
    writer.writerow([300, 'White', 0.00])
    writer.writerow([400, 'Stone', -42.16])
    writer.writerow([500, 'Ritch', 224.62])
    writer.writerow([600, "Jones, Sue", 24.98])
    
#lettura di un file csv ogni record del csv devono avere tutti lo stesso numero di campi
with open('account.csv',mode='r', newline='') as accounts:
    print(f'{"Conto":<10}{"Nome":<10}{"Saldo":>10}')
    reader=csv.reader(accounts)
    for record in reader:
        account, name, balance=record
        print(f'{account:<10}{name:<10}{balance:>10}')
        
#leggere file CSV e inserirli nell'oggetto dataFrame di pandas in locale


df=pd.read_csv('account.csv', names=['conto', 'nome', 'saldo'])
print(df)

#per salvare un oggetto dataFrame in un file usando il formato CSV, si usa il metodo to_csv

df.to_csv('accounts_from_dataframe.csv', index=False)

#lettura di un file csv del Titanic Disaster Dataset

titanic=pd.read_csv('https://vincentarelbundock.github.io/' + 'Rdatasets/csv/carData/TitanicSurvival.csv')
print(titanic)
pd.set_option('precision', 2) #formato per valori floating-point
print(titanic.head())#fa vedere solo le prime 5 righe
print(titanic.tail())#fa vedere le ultime 5 righe

#personalizzazione dei nomi delle colonne si cambia rownamws in name e passengerrClass in class
titanic.columns=['name','survived', 'sex', 'age', 'class']
print(titanic.head())

#analisi dati, pandas ignora i dati mancanti

print(titanic.describe())

#determinare le statistiche sui sopravvissuti scegliendo la colonna survived con 'yes per ottenere un oggetto Series
# contenente valori True/False, e poi usare describe per riepilogare i risultati

print((titanic.survived=='yes').describe())

#Istogramma delle età dei passeggeri utilizza la libreria Matplotlib bisogna prima abilitare Matplotlib in IPython

histogram=titanic.hist()

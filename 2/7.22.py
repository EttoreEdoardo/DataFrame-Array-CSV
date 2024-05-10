import pandas as pd
import numpy as np

# Creare un oggetto Series dalla lista [7, 11, 13, 17]
lista_a = [7, 11, 13, 17]
serie_a = pd.Series(lista_a)
print("a. Oggetto Series dalla lista [7, 11, 13, 17]:")
print(serie_a)

# Creare un oggetto Series con cinque elementi tutti uguali a 100.0
serie_b = pd.Series(100.0, index=range(5))
print("\nb. Oggetto Series con cinque elementi tutti uguali a 100.0:")
print(serie_b)

# Creare un oggetto Series con 20 elementi scelti casualmente nell'intervallo da 0 a 100, e utilizzare il metodo describe per produrre le statistiche descrittive di base
serie_c = pd.Series(np.random.randint(0, 101, 20))
print("\nc. Oggetto Series con 20 elementi casuali nell'intervallo da 0 a 100:")
print(serie_c.describe())

# Creare un oggetto Series chiamato temperatures con valori e indici personalizzati
temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], index=['Julie', 'Charlie', 'Sam', 'Andrea'])
print("\nd. Oggetto Series chiamato 'temperatures' con valori e indici personalizzati:")
print(temperatures)

# Formare un dizionario dai nomi e dai valori dell'oggetto Series nel punto d, poi usare il dizionario per inizializzare un altro oggetto Series
dizionario_e = temperatures.to_dict()
serie_e = pd.Series(dizionario_e)
print("\ne. Oggetto Series inizializzato da un dizionario:")
print(serie_e)


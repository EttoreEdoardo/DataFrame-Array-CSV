import numpy as np
import pandas as pd

# Genera un array di 5 interi casuali nell'intervallo 30-50
temperatures_array = np.random.randint(30, 51, size=5)

# Converto l'array in un oggetto Series chiamato temperatures
temperatures = pd.Series(temperatures_array)

# Calcolo temperatura minima, massima e media
temp_min = temperatures.min()
temp_max = temperatures.max()
temp_mean = temperatures.mean()

# Stampa temperatura minima, massima e media
print("Temperatura minima:", temp_min)
print("Temperatura massima:", temp_max)
print("Temperatura media:", temp_mean)

# Produce statistiche descrittive
print("\nStatistiche descrittive:")
print(temperatures.describe())

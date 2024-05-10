import pandas as pd

# 1) Creare un oggetto DataFrame chiamato temperatures da un dizionario:
temperature_dict = {'Maxine': [25, 27, 23], 'James': [22, 24, 21], 'Amanda': [26, 28, 25]}
temperatures = pd.DataFrame(temperature_dict)

# 2) Ricreare l'oggetto DataFrame con indici personalizzati e indici di riga:
temperatures_custom_index = pd.DataFrame(temperature_dict, index=['Morning', 'Afternoon', 'Evening'])

# 3) Selezionare la colonna delle letture di 'Maxine':
maxine_column = temperatures_custom_index['Maxine']

# 4) Selezionare la riga delle letture 'Morning':
morning_row = temperatures_custom_index.loc['Morning']

# 5) Selezionare le righe 'Morning' e 'Evening':
morning_evening_rows = temperatures_custom_index.loc[['Morning', 'Evening']]

# 6) Selezionare le colonne 'Amanda' e 'Maxine':
amanda_maxine_columns = temperatures_custom_index[['Amanda', 'Maxine']]

# 7) Selezionare gli elementi di 'Amanda' e 'Maxine' nelle righe 'Morning' e 'Afternoon':
amanda_maxine_morning_afternoon = temperatures_custom_index.loc[['Morning', 'Afternoon'], ['Amanda', 'Maxine']]

# 8) Usare il metodo describe per produrre le statistiche descrittive:
description = temperatures_custom_index.describe()

# 9) Trasporre temperatures:
transposed_temperatures = temperatures_custom_index.T

# 10) Ordinare le colonne in ordine alfabetico:
sorted_temperatures = temperatures_custom_index.sort_index(axis=1)

# Stampa dei risultati:
print("2) Oggetto DataFrame con indici personalizzati:")
print(temperatures_custom_index)

print("\n3) Colonna delle letture di 'Maxine':")
print(maxine_column)

print("\n4) Riga delle letture 'Morning':")
print(morning_row)

print("\n5) Righe 'Morning' e 'Evening':")
print(morning_evening_rows)

print("\n6) Colonne 'Amanda' e 'Maxine':")
print(amanda_maxine_columns)

print("\n7) Elementi di 'Amanda' e 'Maxine' nelle righe 'Morning' e 'Afternoon':")
print(amanda_maxine_morning_afternoon)

print("\n8) Statistiche descrittive di temperatures:")
print(description)

print("\n9) Trasposta di temperatures:")
print(transposed_temperatures)

print("\n10) temperatures con colonne ordinate in ordine alfabetico:")
print(sorted_temperatures)

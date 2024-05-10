import pandas as pd

# Dizionario delle temperature
temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82], 'Thu': [75, 97], 'Fri': [62, 79]}

# a. Convertire il dizionario in un DataFrame chiamato temperature con due indici 'Low' e 'High'
temperature = pd.DataFrame(temps, index=['Low', 'High'])

# Visualizza il nuovo oggetto DataFrame
print("DataFrame 'temperature':")
print(temperature)

# b. Scegliere solo le colonne da 'Mon' a 'Wed'
selected_columns = temperature.loc[:, 'Mon':'Wed']
print("\nColonne da 'Mon' a 'Wed':")
print(selected_columns)

# c. Selezionare solo le temperature minime di ogni giorno
min_temperatures = temperature.loc['Low']
print("\nTemperature minime di ogni giorno:")
print(min_temperatures)

# d. Impostare la precisione della virgola mobile a 2, poi calcolare la temperatura media di ogni giorno
mean_temperatures = temperature.mean(axis=1).round(2)
# Stampa della temperatura media di ogni giorno
print("\nTemperatura media di ogni giorno:")
print(mean_temperatures)

# e. Calcolare la media delle temperature massime e di quelle minime
mean_max_temperature = temperature.loc['High'].mean()
mean_min_temperature = temperature.loc['Low'].mean()
print("\nMedia delle temperature massime:", mean_max_temperature)
print("Media delle temperature minime:", mean_min_temperature)

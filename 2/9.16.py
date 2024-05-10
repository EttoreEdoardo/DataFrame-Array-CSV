import pandas as pd

# hhtps://www.kaggle.com/diamonds.csv
# titanic=pd.read_csv('hhtps://www.kaggle.com/diamonds.csv') diamonds_df = pd.read_csv('diamonds.csv', index_col=0)

# a) Caricare il dataset in un DataFrame Pandas con la prima colonna di ogni record come indice:
diamonds_df=pd.read_csv('https://www.kaggle.com/diamonds.csv')

# b) Visualizzare le prime sette righe dell'oggetto DataFrame:
print("Prime sette righe del DataFrame:")
print(diamonds_df.head(7))

# Visualizzare le ultime sette righe dell'oggetto DataFrame:
print("\nUltime sette righe del DataFrame:")
print(diamonds_df.tail(7))

# c) Utilizzare il metodo describe per calcolare le statistiche descrittive delle colonne numeriche:
print("\nStatistiche descrittive delle colonne numeriche:")
print(diamonds_df[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']].describe())

# d) Utilizzare il metodo describe per calcolare le statistiche descrittive delle colonne con dati categorici:
print("\nStatistiche descrittive delle colonne categoriche:")
print(diamonds_df[['cut', 'color', 'clarity']].describe())

# Trovare i valori di categoria univoci:
print("\nValori di categoria univoci per le colonne categoriche:")
print("Cut:", diamonds_df['cut'].unique())
print("Color:", diamonds_df['color'].unique())
print("Clarity:", diamonds_df['clarity'].unique())

# e) Abilitare Matplotlib per la visualizzazione grafica:
plt.hist('Worldwide gross', data=dataframe);

# Visualizzare gli istogrammi di ogni colonna con i dati numerici:
diamonds_df[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']].hist(bins=20, figsize=(12, 8))

import numpy as np

# Creazione di un array 2x2 con numeri da 0 a 3
array = np.arange(4).reshape(2, 2)

# a. Elevare al cubo ogni elemento del vettore
cubed_array = array ** 3
print("Array elevato al cubo:")
print(cubed_array)

# b. Aggiungere 7 ad ogni elemento del vettore
plus_seven_array = array + 7
print("\nArray con 7 aggiunto ad ogni elemento:")
print(plus_seven_array)

# c. Moltiplicare per 2 ogni elemento del vettore
multiplied_by_two_array = array * 2
print("\nArray moltiplicato per 2:")
print(multiplied_by_two_array)

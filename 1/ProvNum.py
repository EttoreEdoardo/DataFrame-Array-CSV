import numpy as np
#crea un array da un array già esistente

numbers= np.array([2, 3, 5, 7, 11])
print(type(numbers))
print(numbers)

#argomenti multidimensionali
n=np.array([[11, 2, 3], [4, 5, 6]])
print(n)

#creare un array a una dimensione a partire da una lista che produca gli interi pari da 2 a 20

n=np.array([x for x in range(2, 21, 2)])
print(n)

#creare un array 2x5  che contenga gli interi pari dsa 2 a 10 nella prima riga e gli interi dispari da 1 a 9 nella seconda riga

n=np.array([[x for x in range(2,11,2)],[y for y in range(1,10,2)]] )
print(n)

#determinare le dimensioni di un array

print(n. ndim)

#determinare il numero di righe e colonne

print(n.shape)

#determinare il numero di elementi totale di un array: righe x colonne

print(n.size)

#gli array iterabili
for r in n:
    for c in r:
        print(c, end= ' ')
    print()
    
#iterare un array con più dimensioni come se fosse a due dimensioni

for i in n.flat:
    print(i, end=' ')
    
#riempimento array con tutti zeri
print()
a=np.zeros(5)
print(a)
a=np.zeros(5, dtype=int)
print(a)

#riempimento tutti 1 2 righe e 4 colonne con interi

b=np.ones((2,4), dtype=int)
print(b)

#riempimento con un qualsiasi valore indicato

c=np.full((3,5), 13)
print(c)

#creare array a partire da intervalli
d=np.arange(5)
print(d)

e=np.arange(5,10)
print(e)

f= np.arange(10,1,-2)
print(f)

#trasformare un array monodimensionale in un multidimensionale attenti a dare le giuste dimensioni della suddivisione tra righe e colonne

q=np.arange(1,21).reshape(4, 5)
print(q)

#visualizzazione di array molto grandi
h=np.arange(1,100001).reshape(4, 25000)
print(h)
t=np.arange(1,100001).reshape(100, 1000)
print(t)

#creare un array di 20 interi pari tra 2 e 40, poi modificarlo per farlo diventare un array 4x5

x=np.arange(2,41,2).reshape(4,5)
print(x)

#operazioni sugli array
numbers =np.arange(1,6)
print(numbers)

n1=numbers*2
print(n1)

n2=numbers**3
print(n2)

n3= numbers+10
print(n3)

#metodi di calcoli media, summa, max, min

grades=np.array([[87, 96, 70], [100, 87,90], [94, 77, 90], [100, 81, 82]])
print(grades)

print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.mean())

#calcoli su tutti i valori delle righe in ciascuna colonna
print(grades.mean(axis=0))

#calcolo su tutti i valori delle colonne in ciascuna riga

print(grades.mean(axis=1))
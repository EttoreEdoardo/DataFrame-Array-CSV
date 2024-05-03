import csv

def inserisci_voti():
    """
    Funzione per inserire i voti degli studenti nel file CSV.
    """
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        num_studenti = int(input("Inserisci il numero di studenti: "))

        for _ in range(num_studenti):
            nome = input("Inserisci il nome dello studente: ")
            cognome = input("Inserisci il cognome dello studente: ")
            voto_esame1 = int(input("Inserisci il voto del primo esame: "))
            voto_esame2 = int(input("Inserisci il voto del secondo esame: "))
            voto_esame3 = int(input("Inserisci il voto del terzo esame: "))

            writer.writerow([nome, cognome, voto_esame1, voto_esame2, voto_esame3])

def leggi_voti_e_resoconto():
    """
    Funzione per leggere i voti degli studenti dal file CSV e generare un resoconto.
    """
    with open('grades.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        studenti = []
        totali_esami = [0, 0, 0]
        num_studenti = 0

        # Leggi i dati e calcola le medie
        for row in reader:
            nome, cognome, voto_esame1, voto_esame2, voto_esame3 = row
            studenti.append([nome, cognome, int(voto_esame1), int(voto_esame2), int(voto_esame3)])
            totali_esami[0] += int(voto_esame1)
            totali_esami[1] += int(voto_esame2)
            totali_esami[2] += int(voto_esame3)
            num_studenti += 1

        # Calcola le medie degli esami
        medie_esami = [totali_esami[0] / num_studenti, totali_esami[1] / num_studenti, totali_esami[2] / num_studenti]

        # Stampa i voti e il resoconto
        print("Voti degli studenti:")
        print("Nome\tCognome\tEsame 1\tEsame 2\tEsame 3\tMedia")
        for studente in studenti:
            media_studente = sum(studente[2:]) / 3
            print(f"{studente[0]}\t{studente[1]}\t{studente[2]}\t{studente[3]}\t{studente[4]}\t{media_studente:.2f}")
        
        print("\nResoconto delle medie degli esami:")
        print(f"Media Esame 1: {medie_esami[0]:.2f}")
        print(f"Media Esame 2: {medie_esami[1]:.2f}")
        print(f"Media Esame 3: {medie_esami[2]:.2f}")

# Inserisci i voti degli studenti
inserisci_voti()

# Leggi i voti e genera il resoconto
leggi_voti_e_resoconto()

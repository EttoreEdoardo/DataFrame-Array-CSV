def stampa_tabellone(tabellone):
    """
    Stampare il tabellone di gioco.
    """
    for riga in tabellone:
        print(" | ".join(riga))
        print("-" * 9)

def controlla_vittoria(tabellone, simbolo):
    """
    Controllare se c'è una vittoria per il giocatore corrente.
    """
    for riga in tabellone:
        if riga.count(simbolo) == 3:
            return True

    for colonna in range(3):
        if tabellone[0][colonna] == tabellone[1][colonna] == tabellone[2][colonna] == simbolo:
            return True

    if tabellone[0][0] == tabellone[1][1] == tabellone[2][2] == simbolo:
        return True

    if tabellone[0][2] == tabellone[1][1] == tabellone[2][0] == simbolo:
        return True

    return False

def gioca_tris():
    """
    Funzione principale per giocare a Tris.
    """
    tabellone = [[" " for _ in range(3)] for _ in range(3)]
    giocatori = ['X', 'O']
    turno = 0

    while True:
        stampa_tabellone(tabellone)
        giocatore_corrente = giocatori[turno % 2]

        print(f"Turno del giocatore {giocatore_corrente}")

        # Input delle coordinate per la mossa
        while True:
            try:
                riga = int(input("Inserisci il numero di riga (0, 1, 2): "))
                colonna = int(input("Inserisci il numero di colonna (0, 1, 2): "))
                if tabellone[riga][colonna] == " ":
                    tabellone[riga][colonna] = giocatore_corrente
                    break
                else:
                    print("La casella è già occupata. Riprova.")
            except (ValueError, IndexError):
                print("Input non valido. Riprova.")

        if controlla_vittoria(tabellone, giocatore_corrente):
            print(f"Il giocatore {giocatore_corrente} ha vinto!")
            break

        if all(all(c != " " for c in riga) for riga in tabellone):
            print("Pareggio!")
            break

        turno += 1

# Avvio del gioco
gioca_tris()

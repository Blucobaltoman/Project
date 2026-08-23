import sqlite3 #libreria di python per SQLite
import os #per non usare percorsi fissi e rendere il codice più portabile

# Definiamo i percorsi dei file
# BASE_DIR rappresenta la directory in cui si trova questo script, __file__ è una variabile speciale che contiene il percorso del file corrente
# absolutepath restituisce il percorso assoluto del file, dirname restituisce la directory del percorso

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #cartella in cui si trova il file corrente
DB_PATH = os.path.join(BASE_DIR, "finanza.db") #percorso del database
SQL_SCRIPT_PATH = os.path.join(BASE_DIR, "02_creazione_tabelle.sql")


def inizializza_db():
    """Legge lo script SQL ed esegue la creazione/popolamento delle tabelle."""
    conn = sqlite3.connect(DB_PATH)#canale di connessione al database, se non esiste lo crea
    cursor = conn.cursor()#esecutor per eseguire comandi SQL

    # Leggiamo il contenuto del file .sql creato ieri
    with open(SQL_SCRIPT_PATH, "r", encoding="utf-8") as file: #apre il file in modalita reading, encoding UTF-8 per evitare problemi di caratteri speciali
        sql_script = file.read() #trasforma il contenuto del file in una stringa

    # executescript permette di eseguire più istruzioni SQL insieme
    cursor.executescript(sql_script)

    conn.commit()#salva le modifiche nel database
    conn.close()#chiude la connessione al database
    print("Database 'finanza.db' creato e popolato con successo!")


def leggi_report_portafoglio():
    """Esegue una query SELECT con JOIN e stampa i risultati in Python."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    #tre apici per scrivere la query su più righe senza usare il carattere di continuazione \
    query = """
    SELECT 
        u.username,
        t.simbolo,
        t.quantita,
        t.prezzo_acquisto,
        (t.quantita * t.prezzo_acquisto) AS totale_valore
    FROM transazioni t
    JOIN utenti u ON t.utente_id = u.id;
    """

    cursor.execute(query) #mandiamo la query al database
    righe = cursor.fetchall()  # Recupera tutti i risultati della SELECT e li trasforma in una lista di tuple

    print("\n--- REPORT PORTAFOGLIO UTENTI ---")
    for riga in righe:
        username, simbolo, quantita, prezzo, totale = riga #i valori della tupla vengono assegnati a variabili separate
        print(
            f"Utente: {username:<10} | Azione: {simbolo:<5} | Qta: {quantita:<3} | Prezzo: ${prezzo:<6.2f} | Totale: ${totale:.2f}"
        )

    conn.close()

#convenzione: se il file viene eseguito direttamente, esegue il codice sotto, altrimenti no (utile per importare funzioni senza eseguire tutto)

# --- ESECUZIONE MAIN ---
if __name__ == "__main__":
    inizializza_db()
    leggi_report_portafoglio()
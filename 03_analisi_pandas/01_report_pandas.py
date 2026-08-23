import os
import sqlite3
import pandas as pd
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #cartella in cui si trova il file corrente
PROJECT_DIR = os.path.dirname(BASE_DIR) #cartella principale del progetto
DB_PATH = os.path.join(PROJECT_DIR, "02_database_sql", "finanza.db") #percorso del database

def carica_dati_portafoglio():
    conn=sqlite3.connect(DB_PATH)
    query="""
    SELECT
        u.username,
        t.simbolo,
        t.quantita,
        t.prezzo_acquisto,
        (t.quantita*t.prezzo_acquisto) AS totale_investito
    FROM transazioni t
    JOIN utenti u ON t.utente_id=u.id;
    """
    df=pd.read_sql_query(query, conn) #legge i dati dal database e li trasforma in un DataFrame
    conn.close()
    return df

if __name__ == "__main__":
    df_portafoglio=carica_dati_portafoglio()
    print("\n--- REPORT PORTAFOGLIO UTENTI (PANDAS) ---")
    print(df_portafoglio)

    totale_generale=df_portafoglio["totale_investito"].sum()
    print(f"\n Valore totale del portafoglio: ${totale_generale:,.2f}")

    print("Totale investito per utente:")
    totale_per_utente=df_portafoglio.groupby("username")["totale_investito"].sum()
    print(totale_per_utente)

    df_portafoglio["peso_%"]=(df_portafoglio["totale_investito"]/totale_generale)*100
    print("\n Portafoglio con peso percentuale per posizione: ")
    print(df_portafoglio[["username", "simbolo", "totale_investito", "peso_%"]])
    
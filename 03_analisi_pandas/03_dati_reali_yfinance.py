import os
import sqlite3
import pandas as pd
import yfinance as yf

# 1. Setup Percorsi
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
DB_PATH = os.path.join(PROJECT_ROOT, "02_database_sql", "finanza.db")


def scarica_prezzi_correnti(ticker_list):
    """Scarica i prezzi correnti per tutti i ticker in una sola chiamata di rete."""

    # yf.download scarica tutti i dati in un unico blocco (molto più rapido e affidabile)
    dati = yf.download(
        ticker_list, period="1d", progress=False, ignore_tz=True
    )["Close"]

    prezzi = {}
    for ticker in ticker_list:
        # Se abbiamo più ticker 'dati' è un DataFrame, se è 1 solo è una Series
        if len(ticker_list) > 1:
            valore = dati[ticker].iloc[-1]
        else:
            valore = dati.iloc[-1]
        prezzi[ticker] = float(valore)

    return prezzi


def calcola_performance_portafoglio():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT 
        u.username,
        t.simbolo,
        t.quantita,
        t.prezzo_acquisto
    FROM transazioni t
    JOIN utenti u ON t.utente_id = u.id;
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    # Estraggiamo i ticker unici correttamente
    ticker_unici = df["simbolo"].unique().tolist()

    # Scarichiamo i prezzi reali
    mappa_prezzi = scarica_prezzi_correnti(ticker_unici)

    # Mappiamo il prezzo corrente dentro il DataFrame
    df["prezzo_corrente"] = df["simbolo"].map(mappa_prezzi)

    # Calcoli finanziari
    df["valore_iniziale"] = df["quantita"] * df["prezzo_acquisto"]
    df["valore_attuale"] = df["quantita"] * df["prezzo_corrente"]
    df["profit_loss_$"] = df["valore_attuale"] - df["valore_iniziale"]
    df["profit_loss_%"] = (
        (df["valore_attuale"] - df["valore_iniziale"]) / df["valore_iniziale"]
    ) * 100

    return df


if __name__ == "__main__":
    df_live = calcola_performance_portafoglio()

    print("\n--- REPORT PORTAFOGLIO IN TEMPO REALE ---")
    print(
        df_live[
            [
                "username",
                "simbolo",
                "quantita",
                "prezzo_acquisto",
                "prezzo_corrente",
                "profit_loss_$",
                "profit_loss_%",
            ]
        ]
    )
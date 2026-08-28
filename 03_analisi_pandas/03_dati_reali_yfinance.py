import os
import sqlite3
import pandas as pd
import yfinance as yf

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT=os.path.dirname(BASE_DIR)
DB_PATH=os.path.join(PROJECT_ROOT, "02_database_sql", "finanza.db")

def scarica_prezzi_correnti(ticker_list):
    prezzi={}
    for ticker in ticker_list:
        azione=yf.Ticker(ticker)
        prezzo_corrente=azione.fast_info["lastPrice"]
        prezzi[ticker]=prezzo_corrente

    return prezzi

def calcola_performance_portafoglio():
    conn=sqlite3.connect(DB_PATH)
    query="""
    SELECT
        u.username,
        t.simbolo,
        t.quantita,
        t.prezzo_acquisto
    FROM transazioni t
    JOIN utenti u ON t.utente_id=  u.id
    """
    df=pd.read_sql_query(query,conn)
    conn.close()

    ticker_unici=df["simbolo"].unique().tolist()
    mappa_prezzi=scarica_prezzi_correnti(ticker_unici)
    df["prezzo_corrente"]=df["simbolo"].map(mappa_prezzi)

    df["valore_iniziale"] = df["quantita"] * df["prezzo_acquisto"]
    df["valore_attuale"] = df["quantita"] * df["prezzo_corrente"]
    df["profit_loss_$"] = df["valore_attuale"] - df["valore_iniziale"]
    df["profit_loss_%"] = (
        (df["valore_attuale"] - df["valore_iniziale"]) / df["valore_iniziale"]
    ) * 100

    return df

if __name__ == "__main__":
    df_live=calcola_performance_portafoglio()
    print("\n --- REPORT PORTAFOGLIO IN TEMPO REALE ---")
    print(
        df_live[
            [
                "username",
                "simbolo",
                "quantita",
                "prezzo_acquisto",
                "prezzo_corrente",
                "profit_loss_$",
                "profit_loss_%"
            ]
        ]
    )
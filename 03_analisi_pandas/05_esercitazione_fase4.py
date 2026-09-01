import os
import sqlite3
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT=os.path.dirname(BASE_DIR)
DB_PATH=os.path.join(PROJECT_ROOT, "02_database_sql", "finanza.db")

def ottieni_ticker_db():
    conn=sqlite3.connect(DB_PATH)
    query="SELECT DISTINCT simbolo FROM transazioni;"
    df=pd.read_sql_query(query, conn)["simbolo"].tolist()
    conn.close()
    return df

def scarica_storico_prezzi(ticker_list, period="1y"):
    dati=yf.download(ticker_list, period=period, progress=False, ignore_tz=True)["Close"]
    return dati

def calcola_rendimenti(prezzi_storici):
    rendimenti_giornalieri=prezzi_storici.pct_change().dropna()
    return rendimenti_giornalieri

def calcola_matrice_correlazione(rendimenti_giornalieri):
    matrice_correlazione=rendimenti_giornalieri.corr()
    return matrice_correlazione

if __name__=="__main__":
    ticker=ottieni_ticker_db()
    prezzi=scarica_storico_prezzi(ticker)
    rendimenti=calcola_rendimenti(prezzi)
    matrice_correlazione=calcola_matrice_correlazione(rendimenti)
    print("Matrice di Correlazione dei Rendimenti:")
    print(matrice_correlazione)
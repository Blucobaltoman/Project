import os
import sqlite3
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT=os.path.dirname(BASE_DIR)
DB_PATH=os.path.join(PROJECT_ROOT, '02_database_sql', 'finanza.db')

def ottieni_ticker_db():
    conn=sqlite3.connect(DB_PATH)
    query="SELECT DISTINCT simbolo FROM transazioni;"
    df=pd.read_sql_query(query, conn)
    conn.close()
    return df["simbolo"].tolist()

def scarica_storico_prezzi(ticker_list, period="1y"):
    dati=yf.download(ticker_list, period=period, progress=False, ignore_tz=True)["Close"]
    return dati

def analizza_rischio_rendimento(prezzi_storici):
    rendimenti_giornalieri=prezzi_storici.pct_change().dropna()
    volatilita_giornalier=rendimenti_giornalieri.std()
    volatilita_annua=volatilita_giornalier * np.sqrt(252)*100
    rendimento_totale=((prezzi_storici.iloc[-1] - prezzi_storici.iloc[0]) / prezzi_storici.iloc[0]) * 100
    report_rischio=pd.DataFrame({
        "Rendimento_Annuo_%": rendimento_totale,
        "Volatilita_Annua_%": volatilita_annua
    })
    return rendimenti_giornalieri, report_rischio

def genera_grafico_andamento(prezzi_storici):
    prezzi_normalizzati=prezzi_storici / prezzi_storici.iloc[0]*100
    plt.figure(figsize=(10, 5))
    for colonna in prezzi_normalizzati.columns:
        plt.plot(prezzi_normalizzati.index, prezzi_normalizzati[colonna], label=colonna)
    plt.title("Andamento Normalizzato dei Prezzi")
    plt.xlabel("Data")
    plt.ylabel("Valore Normalizzato (Base 100)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    chart_path=os.path.join(BASE_DIR, "andamento_storico.png")
    plt.savefig(chart_path)
    print(f"Grafico salvato in: {chart_path}")
    plt.show()

if __name__ == "__main__":
    ticker=ottieni_ticker_db()
    prezzi=scarica_storico_prezzi(ticker)
    rendimenti, report=analizza_rischio_rendimento(prezzi)
    print("Report Rischio e Rendimento:")
    print(report)
    genera_grafico_andamento(prezzi)
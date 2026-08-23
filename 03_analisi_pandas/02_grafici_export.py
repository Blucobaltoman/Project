import os
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

# 1. Setup Percorsi
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
DB_PATH = os.path.join(PROJECT_ROOT, "02_database_sql", "finanza.db")


def carica_e_elabora_dati():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT 
        u.username,
        t.simbolo,
        t.quantita,
        t.prezzo_acquisto,
        (t.quantita * t.prezzo_acquisto) AS totale_investito
    FROM transazioni t
    JOIN utenti u ON t.utente_id = u.id;
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    # Calcolo percentuale sul totale generale
    totale_generale = df["totale_investito"].sum()
    df["peso_%"] = (df["totale_investito"] / totale_generale) * 100

    return df


def esporta_report(df):
    # Percorsi per salvare i file nella cartella 03_analisi_pandas
    csv_path = os.path.join(BASE_DIR, "report_portafoglio.csv")
    excel_path = os.path.join(BASE_DIR, "report_portafoglio.xlsx")

    # Export in CSV e Excel (index=False evita di salvare l'indice numerico di Pandas)
    df.to_csv(csv_path, index=False)
    df.to_excel(excel_path, index=False)

    print(f"✅ Report salvati con successo!\n - {csv_path}\n - {excel_path}")


def genera_grafico_portafoglio(df):
    # Raggruppiamo il totale investito per simbolo azionario
    investimento_per_titolo = df.groupby("simbolo")["totale_investito"].sum()

    # Creazione del grafico a torta
    plt.figure(figsize=(8, 6))
    plt.pie(
        investimento_per_titolo,
        labels=investimento_per_titolo.index,
        autopct="%1.1f%%",
        startangle=140,
    )
    plt.title("Composizione del Portafoglio Complessivo per Titolo")

    # Salva il grafico come immagine PNG
    chart_path = os.path.join(BASE_DIR, "grafico_portafoglio.png")
    plt.savefig(chart_path)
    print(f"📊 Grafico salvato in: {chart_path}")

    # Mostra la finestra del grafico
    plt.show()


if __name__ == "__main__":
    df = carica_e_elabora_dati()
    esporta_report(df)
    genera_grafico_portafoglio(df)
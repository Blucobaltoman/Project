📋 SCHEDA RIASSUNTIVA: PANDAS & DATABASE
1. Caricamento Dati (I/O)

import pandas as pd: Importa la libreria col suo alias standard.

pd.read_sql_query(query, conn): Esegue la query SQL e converte immediatamente il risultato in un DataFrame, gestendo colonne e tipi di dato al posto tuo.

2. Strutture Principali

DataFrame (es. df): L'intera tabella bidimensionale (righe e colonne).

Series (es. df["colonna"]): Una singola colonna estratta dal DataFrame.

3. Calcoli Statistici su Singole Colonne

df["col"].sum(): Somma tutti i valori della colonna.

df["col"].mean(): Calcola la media della colonna.

df["col"].max() / .min(): Trova il valore massimo o minimo.

4. Aggregazione e Nuove Colonne

df.groupby("gruppo")["valore"].sum(): Raggruppa le righe per una colonna e ne somma un'altra (l'equivalente del GROUP BY in SQL).

df["nuova_col"] = df["col1"] / df["col2"]: Crea una nuova colonna calcolata al volo su tutte le righe contemporaneamente (senza usare cicli for).

Comando,A cosa serve
"df[""col""].unique()",Estrae i valori unici di una colonna eliminando i duplicati.
.tolist(),Converte un oggetto Pandas/NumPy in una classica lista Python.
yf.download(),Scarica dati di mercato live per una lista di titoli in un'unica chiamata.
.iloc[-1],Prende l'ultimo valore disponibile in una serie di dati.
"df[""col""].map(dizionario)",Sostituisce/associa i valori di una colonna usando un dizionario come mappa. 
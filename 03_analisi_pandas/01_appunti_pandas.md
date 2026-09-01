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


### 1. Prelievo Dati da Database e Liste Python

* **`pd.read_sql_query(query, conn)`**: Esegue una query SQL sul database tramite la connessione `conn` e trasforma il risultato direttamente in un DataFrame Pandas.
* **`df["colonna"].unique()`**: Estrae i valori unici di una colonna, eliminando i duplicati.
* **`df["colonna"].tolist()`**: Converte una colonna o una serie di Pandas in una normale lista Python `[...]`.

---

### 2. Integrazione Mercato Reale (`yfinance`)

* **`yf.download(ticker_list, period="1y", ...)`**: Scarica lo storico o i prezzi correnti per una lista di titoli in un'unica chiamata di rete.
* Specificare `["Close"]` alla fine estrae solo i prezzi di chiusura.


* **`df.iloc[-1]`**: Accede all'ultimo elemento (o riga) di un DataFrame o di una Serie usando la posizione numerica (`-1` = ultimo).

---

### 3. Trasformazione e Manipolazione Dati in Pandas

* **`df["colonna"].map(dizionario)`**: Sostituisce o associa i valori di una colonna basandosi su un dizionario di supporto (l'equivalente di una `LEFT JOIN` ultraleggera).
* **`df.pct_change()`**: Calcola la variazione percentuale punto su punto (giorno per giorno):

$$\frac{\text{Prezzo}_t - \text{Prezzo}_{t-1}}{\text{Prezzo}_{t-1}}$$


* **`df.dropna()`**: Rimuove le righe o le colonne che contengono valori nulli/mancanti (`NaN`), come la prima riga generata da `.pct_change()`.
* **`pd.DataFrame({...})`**: Crea un nuovo DataFrame da zero passando un dizionario Python dove le chiavi diventano i nomi delle colonne.

---

### 4. Statistica Finanziaria e Rischio

* **`df.std()`**: Calcola la deviazione standard delle colonne, usata per misurare la **volatilità (rischio)** dei rendimenti.
* **`np.sqrt(252)`**: Calcola la radice quadrata del numero di giorni finanziari in un anno ($252$), usata per **annualizzare** la volatilità giornaliera ($\sigma_{\text{annua}} = \sigma_{\text{giornaliera}} \times \sqrt{252}$).
* **`df.corr()`**: Calcola automaticamente la **matrice di correlazione di Pearson** tra tutte le colonne numeriche del DataFrame (valori da $-1$ a $+1$).

---

### 5. Grafici (`matplotlib`)

* **`plt.figure(figsize=(10, 5))`**: Imposta le dimensioni della finestra del grafico.
* **`plt.plot(x, y, label=...)`**: Traccia una linea sul grafico.
* **`plt.savefig(path)`**: Salva il grafico generato come immagine su disco (es. `.png`).

---

Quando vuoi partire con la **Fase 5** (dove uniremo tutto per generare report finali e automatizzare il processo), basta che mi dai il via!
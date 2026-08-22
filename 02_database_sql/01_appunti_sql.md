# 🗄️ Modulo 2: Database Relazionali e SQL

## Concetti Chiave
- **RDBMS:** Relational Database Management System
- **Tabella:** Insieme di righe (records) e colonne (fields)
- **Primary Key (PK):** Identificativo unico di ogni riga
- **Foreign Key (FK):** Collegamento verso una Primary Key di un'altra tabella

# 🗄️ Modulo 2: Database Relazionali e SQL

## 1. Perché usare un RDBMS (Database Relazionale)?
- **Persistenza:** I dati rimangono salvati su disco anche dopo la chiusura del programma.
- **Integrità:** Applica regole rigide sui dati (evita tipi sbagliati o duplicati non voluti).
- **Sicurezza e Concorrenza:** Gestisce accessi simultanei senza corrompere i file.
- **Efficienza:** Ricerche ultra-veloci anche su milioni di righe grazie agli indici.

---

## 2. Architettura Relazionale
- **Tabella:** Struttura che organizza un'entità (es. `utenti`, `transazioni`).
- **Colonna (Field):** Definizione di una specifica proprietà del dato. Ha un tipo fisso.
- **Riga (Record):** Una singola istanza completa salvata nella tabella.

---

## 3. Le Chiavi (Relazioni tra dati)
- **Primary Key (PK):** Identificativo **unico e non nullo** per ogni riga di una tabella (es. `id`).
- **Foreign Key (FK):** Colonna che punta alla Primary Key di un'altra tabella, creando il ponte relazionale ed evitando duplicazioni inutili di dati.

---

## 4. Tipi di Dato Principali (SQLite)
| Tipo SQLite | Descrizione | Equivalente Python |
| :--- | :--- | :--- |
| **`INTEGER`** | Numeri interi (`1`, `100`) | `int` |
| **`REAL`** | Numeri decimali (`175.50`, `3.14`) | `float` |
| **`TEXT`** | Testo e stringhe (`'AAPL'`, `'Marco'`) | `str` |
| **`BLOB`** | Dati binari (immagini, file) | `bytes` |
| **`NULL`** | Dato assente o non specificato | `None` |

## 5. DDL
CREATE TABLE nome_tabella (
    nome_colonna1 TIPO_DATO VINCOLI,
    nome_colonna2 TIPO_DATO VINCOLI,
    ...
);

FOREIGN KEY (colonna_locale) REFERENCES tabella_esterna(colonna_esterna). Per la foreign key serve prima che la colonna sia dichiarata

INSERT INTO nome_tabella (colonna1, colonna2, ...) 
VALUES (valore1, valore2, ...);

-- Prendi solo le transazioni dell'utente Marco (utente_id = 1)
SELECT * 
FROM transazioni 
WHERE utente_id = 1;

=: Uguale
<> o !=: Diverso
>, <, >=, <=: Maggiore, minore, ecc.
BETWEEN x AND y: Compreso tra due valori (es. prezzo_acquisto BETWEEN 100 AND 200)
IN ('AAPL', 'TSLA'): Uguale a uno dei valori nella lista
LIKE 'm%': Cerca testo che inizia per 'm'

-- Transazioni ordinate dalla più cara alla meno cara
SELECT * 
FROM transazioni 
ORDER BY prezzo_acquisto DESC;

-- L'acquisto singolo più costoso in assoluto
SELECT * 
FROM transazioni 
ORDER BY prezzo_acquisto DESC 
LIMIT 1;

Funzione,Cosa Calcola,Esempio
SUM(),Somma tutti i valori di una colonna,SUM(quantita)
AVG(),Media aritmetica dei valori,AVG(prezzo_acquisto)
COUNT(),Conta il numero di righe,COUNT(*) o COUNT(id)
MAX(),Trova il valore massimo,MAX(prezzo_acquisto)
MIN(),Trova il valore minimo,MIN(prezzo_acquisto)
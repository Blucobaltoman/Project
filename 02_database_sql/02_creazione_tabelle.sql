DROP TABLE IF EXISTS transazioni;
DROP TABLE IF EXISTS utenti;

CREATE TABLE utenti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE
)

CREATE TABLE transazioni(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utente_id INTEGER NOT NULL,
    simbolo TEXT NOT NULL,
    quantita REAL NOT NULL,
    prezzo_acquisto REAL NOT NULL CHECK(prezzo_acquisto > 0),
    FOREIGN KEY (utente_id) REFERENCES utenti(id)
)
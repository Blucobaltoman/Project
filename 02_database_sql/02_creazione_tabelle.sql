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

INSERT INTO utenti (username, email) 
VALUES
    ('marcop', 'marcop@example.com'),
    ('giuliav', 'giuliav@example.com');

INSERT INTO transazioni (utente_id, simbolo, quantita, prezzo_acquisto)
VALUES
    (1, 'AAPL', 10, 150.00),
    (1, 'GOOGL', 5, 2800.00),
    (2, 'TSLA', 3, 700.00);
    (2, 'TSLA', 3, 700.00);

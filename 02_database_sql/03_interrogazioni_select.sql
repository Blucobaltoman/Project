SELECT * 
FROM utenti

SELECT simbolo, quantita 
FROM transazioni

SELECT * 
FROM transazioni 
WHERE prezzo_acquisto > 200.00

SELECT * 
FROM transazioni 
ORDER BY quantita DESC 
LIMIT 1

/*SELECT sum(quantita) FROM transazioni

SELECT simbolo, quantita, prezzo_acquisto, (quantita * prezzo_acquisto) AS valore_totale
FROM transazioni

SELECT utente_id, SUM(quantita * prezzo_acquisto) AS valore_totale
FROM transazioni
GROUP BY utente_id*/


SELECT COUNT(*) AS numero_transazioni_totali 
FROM transazioni;

SELECT AVG(prezzo_acquisto) AS prezzo_medio 
FROM transazioni;

SELECT 
    utente_id, 
    SUM(quantita * prezzo_acquisto) AS capitale_totale_investito
FROM transazioni
GROUP BY utente_id;

SELECT 
    simbolo, 
    SUM(quantita) AS quote_totali
FROM transazioni
GROUP BY simbolo;

SELECT 
    u.username,
    u.email,
    t.simbolo,
    t.quantita,
    t.prezzo_acquisto,
    (t.quantita * t.prezzo_acquisto) AS valore_totale
FROM transazioni t
JOIN utenti u ON t.utente_id = u.id;

SELECT 
    u.username,
    COUNT(t.id) AS numero_operazioni,
    SUM(t.quantita * t.prezzo_acquisto) AS valore_portafoglio
FROM utenti u
JOIN transazioni t ON u.id = t.utente_id
GROUP BY u.id;
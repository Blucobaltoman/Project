# 🚀 Percorso di Preparazione: Full-Stack FinTech & Trento

## 📌 Checklist Materiali & Strumenti
- [x] **VS Code** (con estensioni Python, SQLite Viewer, Git)
- [x] **Git & GitHub** (Repository `Progetto-Trento`)
- [ ] **Libro:** *Python Crash Course* (3ª Edizione) - Parte 1
- [ ] **Corso SQL:** SQLBolt + Teoria Relazionale e DDL/DML completa
- [ ] **Corso Web Development:** HTML5, CSS3 avanzato (Flexbox/Grid) e JavaScript moderno (ES6+)

---

## 🗺️ Roadmap Operativa Completa

### Fase 1: Fondamenta di Python & OOP (IN CORSO ⏳)
- **Fonte:** *Python Crash Course* (Capitoli 1–9)
- **Contenuti:** Variabili, strutture dati, cicli, funzioni, gestione errori e **Classi / OOP** (Capitolo 9).
- **Obiettivo Pratico:** Creare una classe `Portafoglio` da riga di comando per gestire titoli e transazioni.

### Fase 2: Database & SQL Avanzato
- **Fonte:** *SQLBolt* + esercitazioni su SQLite
- **Contenuti:** Teoria dei database relazionali, Progettazione Schemi, Primary/Foreign Key, JOIN, Aggregazioni, Normalizzazione e Modulo `sqlite3` in Python.
- **Obiettivo Pratico:** Progettare e interrogare il DB relazionale `finanza.db` (Tabelle: `utenti`, `transazioni`, `asset`).

### Fase 3: Front-End Development (HTML5, CSS3, JavaScript ES6)
- **Fonte:** *The Odin Project* / MDN Web Docs
- **Contenuti:** 
  - **HTML5:** Semantica web, form, input validati.
  - **CSS3:** Box model, Layout moderni (Flexbox e CSS Grid), Responsive Design.
  - **JavaScript:** Sintassi base, Manipolazione del DOM, Eventi, Programmazione Asincrona (`fetch`/API), e integrazione della libreria **Chart.js** per i grafici.
- **Obiettivo Pratico:** Costruire la dashboard finanziaria con tabelle dinamiche e grafici interattivi.

### Fase 4: Back-End, API Integration & Web Framework (Flask)
- **Fonte:** Documentazione Flask / Tutorial Architetture Web
- **Contenuti:** Architettura Client-Server, Protocollo HTTP (GET/POST/PUT/DELETE), Routing in Flask, Template Engine (Jinja2), consumo di API esterne (libreria `yfinance` e `requests`).
- **Obiettivo Pratico:** Integrare Front-End, Back-End e Database per scaricare i prezzi azionari in tempo reale, calcolare il rendimento e mostrare i grafici.

### Fase 5: Refactoring, Security & Testing
- **Contenuti:** Gestione delle variabili d'ambiente, sicurezza delle API key, pulizia del codice (PEP 8) e scrittura del file `README.md` per il portfolio GitHub.

---

## 🛠️ Comandi Git per la fine di ogni sessione

1. `git add .`
2. `git commit -m "Messaggio descrittivo"`
3. `git push`
import sqlite3

DATABASE = "database.db"

def create_table():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS etudiants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            addr TEXT,
            pin TEXT
        )
    """)
    con.commit()
    con.close()

def insert_etudiant(nom, addr, pin):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO etudiants(nom, addr, pin) VALUES (?, ?, ?)", (nom, addr, pin))
    con.commit()
    con.close()

def get_etudiants():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("SELECT * FROM etudiants")
    rows = cur.fetchall()
    con.close()
    return rows

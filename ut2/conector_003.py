import sqlite3

conn = sqlite3.connect("prueba.db")
cur = conn.cursor()
try:
    cur.execute("PRAGMA foreign_keys = ON;")
except Exception as e:
    print(e)

sql_coche = """
CREATE TABLE IF NOT EXISTS coches (
    id INTEGER PRIMARY KEY,
    matricula TEXT NOT NULL CHECK (matricula LIKE '_______'),
    created_at TEXT NOT NULL DEFAULT current_timestamp,
    marca TEXT NOT NULL CHECK (marca IN ('mercedes', 'bmw')),
    owner INTEGER NOT NULL REFERENCES usuarios ON DELETE CASCADE,
    UNIQUE(matricula)
);"""
try:
    cur.execute(sql_coche)
    sql_ins = "INSERT INTO coches (matricula, marca, owner) VALUES ('3LL','mercedes', 2);"
    cur.execute(sql_ins)
    conn.commit()
except Exception as e:
    print(type(e),e)
finally:
    conn.close()
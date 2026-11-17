import sqlite3

SCHEMA = """
        CREATE TABLE IF NOT EXISTS notas(
            id INTEGER PRIMARY KEY,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            title TEXT NOT NULL CHECK (LENGTH(title) <= 50),
            description TEXT NOT NULL CHECK (LENGTH(description) > 5)
        );
         """

with sqlite3.connect("prueba.db") as conn:
    cur = conn.cursor()
    cur.executescript(SCHEMA)
    print("Esquema creado!")

def crear_nota():
    titulo = input("Ingrese el título de la nota:\n")
    descripcion = input("Ingrese la descripción de la nota:\n")
    SQL = "INSERT INTO notas (title, description) VALUES (?,?);"
    with sqlite3.connect("prueba.db") as conn:
        cur = conn.cursor()
        cur.execute(SQL, (titulo, descripcion))
    print(cur.rowcount)

def borrar_nota():
    id_borrar = input("Ingrese el id de la nota a borrar:\n")
    try:
        id_borrar = int(id_borrar)
        with sqlite3.connect("prueba.db") as conn:
            cur = conn.cursor()
            SQL_D = "DELETE FROM notas WHERE id=?;"
            SQL_S = "SELECT id FROM notas WHERE id=?;"
            print(type(id_borrar), id_borrar)
            cur.execute(SQL_S, (id_borrar,))
            registro = cur.fetchall()
            if len(registro) != 1:
                raise Exception(f"La nota con id {id_borrar} no existe")
            cur.execute(SQL_D, (id_borrar,))
            print(cur.rowcount)
    except ValueError:
        print("El id a borrar debe ser un entero")
        return
    except Exception as e:
        print(e)
    

def imprimir_notas():
    SQL = "SELECT * FROM notas;"
    print("id, \tcreated_at, \ttitle, \tdescription")
    print("-" * 90)
    with sqlite3.connect("prueba.db") as conn:
        cur = conn.cursor()
        cur.execute(SQL)
        for f in cur:
            for i,campo in enumerate(f):
                print(f"{f[i]}", end="\t\t")
            print()
            print("-" * 90)
def menu():
    fin = False
    while not fin:
        print("Gestor de notas:")
        print("1.- Crear Nota")
        print("2.- Imprimir notas")
        print("3.- Borrar nota")
        print("5.- FIN")
        opcion = input()
        try:
            opcion = int(opcion)
        except:
            print("La entrada debe ser entera")
            continue
        match opcion:
            case 1:
                crear_nota()
            case 2:
                imprimir_notas()
            case 3:
                borrar_nota()
            case 5:
                print("Bye!")
                fin = True
            case _:
                print("La entrada debe estar comprendida entre 1 y 5")

menu()
    
    
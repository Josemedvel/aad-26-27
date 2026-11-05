import sqlite3
# consulta sobre usuarios

conn = sqlite3.connect("prueba.db")
cur = conn.cursor()

sql = "SELECT edad, id, nombre FROM usuarios WHERE edad > 22;"
cur.execute(sql)

'''
# iterar tal cual
for r in cur:
    print(r)
'''
# fetch
'''
res = cur.fetchone()
print(res)
res = cur.fetchone()
print(res)
res = cur.fetchone()
print(res)
'''
#fetchall
'''
res = cur.fetchall()
print(res)
'''
# fetchmany
res = cur.fetchmany(20)
print(res)

conn.close()
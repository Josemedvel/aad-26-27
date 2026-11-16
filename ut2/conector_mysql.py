import mysql.connector
from mysql.connector import Error

conn = None
try:
    # Conexión a MySQL con las opciones correctas
    conn = mysql.connector.connect(
        host='localhost',
        port=3307,  # Puerto del compose
        user='root',  # Usar root (el usuario jose puede no tener permisos correctos)
        password='1234',
        # allow_public_key_retrieval=True,  # Descomenta si sigues teniendo problemas
        # use_pure=True,  # Descomenta si hay problemas de rendimiento
    )
    
    if conn.is_connected():
        print("✅ Conexión exitosa a MySQL")
        
        cursor = conn.cursor()
        
        # Crear base de datos
        cursor.execute("CREATE DATABASE IF NOT EXISTS test_db;")
        print("✅ Base de datos creada/verificada")
        
        # Usar la base de datos
        cursor.execute("USE test_db;")
        
        # Crear tabla
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                edad INT NOT NULL DEFAULT 18
            );
        """)
        print("✅ Tabla creada/verificada")
        
        # Insertar datos
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s);", ("Patricia", 25))
        conn.commit()
        print("✅ Datos insertados")
        
        # Consultar
        cursor.execute("SELECT * FROM usuarios;")
        for row in cursor.fetchall():
            print(f"   {row}")
        
        cursor.close()

except Error as err:
    if err.errno == 2003:
        print("❌ Error: No se puede conectar al servidor MySQL")
        print("   - ¿Está el contenedor de Docker levantado?")
        print("   - Ejecuta: docker-compose -f ut2/mysql-compose/docker-compose.yml up -d")
    elif "Public Key Retrieval" in str(err):
        print("❌ Error de recuperación de clave pública")
        print("   - Solución: Descomenta 'allow_public_key_retrieval=True' en la conexión")
    else:
        print(f"❌ Error de conexión: {err}")

finally:
    if conn and conn.is_connected():
        conn.close()

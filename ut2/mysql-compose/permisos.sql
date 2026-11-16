-- Script para configurar permisos correctos en MySQL 8.0+
-- Ejecutar desde dentro del contenedor o desde cualquier cliente conectado como root

-- Asegurar que root puede conectarse desde cualquier host
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;

-- Crear usuario jose si no existe (MySQL 8.0+)
CREATE USER IF NOT EXISTS 'jose'@'%' IDENTIFIED BY '1234';

-- Dar permisos a jose sobre test_db
GRANT ALL PRIVILEGES ON test_db.* TO 'jose'@'%';

-- Aplicar cambios
FLUSH PRIVILEGES;

-- Verificar usuarios y permisos (opcional, solo para revisar)
-- SELECT User, Host FROM mysql.user;
-- SHOW GRANTS FOR 'root'@'%';
-- SHOW GRANTS FOR 'jose'@'%';

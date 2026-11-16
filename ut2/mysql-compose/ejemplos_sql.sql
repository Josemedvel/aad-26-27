-- 📝 Ejemplos SQL para usar en DBeaver

-- ==========================================
-- 1. VER INFORMACIÓN DE LA CONEXIÓN
-- ==========================================
SELECT DATABASE();
SELECT VERSION();
SHOW DATABASES;
USE test_db;
SHOW TABLES;


-- ==========================================
-- 2. TRABAJAR CON LA TABLA USUARIOS
-- ==========================================

-- Ver todos los usuarios
SELECT * FROM usuarios;

-- Insertar un nuevo usuario
INSERT INTO usuarios (nombre, edad) VALUES ('Carlos', 28);

-- Actualizar usuarios
UPDATE usuarios SET edad = 26 WHERE nombre = 'Patricia';

-- Eliminar usuarios
DELETE FROM usuarios WHERE edad < 20;

-- Ver con filtros
SELECT * FROM usuarios WHERE edad > 25;

-- Contar registros
SELECT COUNT(*) as total_usuarios FROM usuarios;

-- Ver edad promedio
SELECT AVG(edad) as edad_promedio FROM usuarios;


-- ==========================================
-- 3. CREAR NUEVAS TABLAS
-- ==========================================

-- Tabla de Productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Pedidos
CREATE TABLE IF NOT EXISTS pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL DEFAULT 1,
    total DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);


-- ==========================================
-- 4. INSERTAR DATOS EN NUEVAS TABLAS
-- ==========================================

-- Insertar productos
INSERT INTO productos (nombre, precio, stock) VALUES 
('Laptop', 999.99, 5),
('Mouse', 29.99, 50),
('Teclado', 79.99, 20);

-- Insertar pedidos
INSERT INTO pedidos (usuario_id, producto_id, cantidad, total) VALUES
(1, 1, 1, 999.99),
(2, 2, 2, 59.98);


-- ==========================================
-- 5. CONSULTAS CON JOINS (RELACIONADAS)
-- ==========================================

-- Ver pedidos con nombres de usuarios
SELECT 
    p.id as pedido_id,
    u.nombre as usuario,
    pr.nombre as producto,
    p.cantidad,
    p.total
FROM pedidos p
JOIN usuarios u ON p.usuario_id = u.id
JOIN productos pr ON p.producto_id = pr.id;

-- Ver ingresos por usuario
SELECT 
    u.nombre,
    COUNT(p.id) as total_pedidos,
    SUM(p.total) as total_gastado
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.id, u.nombre;


-- ==========================================
-- 6. BACKUP Y EXPORTACIÓN
-- ==========================================

-- Exportar estructura de tabla
SHOW CREATE TABLE usuarios;

-- Ver índices
SHOW INDEXES FROM usuarios;

-- Ver tamaño de base de datos
SELECT table_name, 
       ROUND(((data_length + index_length) / 1024 / 1024), 2) as size_mb
FROM information_schema.tables 
WHERE table_schema = 'test_db';


-- ==========================================
-- 7. LIMPIAR / RESETEAR DATOS
-- ==========================================

-- Vaciar tabla (sin eliminar estructura)
TRUNCATE TABLE usuarios;

-- Eliminar tabla
DROP TABLE IF EXISTS usuarios;

-- Eliminar base de datos
DROP DATABASE IF EXISTS test_db;

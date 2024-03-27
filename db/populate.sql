CREATE DATABASE IF NOT EXISTS cookies;

USE cookies;

CREATE TABLE IF NOT EXISTS usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS password_histories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    password VARCHAR(100) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES usuario(id)
);

CREATE USER 'compras'@'%' IDENTIFIED BY 'contraseña_compras';
CREATE USER 'venta'@'%' IDENTIFIED BY 'contraseña_venta';
CREATE USER 'Producción'@'%' IDENTIFIED BY 'contraseña_produccion';
CREATE USER 'Administrador'@'%' IDENTIFIED BY 'contraseña_administrador';
CREATE USER 'system'@'localhost' IDENTIFIED BY 'contraseña_system';

GRANT ALL PRIVILEGES ON cookies.* TO 'compras'@'%';
GRANT ALL PRIVILEGES ON cookies.* TO 'venta'@'%';
GRANT ALL PRIVILEGES ON cookies.* TO 'Producción'@'%';
GRANT ALL PRIVILEGES ON cookies.* TO 'Administrador'@'%';
GRANT SELECT, INSERT, UPDATE ON cookies.* TO 'venta'@'%';

FLUSH PRIVILEGES;

DELIMITER //

CREATE TRIGGER password_history_trigger
AFTER INSERT ON usuario
FOR EACH ROW
BEGIN
    INSERT INTO password_histories (user_id, password, fecha_creacion)
    VALUES (NEW.id, NEW.password, NEW.fecha_creacion);
END//

CREATE TRIGGER password_update_trigger
AFTER UPDATE ON usuario
FOR EACH ROW
BEGIN
    INSERT INTO password_histories (user_id, password, fecha_creacion)
    VALUES (NEW.id, NEW.password, CURRENT_TIMESTAMP);
END//

DELIMITER ;

CREATE TABLE MateriaPrima (
    id INT AUTO_INCREMENT PRIMARY KEY,
    material VARCHAR(255) NOT NULL,
    cantidad DECIMAL(10,2) NOT NULL,
    tipo VARCHAR(20) NOT NULL
);

INSERT INTO MateriaPrima (material, cantidad, tipo) VALUES
    ('harina', 1000, 'gramos'),
    ('avena', 500, 'gramos'),
    ('mantequilla', 500, 'gramos'),
    ('azúcar', 500, 'gramos'),
    ('huevo', 12, 'unidad'),
    ('esencia de vainilla', 50, 'mililitros'),
    ('bicarbonato de sodio', 10, 'gramos'),
    ('pasas', 200, 'gramos'),
    ('cacao en polvo', 100, 'gramos'),
    ('chips de chocolate', 200, 'gramos'),
    ('azúcar glass', 200, 'gramos'),
    ('almendras fileteadas', 100, 'gramos'),
    ('jengibre molido', 15, 'gramos'),
    ('canela', 25, 'gramos'),
    ('clavo molido', 5, 'gramos'),
    ('nuez moscada', 5, 'gramos'),
    ('miel', 50, 'mililitros'),
    ('coco rallado', 150, 'gramos'),
    ('nueces picadas', 100, 'gramos');



CREATE TABLE Galletas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    cantidad DECIMAL(10,2) NOT NULL,
    enable INT DEFAULT 1,
    descripcion TEXT
);

CREATE TABLE ingredientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    galleta_id INT NOT NULL,
    material_id INT NOT NULL,
    cantidad DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (galleta_id) REFERENCES Galletas(id),
    FOREIGN KEY (material_id) REFERENCES MateriaPrima(id)
);


#GALLETA DE AVENA
INSERT INTO Galletas (nombre, precio, cantidad, descripcion) VALUES
    ('Galleta de avena', 10, 100, 'Galleta de avena con pasas');

INSERT INTO ingredientes (galleta_id, material_id, cantidad) VALUES
    (1, 2, 500),
    (1, 6, 50),
    (1, 7, 5),
    (1, 8, 100);

#GALLETA DE CHOCOLATE
INSERT INTO Galletas (nombre, precio, cantidad, descripcion) VALUES
    ('Galleta de chocolate', 15, 100, 'Galleta de chocolate con chips de chocolate');

INSERT INTO ingredientes (galleta_id, material_id, cantidad) VALUES
    (2, 2, 500),
    (2, 6, 50),
    (2, 7, 5),
    (2, 9, 100);

#GALLETA DE AZUCAR
INSERT INTO Galletas (nombre, precio, cantidad, descripcion) VALUES
    ('Galleta de azúcar', 5, 100, 'Galleta de azúcar con azúcar glass');

INSERT INTO ingredientes (galleta_id, material_id, cantidad) VALUES
    (3, 2, 500),
    (3, 6, 50),
    (3, 7, 5),
    (3, 10, 100);

#GALLETA DE PASAS Y NUECES
INSERT INTO Galletas (nombre, precio, cantidad, descripcion) VALUES
    ('Galleta de Pasas y Nueces', 8, 100, 'Galleta de avena con pasas y nueces');

INSERT INTO ingredientes (galleta_id, material_id, cantidad) VALUES
    (4, 2, 500),   -- Avena
    (4, 6, 50),    -- Esencia de vainilla
    (4, 7, 5),     -- Bicarbonato de sodio
    (4, 8, 100),   -- Pasas
    (4, 19, 50);   -- Nueces picadas

#GALLETA DE COCO y LImon
INSERT INTO Galletas (nombre, precio, cantidad, descripcion) VALUES
    ('Galleta de Limón y Coco', 12, 100, 'Galleta de limón con coco rallado');

INSERT INTO ingredientes (galleta_id, material_id, cantidad) VALUES
    (5, 1, 500),   -- Harina
    (5, 3, 50),    -- Mantequilla
    (5, 4, 5),     -- Azúcar
    (5, 5, 1),     -- Huevo
    (5, 12, 10),   -- Ralladura de limón
    (5, 18, 50);   -- Coco rallado

#GALLETA DE JENGIBRE
INSERT INTO Galletas (nombre, precio, cantidad, descripcion) VALUES
    ('Galleta de Jengibre', 7, 100, 'Galleta de jengibre con azúcar glass');

INSERT INTO ingredientes (galleta_id, material_id, cantidad) VALUES
    (6, 1, 500),   -- Harina
    (6, 3, 50),    -- Mantequilla
    (6, 4, 5),     -- Azúcar
    (6, 5, 1),     -- Huevo
    (6, 13, 15),   -- Jengibre molido
    (6, 10, 100);  -- Azúcar glass

#GALLETA DE ESPECIAS
INSERT INTO Galletas (nombre, precio, cantidad, descripcion) VALUES
    ('Galleta de Especias', 6, 100, 'Galleta de especias con azúcar glass');

INSERT INTO ingredientes (galleta_id, material_id, cantidad) VALUES
    (7, 1, 500),   -- Harina
    (7, 3, 50),    -- Mantequilla
    (7, 4, 5),     -- Azúcar
    (7, 5, 1),     -- Huevo
    (7, 14, 25),   -- Canela
    (7, 15, 5),    -- Clavo molido
    (7, 16, 5),    -- Nuez moscada
    (7, 10, 100);  -- Azúcar glass

#GALLETA DE MIEL
INSERT INTO Galletas (nombre, precio, cantidad, descripcion) VALUES
    ('Galleta de Miel', 9, 100, 'Galleta de miel con almendras fileteadas');

INSERT INTO ingredientes (galleta_id, material_id, cantidad) VALUES
    (8, 1, 500),   -- Harina
    (8, 3, 50),    -- Mantequilla
    (8, 4, 5),     -- Azúcar
    (8, 5, 1),     -- Huevo
    (8, 17, 50),   -- Miel
    (8, 11, 100);  -- Almendras fileteadas

#GALLETA DE CHOCOLATE Y COCO
INSERT INTO Galletas (nombre, precio, cantidad, descripcion) VALUES
    ('Galleta de Chocolate y Coco', 14, 100, 'Galleta de chocolate con coco rallado');

INSERT INTO ingredientes (galleta_id, material_id, cantidad) VALUES
    (9, 1, 500),   -- Harina
    (9, 3, 50),    -- Mantequilla
    (9, 4, 5),     -- Azúcar
    (9, 5, 1),     -- Huevo
    (9, 9, 100),   -- Chips de chocolate
    (9, 18, 50);   -- Coco rallado

# GALLETA DE AVENA Y MIEL
INSERT INTO Galletas (nombre, precio, cantidad, descripcion) VALUES
    ('Galleta de Avena y Miel', 11, 100, 'Galleta de avena con miel');

INSERT INTO ingredientes (galleta_id, material_id, cantidad) VALUES
    (10, 2, 500),   -- Avena
    (10, 6, 50),    -- Esencia de vainilla
    (10, 7, 5),     -- Bicarbonato de sodio
    (10, 17, 50);  

#quitar de ingredientes el campo receta
ALTER TABLE ingredientes DROP COLUMN cantidad;

#agregarlo en galleteas
ALTER TABLE Galletas ADD COLUMN receta TEXT;

#actualizar receta
UPDATE Galletas SET receta = 'Galleta de avena con pasas' WHERE id = 1;
UPDATE Galletas SET receta = 'Galleta de chocolate con chips de chocolate' WHERE id = 2;
UPDATE Galletas SET receta = 'Galleta de azúcar con azúcar glass' WHERE id = 3;
UPDATE Galletas SET receta = 'Galleta de avena con pasas y nueces' WHERE id = 4;
UPDATE Galletas SET receta = 'Galleta de limón con coco rallado' WHERE id = 5;
UPDATE Galletas SET receta = 'Galleta de jengibre con azúcar glass' WHERE id = 6;
UPDATE Galletas SET receta = 'Galleta de especias con azúcar glass' WHERE id = 7;
UPDATE Galletas SET receta = 'Galleta de miel con almendras fileteadas' WHERE id = 8;
UPDATE Galletas SET receta = 'Galleta de chocolate con coco rallado' WHERE id = 9;
UPDATE Galletas SET receta = 'Galleta de avena con miel' WHERE id = 10;


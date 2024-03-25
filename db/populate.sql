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

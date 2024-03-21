CREATE USER 'compras'@'%' IDENTIFIED BY 'contraseña_compras';
CREATE USER 'venta'@'%' IDENTIFIED BY 'contraseña_venta';
CREATE USER 'Producción'@'%' IDENTIFIED BY 'contraseña_produccion';
CREATE USER 'Administrador'@'%' IDENTIFIED BY 'contraseña_administrador';


GRANT ALL PRIVILEGES ON base_compras.* TO 'compras'@'%';
GRANT ALL PRIVILEGES ON base_ventas.* TO 'venta'@'%';
GRANT ALL PRIVILEGES ON base_produccion.* TO 'Producción'@'%';
GRANT ALL PRIVILEGES ON base_administracion.* TO 'Administrador'@'%';


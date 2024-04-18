-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: dream
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CorteDiario`
--

DROP TABLE IF EXISTS `CorteDiario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CorteDiario` (
  `idCorte` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `totalEntrada` decimal(10,2) NOT NULL,
  `totalSalida` decimal(10,2) NOT NULL,
  `totalEfectivo` decimal(10,2) NOT NULL,
  PRIMARY KEY (`idCorte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `compras`
--

DROP TABLE IF EXISTS `compras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compras` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_proveedor` int NOT NULL,
  `id_usuario` int NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_proveedor` (`id_proveedor`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `compras_ibfk_1` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`id`),
  CONSTRAINT `compras_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `conversiones`
--

DROP TABLE IF EXISTS `conversiones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conversiones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cantidadSinConvertir` decimal(10,2) NOT NULL,
  `cantidadConvertida` decimal(10,2) NOT NULL,
  `tipoSinConvertir` varchar(100) NOT NULL,
  `tipoConvertido` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `detalle_compra`
--

DROP TABLE IF EXISTS `detalle_compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_compra` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_materia` int NOT NULL,
  `precio_materia` float NOT NULL,
  `cantidad` varchar(100) NOT NULL,
  `tipo` varchar(100) NOT NULL,
  `caducidad` varchar(100) NOT NULL,
  `id_compra` int NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_compra` (`id_compra`),
  KEY `id_materia` (`id_materia`),
  CONSTRAINT `detalle_compra_ibfk_1` FOREIGN KEY (`id_compra`) REFERENCES `compras` (`id`),
  CONSTRAINT `detalle_compra_ibfk_2` FOREIGN KEY (`id_materia`) REFERENCES `materiaprima` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `detalleventa`
--

DROP TABLE IF EXISTS `detalleventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalleventa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `venta_id` int DEFAULT NULL,
  `galleta_id` int DEFAULT NULL,
  `cantidad` decimal(10,2) NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `created_at` datetime NOT NULL,
  `tipoVenta` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `venta_id` (`venta_id`),
  KEY `galleta_id` (`galleta_id`),
  CONSTRAINT `detalleventa_ibfk_1` FOREIGN KEY (`venta_id`) REFERENCES `venta` (`id`),
  CONSTRAINT `detalleventa_ibfk_2` FOREIGN KEY (`galleta_id`) REFERENCES `galletas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `galletas`
--

DROP TABLE IF EXISTS `galletas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `galletas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `enable` int DEFAULT '1',
  `descripcion` text,
  `receta` text,
  `totalGalletas` int NOT NULL,
  `pesoGalleta` decimal(10,2) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ingredientes`
--

DROP TABLE IF EXISTS `ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `galleta_id` int NOT NULL,
  `material_id` int NOT NULL,
  `cantidad` decimal(10,2) NOT NULL,
  `estatus` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `galleta_id` (`galleta_id`),
  KEY `material_id` (`material_id`),
  CONSTRAINT `ingredientes_ibfk_1` FOREIGN KEY (`galleta_id`) REFERENCES `galletas` (`id`),
  CONSTRAINT `ingredientes_ibfk_2` FOREIGN KEY (`material_id`) REFERENCES `materiaprima` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `after_ingredient_insert` AFTER INSERT ON `ingredientes` FOR EACH ROW BEGIN
    
    DECLARE new_cost DECIMAL(10,2);
    
    SELECT COALESCE(SUM(costo_produccion) / min(totalGalletas), 0) into new_cost
FROM (
    SELECT
        nombre_material,
        SUM(cantidad_utilizada * precio_material) AS costo_produccion,
        totalGalletas AS totalGalletas,
        nombre
    FROM (
        SELECT
            mp.material AS nombre_material,
            SUM(i.cantidad) AS cantidad_utilizada,
            ROUND((SUM(mpp.cantidad)  * AVG(mpp.precio)), 2)/ 10000 AS precio_material,
            g.totalGalletas,
            g.nombre nombre
        FROM
            ingredientes i
        JOIN
            materiaprima mp ON i.material_id = mp.id
        JOIN
            galletas g ON i.galleta_id = g.id
JOIN 
materia_prima_proveedor mpp on mpp.materiaprima_id = mp.id
        WHERE
            g.id = NEW.galleta_id and g.enable = 1
        GROUP BY
            mp.material, g.totalGalletas, g.precio, mpp.materiaprima_id, g.nombre, totalGalletas  
    ) AS materiales
    GROUP BY
        nombre_material, nombre, totalGalletas  
) AS materiales;


    
    SET new_cost = CEIL(new_cost * 1.5);

    
    UPDATE galletas
    SET precio = new_cost
    WHERE id = NEW.galleta_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `after_ingredient_update` BEFORE UPDATE ON `ingredientes` FOR EACH ROW BEGIN
    
    DECLARE new_cost DECIMAL(10,2);
    
    SELECT COALESCE(SUM(costo_produccion) / min(totalGalletas), 0) into new_cost
FROM (
    SELECT
        nombre_material,
        SUM(cantidad_utilizada * precio_material) AS costo_produccion,
        totalGalletas AS totalGalletas,
        nombre
    FROM (
        SELECT
            mp.material AS nombre_material,
            SUM(i.cantidad) AS cantidad_utilizada,
            ROUND((SUM(mpp.cantidad)  * AVG(mpp.precio)), 2)/ 10000 AS precio_material,
            g.totalGalletas,
            g.nombre nombre
        FROM
            ingredientes i
        JOIN
            materiaprima mp ON i.material_id = mp.id
        JOIN
            galletas g ON i.galleta_id = g.id
JOIN 
materia_prima_proveedor mpp on mpp.materiaprima_id = mp.id
        WHERE
            g.id = NEW.galleta_id and g.enable = 1
        GROUP BY
            mp.material, g.totalGalletas, g.precio, mpp.materiaprima_id, g.nombre, totalGalletas  
    ) AS materiales
    GROUP BY
        nombre_material, nombre, totalGalletas  
) AS materiales;


    
    SET new_cost = CEIL(new_cost * 1.5);

    
    UPDATE galletas
    SET precio = new_cost
    WHERE id = NEW.galleta_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `inventarioGalletas`
--

DROP TABLE IF EXISTS `inventarioGalletas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventarioGalletas` (
  `idLoteGalletas` int NOT NULL AUTO_INCREMENT,
  `idGalleta` int NOT NULL,
  `cantidad` int NOT NULL,
  `estatus` tinyint(1) DEFAULT NULL,
  `fechaCaducidad` datetime NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`idLoteGalletas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `inventario_materias`
--

DROP TABLE IF EXISTS `inventario_materias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventario_materias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_materia_prima` int NOT NULL,
  `cantidad` varchar(100) NOT NULL,
  `idCompra` int NOT NULL,
  `caducidad` datetime NOT NULL,
  `estatus` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_materia_prima` (`id_materia_prima`),
  KEY `idCompra` (`idCompra`),
  CONSTRAINT `inventario_materias_ibfk_1` FOREIGN KEY (`id_materia_prima`) REFERENCES `MateriaPrima` (`id`),
  CONSTRAINT `inventario_materias_ibfk_2` FOREIGN KEY (`idCompra`) REFERENCES `compras` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `inventario_mp`
--

DROP TABLE IF EXISTS `inventario_mp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventario_mp` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_materia_prima` int NOT NULL,
  `cantidad` varchar(100) NOT NULL,
  `idCompra` int NOT NULL,
  `caducidad` datetime NOT NULL,
  `estatus` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_materia_prima` (`id_materia_prima`),
  KEY `idCompra` (`idCompra`),
  CONSTRAINT `inventario_mp_ibfk_1` FOREIGN KEY (`id_materia_prima`) REFERENCES `materiaprima` (`id`),
  CONSTRAINT `inventario_mp_ibfk_2` FOREIGN KEY (`idCompra`) REFERENCES `compras` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `inventariogalletas`
--

DROP TABLE IF EXISTS `inventariogalletas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventariogalletas` (
  `idLoteGalletas` int NOT NULL AUTO_INCREMENT,
  `idGalleta` int NOT NULL,
  `cantidad` int NOT NULL,
  `fechaCaducidad` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `estatus` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`idLoteGalletas`),
  KEY `idGalleta` (`idGalleta`),
  CONSTRAINT `inventariogalletas_ibfk_1` FOREIGN KEY (`idGalleta`) REFERENCES `galletas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `login_log`
--

DROP TABLE IF EXISTS `login_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `fecha_login` datetime DEFAULT CURRENT_TIMESTAMP,
  `estado` enum('correcto','incorrecto') DEFAULT 'correcto',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `materia_prima_proveedor`
--

DROP TABLE IF EXISTS `materia_prima_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materia_prima_proveedor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `materiaprima_id` int NOT NULL,
  `proveedor_id` int NOT NULL,
  `precio` float NOT NULL,
  `cantidad` varchar(100) NOT NULL,
  `tipo` varchar(100) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `materiaprima_id` (`materiaprima_id`),
  KEY `proveedor_id` (`proveedor_id`),
  CONSTRAINT `materia_prima_proveedor_ibfk_1` FOREIGN KEY (`materiaprima_id`) REFERENCES `materiaprima` (`id`),
  CONSTRAINT `materia_prima_proveedor_ibfk_2` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `materiaprima`
--

DROP TABLE IF EXISTS `materiaprima`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materiaprima` (
  `id` int NOT NULL AUTO_INCREMENT,
  `material` varchar(255) NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `estatus` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `merma_galletas`
--

DROP TABLE IF EXISTS `merma_galletas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `merma_galletas` (
  `idLoteMermas` int NOT NULL AUTO_INCREMENT,
  `idInventarioGalletas` int NOT NULL,
  `cantidad` int NOT NULL,
  `fechaCaducidad` timestamp NULL DEFAULT NULL,
  `justificaion` varchar(255) NOT NULL,
  `estatus` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`idLoteMermas`),
  KEY `idInventarioGalletas` (`idInventarioGalletas`),
  CONSTRAINT `merma_galletas_ibfk_1` FOREIGN KEY (`idInventarioGalletas`) REFERENCES `inventariogalletas` (`idLoteGalletas`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mermas_material`
--

DROP TABLE IF EXISTS `mermas_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mermas_material` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idInventarioMaterias` int NOT NULL,
  `merma_tipo` varchar(100) NOT NULL,
  `merma_fecha` varchar(50) NOT NULL,
  `cantidad` int NOT NULL,
  `created_at` datetime NOT NULL,
  `id_produccion` int DEFAULT NULL,
  `justificacion` varchar(255) NOT NULL,
  `id_proveedor` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_produccion` (`id_produccion`),
  KEY `idInventarioMaterias` (`idInventarioMaterias`),
  KEY `id_proveedor` (`id_proveedor`),
  CONSTRAINT `mermas_material_ibfk_1` FOREIGN KEY (`id_produccion`) REFERENCES `produccion` (`idProduccion`),
  CONSTRAINT `mermas_material_ibfk_2` FOREIGN KEY (`idInventarioMaterias`) REFERENCES `inventario_mp` (`id`),
  CONSTRAINT `mermas_material_ibfk_3` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `password_histories`
--

DROP TABLE IF EXISTS `password_histories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `password_histories` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `password_histories_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `produccion`
--

DROP TABLE IF EXISTS `produccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produccion` (
  `idProduccion` int NOT NULL AUTO_INCREMENT,
  `idSolicitud` int NOT NULL,
  `produccionActual` int NOT NULL,
  `idUsuario` int NOT NULL,
  `estatus` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`idProduccion`),
  KEY `idSolicitud` (`idSolicitud`),
  KEY `produccion_ibfk_2` (`idUsuario`),
  CONSTRAINT `produccion_ibfk_1` FOREIGN KEY (`idSolicitud`) REFERENCES `solicitudproduccion` (`idSolicitud`),
  CONSTRAINT `produccion_ibfk_2` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_empresa` varchar(200) NOT NULL,
  `direccion_empresa` varchar(200) NOT NULL,
  `telefono_empresa` varchar(13) NOT NULL,
  `nombre_encargado` varchar(80) NOT NULL,
  `estatus` tinyint(1) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `id_usuario` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proveedor_ibfk_1` (`id_usuario`),
  CONSTRAINT `proveedor_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `relacionGalletaMateria`
--

DROP TABLE IF EXISTS `relacionGalletaMateria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `relacionGalletaMateria` (
  `idRelacion` int NOT NULL AUTO_INCREMENT,
  `idLoteMateria` int NOT NULL,
  `idLoteGalletas` int NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`idRelacion`),
  KEY `idLoteMateria` (`idLoteMateria`),
  KEY `idLoteGalletas` (`idLoteGalletas`),
  CONSTRAINT `relacionGalletaMateria_ibfk_1` FOREIGN KEY (`idLoteMateria`) REFERENCES `inventario_materias` (`id`),
  CONSTRAINT `relacionGalletaMateria_ibfk_2` FOREIGN KEY (`idLoteGalletas`) REFERENCES `inventarioGalletas` (`idLoteGalletas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `solicitudProduccion`
--

DROP TABLE IF EXISTS `solicitudProduccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `solicitudProduccion` (
  `idSolicitud` int NOT NULL AUTO_INCREMENT,
  `idGalleta` int NOT NULL,
  `cantidad` int NOT NULL,
  `estatus` varchar(50) DEFAULT NULL,
  `justificacion` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`idSolicitud`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `solicitudproduccion`
--

DROP TABLE IF EXISTS `solicitudproduccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `solicitudproduccion` (
  `idSolicitud` int NOT NULL AUTO_INCREMENT,
  `idLoteGalletas` int NOT NULL,
  `cantidad` int NOT NULL,
  `estatus` varchar(20) DEFAULT NULL,
  `justificacion` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`idSolicitud`),
  KEY `idLoteGalletas` (`idLoteGalletas`),
  CONSTRAINT `solicitudproduccion_ibfk_1` FOREIGN KEY (`idLoteGalletas`) REFERENCES `inventariogalletas` (`idLoteGalletas`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(64) NOT NULL,
  `rol` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `is_blocked` tinyint(1) DEFAULT '0',
  `blocked_until` datetime DEFAULT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fecha_venta` datetime NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `created_at` datetime NOT NULL,
  `idUsuario` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `venta_ibfk_1` (`idUsuario`),
  CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `verification_code`
--

DROP TABLE IF EXISTS `verification_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `verification_code` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-17 21:32:04

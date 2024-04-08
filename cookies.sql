-- Active: 1710919255921@@127.0.0.1@3306@cookies
#drop DATABASE cookies;
CREATE DATABASE  IF NOT EXISTS `cookies` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cookies`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cookies
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

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
  `created_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`id`),
  FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compras`
--

LOCK TABLES `compras` WRITE;
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cortediario`
--

DROP TABLE IF EXISTS `CorteDiario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CorteDiario` (
  `idCorte` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `totalEntrada` DECIMAL(10,2) NOT NULL,
  `totalSalida` DECIMAL(10,2) NOT NULL,
  `totalEfectivo` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`idCorte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cortediario`
--

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
  `created_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`id_compra`) REFERENCES `compras` (`id`),
  FOREIGN KEY (`id_materia`) REFERENCES `materiaprima` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_compra`
--

LOCK TABLES `detalle_compra` WRITE;
/*!40000 ALTER TABLE `detalle_compra` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_compra` ENABLE KEYS */;
UNLOCK TABLES;

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
  `created_at` DATETIME NOT NULL,
  `tipoVenta` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `venta_id` (`venta_id`),
  KEY `galleta_id` (`galleta_id`),
  CONSTRAINT `detalleventa_ibfk_1` FOREIGN KEY (`venta_id`) REFERENCES `venta` (`id`),
  CONSTRAINT `detalleventa_ibfk_2` FOREIGN KEY (`galleta_id`) REFERENCES `galletas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalleventa`
--

LOCK TABLES `detalleventa` WRITE;
/*!40000 ALTER TABLE `detalleventa` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalleventa` ENABLE KEYS */;
UNLOCK TABLES;

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
  `totalGalletas` int not null,
  `pesoGalleta` decimal(10,2) NOT NULL,
  `created_at` DATETIME NOT NULL default now(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




--
-- Dumping data for table `galletas`
--

LOCK TABLES `galletas` WRITE;
/*!40000 ALTER TABLE `galletas` DISABLE KEYS */;
INSERT INTO `galletas`(id,nombre,precio,enable,descripcion,receta,totalGalletas,pesoGalleta) VALUES (1,'Galleta de avena',10.00,1,'Galleta de avena con pasas','Galleta de avena con pasas',100,10.00),(2,'Galleta de chocolate',15.00,1,'Galleta de chocolate con chips de chocolate','Galleta de chocolate con chips',100,10.00),(3,'Galleta de azúcar',5.00,1,'Galleta de azúcar con azúcar glass','Galleta de azúcar con azúcar glass',100,10.00),(4,'Galleta de Pasas y Nueces',8.00,1,'Galleta de avena con pasas y nueces','Galleta de avena con pasas y nueces',100,10.00),(5,'Galleta de Limón y Coco',12.00,1,'Galleta de limón con coco rallado','Galleta de limón con coco rallado',100,10.00),(6,'Galleta de Jengibre',7.00,1,'Galleta de jengibre con azúcar glass','Galleta de jengibre con azúcar glass',100,10.00),(7,'Galleta de Especias',6.00,1,'Galleta de especias con azúcar glass','Galleta de especias con azúcar glass',100,10.00),(8,'Galleta de Miel',9.00,1,'Galleta de miel con almendras fileteadas','Galleta de miel con almendras fileteadas',100,10.00),(9,'Galleta de Chocolate y Coco',14.00,1,'Galleta de chocolate con coco rallado','Galleta de chocolate con coco rallado muy bueno',100,10.00),(10,'Galleta de Avena y Miel',11.00,1,'Galleta de avena con miel','Galleta de avena con miel',100,10.00);

/*!40000 ALTER TABLE `galletas` ENABLE KEYS */;
UNLOCK TABLES;

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
  `estatus` BOOLEAN NOT NULL DEFAULT TRUE,
  `created_at` DATETIME NOT NULL DEFAULT now(),
  `updated_at` DATETIME NOT NULL,
  `deleted_at` DATETIME,
  PRIMARY KEY (`id`),
  KEY `galleta_id` (`galleta_id`),
  KEY `material_id` (`material_id`),
  CONSTRAINT `ingredientes_ibfk_1` FOREIGN KEY (`galleta_id`) REFERENCES `galletas` (`id`),
  CONSTRAINT `ingredientes_ibfk_2` FOREIGN KEY (`material_id`) REFERENCES `materiaprima` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientes`
--

LOCK TABLES `ingredientes` WRITE;
/*!40000 ALTER TABLE `ingredientes` DISABLE KEYS */;
INSERT INTO `ingredientes`(id,galleta_id,material_id,cantidad) VALUES (1,1,2,500.00),(2,1,6,50.00),(3,1,7,5.00),(4,1,8,100.00),(5,2,2,500.00),(6,2,6,5.00),(7,2,7,50.00),(8,2,9,100.00),(9,3,2,500.00),(10,3,6,50.00),(11,3,7,5.00),(12,3,10,100.00),(13,4,2,500.00),(14,4,6,50.00),(15,4,7,5.00),(16,4,8,100.00),(17,4,19,50.00),(18,5,1,500.00),(19,5,3,50.00),(20,5,4,5.00),(21,5,5,1.00),(22,5,12,10.00),(23,5,18,50.00),(24,6,1,500.00),(25,6,3,50.00),(26,6,4,5.00),(27,6,5,1.00),(28,6,13,15.00),(29,6,10,100.00),(30,7,1,500.00),(31,7,3,50.00),(32,7,4,5.00),(33,7,5,1.00),(34,7,14,25.00),(35,7,15,5.00),(36,7,16,5.00),(37,7,10,100.00),(38,8,1,500.00),(39,8,3,50.00),(40,8,4,5.00),(41,8,5,1.00),(42,8,17,50.00),(43,8,11,100.00),(44,9,1,500.00),(45,9,3,50.00),(46,9,4,5.00),(47,9,5,1.00),(48,9,9,100.00),(49,9,18,50.00),(50,10,2,500.00),(51,10,6,50.00),(52,10,7,5.00),(53,10,17,50.00);
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventario_materias`
--

DROP TABLE IF EXISTS `inventario_materias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventario_materias` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_materia_prima` INT NOT NULL,
    `cantidad` VARCHAR(100) NOT NULL,
    `idCompra` INT NOT NULL,
    `caducidad` DATETIME NOT NULL,
    `estatus` BOOLEAN NOT NULL DEFAULT TRUE,
    `created_at` DATETIME NOT NULL,
    FOREIGN KEY (id_materia_prima) REFERENCES MateriaPrima (id),
    FOREIGN KEY (idCompra) REFERENCES compras (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventario_materias`
--

LOCK TABLES `inventario_materias` WRITE;
/*!40000 ALTER TABLE `inventario_materias` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventario_materias` ENABLE KEYS */;
UNLOCK TABLES;

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
  `estatus` BOOLEAN NOT NULL DEFAULT TRUE,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `deleted_at` DATETIME,
  PRIMARY KEY (`idLoteGalletas`),
  KEY `idGalleta` (`idGalleta`),
  CONSTRAINT `inventariogalletas_ibfk_1` FOREIGN KEY (`idGalleta`) REFERENCES `galletas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventariogalletas`
--

LOCK TABLES `inventariogalletas` WRITE;
/*!40000 ALTER TABLE `inventariogalletas` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventariogalletas` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_log`
--

LOCK TABLES `login_log` WRITE;
/*!40000 ALTER TABLE `login_log` DISABLE KEYS */;
INSERT INTO `login_log` VALUES (1,5,'2024-03-25 16:34:38','correcto'),(2,5,'2024-03-25 16:35:01','correcto'),(3,5,'2024-03-25 16:35:39','incorrecto'),(4,5,'2024-03-25 16:37:33','incorrecto'),(5,5,'2024-03-25 16:37:38','incorrecto');
/*!40000 ALTER TABLE `login_log` ENABLE KEYS */;
UNLOCK TABLES;

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
  `estatus` BOOLEAN NOT NULL DEFAULT TRUE,
  `created_at` DATETIME NOT NULL DEFAULT now(),
  `updated_at` DATETIME,
  `deleted_at` DATETIME,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materiaprima`
--

LOCK TABLES `materiaprima` WRITE;
/*!40000 ALTER TABLE `materiaprima` DISABLE KEYS */;
INSERT INTO `materiaprima`(id,material,tipo) VALUES (1,'harina','gramos'),(2,'avena','gramos'),(3,'mantequilla','gramos'),(4,'azúcar','gramos'),(5,'huevo','unidad'),(6,'esencia de vainilla','mililitros'),(7,'bicarbonato de sodio','gramos'),(8,'pasas','gramos'),(9,'cacao en polvo','gramos'),(10,'chips de chocolate','gramos'),(11,'azúcar glass','gramos'),(12,'almendras fileteadas','gramos'),(13,'jengibre molido','gramos'),(14,'canela','gramos'),(15,'clavo molido','gramos'),(16,'nuez moscada','gramos'),(17,'miel','mililitros'),(18,'coco rallado','gramos'),(19,'nueces picadas','gramos');
/*!40000 ALTER TABLE `materiaprima` ENABLE KEYS */;
UNLOCK TABLES;

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
  `estatus` BOOLEAN NOT NULL DEFAULT TRUE,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `deleted_at` DATETIME,
  PRIMARY KEY (`idLoteMermas`),
  KEY `idInventarioGalletas` (`idInventarioGalletas`),
  CONSTRAINT `merma_galletas_ibfk_1` FOREIGN KEY (`idInventarioGalletas`) REFERENCES `inventariogalletas` (`idLoteGalletas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS `mermas_material`;
CREATE TABLE mermas_material (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  	idInventarioMaterias INT NOT NULL,
    merma_tipo VARCHAR(100) NOT NULL,
    merma_fecha VARCHAR(50) NOT NULL,
    cantidad INT NOT NULL,
    created_at DATETIME NOT NULL,
    id_produccion INT,
    justificacion VARCHAR(255) NOT NULL,
    id_proveedor INT,
    FOREIGN KEY (id_produccion) REFERENCES produccion (idProduccion),
    FOREIGN KEY (idInventarioMaterias) REFERENCES inventario_mp (id),
    FOREIGN KEY (id_proveedor) REFERENCES proveedor (id)
);

--
-- Dumping data for table `merma_galletas`
--

LOCK TABLES `merma_galletas` WRITE;
/*!40000 ALTER TABLE `merma_galletas` DISABLE KEYS */;
/*!40000 ALTER TABLE `merma_galletas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `password_histories`
--

DROP TABLE IF EXISTS `password_histories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `password_histories` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `password_histories`
--

LOCK TABLES `password_histories` WRITE;
/*!40000 ALTER TABLE `password_histories` DISABLE KEYS */;
INSERT INTO `password_histories` VALUES (1,5,'contraseña123','2024-03-25 21:41:21'),(2,1,'nueva_contraseña456','2024-03-25 21:41:31'),(3,5,'contraseña123','2024-03-25 22:38:03');
/*!40000 ALTER TABLE `password_histories` ENABLE KEYS */;
UNLOCK TABLES;

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
  `estatus` BOOLEAN NOT NULL DEFAULT true,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `deleted_at` DATETIME,
  PRIMARY KEY (`idProduccion`),
  KEY `idSolicitud` (`idSolicitud`),
  CONSTRAINT `produccion_ibfk_1` FOREIGN KEY (`idSolicitud`) REFERENCES `solicitudproduccion` (`idSolicitud`),
  CONSTRAINT `produccion_ibfk_2` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion`
--

LOCK TABLES `produccion` WRITE;
/*!40000 ALTER TABLE `produccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `produccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`nombre_empresa` VARCHAR(200) NOT NULL,
    `direccion_empresa` VARCHAR(200) NOT NULL,
    `telefono_empresa` VARCHAR(13) NOT NULL,
    `nombre_encargado` VARCHAR(80) NOT NULL,
    `estatus` BOOLEAN NOT NULL,
    `created_at` DATETIME NOT NULL,
    `updated_at` DATETIME,
    `deleted_at` DATETIME,
	`id_usuario`int ,
  CONSTRAINT `proveedor_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

CREATE TABLE `materia_prima_proveedor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `materiaprima_id` int NOT NULL,
  `proveedor_id` int NOT NULL,
  `precio` float NOT NULL,
  `cantidad` varchar(100) NOT NULL,
  `tipo` varchar(100) NOT NULL,
  `created_at` DATETIME NOT NULL,

  PRIMARY KEY (`id`),
  FOREIGN KEY (`materiaprima_id`) REFERENCES `materiaprima`(`id`),
  FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor`(`id`)
);

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
  `justificacion` varchar(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`idSolicitud`),
  KEY `idLoteGalletas` (`idLoteGalletas`),
  CONSTRAINT `solicitudproduccion_ibfk_1` FOREIGN KEY (`idLoteGalletas`) REFERENCES `inventariogalletas` (`idLoteGalletas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solicitudproduccion`
--

LOCK TABLES `solicitudproduccion` WRITE;
/*!40000 ALTER TABLE `solicitudproduccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `solicitudproduccion` ENABLE KEYS */;
UNLOCK TABLES;

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
  `estado` BOOLEAN NOT NULL DEFAULT TRUE,
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `is_blocked` tinyint(1) DEFAULT '0',
  `blocked_until` datetime DEFAULT NULL,
  `updated_at` DATETIME NOT NULL,
  `deleted_at` DATETIME,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario`
(id,nombre,apellido,email,password,rol,estado,fecha_creacion,is_blocked,blocked_until)
 VALUES (1,'Elena','Martínez','elena@example.com','nueva_contraseña456','ventas','activo','2024-03-21 18:53:51',0,NULL),(2,'Yuri','Gómez','jonarrodi99@gmail.com','admin_pass456','admin','activo','2024-03-21 18:54:19',0,NULL),(3,'Laura','Hernández','laura@example.com','compras_pass789','compras','activo','2024-03-21 18:54:28',0,NULL),(4,'Pedro','Sánchez','pedro@example.com','produccion_pass321','produccion','activo','2024-03-21 18:54:35',0,NULL),(5,'Juan','Perez','juan@example.com','contraseña123','usuario','activo','2024-03-25 21:41:21',1,'2024-03-25 16:43:03');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `password_history_trigger` AFTER INSERT ON `usuario` FOR EACH ROW BEGIN
    INSERT INTO password_histories (user_id, password, fecha_creacion)
    VALUES (NEW.id, NEW.password, NEW.fecha_creacion);
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
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `password_update_trigger` AFTER UPDATE ON `usuario` FOR EACH ROW BEGIN
    INSERT INTO password_histories (user_id, password, fecha_creacion)
    VALUES (NEW.id, NEW.password, CURRENT_TIMESTAMP);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;


DROP PROCEDURE IF EXISTS block_user;
DELIMITER //
CREATE PROCEDURE unblock_user(IN user_email VARCHAR(50))
BEGIN
    DECLARE actual_date DATETIME;
    DECLARE blocked_until DATETIME;
    SET actual_date = NOW();

    # ver si la fecha de bloqueo es menor a la fecha actual
    SET blocked_until = (SELECT blocked_until FROM usuario WHERE email = user_email);

    IF blocked_until < actual_date THEN
        UPDATE usuario SET is_blocked = 0, blocked_until = NULL WHERE email = user_email;
    END IF;
END //
DELIMITER ;




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
  `created_at` DATETIME NOT NULL,
  `idUsuario` int NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'cookies'
--

--
-- Dumping routines for database 'cookies'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-27 21:24:14


INSERT INTO proveedor (nombre_empresa, direccion_empresa, telefono_empresa, nombre_encargado
, estatus, created_at, updated_at)
VALUES ('Proveedor 1', 'Dirección 1', '123456789', 'Persona 1', 1, NOW(), NOW());

INSERT INTO proveedor (nombre_empresa, direccion_empresa, telefono_empresa, nombre_encargado, estatus, created_at, updated_at)
VALUES ('Proveedor 2', 'Dirección 2', '987654321', 'Persona 2', 1, NOW(), NOW());

INSERT INTO proveedor (nombre_empresa, direccion_empresa, telefono_empresa, nombre_encargado, estatus, created_at, updated_at)
VALUES ('Proveedor 3', 'Dirección 3', '555555555', 'Persona 3', 1, NOW(), NOW());

INSERT INTO proveedor (nombre_empresa, direccion_empresa, telefono_empresa, nombre_encargado, estatus, created_at, updated_at)
VALUES ('Proveedor 4', 'Dirección 4', '666666666', 'Persona 4', 1, NOW(), NOW());

INSERT INTO proveedor (nombre_empresa, direccion_empresa, telefono_empresa, nombre_encargado, estatus, created_at, updated_at)
VALUES ('Proveedor 5', 'Dirección 5', '777777777', 'Persona 5', 1, NOW(), NOW());

INSERT INTO materia_prima_proveedor (materiaprima_id, proveedor_id, precio, cantidad, tipo, created_at)
VALUES (1, 1, 100, '20', 'costal', NOW());


INSERT INTO materia_prima_proveedor (materiaprima_id, proveedor_id, precio, cantidad, tipo, created_at)
VALUES (2, 1, 50, '20', 'costal', NOW());

INSERT INTO materia_prima_proveedor (materiaprima_id, proveedor_id, precio, cantidad, tipo, created_at)
VALUES (3, 2, 50, '20', 'costal', NOW());

drop trigger if EXISTS password_history_trigger;
drop trigger if EXISTS password_update_trigger;

DROP PROCEDURE IF EXISTS EncriptarContrasenas;

DELIMITER //

CREATE PROCEDURE EncriptarContrasenas()
BEGIN
    -- Actualiza la columna de contraseña con su versión encriptada
    UPDATE usuario SET password = SHA2(password, 256);
END //

DELIMITER ;




-- CALL EncriptarContrasenas();



use cookies;

/*
necesitamos materiaprima, cuantos se requiere, a quien se compra, cuando compre, como pague
no es lo mismo comprar al proveedor un costal de 20kilos a los gramos,
estos caducan


quiero producir una charola de 60 galletas, esa recetas ocupa 3k de harina
en el almacen quedaba 1kilo de harina de un costal y 2kilos de un costal,
el costal de 1k costaba 250 y el segundo 385

materia_prima - disponibilidad(clave,fecha_caducidad,cantidad)

materia: id:1, 15:cantidad galones:tipo, 10-03-202

*/


-- select * 
-- from inventario_materias im
-- join materiaprima mp on mp.id = im.id_materia_prima
-- join materia_prima_proveedor mpp on mpp.materiaprima_id = im.id_materia_prima
-- join proveedor p on p.id = mpp.proveedor_id;

describe produccion;
/*
cuantos insumos tengo y cuando necesito,
*/


# Crear una tabla donde se pueda tener una tabla de conversiones
# ya que un proveedor puede venderme un costal de 20 kilos y otro de 50 kilos
# y necesito saber cuanto es en gramos
# ejemplo 1 kilo = 1000 gramos
# un galon = 3785.41 mililitros
# carton de huevo = 30 huevos
# 1 cucharada = 15 mililitros
# 1 cucharadita = 5 mililitros
# 1 taza = 250 mililitros


# tabla de conversiones

CREATE TABLE conversiones (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cantidadSinConvertir DECIMAL(10,2) NOT NULL,
    cantidadConvertida DECIMAL(10,2) NOT NULL,
    tipoSinConvertir VARCHAR(100) NOT NULL,
    tipoConvertido VARCHAR(100) NOT NULL
);


#kilos a gramos
INSERT INTO conversiones (cantidadSinConvertir, cantidadConvertida, tipoSinConvertir, tipoConvertido)
VALUES (1, 1000, 'kilos', 'gramos');

#galones a mililitros
INSERT INTO conversiones (cantidadSinConvertir, cantidadConvertida, tipoSinConvertir, tipoConvertido)
VALUES (1, 3785.41, 'galones', 'mililitros');

#carton de huevo a huevos
INSERT INTO conversiones (cantidadSinConvertir, cantidadConvertida, tipoSinConvertir, tipoConvertido)
VALUES (1, 30, 'carton de huevo', 'huevos');

#cucharada a mililitros
INSERT INTO conversiones (cantidadSinConvertir, cantidadConvertida, tipoSinConvertir, tipoConvertido)
VALUES (1, 15, 'cucharada', 'mililitros');

#cucharadita a mililitros
INSERT INTO conversiones (cantidadSinConvertir, cantidadConvertida, tipoSinConvertir, tipoConvertido)
VALUES (1, 5, 'cucharadita', 'mililitros');

#taza a mililitros
INSERT INTO conversiones (cantidadSinConvertir, cantidadConvertida, tipoSinConvertir, tipoConvertido)
VALUES (1, 250, 'taza', 'mililitros');

#costal de 20 kilos a gramos
INSERT INTO conversiones (cantidadSinConvertir, cantidadConvertida, tipoSinConvertir, tipoConvertido)
VALUES (20, 20000, 'costal', 'gramos');


# consulta para saber el nombre de los materiales por galleta

SELECT g.nombre, mp.material, i.cantidad FROM galletas g
JOIN ingredientes i ON i.galleta_id = g.id
JOIN materiaprima mp ON mp.id = i.material_id
where g.nombre = 'Galleta de avena';
;

drop table if exists materia_prima_proveedor;
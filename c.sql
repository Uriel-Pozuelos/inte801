-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: cookies
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.20.04.2

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
-- Current Database: `cookies`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `cookies` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `cookies`;

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
-- Dumping data for table `CorteDiario`
--

LOCK TABLES `CorteDiario` WRITE;
/*!40000 ALTER TABLE `CorteDiario` DISABLE KEYS */;
/*!40000 ALTER TABLE `CorteDiario` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `conversiones`
--

LOCK TABLES `conversiones` WRITE;
/*!40000 ALTER TABLE `conversiones` DISABLE KEYS */;
INSERT INTO `conversiones` VALUES (1,1.00,1000.00,'kilos','gramos'),(2,1.00,3785.41,'galones','mililitros'),(3,1.00,30.00,'carton de huevo','huevos'),(4,1.00,15.00,'cucharada','mililitros'),(5,1.00,5.00,'cucharadita','mililitros'),(6,1.00,250.00,'taza','mililitros'),(7,20.00,20000.00,'costal','gramos');
/*!40000 ALTER TABLE `conversiones` ENABLE KEYS */;
UNLOCK TABLES;

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
  `created_at` datetime NOT NULL,
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
  `totalGalletas` int NOT NULL,
  `pesoGalleta` decimal(10,2) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `galletas`
--

LOCK TABLES `galletas` WRITE;
/*!40000 ALTER TABLE `galletas` DISABLE KEYS */;
INSERT INTO `galletas` VALUES (1,'Galleta de avena',10.00,1,'Galleta de avena con pasas','Galleta de avena con pasas',100,10.00,'2024-04-04 00:05:21'),(2,'Galleta de chocolate',15.00,1,'Galleta de chocolate con chips de chocolate','Galleta de chocolate con chips',100,10.00,'2024-04-04 00:05:21'),(3,'Galleta de azúcar',5.00,1,'Galleta de azúcar con azúcar glass','Galleta de azúcar con azúcar glass',100,10.00,'2024-04-04 00:05:21'),(4,'Galleta de Pasas y Nueces',8.00,1,'Galleta de avena con pasas y nueces','Galleta de avena con pasas y nueces',100,10.00,'2024-04-04 00:05:21'),(5,'Galleta de Limón y Coco',12.00,1,'Galleta de limón con coco rallado','Galleta de limón con coco rallado',100,10.00,'2024-04-04 00:05:21'),(6,'Galleta de Jengibre',7.00,1,'Galleta de jengibre con azúcar glass','Galleta de jengibre con azúcar glass',100,10.00,'2024-04-04 00:05:21'),(7,'Galleta de Especias',6.00,1,'Galleta de especias con azúcar glass','Galleta de especias con azúcar glass',100,10.00,'2024-04-04 00:05:21'),(8,'Galleta de Miel',9.00,1,'Galleta de miel con almendras fileteadas','Galleta de miel con almendras fileteadas',100,10.00,'2024-04-04 00:05:21'),(9,'Galleta de Chocolate y Coco',14.00,1,'Galleta de chocolate con coco rallado','Galleta de chocolate con coco rallado muy bueno',100,10.00,'2024-04-04 00:05:21'),(10,'Galleta de Avena y Miel',11.00,1,'Galleta de avena con miel','Galleta de avena con miel',100,10.00,'2024-04-04 00:05:21');
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
  `estatus` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
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
INSERT INTO `ingredientes` VALUES (1,1,2,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(2,1,6,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(3,1,7,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(4,1,8,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(5,2,2,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(6,2,6,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(7,2,7,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(8,2,9,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(9,3,2,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(10,3,6,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(11,3,7,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(12,3,10,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(13,4,2,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(14,4,6,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(15,4,7,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(16,4,8,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(17,4,19,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(18,5,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(19,5,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(20,5,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(21,5,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(22,5,12,10.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(23,5,18,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(24,6,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(25,6,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(26,6,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(27,6,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(28,6,13,15.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(29,6,10,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(30,7,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(31,7,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(32,7,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(33,7,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(34,7,14,25.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(35,7,15,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(36,7,16,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(37,7,10,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(38,8,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(39,8,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(40,8,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(41,8,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(42,8,17,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(43,8,11,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(44,9,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(45,9,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(46,9,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(47,9,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(48,9,9,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(49,9,18,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(50,10,2,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(51,10,6,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(52,10,7,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(53,10,17,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL);
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

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
  `estatus` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_log`
--

LOCK TABLES `login_log` WRITE;
/*!40000 ALTER TABLE `login_log` DISABLE KEYS */;
INSERT INTO `login_log` VALUES (1,5,'2024-03-25 16:34:38','correcto'),(2,5,'2024-03-25 16:35:01','correcto'),(3,5,'2024-03-25 16:35:39','incorrecto'),(4,5,'2024-03-25 16:37:33','incorrecto'),(5,5,'2024-03-25 16:37:38','incorrecto'),(6,2,'2024-04-03 18:22:19','incorrecto'),(7,2,'2024-04-03 18:22:23','incorrecto'),(8,2,'2024-04-03 18:22:36','correcto');
/*!40000 ALTER TABLE `login_log` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materia_prima_proveedor`
--

LOCK TABLES `materia_prima_proveedor` WRITE;
/*!40000 ALTER TABLE `materia_prima_proveedor` DISABLE KEYS */;
INSERT INTO `materia_prima_proveedor` VALUES (1,1,1,100,'20','costal','2024-04-03 18:05:22'),(2,2,1,50,'20','costal','2024-04-03 18:05:22'),(3,3,2,50,'20','costal','2024-04-03 18:05:22');
/*!40000 ALTER TABLE `materia_prima_proveedor` ENABLE KEYS */;
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
  `estatus` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materiaprima`
--

LOCK TABLES `materiaprima` WRITE;
/*!40000 ALTER TABLE `materiaprima` DISABLE KEYS */;
INSERT INTO `materiaprima` VALUES (1,'harina','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(2,'avena','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(3,'mantequilla','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(4,'azúcar','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(5,'huevo','unidad',1,'2024-04-04 00:05:21',NULL,NULL),(6,'esencia de vainilla','mililitros',1,'2024-04-04 00:05:21',NULL,NULL),(7,'bicarbonato de sodio','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(8,'pasas','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(9,'cacao en polvo','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(10,'chips de chocolate','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(11,'azúcar glass','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(12,'almendras fileteadas','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(13,'jengibre molido','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(14,'canela','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(15,'clavo molido','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(16,'nuez moscada','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(17,'miel','mililitros',1,'2024-04-04 00:05:21',NULL,NULL),(18,'coco rallado','gramos',1,'2024-04-04 00:05:21',NULL,NULL),(19,'nueces picadas','gramos',1,'2024-04-04 00:05:21',NULL,NULL);
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
  `estatus` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`idLoteMermas`),
  KEY `idInventarioGalletas` (`idInventarioGalletas`),
  CONSTRAINT `merma_galletas_ibfk_1` FOREIGN KEY (`idInventarioGalletas`) REFERENCES `inventariogalletas` (`idLoteGalletas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `merma_galletas`
--

LOCK TABLES `merma_galletas` WRITE;
/*!40000 ALTER TABLE `merma_galletas` DISABLE KEYS */;
/*!40000 ALTER TABLE `merma_galletas` ENABLE KEYS */;
UNLOCK TABLES;

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
  `id_produccion` int NOT NULL,
  `justificacion` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_produccion` (`id_produccion`),
  KEY `idInventarioMaterias` (`idInventarioMaterias`),
  CONSTRAINT `mermas_material_ibfk_1` FOREIGN KEY (`id_produccion`) REFERENCES `produccion` (`idProduccion`),
  CONSTRAINT `mermas_material_ibfk_2` FOREIGN KEY (`idInventarioMaterias`) REFERENCES `inventario_materias` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mermas_material`
--

LOCK TABLES `mermas_material` WRITE;
/*!40000 ALTER TABLE `mermas_material` DISABLE KEYS */;
/*!40000 ALTER TABLE `mermas_material` ENABLE KEYS */;
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
  KEY `user_id` (`user_id`),
  CONSTRAINT `password_histories_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`)
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
  `estatus` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`idProduccion`),
  KEY `idSolicitud` (`idSolicitud`),
  KEY `produccion_ibfk_2` (`idUsuario`),
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
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (1,'Proveedor 1','Dirección 1','123456789','Persona 1',1,'2024-04-03 18:05:22','2024-04-03 18:05:22',NULL,NULL),(2,'Proveedor 2','Dirección 2','987654321','Persona 2',1,'2024-04-03 18:05:22','2024-04-03 18:05:22',NULL,NULL),(3,'Proveedor 3','Dirección 3','555555555','Persona 3',1,'2024-04-03 18:05:22','2024-04-03 18:05:22',NULL,NULL),(4,'Proveedor 4','Dirección 4','666666666','Persona 4',1,'2024-04-03 18:05:22','2024-04-03 18:05:22',NULL,NULL),(5,'Proveedor 5','Dirección 5','777777777','Persona 5',1,'2024-04-03 18:05:22','2024-04-03 18:05:22',NULL,NULL);
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

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
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
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
  `estado` tinyint(1) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `is_blocked` tinyint(1) DEFAULT '0',
  `blocked_until` datetime DEFAULT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Elena','Martínez','elena@example.com','f31ed2eb048061d4e344ef0b4cf4b9d8bd23725be583c7ce14d1b1934631a09d','ventas',0,'2024-03-21 18:53:51',0,NULL,'0000-00-00 00:00:00',NULL),(2,'Yuri','Gómez','jonarrodi99@gmail.com','cdc8d376c2a8342ebf8c7424442d092c2add2a4e83442ada5e40b7d0751d60a1','admin',0,'2024-03-21 18:54:19',0,NULL,'0000-00-00 00:00:00',NULL),(3,'Laura','Hernández','laura@example.com','be1da4da2ec5ed3f0264acb96f7c22b58428f088f75b2279afab2cceae29fd06','compras',0,'2024-03-21 18:54:28',0,NULL,'0000-00-00 00:00:00',NULL),(4,'Pedro','Sánchez','pedro@example.com','bdcbc2e12f2dfe1e6af3167a381f2ac5b7613af8b0623798c3ea627df84a68bc','produccion',0,'2024-03-21 18:54:35',0,NULL,'0000-00-00 00:00:00',NULL),(5,'Juan','Perez','juan@example.com','8e7ab8d9fe3b324acdd1f76735eea350ea61ac24cbd17e5446946e5a4c71d999','usuario',0,'2024-03-25 21:41:21',1,'2024-03-25 16:43:03','0000-00-00 00:00:00',NULL);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-04 22:53:20

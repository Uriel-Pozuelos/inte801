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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compras`
--

LOCK TABLES `compras` WRITE;
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` VALUES (2,1,5,'2024-04-08 18:22:07'),(3,1,5,'2024-04-08 18:23:30');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_compra`
--

LOCK TABLES `detalle_compra` WRITE;
/*!40000 ALTER TABLE `detalle_compra` DISABLE KEYS */;
INSERT INTO `detalle_compra` VALUES (1,1,256,'8','costal','2024-04-18',3,'2024-04-08 18:23:30');
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
  `tipoVenta` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `venta_id` (`venta_id`),
  KEY `galleta_id` (`galleta_id`),
  CONSTRAINT `detalleventa_ibfk_1` FOREIGN KEY (`venta_id`) REFERENCES `venta` (`id`),
  CONSTRAINT `detalleventa_ibfk_2` FOREIGN KEY (`galleta_id`) REFERENCES `galletas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalleventa`
--

LOCK TABLES `detalleventa` WRITE;
/*!40000 ALTER TABLE `detalleventa` DISABLE KEYS */;
INSERT INTO `detalleventa` VALUES (1,1,1,1.00,2.50,'2024-04-08 15:02:09','3'),(2,1,1,1.00,2.50,'2024-04-08 15:35:08','3'),(3,1,6,1.00,3.00,'2024-04-08 15:35:08','3'),(4,2,1,1.00,2.50,'2024-04-08 15:40:59','3'),(5,2,7,1.00,3.00,'2024-04-08 15:40:59','3'),(6,2,1,1.00,2.50,'2024-04-08 15:43:49','3');
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
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientes`
--

LOCK TABLES `ingredientes` WRITE;
/*!40000 ALTER TABLE `ingredientes` DISABLE KEYS */;
INSERT INTO `ingredientes` VALUES (5,2,2,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(6,2,6,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(7,2,7,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(8,2,9,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(9,3,2,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(10,3,6,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(11,3,7,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(12,3,10,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(13,4,2,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(14,4,6,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(15,4,7,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(16,4,8,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(17,4,19,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(18,5,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(19,5,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(20,5,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(21,5,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(22,5,12,10.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(23,5,18,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(24,6,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(25,6,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(26,6,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(27,6,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(28,6,13,15.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(29,6,10,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(30,7,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(31,7,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(32,7,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(33,7,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(34,7,14,25.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(35,7,15,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(36,7,16,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(37,7,10,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(38,8,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(39,8,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(40,8,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(41,8,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(42,8,17,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(43,8,11,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(44,9,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(45,9,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(46,9,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(47,9,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(48,9,9,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(49,9,18,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(50,10,2,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(51,10,6,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(52,10,7,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(53,10,17,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(58,1,4,400.00,1,'2024-04-08 18:49:48','2024-04-08 18:51:21',NULL);
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `inventarioGalletas`
--

LOCK TABLES `inventarioGalletas` WRITE;
/*!40000 ALTER TABLE `inventarioGalletas` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventarioGalletas` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventario_mp`
--

LOCK TABLES `inventario_mp` WRITE;
/*!40000 ALTER TABLE `inventario_mp` DISABLE KEYS */;
INSERT INTO `inventario_mp` VALUES (22,1,'20000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(23,2,'2000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(24,3,'5000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(25,4,'20000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(26,5,'900',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(27,6,'500',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(28,7,'800',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(29,8,'2000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(30,9,'6000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(31,10,'2000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(32,1,'160',3,'2024-04-18 00:00:00',1,'2024-04-08 18:23:30');
/*!40000 ALTER TABLE `inventario_mp` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventariogalletas`
--

LOCK TABLES `inventariogalletas` WRITE;
/*!40000 ALTER TABLE `inventariogalletas` DISABLE KEYS */;
INSERT INTO `inventariogalletas` VALUES (21,1,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 17:35:43',NULL),(22,2,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 17:35:43',NULL),(23,3,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 17:35:43',NULL),(24,4,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 17:35:43',NULL),(25,5,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 18:43:12',NULL),(26,6,1,'2024-04-30 08:54:24',0,'2024-04-08 17:35:43','2024-04-08 17:36:29',NULL),(27,7,1,'2024-04-30 08:54:24',0,'2024-04-08 17:35:43','2024-04-08 18:44:34',NULL),(28,8,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 18:16:18',NULL),(29,9,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 17:35:43',NULL),(30,10,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 17:35:43',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_log`
--

LOCK TABLES `login_log` WRITE;
/*!40000 ALTER TABLE `login_log` DISABLE KEYS */;
INSERT INTO `login_log` VALUES (1,5,'2024-03-25 16:34:38','correcto'),(2,5,'2024-03-25 16:35:01','correcto'),(3,5,'2024-03-25 16:35:39','incorrecto'),(4,5,'2024-03-25 16:37:33','incorrecto'),(5,5,'2024-03-25 16:37:38','incorrecto'),(6,2,'2024-04-03 18:22:19','incorrecto'),(7,2,'2024-04-03 18:22:23','incorrecto'),(8,2,'2024-04-03 18:22:36','correcto'),(9,2,'2024-04-05 11:53:38','correcto'),(10,2,'2024-04-06 19:59:03','incorrecto'),(11,2,'2024-04-06 19:59:43','incorrecto'),(12,2,'2024-04-06 20:00:22','correcto'),(13,4,'2024-04-06 20:28:48','correcto'),(14,2,'2024-04-06 20:49:06','incorrecto'),(15,2,'2024-04-06 20:49:10','incorrecto'),(16,2,'2024-04-06 20:49:16','incorrecto'),(17,4,'2024-04-06 21:11:43','correcto'),(18,5,'2024-04-07 12:34:21','correcto'),(19,4,'2024-04-07 12:38:46','incorrecto'),(20,5,'2024-04-07 12:38:59','correcto'),(21,5,'2024-04-07 12:39:18','incorrecto'),(22,5,'2024-04-07 12:39:22','incorrecto'),(23,5,'2024-04-07 12:39:28','incorrecto'),(24,2,'2024-04-07 12:56:44','correcto'),(25,4,'2024-04-07 12:58:57','correcto'),(26,5,'2024-04-07 12:59:36','correcto'),(27,5,'2024-04-08 13:56:12','correcto'),(28,5,'2024-04-08 14:08:10','correcto'),(29,5,'2024-04-08 14:45:29','correcto'),(30,5,'2024-04-08 15:53:27','correcto'),(31,5,'2024-04-08 16:02:56','correcto'),(32,5,'2024-04-08 17:27:06','correcto'),(33,5,'2024-04-08 18:28:38','correcto'),(34,5,'2024-04-08 18:41:03','correcto');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion`
--

LOCK TABLES `produccion` WRITE;
/*!40000 ALTER TABLE `produccion` DISABLE KEYS */;
INSERT INTO `produccion` VALUES (1,1,0,1,0,'2024-04-08 18:15:05','2024-04-08 18:15:05',NULL),(2,4,0,1,0,'2024-04-08 18:44:42','2024-04-08 18:44:42',NULL);
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
INSERT INTO `proveedor` VALUES (1,'Proveedor 1','Dirección 1','123456789','Persona 1',1,'2024-04-03 18:05:22','2024-04-03 18:05:22',NULL,NULL),(2,'Proveedor 2','Dirección 2','987654321','Persona 2',1,'2024-04-03 18:05:22','2024-04-03 18:05:22',NULL,NULL),(3,'Proveedor 3','Dirección 3','555555555','Persona 3',1,'2024-04-03 18:05:22','2024-04-03 18:05:22',NULL,NULL),(4,'Proveedor 4','Dirección 4','666666666','Persona 4',1,'2024-04-03 18:05:22','2024-04-03 18:05:22',NULL,NULL),(5,'Proveedor 5','Dirección 5','99999999','Persona 5',1,'2024-04-03 18:05:22','2024-04-08 17:27:59',NULL,5);
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `solicitudProduccion`
--

LOCK TABLES `solicitudProduccion` WRITE;
/*!40000 ALTER TABLE `solicitudProduccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `solicitudProduccion` ENABLE KEYS */;
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
  `justificacion` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`idSolicitud`),
  KEY `idLoteGalletas` (`idLoteGalletas`),
  CONSTRAINT `solicitudproduccion_ibfk_1` FOREIGN KEY (`idLoteGalletas`) REFERENCES `inventariogalletas` (`idLoteGalletas`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solicitudproduccion`
--

LOCK TABLES `solicitudproduccion` WRITE;
/*!40000 ALTER TABLE `solicitudproduccion` DISABLE KEYS */;
INSERT INTO `solicitudproduccion` VALUES (1,26,12,'Aceptada',NULL,'2024-04-08 17:36:29','2024-04-08 18:15:05'),(2,25,12,'Rechazada','no hay suficiente materia','2024-04-08 17:36:39','2024-04-08 18:43:12'),(3,28,20,'Rechazada','No hay suficiente material','2024-04-08 18:00:02','2024-04-08 18:16:18'),(4,27,40,'Aceptada',NULL,'2024-04-08 18:44:34','2024-04-08 18:44:42');
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
INSERT INTO `usuario` VALUES (1,'Elena','Martínez','elena@example.com','f31ed2eb048061d4e344ef0b4cf4b9d8bd23725be583c7ce14d1b1934631a09d','ventas',0,'2024-03-21 18:53:51',0,NULL,'0000-00-00 00:00:00',NULL),(2,'Yuri','Gómez','jonarrodi99@gmail.com','cdc8d376c2a8342ebf8c7424442d092c2add2a4e83442ada5e40b7d0751d60a1','admin',0,'2024-03-21 18:54:19',0,NULL,'2024-04-07 12:56:44',NULL),(3,'Laura','Hernández','laura@example.com','be1da4da2ec5ed3f0264acb96f7c22b58428f088f75b2279afab2cceae29fd06','compras',0,'2024-03-21 18:54:28',0,NULL,'0000-00-00 00:00:00',NULL),(4,'Pedro','Sánchez Juarez','pedro@example.com','bdcbc2e12f2dfe1e6af3167a381f2ac5b7613af8b0623798c3ea627df84a68bc','produccion',0,'2024-03-21 18:54:35',0,NULL,'2024-04-07 12:58:34',NULL),(5,'Juan','Perez','juan@example.com','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','admin',0,'2024-03-25 21:41:21',0,NULL,'2024-04-07 12:59:36',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES (1,'2024-04-08 14:56:58',5.50,'2024-04-08 14:56:58',5),(2,'2024-04-08 15:40:41',2.50,'2024-04-08 15:40:41',5);
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

#consulta para saber las ganancias de las ventas quitando 

describe venta;

# consulta para saber las ventas que de hicieron en un determinado rango de fechas

SELECT 
    venta.id,
    venta.fecha_venta,
    venta.total,
    usuario.nombre,
    usuario.apellido

 FROM venta join usuario on venta.idUsuario = usuario.id WHERE fecha_venta BETWEEN now() AND now();

insert into materia_prima_proveedor (materiaprima_id, proveedor_id, precio, cantidad, tipo, created_at) values (1, 1, '100', '20', 'red', '2024-04-03 18:05:22');


INSERT into materia_prima_proveedor (materiaprima_id, proveedor_id, precio, cantidad, tipo, created_at) values (13 5, 100, '20', 'costal', '2024-04-03 18:05:22');

SELECT * from inventariogalletas;

# consulta para saber las materias primas que tienen menos materiales en inventario

SELECT *
FROM materiaprima
JOIN inventario_mp ON inventario_mp.idMateriaPrima = materiaprima.id
WHERE inventario_mp.cantidad < 10
LIMIT 10;

 SELECT * FROM materiaprima JOIN inventario_mp ON inventario_mp.id_materia_prima = materiaprima.id
 WHERE inventario_mp.cantidad < 100
LIMIT 10
 ;



-- Dump completed on 2024-04-08 20:09:24

# consulta para saber un determinado lote de galletas, saber que empreado la produjo

SELECT inventariogalletas.idLoteGalletas, inventariogalletas.idGalleta, inventariogalletas.cantidad, inventariogalletas.fechaCaducidad, inventariogalletas.estatus, inventariogalletas.created_at, inventariogalletas.updated_at, inventariogalletas.deleted_at, usuario.nombre, usuario.apellido
FROM inventariogalletas
JOIN produccion ON produccion.idProduccion = inventariogalletas.idLoteGalletas
JOIN usuario ON usuario.id = produccion.idUsuario
WHERE inventariogalletas.idLoteGalletas = 1;

# consulta para saber un determinado lote de galletas, saber que proveedor proporciono la materia prima

SELECT inventariogalletas.idLoteGalletas, inventariogalletas.idGalleta, inventariogalletas.cantidad, inventariogalletas.fechaCaducidad, inventariogalletas.estatus, inventariogalletas.created_at, inventariogalletas.updated_at, inventariogalletas.deleted_at, proveedor.nombre_empresa
FROM inventariogalletas
JOIN materia_prima_proveedor ON materia_prima_proveedor.materiaprima_id = inventariogalletas.idGalleta
JOIN proveedor ON proveedor.id = materia_prima_proveedor.proveedor_id
WHERE inventariogalletas.idLoteGalletas = 22;

#ver los imgredientes de una galleta

SELECT galletas.id, galletas.nombre, galletas.precio, galletas.estatus, galletas.created_at, galletas.updated_at, galletas.deleted_at, materiaprima.material, materiaprima.tipo
FROM galletas
JOIN (
    SELECT galletas.id, galletas.nombre, galletas.precio, galletas.estatus, galletas.created_at, galletas.updated_at, galletas.deleted_at, materia_prima_galleta.materiaprima_id
    FROM galletas
    JOIN materia_prima_galleta ON materia_prima_galleta.galleta_id = galletas.id
    WHERE galletas.id = 1
) AS galletas_materia_prima ON galletas_materia_prima.id = galletas.id


# sacar el precio promedio por materia prima
SELECT materiaprima.id, materiaprima.material, materiaprima.tipo, AVG(materia_prima_proveedor.precio) AS precio_promedio
FROM materiaprima
JOIN materia_prima_proveedor ON materia_prima_proveedor.materiaprima_id = materiaprima.id
GROUP BY materiaprima.id;

#usando la QUERY anterior, sacar el precio promedio por materia prima, por gallleta

SELECT galletas.id, galletas.nombre, galletas.precio AVG(materia_prima_proveedor.precio) AS precio_promedio
FROM galletas
JOIN materia_prima_galleta ON materia_prima_galleta.galleta_id = galletas.id
JOIN materia_prima_proveedor ON materia_prima_proveedor.materiaprima_id = materia_prima_galleta.materiaprima_id
GROUP BY galletas.id;

SELECT
    mp.id AS id_material,
    mp.material AS nombre_material,
    AVG(ROUND((i.cantidad * g.precio), 2) / 100) AS costo_promedio_material
FROM
    ingredientes i
JOIN
    materiaprima mp ON i.material_id = mp.id
JOIN
    galletas g ON i.galleta_id = g.id
WHERE
    g.id = 4
GROUP BY
    mp.id, mp.material;
    
    
    select sum(costo_produccion) costo from(
SELECT 
    nombre_material,
    sum(costo_material) as costo_produccion,
    cantidad_utilizada
FROM
    (SELECT
        mp.material AS nombre_material,
        i.cantidad AS cantidad_utilizada,
        AVG(ROUND((i.cantidad* mpp.precio), 2) / 100) AS costo_material
    FROM
        ingredientes i
    JOIN
        materiaprima mp ON i.material_id = mp.id
    JOIN
        materia_prima_proveedor mpp ON mp.id = mpp.materiaprima_id
    JOIN
        galletas g ON i.galleta_id = g.id
    WHERE
        g.id = 7) AS materiales
GROUP BY
    nombre_material) as p;

# saber los materiales que se usaron en una galleta
SELECT g.nombre, mp.material, i.cantidad
FROM galletas g
JOIN ingredientes i ON g.id = i.galleta_id
JOIN materiaprima mp ON i.material_id = mp.id
WHERE g.id = 1;



#pasar los productos de materia_prima_proveedor  a tipo convertido usando la tabla de conversiones

SELECT mpp.id, mpp.materiaprima_id, mpp.proveedor_id, mpp.precio, mpp.cantidad, mpp.tipo, mpp.created_at, c.tipo_convertido
FROM materia_prima_proveedor mpp
JOIN conversiones c ON mpp.tipo = c.tipo_original;


DELIMITER $$

CREATE TRIGGER after_ingredient_insert
AFTER INSERT ON ingredientes
FOR EACH ROW
BEGIN
    -- Variable para almacenar el nuevo costo de producción
    DECLARE new_cost DECIMAL(10,2);

    -- Calcular el costo total de producción actualizado
    SELECT SUM(cantidad * precio_material) INTO new_cost
    FROM (
        SELECT i.galleta_id, i.material_id, i.cantidad, (mpp.precio / 10000) AS precio_material
        FROM ingredientes i
        JOIN materia_prima_proveedor mpp ON i.material_id = mpp.materiaprima_id
        WHERE i.galleta_id = NEW.galleta_id
    ) AS updated_costs;

    -- Calcular el nuevo precio de la galleta: costo de producción + 50%
    SET new_cost = CEIL(new_cost * 1.5);

    -- Actualizar el precio en la tabla de galletas
    UPDATE galletas
    SET precio = new_cost
    WHERE id = NEW.galleta_id;
END$$

DELIMITER ;
SELECT mp.material, mpp.precio, mpp.cantidad, mpp.tipo FROM inventariogalletas ig JOIN materia_prima_proveedor mpp ON mpp.materiaprima_id = ig.idGalleta JOIN materiaprima mp ON mp.id = mpp.materiaprima_id WHERE ig.idLoteGalletas = 1 AND mpp.proveedor_id = 1;

#en la consulta hay un error ya que une el materia_prima_proveedor usando el id de la materia
#prima con el id de la galleta, lo cual no es correcto, ya que el id de la materia prima
#debe ser igual al id de la materia prima en la tabla de materia prima proveedor
#por lo que primero se debe hacer una subconsulta para saber que materias primas 
# se usan en una galleta y despues hacer el join con la tabla de materia prima proveedor
#para saber el precio de cada materia prima y que proveedor la proporciona



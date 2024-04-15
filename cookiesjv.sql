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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compras`
--

LOCK TABLES `compras` WRITE;
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` VALUES (2,1,5,'2024-04-08 18:22:07'),(3,1,5,'2024-04-08 18:23:30'),(4,1,5,'2024-04-11 18:29:33'),(5,2,5,'2024-04-11 18:30:13'),(6,2,5,'2024-04-11 18:32:25'),(7,5,5,'2024-04-13 10:04:41'),(8,5,5,'2024-04-13 10:06:39'),(9,1,5,'2024-04-13 10:10:13'),(10,1,5,'2024-04-13 10:12:09'),(11,2,5,'2024-04-13 18:15:35'),(12,2,5,'2024-04-13 20:26:33');
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_compra`
--

LOCK TABLES `detalle_compra` WRITE;
/*!40000 ALTER TABLE `detalle_compra` DISABLE KEYS */;
INSERT INTO `detalle_compra` VALUES (1,1,256,'8','costal','2024-04-18',3,'2024-04-08 18:23:30'),(2,6,30,'5','frasco 500 ml','2024-04-30',4,'2024-04-11 18:29:33'),(3,1,70,'23','costal','2024-05-01',5,'2024-04-11 18:30:13'),(4,8,20,'8','bolsa','2024-04-25',6,'2024-04-11 18:32:25'),(5,1,315,'1','costal','2024-04-13',7,'2024-04-13 10:04:41'),(6,2,21.5,'20','costal','2024-04-13',8,'2024-04-13 10:06:39'),(7,7,20000,'10000','bolsa','2024-04-30',10,'2024-04-13 10:12:09'),(8,7,6000,'20000','bolsa','2024-04-16',11,'2024-04-13 18:15:35'),(9,2,100,'5','costal','2024-04-25',12,'2024-04-13 20:26:33');
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalleventa`
--

LOCK TABLES `detalleventa` WRITE;
/*!40000 ALTER TABLE `detalleventa` DISABLE KEYS */;
INSERT INTO `detalleventa` VALUES (1,1,1,1.00,2.50,'2024-04-08 15:02:09','3'),(2,1,1,1.00,2.50,'2024-04-08 15:35:08','3'),(3,1,6,1.00,3.00,'2024-04-08 15:35:08','3'),(4,2,1,1.00,2.50,'2024-04-08 15:40:59','3'),(5,2,7,1.00,3.00,'2024-04-08 15:40:59','3'),(6,2,1,1.00,2.50,'2024-04-08 15:43:49','3'),(7,4,3,1.00,3.00,'2024-04-11 18:25:42','3'),(8,5,2,10.00,4.00,'2024-04-11 18:39:01','3');
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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `galletas`
--

LOCK TABLES `galletas` WRITE;
/*!40000 ALTER TABLE `galletas` DISABLE KEYS */;
INSERT INTO `galletas` VALUES (1,'Galleta de avena',4.00,1,'Galleta de avena con pasas','Rica galleta',24,10.00,'2024-04-04 00:05:21'),(2,'Galleta de chocolate',15.00,1,'Galleta de chocolate con chips de chocolate','Galleta de chocolate con chips',76,10.00,'2024-04-04 00:05:21'),(3,'Galleta de azúcar',5.00,1,'Galleta de azúcar con azúcar glass','Galleta de azúcar con azúcar glass',90,10.00,'2024-04-04 00:05:21'),(4,'Galleta de Pasas y Nueces',8.00,1,'Galleta de avena con pasas y nueces','Galleta de avena con pasas y nueces',100,10.00,'2024-04-04 00:05:21'),(5,'Galleta de Limón y Coco',12.00,1,'Galleta de limón con coco rallado','Galleta de limón con coco rallado',100,10.00,'2024-04-04 00:05:21'),(6,'Galleta de Jengibre',7.00,1,'Galleta de jengibre con azúcar glass','Galleta de jengibre con azúcar glass',100,10.00,'2024-04-04 00:05:21'),(7,'Galleta de Especias',6.00,1,'Galleta de especias con azúcar glass','Galleta de especias con azúcar glass',100,10.00,'2024-04-04 00:05:21'),(8,'Galleta de Miel',9.00,1,'Galleta de miel con almendras fileteadas','Galleta de miel con almendras fileteadas',100,10.00,'2024-04-04 00:05:21'),(9,'Galleta de Chocolate y Coco',14.00,1,'Galleta de chocolate con coco rallado','Galleta de chocolate con coco rallado muy bueno',100,10.00,'2024-04-04 00:05:21'),(10,'Galleta de Avena y Miel',11.00,1,'Galleta de avena con miel','Galleta de avena con miel',100,10.00,'2024-04-04 00:05:21'),(11,'galleta de bombom',10.00,0,'rica galleta de bombom','galleta fea',40,20.50,'2024-04-08 20:54:32'),(12,'galleta de bombom',45.00,0,'rica galleta de bombom','es muy rica la galleta',23,20.50,'2024-04-08 20:56:45'),(13,'galleta de bombom',45.00,0,'rica galleta de bombom',NULL,23,20.50,'2024-04-08 20:56:45'),(14,'galleta de flor',400.00,1,'galleta de flor','batir por 20 min a fuego lento',1,50.00,'2024-04-08 21:47:29'),(15,'galleta de flor',400.00,0,'galleta de flor','batir por 20 min a fuego lento',1,50.00,'2024-04-08 21:47:29'),(16,'galleta de flor',400.00,1,'galleta de flor','galleta ',23,20.50,'2024-04-09 14:13:02'),(17,'Galleta grande',45.00,0,'Galleta muy grande','Añade en un recipiente',20,20.00,'2024-04-10 17:19:48'),(18,'Galleta bombom con chocolate',20.00,1,'galleta con cubierta de chocolate','receta',10,30.00,'2024-04-10 17:27:37'),(19,'galleta de flor',400.00,0,'rica galleta de bombom','sdadasda',23,20.50,'2024-04-10 17:54:38'),(20,'pedro',400.00,0,'galleta de flor','sada',1,50.00,'2024-04-10 17:55:24'),(21,'pedro',400.00,0,'galleta de flor','jksadjd',1,50.00,'2024-04-10 17:55:44'),(22,'das',0.00,0,'dsad','',0,90.00,'2024-04-10 18:26:47'),(23,'Oreo',0.00,0,'relleno','sasa',6,25.00,'2024-04-10 20:42:40'),(24,'Galleta espacial',22.00,1,'rica galleta espacial','en esta galleta se hace con mucho esfuerzo',8,50.00,'2024-04-11 17:28:23');
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
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientes`
--

LOCK TABLES `ingredientes` WRITE;
/*!40000 ALTER TABLE `ingredientes` DISABLE KEYS */;
INSERT INTO `ingredientes` VALUES (5,2,2,500.00,1,'2024-04-04 00:05:21','2024-04-10 21:13:42',NULL),(6,2,6,5.00,1,'2024-04-04 00:05:21','2024-04-10 21:13:42',NULL),(7,2,7,50.00,1,'2024-04-04 00:05:21','2024-04-10 21:13:42',NULL),(8,2,9,100.00,1,'2024-04-04 00:05:21','2024-04-10 21:13:42',NULL),(9,3,2,500.00,1,'2024-04-04 00:05:21','2024-04-10 20:47:10',NULL),(10,3,6,50.00,1,'2024-04-04 00:05:21','2024-04-10 20:47:10',NULL),(11,3,7,5.00,1,'2024-04-04 00:05:21','2024-04-10 20:47:10',NULL),(12,3,10,100.00,1,'2024-04-04 00:05:21','2024-04-10 20:47:10',NULL),(13,4,2,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(14,4,6,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(15,4,7,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(16,4,8,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(17,4,19,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(18,5,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(19,5,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(20,5,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(21,5,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(22,5,12,10.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(23,5,18,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(24,6,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(25,6,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(26,6,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(27,6,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(28,6,13,15.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(29,6,10,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(30,7,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(31,7,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(32,7,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(33,7,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(34,7,14,25.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(35,7,15,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(36,7,16,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(37,7,10,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(38,8,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(39,8,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(40,8,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(41,8,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(42,8,17,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(43,8,11,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(44,9,1,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(45,9,3,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(46,9,4,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(47,9,5,1.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(48,9,9,100.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(49,9,18,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(50,10,2,500.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(51,10,6,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(52,10,7,5.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(53,10,17,50.00,1,'2024-04-04 00:05:21','0000-00-00 00:00:00',NULL),(58,1,4,50.00,1,'2024-04-08 18:49:48','2024-04-13 22:15:37',NULL),(59,12,5,1.00,1,'2024-04-08 20:57:56','2024-04-08 20:57:56',NULL),(60,11,7,70.00,1,'2024-04-08 21:44:23','2024-04-08 21:44:35',NULL),(61,17,5,3.00,1,'2024-04-10 17:20:02','2024-04-10 17:20:02',NULL),(62,18,5,1.00,1,'2024-04-10 17:27:52','2024-04-11 17:34:13',NULL),(64,18,4,50.00,1,'2024-04-10 17:28:18','2024-04-11 17:34:13',NULL),(65,18,9,40.00,1,'2024-04-10 17:28:33','2024-04-11 17:34:13',NULL),(66,21,1,70.00,1,'2024-04-10 17:57:17','2024-04-10 20:11:23',NULL),(67,21,7,400.00,1,'2024-04-10 17:57:27','2024-04-10 20:11:23',NULL),(68,23,4,400.00,1,'2024-04-10 20:45:31','2024-04-10 21:16:32',NULL),(69,23,1,70.00,1,'2024-04-10 20:45:40','2024-04-10 21:16:33',NULL),(70,11,5,1.00,1,'2024-04-11 17:26:34','2024-04-11 17:26:34',NULL),(71,11,13,40.00,1,'2024-04-11 17:26:46','2024-04-11 17:26:46',NULL),(72,11,17,45.00,1,'2024-04-11 17:26:59','2024-04-11 17:26:59',NULL),(73,24,5,2.00,1,'2024-04-11 17:29:23','2024-04-13 21:53:41',NULL),(74,24,11,30.00,1,'2024-04-11 17:31:43','2024-04-13 21:53:41',NULL),(75,24,15,400.00,1,'2024-04-11 17:31:59','2024-04-13 21:53:41',NULL),(77,18,4,30.00,1,'2024-04-11 17:35:04','2024-04-11 17:35:04',NULL),(79,1,5,23.00,1,'2024-04-11 17:35:44','2024-04-13 22:15:37',NULL),(82,24,18,10.00,1,'2024-04-11 17:40:20','2024-04-13 21:53:41',NULL),(88,24,1,15.00,1,'2024-04-13 21:53:30','2024-04-13 21:53:41',NULL),(89,1,1,3.00,1,'2024-04-13 22:15:16','2024-04-13 22:15:37',NULL),(90,1,14,10.00,1,'2024-04-13 22:15:35','2024-04-13 22:15:37',NULL);
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventario_mp`
--

LOCK TABLES `inventario_mp` WRITE;
/*!40000 ALTER TABLE `inventario_mp` DISABLE KEYS */;
INSERT INTO `inventario_mp` VALUES (1,1,'20000',2,'2024-04-11 18:15:02',1,'2024-04-30 02:54:24'),(22,1,'19600',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(23,2,'2000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(24,3,'5000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(25,4,'20000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(26,5,'900',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(27,6,'500',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(28,7,'800',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(29,8,'2000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(30,9,'6000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(31,10,'2000',2,'2024-04-30 02:54:24',1,'2024-04-08 18:22:51'),(32,1,'160',3,'2024-04-18 00:00:00',1,'2024-04-08 18:23:30'),(33,1,'20000',2,'2024-04-11 18:16:08',1,'2024-04-30 02:54:24'),(37,6,'2500',4,'2024-04-30 00:00:00',1,'2024-04-11 18:29:33'),(38,1,'460',5,'2024-05-01 00:00:00',1,'2024-04-11 18:30:13'),(39,8,'40',6,'2024-04-25 00:00:00',1,'2024-04-11 18:32:25'),(40,1,'20',7,'2024-04-13 00:00:00',1,'2024-04-13 10:04:41'),(41,2,'400',8,'2024-04-13 00:00:00',1,'2024-04-13 10:06:39'),(42,7,'10000',10,'2024-04-30 00:00:00',1,'2024-04-13 10:12:09'),(43,7,'20000',11,'2024-04-16 00:00:00',1,'2024-04-13 18:15:35'),(44,2,'100',12,'2024-04-25 00:00:00',1,'2024-04-13 20:26:33');
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
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventariogalletas`
--

LOCK TABLES `inventariogalletas` WRITE;
/*!40000 ALTER TABLE `inventariogalletas` DISABLE KEYS */;
INSERT INTO `inventariogalletas` VALUES (1,2,20,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-11 18:39:01',NULL),(2,1,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 17:35:43',NULL),(23,3,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-11 18:25:42',NULL),(24,4,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 17:35:43',NULL),(25,5,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 18:43:12',NULL),(26,6,1,'2024-04-30 08:54:24',0,'2024-04-08 17:35:43','2024-04-08 17:36:29',NULL),(27,7,1,'2024-04-30 08:54:24',0,'2024-04-08 17:35:43','2024-04-08 18:44:34',NULL),(28,8,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 18:16:18',NULL),(29,9,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 17:35:43',NULL),(30,10,1,'2024-04-30 08:54:24',1,'2024-04-08 17:35:43','2024-04-08 17:35:43',NULL),(31,21,0,'2022-01-01 06:00:00',0,'2024-04-10 17:55:45','2024-04-11 20:35:24',NULL),(32,22,1,'2022-01-01 06:00:00',0,'2024-04-10 18:26:47','2022-01-01 00:00:00',NULL),(33,23,1,'2022-01-01 06:00:00',0,'2024-04-10 20:42:40','2022-01-01 00:00:00',NULL),(34,24,1,'2022-01-01 06:00:00',0,'2024-04-11 17:28:23','2022-01-01 00:00:00',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_log`
--

LOCK TABLES `login_log` WRITE;
/*!40000 ALTER TABLE `login_log` DISABLE KEYS */;
INSERT INTO `login_log` VALUES (1,5,'2024-03-25 16:34:38','correcto'),(2,5,'2024-03-25 16:35:01','correcto'),(3,5,'2024-03-25 16:35:39','incorrecto'),(4,5,'2024-03-25 16:37:33','incorrecto'),(5,5,'2024-03-25 16:37:38','incorrecto'),(6,2,'2024-04-03 18:22:19','incorrecto'),(7,2,'2024-04-03 18:22:23','incorrecto'),(8,2,'2024-04-03 18:22:36','correcto'),(9,2,'2024-04-05 11:53:38','correcto'),(10,2,'2024-04-06 19:59:03','incorrecto'),(11,2,'2024-04-06 19:59:43','incorrecto'),(12,2,'2024-04-06 20:00:22','correcto'),(13,4,'2024-04-06 20:28:48','correcto'),(14,2,'2024-04-06 20:49:06','incorrecto'),(15,2,'2024-04-06 20:49:10','incorrecto'),(16,2,'2024-04-06 20:49:16','incorrecto'),(17,4,'2024-04-06 21:11:43','correcto'),(18,5,'2024-04-07 12:34:21','correcto'),(19,4,'2024-04-07 12:38:46','incorrecto'),(20,5,'2024-04-07 12:38:59','correcto'),(21,5,'2024-04-07 12:39:18','incorrecto'),(22,5,'2024-04-07 12:39:22','incorrecto'),(23,5,'2024-04-07 12:39:28','incorrecto'),(24,2,'2024-04-07 12:56:44','correcto'),(25,4,'2024-04-07 12:58:57','correcto'),(26,5,'2024-04-07 12:59:36','correcto'),(27,5,'2024-04-08 13:56:12','correcto'),(28,5,'2024-04-08 14:08:10','correcto'),(29,5,'2024-04-08 14:45:29','correcto'),(30,5,'2024-04-08 15:53:27','correcto'),(31,5,'2024-04-08 16:02:56','correcto'),(32,5,'2024-04-08 17:27:06','correcto'),(33,5,'2024-04-08 18:28:38','correcto'),(34,5,'2024-04-08 18:41:03','correcto'),(35,5,'2024-04-08 20:14:11','correcto'),(36,5,'2024-04-08 21:42:42','correcto'),(37,5,'2024-04-09 14:02:03','correcto'),(38,5,'2024-04-09 21:09:25','correcto'),(39,5,'2024-04-09 22:56:03','correcto'),(40,5,'2024-04-10 15:46:31','correcto'),(41,5,'2024-04-10 17:18:56','correcto'),(42,5,'2024-04-10 18:21:21','correcto'),(43,5,'2024-04-10 18:31:20','correcto'),(44,5,'2024-04-10 19:56:31','correcto'),(45,5,'2024-04-10 21:12:36','correcto'),(46,2,'2024-04-10 22:12:46','incorrecto'),(47,5,'2024-04-10 22:14:28','correcto'),(48,5,'2024-04-10 22:18:47','incorrecto'),(49,5,'2024-04-10 22:18:51','correcto'),(50,5,'2024-04-10 22:28:16','correcto'),(51,5,'2024-04-11 12:32:16','correcto'),(52,5,'2024-04-11 14:45:42','correcto'),(53,5,'2024-04-11 14:46:26','incorrecto'),(54,5,'2024-04-11 14:46:30','correcto'),(55,0,'2024-04-11 15:41:03','incorrecto'),(56,0,'2024-04-11 15:41:11','incorrecto'),(57,0,'2024-04-11 15:41:46','incorrecto'),(58,0,'2024-04-11 15:42:07','incorrecto'),(59,0,'2024-04-11 15:44:23','incorrecto'),(60,5,'2024-04-11 15:46:39','incorrecto'),(61,5,'2024-04-11 15:46:47','correcto'),(62,2,'2024-04-11 15:46:58','correcto'),(63,5,'2024-04-11 17:16:39','correcto'),(64,5,'2024-04-11 18:23:13','correcto'),(65,5,'2024-04-11 18:28:51','incorrecto'),(66,5,'2024-04-11 18:28:56','correcto'),(67,5,'2024-04-11 18:56:57','correcto'),(68,5,'2024-04-11 19:09:19','correcto'),(69,5,'2024-04-11 19:15:21','incorrecto'),(70,5,'2024-04-11 19:15:26','correcto'),(71,1,'2024-04-11 19:23:55','incorrecto'),(72,1,'2024-04-11 19:24:39','correcto'),(73,5,'2024-04-11 19:26:02','incorrecto'),(74,5,'2024-04-11 19:26:08','correcto'),(75,2,'2024-04-11 20:16:25','correcto'),(76,1,'2024-04-11 20:17:04','incorrecto'),(77,1,'2024-04-11 20:17:08','incorrecto'),(78,1,'2024-04-11 20:17:11','incorrecto'),(79,1,'2024-04-11 20:17:15','incorrecto'),(80,3,'2024-04-11 20:17:59','incorrecto'),(81,3,'2024-04-11 20:18:21','correcto'),(82,5,'2024-04-11 20:24:26','correcto'),(83,5,'2024-04-11 20:25:42','correcto'),(84,5,'2024-04-11 20:27:03','correcto'),(85,5,'2024-04-11 20:27:51','correcto'),(86,5,'2024-04-11 20:39:06','correcto'),(87,5,'2024-04-11 20:39:18','correcto'),(88,5,'2024-04-11 20:48:01','correcto'),(89,5,'2024-04-12 20:42:05','correcto'),(90,5,'2024-04-12 21:43:17','correcto'),(91,5,'2024-04-13 08:54:48','correcto'),(92,5,'2024-04-13 09:35:28','correcto'),(93,5,'2024-04-13 09:58:07','correcto'),(94,5,'2024-04-13 18:04:33','correcto'),(95,5,'2024-04-13 19:05:42','correcto'),(96,5,'2024-04-13 20:22:50','incorrecto'),(97,5,'2024-04-13 20:22:55','correcto'),(98,5,'2024-04-13 21:23:04','correcto'),(99,5,'2024-04-13 22:26:26','incorrecto'),(100,5,'2024-04-13 22:26:30','correcto'),(101,5,'2024-04-14 11:59:36','correcto');
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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materia_prima_proveedor`
--

LOCK TABLES `materia_prima_proveedor` WRITE;
/*!40000 ALTER TABLE `materia_prima_proveedor` DISABLE KEYS */;
INSERT INTO `materia_prima_proveedor` VALUES (1,1,1,18,'20','costal','2024-04-03 18:05:22'),(2,2,1,15,'20','costal','2024-04-03 18:05:22'),(3,3,2,160,'20','costal','2024-04-03 18:05:22'),(4,1,1,10.5,'20','costal','2024-04-11 13:08:45'),(5,1,2,12,'20','costal','2024-04-11 13:08:45'),(6,2,1,8,'15','costal','2024-04-11 13:08:45'),(7,2,2,9.5,'15','costal','2024-04-11 13:08:45'),(8,3,1,15.75,'1','barra','2024-04-11 13:08:45'),(9,3,2,17,'1','barra','2024-04-11 13:08:45'),(10,4,1,6.8,'30','costal','2024-04-11 13:08:45'),(11,4,2,7.5,'30','costal','2024-04-11 13:08:45'),(12,5,1,0.25,'100','unidad','2024-04-11 13:08:45'),(13,5,2,0.3,'100','unidad','2024-04-11 13:08:45'),(14,6,1,3.5,'500','frasco 500 ml','2024-04-11 13:08:45'),(15,6,2,4,'500','frasco 500 ml','2024-04-11 13:08:45'),(16,7,1,2,'1','bolsa','2024-04-11 13:08:45'),(17,7,2,2.5,'1','bolsa','2024-04-11 13:08:45'),(18,8,1,7,'5','bolsa','2024-04-11 13:08:45'),(19,8,2,8,'5','bolsa','2024-04-11 13:08:45'),(20,9,1,10,'2','lata','2024-04-11 13:08:45'),(21,9,2,11.5,'2','lata','2024-04-11 13:08:45'),(22,10,1,9,'3 ','bolsa','2024-04-11 13:08:45'),(23,10,2,10,'3','bolsa','2024-04-11 13:08:45'),(24,1,5,100,'20','costal','2024-04-03 18:05:22'),(25,2,5,100,'20','costal','2024-04-03 18:05:22'),(26,3,5,100,'20','costal','2024-04-03 18:05:22'),(27,4,5,100,'20','costal','2024-04-03 18:05:22'),(29,15,5,100,'20','costal','2024-04-03 18:05:22'),(30,16,5,100,'20','costal','2024-04-03 18:05:22'),(31,7,2,6000,'20000','bolsa','2024-04-13 18:15:35'),(32,2,2,100,'5','costal','2024-04-13 20:26:33');
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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `merma_galletas`
--

LOCK TABLES `merma_galletas` WRITE;
/*!40000 ALTER TABLE `merma_galletas` DISABLE KEYS */;
INSERT INTO `merma_galletas` VALUES (11,1,1,NULL,'Se cayo al suelo',1,'2024-04-11 14:37:12','2024-04-11 14:37:12',NULL),(12,2,1,NULL,'Se cayo al suelo',1,'2024-04-11 14:37:12','2024-04-11 14:37:12',NULL),(13,23,1,NULL,'Se cayo al suelo',1,'2024-04-11 14:37:12','2024-04-11 14:37:12',NULL),(14,24,1,NULL,'Se cayo al suelo',1,'2024-04-11 14:37:12','2024-04-11 14:37:12',NULL),(15,25,1,NULL,'Se cayo al suelo',1,'2024-04-11 14:37:12','2024-04-11 14:37:12',NULL),(16,26,1,NULL,'Se cayo al suelo',1,'2024-04-11 14:37:12','2024-04-11 14:37:12',NULL),(17,27,1,NULL,'Se cayo al suelo',1,'2024-04-11 14:37:12','2024-04-11 14:37:12',NULL),(18,28,1,NULL,'Se cayo al suelo',1,'2024-04-11 14:37:12','2024-04-11 14:37:12',NULL),(19,29,1,NULL,'Se cayo al suelo',1,'2024-04-11 14:37:12','2024-04-11 14:37:12',NULL),(20,30,1,NULL,'Se cayo al suelo',1,'2024-04-11 14:37:12','2024-04-11 14:37:12',NULL),(21,1,5,NULL,'Se cayo al suelo',1,'2024-04-11 14:37:46','2024-04-11 14:37:46',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mermas_material`
--

LOCK TABLES `mermas_material` WRITE;
/*!40000 ALTER TABLE `mermas_material` DISABLE KEYS */;
INSERT INTO `mermas_material` VALUES (1,22,'Produccion','2024-04-10',400,'2024-04-10 17:37:06',NULL,'se perdio producto',NULL);
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
  `password` varchar(255) DEFAULT NULL,
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `password_histories_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `password_histories`
--

LOCK TABLES `password_histories` WRITE;
/*!40000 ALTER TABLE `password_histories` DISABLE KEYS */;
INSERT INTO `password_histories` VALUES (1,5,'contraseña123','2024-03-25 21:41:21'),(2,1,'nueva_contraseña456','2024-03-25 21:41:31'),(3,5,'contraseña123','2024-03-25 22:38:03'),(4,2,'2a7efffe46b23caebf3ef9553a11a072fc40b3abc83ebd783ecbc6afe6606473','2024-04-11 21:57:57'),(5,2,'52831e47b02c6be24dd0701ab12feef65792a63b91398a97e13ef89c2a076ff7','2024-04-11 21:59:21'),(6,2,'29a4de11060b1b869444ea61966c35e59f31bcca28a650e30c99023e1fe414cd','2024-04-11 22:00:00'),(7,2,'9d7d3293fca9dd34eca99f3730842f3a0d52f8ef961fde06476491a1f6084cbb','2024-04-12 02:16:15');
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion`
--

LOCK TABLES `produccion` WRITE;
/*!40000 ALTER TABLE `produccion` DISABLE KEYS */;
INSERT INTO `produccion` VALUES (1,1,0,1,0,'2024-04-08 18:15:05','2024-04-08 18:15:05',NULL),(2,4,0,1,0,'2024-04-08 18:44:42','2024-04-08 18:44:42',NULL),(3,6,0,1,0,'2024-04-10 17:59:54','2024-04-10 17:59:54',NULL),(4,5,0,1,0,'2024-04-11 20:32:01','2024-04-11 20:32:01',NULL);
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
-- Table structure for table `relacionGalletaMateria`
--

DROP TABLE IF EXISTS `relacionGalletaMateria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `relacionGalletaMateria` (
  `idRelacion` int PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `idLoteMateria` int NOT NULL,
  `idLoteGalletas` int NOT NULL,
  `created_at` datetime NOT NULL,
  KEY `idLoteMateria` (`idLoteMateria`),
  KEY `idLoteGalletas` (`idLoteGalletas`),
  CONSTRAINT `relacionGalletaMateria_ibfk_1` FOREIGN KEY (`idLoteMateria`) REFERENCES `inventario_materias` (`id`),
  CONSTRAINT `relacionGalletaMateria_ibfk_2` FOREIGN KEY (`idLoteGalletas`) REFERENCES `inventarioGalletas` (`idLoteGalletas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `relacionGalletaMateria`
--

LOCK TABLES `relacionGalletaMateria` WRITE;
/*!40000 ALTER TABLE `relacionGalletaMateria` DISABLE KEYS */;
/*!40000 ALTER TABLE `relacionGalletaMateria` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solicitudproduccion`
--

LOCK TABLES `solicitudproduccion` WRITE;
/*!40000 ALTER TABLE `solicitudproduccion` DISABLE KEYS */;
INSERT INTO `solicitudproduccion` VALUES (1,26,12,'Aceptada',NULL,'2024-04-08 17:36:29','2024-04-08 18:15:05'),(2,25,12,'Rechazada','no hay suficiente materia','2024-04-08 17:36:39','2024-04-08 18:43:12'),(3,28,20,'Rechazada','No hay suficiente material','2024-04-08 18:00:02','2024-04-08 18:16:18'),(4,27,40,'Aceptada',NULL,'2024-04-08 18:44:34','2024-04-08 18:44:42'),(5,31,30,'Aceptada',NULL,'2024-04-10 17:58:33','2024-04-11 20:32:01'),(6,31,1,'Aceptada',NULL,'2024-04-10 17:59:37','2024-04-10 17:59:54'),(7,31,34,'Pendiente',NULL,'2024-04-11 20:32:14','2024-04-11 20:32:14'),(8,31,34,'Pendiente',NULL,'2024-04-11 20:35:24','2024-04-11 20:35:24');
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'christopher','Martínez','elena@example.com','f31ed2eb048061d4e344ef0b4cf4b9d8bd23725be583c7ce14d1b1934631a09d','ventas',0,'2024-03-21 18:53:51',1,'2024-04-11 20:18:15','2024-04-11 20:27:20',NULL),(2,'Yuri','Gómez','jonarrodi99@gmail.com','9d7d3293fca9dd34eca99f3730842f3a0d52f8ef961fde06476491a1f6084cbb','admin',0,'2024-03-21 18:54:19',0,NULL,'2024-04-11 20:16:15',NULL),(3,'Laura','Hernández','laura@example.com','be1da4da2ec5ed3f0264acb96f7c22b58428f088f75b2279afab2cceae29fd06','compras',0,'2024-03-21 18:54:28',0,NULL,'0000-00-00 00:00:00',NULL),(4,'Pedro','Sánchez Juarez','pedro@example.com','bdcbc2e12f2dfe1e6af3167a381f2ac5b7613af8b0623798c3ea627df84a68bc','produccion',0,'2024-03-21 18:54:35',0,NULL,'2024-04-07 12:58:34',NULL),(5,'Juan','Perez','juan@example.com','5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5','admin',0,'2024-03-25 21:41:21',0,NULL,'2024-04-11 14:46:19',NULL),(6,'Brenda','perez','bren@example.com','00d8c9e87b9485c3a3155c1eaf30c906286e7639714e6d3d6cba27713166efa6','admin',0,'2024-04-10 03:18:51',0,NULL,'2024-04-09 21:21:36',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES (1,'2024-04-08 14:56:58',5.50,'2024-04-08 14:56:58',5),(2,'2024-04-08 15:40:41',2.50,'2024-04-08 15:40:41',5),(3,'2024-04-10 17:29:59',0.00,'2024-04-10 17:29:59',5),(4,'2024-04-11 18:25:23',3.00,'2024-04-11 18:25:23',5),(5,'2024-04-11 18:38:19',40.00,'2024-04-11 18:38:19',5),(6,'2024-04-13 22:08:59',0.00,'2024-04-13 22:08:59',5);
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;

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

--
-- Dumping data for table `verification_code`
--

LOCK TABLES `verification_code` WRITE;
/*!40000 ALTER TABLE `verification_code` DISABLE KEYS */;
INSERT INTO `verification_code` VALUES (1,'17cb3fe709','jonarrodi99@gmail.com'),(2,'777ad852cb','jonarrodi99@gmail.com'),(4,'7364941f26','jonarrodi99@gmail.com'),(8,'68d4249be8',NULL),(15,'50bb704b69','jonarrodi99@gmail.com'),(16,'31198b270c','jonarrodi99@gmail.com'),(18,'358083ee3d','jonarrodi99@gmail.com');
/*!40000 ALTER TABLE `verification_code` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-14 15:32:01

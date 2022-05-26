-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.7.3-MariaDB-1:10.7.3+maria~focal - mariadb.org binary distribution
-- SO del servidor:              debian-linux-gnu
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando datos para la tabla tesla.categoria: ~2 rows (aproximadamente)
DELETE FROM `categoria`;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` (`categoria_id`, `categoria_nombre`) VALUES
	(0, 'Deportivos'),
	(1, 'Familiares');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;

-- Volcando datos para la tabla tesla.pedido: ~0 rows (aproximadamente)
DELETE FROM `pedido`;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;

-- Volcando datos para la tabla tesla.pedido-producto: ~0 rows (aproximadamente)
DELETE FROM `pedido-producto`;
/*!40000 ALTER TABLE `pedido-producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedido-producto` ENABLE KEYS */;

-- Volcando datos para la tabla tesla.producto: ~0 rows (aproximadamente)
DELETE FROM `producto`;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;

-- Volcando datos para la tabla tesla.usuarios: ~2 rows (aproximadamente)
DELETE FROM `usuarios`;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`usuario_id`, `usuario_nombre`, `usuario_correo`, `usuario_password`) VALUES
	(1, 'Leonardo Gallegos', 'leonardogallegos@model.com', '123456'),
	(2, 'Leonardo Gallegos', 'leonardogallegos@model.com', '123456'),
	(3, 'Leonardo Gallegos', 'leonardogallegos@model.com', '123456');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

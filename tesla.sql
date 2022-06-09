-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.8.3-MariaDB-1:10.8.3+maria~jammy - mariadb.org binary distribution
-- SO del servidor:              debian-linux-gnu
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando datos para la tabla tesla.categoria: ~3 rows (aproximadamente)
DELETE FROM `categoria`;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` (`categoria_id`, `categoria_nombre`, `categoria_imagen`) VALUES
	(1, 'Autos', 'https://autotest.com.ar/wp-content/uploads/2021/06/tesla-model-s-plaid-frente.jpg'),
	(2, 'Camionetas', 'https://s1.eestatic.com/2019/06/03/actualidad/actualidad_403473194_130559332_1024x576.jpg'),
	(3, 'Camiones', 'https://d500.epimg.net/cincodias/imagenes/2017/08/25/motor/1503648403_960717_1503648862_noticia_normal.jpg');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;

-- Volcando datos para la tabla tesla.pedido: ~15 rows (aproximadamente)
DELETE FROM `pedido`;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
INSERT INTO `pedido` (`pedido_id`, `pedido_estatus`, `usuarios_usuario_id`) VALUES
	(1, 1, 4),
	(2, 1, 4),
	(3, 1, 4),
	(4, 1, 4),
	(5, 1, 4),
	(6, 1, 4),
	(13, 1, 4),
	(14, 1, 4),
	(15, 1, 4),
	(16, 1, 4),
	(17, 1, 4),
	(18, 1, 4),
	(19, 1, 4),
	(20, 1, 5),
	(21, 1, 5);
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;

-- Volcando datos para la tabla tesla.pedido_producto: ~14 rows (aproximadamente)
DELETE FROM `pedido_producto`;
/*!40000 ALTER TABLE `pedido_producto` DISABLE KEYS */;
INSERT INTO `pedido_producto` (`pedido_pedido_id`, `producto_producto_id`, `cantidad`) VALUES
	(1, 3, 4),
	(2, 3, 4),
	(5, 3, 4),
	(6, 3, 4),
	(19, 1, 2),
	(19, 2, 1),
	(19, 3, 4),
	(20, 1, 2),
	(20, 2, 1),
	(20, 3, 4),
	(21, 1, 1),
	(21, 2, 1),
	(21, 4, 2),
	(21, 7, 1);
/*!40000 ALTER TABLE `pedido_producto` ENABLE KEYS */;

-- Volcando datos para la tabla tesla.producto: ~7 rows (aproximadamente)
DELETE FROM `producto`;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` (`producto_id`, `producto_nombre`, `producto_descripcion`, `producto_precio`, `producto_imagen`, `categoria_categoria_id`) VALUES
	(1, 'Tesla Model 3', 'asdasd', 45190, 'https://www.km77.com/images/medium/3/8/5/5/tesla-model-3-2021-gran-autonomia-frontal.353855.jpg', 1),
	(2, 'Tesla Model S', 'qweqwe', 96190, 'https://tesla-cdn.thron.com/delivery/public/image/tesla/03c34975-991c-45ee-a340-2b700bf7de01/bvlatuR/std/960x540/meet-your-tesla_model-s?20190221', 1),
	(3, 'Tesla Model Y', 'fwefwd', 58190, 'https://www.tesla.com/ownersmanual/images/GUID-1F2D8746-336F-4CF9-9A04-F35E960F31FE-online-en-US.png', 2),
	(4, 'Tesla Model X', 'ewrrwer', 106190, 'https://www.tesla.com/ownersmanual/images/GUID-999EC68D-FD44-4237-8AB8-AB97A724F3B0-online-en-US.png', 2),
	(5, 'Tesla Roadster - MT Estimate', 'gregerg', 200000, 'https://www.tesla.com/sites/default/files/images/roadster/roadster-social.jpg', 1),
	(6, 'Tesla Cybertruck - MT Estimate', 'thdgdfg', 39900, 'https://img.remediosdigitales.com/d0fde0/tesla-pick-up-011/840_560.jpg', 2),
	(7, 'Tesla Semi -MT Estimate', 'sdfsdfsd', 150000, 'https://i0.wp.com/www.transportelatino.net/wp-content/uploads/2021/11/breves4.jpg?resize=850%2C560&ssl=1', 3);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;

-- Volcando datos para la tabla tesla.usuarios: ~2 rows (aproximadamente)
DELETE FROM `usuarios`;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`usuario_id`, `usuario_nombre`, `usuario_correo`, `usuario_password`) VALUES
	(4, 'Cristell Naranjo', 'cristelnaranjo@model.com', '123456'),
	(5, 'Leonardo Gallegos', 'leonardogallegos@model.com', '123456');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
Telcel
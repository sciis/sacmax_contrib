CREATE DATABASE  IF NOT EXISTS `sacmax_sample_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `sacmax_sample_db`;

--
-- Host: localhost    Database: multisensor
-- ------------------------------------------------------
-- Server version	5.5.47-0ubuntu0.14.04.4


CREATE TABLE `test` (
  `id` int(10) unsigned NOT NULL,
  `sacmax_num` int(10) DEFAULT NULL,
  `sacmax_year` int(10) DEFAULT NULL,
  `sacmax_char` varchar(255) DEFAULT NULL,
  `user_note` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;



INSERT INTO sample VALUES(
    '1',
    'samplename',
    '2016',
    'SAC-MAX.',
    'Sensor, Actuator and Camera - easy to MAXimum'
);
/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50719
Source Host           : 127.0.0.1:3306
Source Database       : devops

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2017-10-12 19:25:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tb_eureka_manager
-- ----------------------------
DROP TABLE IF EXISTS `tb_eureka_manager`;
CREATE TABLE `tb_eureka_manager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(100) NOT NULL,
  `eureka_url` varchar(200) NOT NULL,
  `manager` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

USE news_test;

CREATE TABLE `articles` (
  `aid` int(11) NOT NULL AUTO_INCREMENT COMMENT '文章id',
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '文章标题',
  `category` CHAR(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章分类',
  `url` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章url',
  `author` CHAR(100) COLLATE utf8mb4_unicode_ci COMMENT '文章作者',
  `content` text COLLATE utf8mb4_unicode_ci COMMENT '文章内容',
  `publish_time` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章发表时间',
  `source_site` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '来源网站',
  `extra1` varchar(255) COLLATE utf8mb4_unicode_ci,
  `extra2` varchar(255) COLLATE utf8mb4_unicode_ci,
  `extra3` varchar(255) COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `rules` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_name` varchar(255) NOT NULL,
  `allow_domains` varchar(255),
  `start_urls` text NOT NULL,
  `next_page` varchar(255),
  `allow_url` varchar(255),
  `extract_from` varchar(255),
  `title_xpath` varchar(255),
  `category_xpath` VARCHAR(255),
  `author_xpath` VARCHAR(255),
  `content_xpath` varchar(255) ,
  `publish_time_xpath` varchar(255) ,
  `source_site_xpath` varchar(255) ,
  `enable` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

LOCK TABLES `rules` WRITE;

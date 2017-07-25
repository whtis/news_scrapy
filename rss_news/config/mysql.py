# mysql 配置
from scrapy.utils.project import get_project_settings
import pymysql

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

settings = get_project_settings()

conn = pymysql.connect(host=settings['MYSQL_HOST'],
                       port=int(settings['MYSQL_PORT']),
                       user=settings['MYSQL_USER'],
                       passwd=settings['MYSQL_PASSWD'],
                       db=settings['MYSQL_DBNAME']
                       )

# 初始化数据库连接:
# engine = create_engine('mysql+pymysql://root:root@localhost:3306/spider?charset=utf8mb4')
engine = create_engine('mysql+pymysql://' +
                       settings['MYSQL_USER'] + ':' +
                       settings['MYSQL_PASSWD'] + '@' +
                       settings['MYSQL_HOST'] + ':' +
                       settings['MYSQL_PORT'] + '/' +
                       settings['MYSQL_DBNAME'] + '?' + 'charset=utf8mb4'
                       )
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

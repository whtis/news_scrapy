# 初始化redis数据库连接
import redis

Redis = redis.StrictRedis(host='localhost', port=6379, db=0)

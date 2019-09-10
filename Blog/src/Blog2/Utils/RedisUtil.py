import redis


def getRedisClient():
    return redis.Redis(host='localhost',port=6379,charset='GBK',decode_responses=True) #后面是解决中文乱码问题
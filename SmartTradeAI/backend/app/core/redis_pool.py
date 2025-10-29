import aioredis
from app.core.config import settings

redis = None

async def init_redis():
    global redis
    redis = await aioredis.from_url(settings.REDIS_URL)
    return redis

async def get_redis():
    if redis is None:
        await init_redis()
    return redis

async def close_redis():
    if redis is not None:
        await redis.close()
        await redis.wait_closed()
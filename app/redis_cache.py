import redis
import os
import json

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True
)


def get_user_cache(user_id):
    data = r.get(f"user:{user_id}")
    return json.loads(data) if data else None


def set_user_cache(user_id, user_data):
    r.setex(f"user:{user_id}", 300, json.dumps(user_data))

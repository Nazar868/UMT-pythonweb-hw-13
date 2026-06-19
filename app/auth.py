from datetime import datetime, timedelta
from jose import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"


def create_access_token(data: dict, expires=30):
    payload = data.copy()
    payload.update({"exp": datetime.utcnow() + timedelta(minutes=expires)})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict):
    payload = data.copy()
    payload.update({"exp": datetime.utcnow() + timedelta(days=7)})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

import random
import string
import time
import bcrypt
import hashlib
import config

async def random_str(length):
    """
    产生length位数随机字符串
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


async def login_token(username, userid):
    """
    生成一个随机字符串作为token
    timestamp,随机字符串,用户id,用户名称
    """
    return hashlib.sha256(f"{time.time()}{await random_str(10)}{userid}{username}".encode('utf-8')).hexdigest()


async def get_password(password):
    """
    获取加密后密码
    """
    return bcrypt.hashpw((config.common.secret_salt + password).encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


async def verify_password(hashed_password, password):
    """
    验证加密后的密码
    """
    return bcrypt.checkpw((config.common.secret_salt + password).encode(), hashed_password.encode())
# 后台管理
import config

from fastapi import APIRouter

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

router = APIRouter()

engine = create_engine(config.db.locate)
Session = sessionmaker(bind=engine, autoflush=False)
db = Session()

@router.get('login')
async def login(username: str, password: str):
    pass
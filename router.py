# 路由配置
from fastapi import APIRouter

from app.admin import router as admin

router = APIRouter()
router.include_router(admin, tags=["RTOT后台管理"], prefix="/admin")
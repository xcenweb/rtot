import config

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles

def app() -> FastAPI:

    app = FastAPI(debug=config.DEBUG,
                  title="BCSA Locate System",
                  description="API for BCSA Locate System",
                  version="1.0.0",
                  docs_url="/docs",
                  redoc_url="/redoc")

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins = config.CORS.allow_origins,
        allow_credentials = config.CORS.allow_credentials,
        allow_methods = config.CORS.allow_methods,
        allow_headers = config.CORS.allow_headers,
        max_age = config.CORS.max_age
    )
    
    # Gzip
    app.add_middleware(GZipMiddleware, minimum_size=500)
    
    # 注册后台管理
    # from admin import admin
    # admin.mount_to(app)
    
    # 导入路由
    import router
    app.include_router(router.router)

    # static
    app.mount(path="/static",
              app=StaticFiles(directory="static"),
              name="static")

    return app
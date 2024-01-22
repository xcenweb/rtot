from urllib.parse import quote_plus

### 项目调试模式 ###
DEBUG = True


### 全局通用配置 ###
class common:
    secret_salt = 'wS4|hZ5%xG8(mM3}oM3@'  # 自动盐值

### 数据库 ###
class db:
    locate = 'mysql+pymysql://root:'+ quote_plus('Data@bcsa@2024')+'@127.0.0.1:3306/locate?charset=utf8mb4'
    smrz = 'mysql+pymysql://smrz_sync_user:'+ quote_plus('Zv&s2j%kPRfCWgY8JfPET8Lx8QYU')+'@10.230.192.138:6890/sf-smrz?charset=utf8mb4'


### 后台设置 ###
class admin:
    token_exp = 86400 # 后台token过期时间


### 跨域请求 https://fastapi.tiangolo.com/zh/tutorial/cors/ ###
class CORS:
    allow_origins = ['*']
    allow_methods = ['*']
    allow_headers = ['*']
    allow_credentials = True
    max_age = 600


### 模板目录 jinja2 ###
Jinja2directory = 'template'


### 微信公众号配置 ###
class wechat:
    corpid = 'ww1125b06d76a9694a'
    corpsecret = 'UK_iMR299_3LIuJG_IQH0TNO4VtfABOdyMHn1ClMWzI'
import uvicorn
from app import app

app = app()

if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True, host="0.0.0.0", port=4566)
from fastapi import FastAPI
from typing import Optional
import uvicorn as uvc


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = Optional[None]):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvc.run("main:app",
        host="127.0.0.1",
        port=8000,
        log_level="debug",
        reload=True)
    

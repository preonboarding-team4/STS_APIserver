import uvicorn
from fastapi import FastAPI

from app.router import predict

app = FastAPI()

app.include_router(predict.router)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

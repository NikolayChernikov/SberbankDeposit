import uvicorn
from fastapi import FastAPI
from src.deposit_router import router as deposit_router

app = FastAPI()
app.include_router(deposit_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API! Teste"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "nome": f"Item {item_id}"} 
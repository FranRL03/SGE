from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel, PositiveInt

app = FastAPI()

class User (BaseModel):
    id: int
    nombre: str = 'Peepe peepe'
    # fecha_alta = datetime | None
    aficiones = dict[str, PositiveInt]
@app.get("/")
async def get():
    return {"mensaje": "Hola Mundo"}
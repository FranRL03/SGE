from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class Coche:
#     def __init__(self, id, modelo, color, puertas):
#         self.id = id
#         self.modelo = modelo
#         self.color = color
#         self.puertas = puertas
#
#
#
#
# carList = [
#     Coche(1, "Golf GTI", "Blanco", 4),
#     Coche(2, "SEAT León FR", "Gris", 4)
# ]

class Coche(BaseModel):
    id: int
    modelo: str
    color: str
    puertas: int

carList = [
    Coche(id=1, modelo="Golf GTI", color="Blanco", puertas=4),
    Coche(id=2, modelo="SEAT León FR", color="Gris", puertas=4)
]

@app.get("/")
def getAll ():
    return carList


@app.get("/{id}")
def getCarFindById(id: int):
    findCar = list(filter(lambda x: x.id == id, carList))

    return findCar

@app.post("/coche")
def createCar(newcar: Coche):

    #carList.append(Coche(3, "Porche Panamera", "Negro", 4))
    carList.append(newcar)

    return newcar

@app.put("/coche/{id}")
def editCar(carEdit: Coche, id: int):

    editCar = list(filter(lambda x: x.id == id, carList))

    if editCar:

        editCar = editCar[0]
        editCar.modelo = carEdit.modelo
        editCar.color = carEdit.color
        editCar.puertas = carEdit.puertas

        return editCar

@app.delete("/{id}")
def deleteCar(id: int):
    delete = list(filter(lambda x: x.id == id, carList))

    if delete:
        carList.remove(delete[0])

        return carList








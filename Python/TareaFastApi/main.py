from fastapi import FastAPI

app = FastAPI()

class Coche:
    def __init__(self, id, modelo, color, puertas):
        self.id = id
        self.modelo = modelo
        self.color = color
        self.puertas = puertas




carList = [
    Coche(1, "Golf GTI", "Blanco", 4),
    Coche(2, "SEAT León FR", "Gris", 4)
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






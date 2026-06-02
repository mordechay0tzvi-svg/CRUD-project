import fastapi
from fastapi import Body
import uvicorn
from handlers import *
from shape_manager import ShapeManager


app = fastapi.FastAPI()
sm = ShapeManager()


@app.get("/shapes")
def get__shapes():
    sm.get_all_shapes()


@app.get("/shapes/{id}")
def get_shape(id):
    for shape in sm.get_all_shapes():
        if shape.shape_id == id:
            return shape.to_dict()


@app.post("/shapes")
def create(shape: dict = Body(...)):
    sm.create_shape(shape)
    return {"message": "created"}


@app.put("/shapes/{id}")
def replace(id):
    sm.update_shape(id)
    return {"message":f"{id} updated"}


@app.delete("/shapes/{id}")
def delete(id):
    sm.delete_shape(id)
    return {"message":f"{id} deleted"}


@app.get("/shapes/total-area")
def total_area():
    total = 0 
    for shpae in sm.get_all_shapes():
        total += shpae.get_area()
    return {"total area":total}


@app.get("/shapes/count")
def count():
    return {"count":len(sm.get_all_shapes())}









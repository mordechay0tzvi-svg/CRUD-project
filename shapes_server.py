import fastapi
from fastapi import Body
import uvicorn
from handlers import *
from shape_manager import ShapeManager


class NotAShapeError(Exception):
    pass

class IdNotFound(Exception):
    pass


app = fastapi.FastAPI()
sm = ShapeManager()


@app.get("/shapes")
def get__shapes():
    shape_list = []
    for shape in sm.get_all_shapes():
        shape_list.append(shape.to_dict())
    return shape_list


@app.get("/shapes/total-area")
def total_area():
    total = 0 
    for shpae in sm.get_all_shapes():
        total += shpae.get_area()
    return {"total area":total}


@app.get("/shapes/count")
def count():
    return {"count":len(sm.get_all_shapes())}


@app.post("/shapes")
def create(shape_data: dict = Body(...)):
    try:
        sm.create_shape(creation(shape_data)) 
        return {"message": "created"}
    except NotAShapeError:
        return {"message": "this shape type is not valid"}


@app.get("/shapes/{id}")
def get_shape(id:int):
    for shape in sm.get_all_shapes():
        if shape.shape_id == id:
            return shape.to_dict()
    return {"message":"shape not found"}


@app.put("/shapes/{id}")
def replace(id:int, new_data=Body(...)):
    try:
        sm.update_shape(id, updating(new_data))
        return {"message":f"{id} updated"}
    except IdNotFound:
        return {"message":"id not found"}



@app.delete("/shapes/{id}")
def delete(id:int):
    sm.delete_shape(id)
    return {"message":f"{id} deleted"}


uvicorn.run(app, host="localhost", port=8888)




def creation(data):
    new_id = sm.get_id()
    type = data["type"]
    if type == "c":
        return Circle(data["radius"], new_id)
    elif type == "s":
         return Square(data["side"] ,new_id)
    elif type == "r":
        return Rectangle(data['length'], data ["height"], new_id)
    else:
        raise NotAShapeError

def updating(data):
    id = data["id"]
    type = sm.find_type(id)
    if type is None :
        raise IdNotFound
    if type == "circle":
        return{id,{"radius": data["radius"]}}
    elif type == "rectangle":
        return{id, {"length":data["length"], "height":data["height"]}}
    elif type == "square":
        return{id,{"side": data["side"]}}
    


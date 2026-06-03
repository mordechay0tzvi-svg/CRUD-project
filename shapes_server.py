import fastapi
from fastapi import Body
import uvicorn
from handlers import *
from shape_manager import ShapeManager
from fastapi import HTTPException


app = fastapi.FastAPI()
sm = ShapeManager()


@app.get("/shapes")
def get__shapes():
    """returns the shape list from the instance or raises if no shape"""
    shape_list = []
    shapes = sm.get_all_shapes()
    if not shapes:
        raise HTTPException(status_code=404, detail="no shapes")
    for shape in sm.get_all_shapes():
        shape_list.append(shape.to_dict())
    return shape_list


@app.get("/shapes/total-area")
def total_area():
    """returns the combiend area of all the shapes or raises an error if no shapes"""
    if not sm.get_all_shapes():
        raise HTTPException(status_code=404, detail="no shapes yet")
    total = 0 
    for shape in sm.get_all_shapes():
        total += shape.get_area()
    return {"total area":total}


@app.get("/shapes/count")
def count():
    """returns how many shapes are"""
    if not sm.get_all_shapes():
        raise HTTPException(status_code=404, detail="no shapes yet")
    return {"count":len(sm.get_all_shapes())}
 
    
@app.post("/shapes")
def create(shape_data: dict = Body(...)): 
    """adds a new shape and raises error if shape type is not good"""
    shape_type = shape_data.get("type")
    new_id = sm.get_id()
    if shape_type == "circle":
        shape_obj = Circle(shape_data["radius"], new_id)
    elif shape_type == "square":
        shape_obj = Square(shape_data["side"], new_id)
    elif shape_type == "rectangle":
        shape_obj = Rectangle(shape_data["length"], shape_data["height"], new_id)
    else:
        raise HTTPException(status_code=400, detail="this shape type is not valid")
    sm.create_shape(shape_obj)
    return {"message": "created"}



@app.put("/shapes/{id}")
def replace(id: int, new_data: dict = Body(...)):
    """updates shape attributes or error if id is wrong"""
    shape_type = sm.find_type(id)
    if shape_type is None:
        raise HTTPException(status_code=400, detail="wrong id")
    if shape_type == "circle":
        update_dict = {"radius": new_data["radius"]}
    elif shape_type == "square":
        update_dict = {"side": new_data["side"]}
    elif shape_type == "rectangle":
        update_dict = {"length": new_data["length"], "height": new_data["height"]}
    sm.update_shape(id, update_dict)
    return {"message": f"{id} updated"}

    

@app.get("/shapes/{id}")
def get_shape(id:int):
    """returns a shape by it's id or error if id is wrong"""
    for shape in sm.get_all_shapes():
        if shape.shape_id == id:
            return shape.to_dict()
    raise HTTPException(status_code=404,detail="shape not found")


@app.delete("/shapes/{id}")
def delete(id:int):
    """deletes shape by it's id or error if id not exists"""
    try:
        sm.delete_shape(id)
        return {"message":f"{id} deleted"}
    except:
        raise HTTPException(status_code=400, detail="wrong id")

@app.get("/shapes/types/{type}")
def type_filter(type:str):
    """return all shape from certain type and error if type not valid"""
    filterd = []
    for shape in sm.get_all_shapes():
        if shape.type == type:
            filterd.append(shape.to_dict())
    if not filterd:
        raise HTTPException(status_code=400, detail="type is wrong")
    return filterd

        

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8888)



 

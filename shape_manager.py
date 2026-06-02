import json
from circle import Circle
from rectangle import Rectangle
from square import Square
from json.decoder import JSONDecodeError

class ShapeManager:
    def __init__(self):
        self.shapes = []

    def create_shape(self, shape):
        """gets a shape object fron main and adds it to the list"""
        self.load_from_json()
        self.shapes.append(shape)
        self.save_to_json()
        print("===========\n Shape added\n =============")

    def get_all_shapes(self):
        '''return the shapes list'''
        self.load_from_json()
        if not self.shapes:
            return []
        return self.shapes

    def get_id(self):
        """returns the id for the shape created on main by checking the last id given or 1 if no shapes yet"""
        try:
            self.load_from_json()
            if not self.shapes:
                return 1
            return max(shape.shape_id for shape in self.shapes) + 1
        except FileNotFoundError:
            return 1

    def update_shape(self, shape_id, new_data):
        """changes attributes of shape by its id"""
        self.load_from_json()
        for shape in self.shapes:
            if shape.shape_id == shape_id:
                if isinstance(shape, Circle):
                    shape.radius = new_data["radius"]
                    break
                elif isinstance(shape, Square):
                    shape.side = new_data["side"]
                    break
                elif isinstance(shape, Rectangle):
                    shape.length = new_data["length"]
                    shape.height = new_data["height"]
                    break
        self.save_to_json()
        print("===========\n Shape updated\n =============")
        return

    def delete_shape(self, shape_id):
        """gets an id and removes the shape that matches that id"""
        try:
            self.load_from_json()
            for shape in self.shapes:
                if shape.shape_id == shape_id:
                    self.shapes.remove(shape)
                    self.save_to_json()
                    print("===========\n Shape deleted\n =============")
                    return
            print("!!Shape not found!!")     
        except IndexError:
            print("!!Shape not found!!")


    def save_to_json(self):
        """saves thet shapes list to the file by converting them to dict string"""
        with open("shapes.json", "w") as f:
            shapes = []
            for shape in self.shapes:
                shapes.append(shape.to_dict())
            json.dump(shapes, f, indent=2)

    def load_from_json(self):
        """loads the shapes from the file to the shapes list"""
        try:
            with open("shapes.json", "r") as f:
                file = json.load(f)
                self.shapes = []
                for line in file:
                    if line["shape_type"] == "circle":
                        self.shapes.append(Circle(line["radius"],line["shape_id"]))
                    elif line["shape_type"] == "square":
                            self.shapes.append(Square(line["side"],line["shape_id"]))
                    elif line["shape_type"] == "rectangle":
                        self.shapes.append(Rectangle(line["length"], line["height"],line["shape_id"]))

        except JSONDecodeError:
            self.shapes = []
            print("!!No shapes yet!!")

    def find_type(self,id):
        """returns the type of the shape by the given id the know how many inputs needed for the updating"""
        for shape in self.shapes.copy():
            if shape.shape_id == id:
                return shape.type
        return None

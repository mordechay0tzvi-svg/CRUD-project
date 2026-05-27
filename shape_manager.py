import json
from circle import Circle
from rectangle import Rectangle
from square import Square
from shape import Shape

class ShapeManager:
    def __init__(self):
        self.shapes = []

    def create_shape(self, shape):
        self.load_from_json()
        self.shapes.append(shape)
        self.save_to_json()
        print("===========\n shape added\n =============")

    def get_all_shapes(self):
        self.load_from_json()
        return self.shapes


    def update_shape(self, shape_id, new_data):
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
        return

    def delete_shape(self, shape_id):
        self.load_from_json()
        for shape in self.shapes:
            if shape.shape_id == shape_id:
                self.shapes.remove(shape)
                break
        self.save_to_json()
        print("shape not found")

    def save_to_json(self):
            with open("shapes.json", "w") as f:
                shapes = []
                for shape in self.shapes:
                    shapes.append(shape.to_dict())
                json.dump(shapes, f, indent=2)
            Shape.count = 0

    def load_from_json(self):
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
                if self.shapes:
                    Shape.count = max(shape.shape_id for shape in self.shapes) + 1
                else:
                    Shape.count = 1
        except FileNotFoundError:
            self.shapes = []

    def find_type(self,id):
        for shape in self.shapes.copy():
            if shape.shape_id == id:
                return shape.shape_type
        return None

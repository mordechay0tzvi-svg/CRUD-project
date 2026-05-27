import json
from circle import Circle
from rectangle import Rectangle
from square import Square


class ShapeManager:
    shape_types = {"circle":Circle, "square":Square, "rectangle":Rectangle}
    def __init__(self):
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape):
        try:
            if shape == "circle":
                new_shape = Circle(int(input("enter radius")))
                self.shapes.append(new_shape)
            elif shape == "square":
                new_shape = Square(int(input("enter side")))
                self.shapes.append(new_shape)
            elif shape == "rectangle":
                new_shape = Rectangle(int(input("enter length")),int(input("enter height")))
                self.shapes.append(new_shape)
        except ValueError:
            print("must be number")
    def get_all_shapes(self):
        return self.shapes

    def update_shape(self, shape_id, new_data):
        for shape in self.shapes:
            if shape.id == shape_id:
                if isinstance(shape, Circle):
                    shape.radius = new_data["radius"]
                elif isinstance(shape, Square):
                    shape.side = new_data["side"]
                elif isinstance(shape, Rectangle):
                    shape.length = new_data[0]
                    shape.height = new_data[1]
                return
    def delete_shape(self, shape_id):
        for shape in self.shapes:
            if shape.id == shape_id:
                self.shapes.remove(shape)
    def save_to_json(self):
            with open("shapes.json", "w") as f:
                for shape in self.shapes:
                    json.dump(shape.to_dict(), f, indent=2)
    def load_from_json(self):
        try:
            with open("shapes.json", "r") as f:
                file = json.load(f)
                self.shapes = []
                for line in file:
                    if line["shape_type"] == "circle":
                        self.shapes.append(Circle(line["radius"]))
                    elif line["shape_type"] == "square":
                            self.shapes.append(Square(line["side"]))
                    elif line["shape_type"] == "rectangle":
                        self.shapes.append(Rectangle(line["length"], line["height"]))
        except FileNotFoundError:
            print("file not found")
            self.shapes = []


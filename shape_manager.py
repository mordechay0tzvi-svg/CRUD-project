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

    def get_all_shapes(self):
        self.load_from_json()
        return self.shapes.copy()

    def update_shape(self, shape_id, new_data):
        for shape in self.shapes:
            if shape.id == shape_id:
                if isinstance(shape, Circle):
                    shape.radius = new_data["radius"]
                elif isinstance(shape, Square):
                    shape.side = new_data["side"]
                elif isinstance(shape, Rectangle):
                    shape.length = new_data["length"]
                    shape.height = new_data["height"]
                return

    def delete_shape(self, shape_id):
        self.load_from_json()
        for shape in self.shapes:
            if shape.id == shape_id:
                self.shapes.remove(shape)
                break
        self.save_to_json()

    def save_to_json(self):
            with open("shapes.json", "w") as f:
                shapes = []
                for shape in self.shapes:
                    shapes.append(shape.to_dict())
                json.dump(shapes, f, indent=2)

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
            Shape.count = 0
        except FileNotFoundError:
            print("file not found")
            self.shapes = []


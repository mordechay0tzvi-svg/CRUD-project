from shape import Shape
class Rectangle(Shape):
    type = "rectangle"
    def __init__(self, shape_id, shape_type, height, length):
        super().__init__(shape_id, shape_type)
        self.shape_id = Shape.count
        Shape.count += 1
        self.shape_type = Rectangle.type
        self.height = height
        self.length = length
    def get_area(self):
        return self.length * self.height
    def get_circumference(self):
        return self.length * 2 + self.height * 2
    def to_dict(self):
        pass
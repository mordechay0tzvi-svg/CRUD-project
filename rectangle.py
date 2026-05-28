from shape import Shape
class Rectangle(Shape):
    type = "rectangle"
    def __init__(self, height, length, shape_id=None):
        self.type = Rectangle.type
        super().__init__(shape_id, Rectangle.type)
        self.height = height
        self.length = length
    def get_area(self):
        return self.length * self.height
    def get_circumference(self):
        return self.length * 2 + self.height * 2
    def to_dict(self):
        return {"shape_id":self.shape_id,
                "shape_type": Rectangle.type,
                "length":self.length,
                "height":self.height,
                }
    def __str__(self):
        return f"{self.type}-  shape id: {self.shape_id}, length: {self.length}, height: {self.height} area: {self.get_area()}, circumference: {self.get_circumference()}"


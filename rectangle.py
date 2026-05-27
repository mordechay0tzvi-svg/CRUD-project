from shape import Shape
class Rectangle(Shape):
    type = "rectangle"
    def __init__(self, height, length):
        shape_id = Shape.count
        Shape.count += 1
        super().__init__(shape_id, Rectangle.type)
        self.height = height
        self.length = length
    def get_area(self):
        return self.length * self.height
    def get_circumference(self):
        return self.length * 2 + self.height * 2
    def to_dict(self):
        return {"id":self.shape_id,
                "type": self.shape_type,
                "length":self.length,
                "height":self.height,
                "area": self.get_area(),
                "perimeter":self.get_circumference()}
    def __str__(self):
        print(f"{self.type}-{self.shape_id}, length: {self.length}, height: {self.height} area: {self.get_area()}, circumference: {self.get_circumference()}")
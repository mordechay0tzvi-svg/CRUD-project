from shape import Shape
class Circle(Shape):
    type = "circle"
    def __init__(self, radius, shape_id=None):
        self.type = Circle.type
        super().__init__(shape_id, Circle.type)
        self.radius = radius
    def get_area(self):
        return self.radius ** 2 * 3.14159
    def get_circumference(self):
        return 2 * self.radius * 3.14159
    def to_dict(self):
        return {"shape_id": self.shape_id,
                "shape_type": Circle.type,
                "radius": self.radius,
                }
    def __str__(self):
        return f"{self.type}-{self.shape_id}, radius: {self.radius} area: {self.get_area()}, circumference: {self.get_circumference()}"





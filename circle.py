from shape import Shape
class Circle(Shape):
    type = "circle"
    def __init__(self, radius):
        shape_id = Shape.count
        Shape.count += 1
        super().__init__(shape_id, Circle.type)
        self.radius = radius
    def get_area(self):
        return self.radius ** 2 * 3.147
    def get_circumference(self):
        return 2 * self.radius * 3.147
    def to_dict(self):
        return {"id": self.shape_id,
                "type": self.shape_type,
                "radius": self.radius,
                "area": self.get_area(),
                "perimeter": self.get_circumference()}


c1 = Circle(7)
print(c1.radius)
print(c1.type)
print(c1.get_area())
print(c1.get_circumference())



from shape import Shape
class Circle(Shape):
    type = "circle"
    def __init__(self, shape_id, shape_type, radius):
        super().__init__(shape_id, shape_type)
        self.shape_id = Shape.count
        Shape.count += 1
        self.shape_type = Circle.type
        self.radius = radius
    def get_area(self):
        return self.radius ** 2 * 3.147
    def get_circumference(self):
        return 2 * self.radius * 3.147
    def to_dict(self):
        pass



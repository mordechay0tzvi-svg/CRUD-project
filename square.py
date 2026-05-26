from shape import Shape
class Square(Shape):
    type = "square"
    def __init__(self,shape_id, shape_type, side):
        super().__init__(shape_id, shape_type,)
        self.shape_id = Shape.count
        Shape.count += 1
        self.shape_type = Square.type
        self.side = side
    def get_area(self):
        return self.side ** 2
    def get_circumference(self):
        return self.side * 4
    def to_dict(self):
        return {"id":self.shape_id,
                "type":self.shape_type,
                "side":self.side,
                "area":self.get_area(),
                "perimeter":self.get_circumference()}


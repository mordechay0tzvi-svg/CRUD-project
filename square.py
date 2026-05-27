from shape import Shape
class Square(Shape):
    type = "square"
    def __init__(self, side, shape_id=None):
        self.type = Square.type
        super().__init__(shape_id, Square.type)
        self.side = side
    def get_area(self):
        return self.side ** 2
    def get_circumference(self):
        return self.side * 4
    def to_dict(self):
        return {"shape_id":self.shape_id,
                "shape_type":Square.type,
                "side":self.side,
                }
    def __str__(self):
        return f"{self.type}-{self.shape_id}, side: {self.side} area: {self.get_area()}, circumference: {self.get_circumference()}"


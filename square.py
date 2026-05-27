from shape import Shape
class Square(Shape):
    type = "square"
    def __init__(self, side):
        shape_id = Shape.count
        Shape.count += 1
        super().__init__(shape_id, Square.type)
        self.side = side
    def get_area(self):
        return self.side ** 2
    def get_circumference(self):
        return self.side * 4
    def to_dict(self):
        return {"id":self.shape_id,
                "type":self.shape_type,
                "side":self.side,
                }
    def __str__(self):
        print(f"{self.type}-{self.shape_id}, side: {self.side} area: {self.get_area()}, circumference: {self.get_circumference()}")


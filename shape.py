class Shape:
    count = 1
    def __init__(self, shape_id=None, shape_type=None):
        if shape_id is None:
            self.shape_id = Shape.count
            Shape.count += 1
        else:
            self.shape_id = shape_id
    def get_area(self):
        pass
    def get_circumference(self):
        pass
    def to_dict(self):
        pass


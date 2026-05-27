class Shape:
    count = 1
    def __init__(self, shape_id, shape_type):
        self.shape_type = shape_type
        self.shape_id = shape_id
    def get_area(self):
        pass
    def get_circumference(self):
        pass
    def to_dict(self):
        pass

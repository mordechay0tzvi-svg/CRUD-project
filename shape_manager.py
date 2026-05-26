import json
class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()
    def create_shape(self, shape):
        pass
    def get_all_shapes(self):
        return self.shapes
    def update_shape(self, shape_id, new_data):
        for shape in self.shapes:
            if shape.id == shape_id:
                self.shapes.append(new_data)
    def delete_shape(self, shape_id):
        for shape in self.shapes:
            if shape.id == shape_id:
                self.shapes.remove(shape)
    def save_to_json(self):
        pass
    def load_from_json(self):
        pass

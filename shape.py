


class Shape:
    def __init__(self, shape_id, shape_type):
        self.shape_id = shape_id
        self.shape_type = shape_type
    def get_area(self):
        pass
    def get_perimeter(self):
        pass  
    def to_dict(self):
        dict_of_shape = {'id': self.shape_id,'type': self.shape_type}
        return dict_of_shape
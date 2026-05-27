import circle,rectangle,square


class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()
    def create_shape(self, shape):  
        """add a the shape to json file
        taken : none
        return : None
        """
        self.shapes.append(shape)
        self.load_from_json()
        #log
        return None
    def get_all_shapes(self):
        pass
    def update_shape(self, shape_id, new_data):
        pass
    def delete_shape(self, shape_id):
        pass
    def save_to_json(self):
        pass
    def load_from_json(self):
        pass
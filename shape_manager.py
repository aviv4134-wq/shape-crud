import circle,rectangle,square


class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()
    def create_shape(self, shape:object):  
        """add a the shape to json file
        taken : none
        return : None
        """
        self.shapes.append(shape)
        self.save_to_json()
        return None
    def get_all_shapes(self):
        for shape in self.shapes:
            print(f'{shape}\n')

    def update_shape(self, shape_id, new_data):
        pass
    def delete_shape(self, shape_id):
        pass
    def save_to_json(self):
        pass
    def load_from_json(self):
        pass


if __name__ == '__main__':
    manager = ShapeManager()
    manager.create_shape(circle.c)
    manager.create_shape(circle.t)
    manager.get_all_shapes()
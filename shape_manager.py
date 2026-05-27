import circle,rectangle,square,json
from logger_file import logger

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
        data = ShapeManager().load_from_json()
        for shape in data:
            if shape['id'] == shape_id:
               if not shape.get('radius'):
                   shape['side'] = new_data
                   ShapeManager().save_to_json()
                   return None               
               else:
                   shape['radius'] = new_data
                   ShapeManager().save_to_json()
                   return None
            


            
    def delete_shape(self, shape_id):
        pass
    def save_to_json(self):
        pass
    def load_from_json(self):
        with open('shapes.json','r') as f:
           data = json.load(f)
           return(data)


if __name__ == '__main__':
    manager = ShapeManager()
    manager.create_shape(circle.c)
    manager.create_shape(circle.t)
    #manager.get_all_shapes()
    print(manager.load_from_json())
    manager.update_shape(1,1)
    print(manager.load_from_json())

    #with open('shapes.json','r') as f:
     #   q=json.load(f)
      #  print(q)
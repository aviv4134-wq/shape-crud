import circle,rectangle,square,json
from logger_file import logger

class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()
    def is_id_exists(self,shape_id:int) ->bool:
        logger.info('start checking if id exists in shapes')
        for shape in self.shapes:
            if shape.shape_id  == shape_id: 
                logger.error('the id of the shape already exists')
                return True
        return False
                    
    def create_shape(self, shape:object):  
        """add a the shape check if the id exists to json file 
        taken : none
        return : None
        """
        shape_id = shape.shape_id
        if self.is_id_exists(shape_id):
           raise ValueError('error the id already exists')
        self.shapes.append(shape)
        self.save_to_json()
        return None
    def get_all_shapes(self):
        for shape in self.shapes:
            print(f'{shape}\n')

    def update_shape(self, shape_id, new_data):
        if not self.is_id_exists(shape_id):
            raise ValueError('error the id not exists')
        for shape in self.shapes:
            #shape = shape.to_dict()
            if shape.shape_id == shape_id:
                if isinstance(shape,circle.Circle):
                    shape.radius = new_data
                if isinstance(shape,(rectangle.Rectangle,square.Square)):
                    shape.side = new_data
                self.save_to_json()
                return None      
    def delete_shape(self, shape_id):
        for shape in self.shapes:
            shape_dict:dict = shape.to_dict()
            if shape_dict['id'] == shape_id:
                self.shapes.remove(shape)
                self.save_to_json()
                return None
    def save_to_json(self) ->None:
        try:
            data = self.load_from_json()
            for shape in self.shapes:
                shape = shape.to_dict()
                data.append(shape)
            with open('shapes.json', 'w', encoding='utf-8') as f:
                    json.dump(data,f)
                    return None        
        except Exception as e:
                print(f"{e}")
                return None
    def load_from_json(self):
        with open('shapes.json','r', encoding='utf-8') as f:
           data = json.load(f)
           return(data)
           

if __name__ == '__main__':
    manager = ShapeManager()
    manager.create_shape(circle.c)
    #manager.create_shape(circle.t)
    manager.get_all_shapes()
    #print(manager.save_to_json())
    manager.update_shape(6,90)
    #print(manager.load_from_json())
    #print(manager.delete_shape(6))
    manager.get_all_shapes()
    #with open('shapes.json','r') as f:
     #   q=json.load(f)
      #  print(q)
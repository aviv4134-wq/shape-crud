import circle,rectangle,square,json
from logger_file import logger
from shape import Shape

class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()
    def is_id_exists(self,shape_id:int) ->bool:
        """taken shape_id and check if id already exists in list of shapes return bool
        True  = exists
        False = not exists"""
        logger.info('start checking if id exists in shapes')
        for shape in self.shapes:
            if shape.shape_id  == shape_id: 
                logger.info('the id exists')
                return True
        logger.info('the id not exists')
        return False
                    
    def create_shape(self, shape:object):  
        """add a the shape to list of shape and saves in json file
        taken : none
        return : None
        """

        shape_id = shape.shape_id
        if self.is_id_exists(shape_id):
           logger.error('the id of the shape already exists')
           raise ValueError('error the id already exists')
        self.shapes.append(shape)
        logger.info('saved shape in the list ')
        self.save_to_json()
        return None
    def get_all_shapes(self):
        """print all shape in the list in order and clean way
        return None"""
        logger.info('start printing data')
        for shape in self.shapes:
            print(f'{shape}\n')
        logger.info('success all data printed ')
        return None
    def update_shape(self, shape_id, new_data):
        shape_id,new_data = Shape.validate_input_object(shape_id,new_data)
        if not self.is_id_exists(shape_id):
            logger.error('the id not exists in the system ')
            raise ValueError('error the id not exists')
        logger.info('start updating data...')
        for shape in self.shapes:
            if shape.shape_id == shape_id:
                if isinstance(shape,circle.Circle):
                    shape.radius = new_data
                if isinstance(shape,(rectangle.Rectangle,square.Square)):
                    shape.side = new_data
        self.save_to_json()
        logger.info('success the shape updated')
        return None      
    def delete_shape(self, shape_id):
        """deleting shape from list and save it in json file
        taken : shape id
        return : None"""
        
        shape_id,additional = Shape.validate_input_object(shape_id,shape_id)
        if not self.is_id_exists(shape_id):
            logger.error('the id not exists in the system ')
            raise ValueError('error the id not exists')
        logger.info('start deleting process')
        for shape in self.shapes:
            shape_dict:dict = shape.to_dict()
            if shape_dict['id'] == shape_id:
                self.shapes.remove(shape)
                self.save_to_json()
                logger.info('success shape deleted')
                return None
    def save_to_json(self) ->None:
        """load data and save new dat ain json file
        taken : None
        return : None"""
        logger.info('start save process')
        try:
            data = self.load_from_json()
            for shape in self.shapes:
                shape = shape.to_dict()
                data.append(shape)
            with open('shapes.json', 'w', encoding='utf-8') as f:
                    json.dump(data,f)
            logger.info('success save to file')
            return None        
        except Exception as e:
                print(f"{e}")
                return None
    def load_from_json(self):
        """load data from json  and return the data 
        taken : None
        return : data """
        logger.info('loading data')
        with open('shapes.json','r', encoding='utf-8') as f:
           data = json.load(f)
           logger.info('success data loaded')
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
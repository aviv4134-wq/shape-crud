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
            if shape.shape_id == shape_id:
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
        logger.info('success all data printed ')
        shapes = []
        for shape in  self.shapes:
            #shape = shape.to_dict()
            shapes.append(shape)
        return shapes
    def update_shape(self, shape_id, new_data):
        """taken shape id and data and update the shape"""
        shape_id,new_data = Shape.validate_input_object(shape_id,new_data)
        if not self.is_id_exists(shape_id):
            logger.error('the id not exists in the system ')
            raise ValueError('error the id not exists')
        logger.info('start updating data...')
        for shape in self.shapes:
            if shape.shape_id == shape_id:
                if isinstance(shape,circle.Circle):
                    shape.radius = new_data
                if isinstance(shape,(rectangle.Rectangle)):
                    shape.side_length = new_data
                    shape.side_width = new_data
                if isinstance(shape,square.Square):
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
            if shape.shape_id == shape_id:
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
            data = []
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
        """load data from json  and load the list of shapes objects 
        taken : None
        return : None"""
        logger.info('loading data')
        with open('shapes.json','r', encoding='utf-8') as f:
           data = json.load(f)
           for shape in data:
               if shape['type'] == 'circle':
                   shape = circle.Circle(shape['id'],shape['type'],shape['radius']) 
               elif shape['type'] == 'square':
                   shape = square.Square(shape['id'],shape['type'],shape['side'])
               elif shape['type'] == 'rectangle':
                   shape = rectangle.Rectangle(shape['id'],shape['type'],shape['side length'],shape['side width'])
               self.shapes.append(shape)           
           logger.info('success data loaded')
           return None
           


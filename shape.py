from logger_file import logger


class Shape:
    def __init__(self, shape_id, shape_type):
        self.shape_id = shape_id
        self.shape_type = shape_type
    @staticmethod
    def validate_input_object(shape_id,additional):
        """taken shape id and additional parameter and check validation
        raise error if validation failed in conditions
        return none    """
        logger.info('start input object validation process')
        try:
            shape_id = int(shape_id)
            additional = int(additional)
            if shape_id <= 0 or shape_id > 100 :
                logger.error(f'the id is {shape_id} only 0 - 100 numbers ids allowed')
                raise TypeError('this id number not allowed (only 1 - 100 ids)') 
            if additional <= 0 or additional > 50 :
                logger.error(f'the additional parameter is {additional} only 1 - 50 allowed ')
                raise TypeError('this id number not allowed (only 1 - 100 radius)')     
        except ValueError :
             logger.error('user enter letters only numbers allowed ')
             raise ValueError("you enter letters only numbers allowed!!! ")
        else:     
            logger.info('validation completed success')
            return shape_id,additional
    def get_area(self):
        pass
    def get_perimeter(self):
        pass  
    def to_dict(self):
        """add side parameter to dict of a shape
         taken : none
         return : dict """
        dict_of_shape = {'id': self.shape_id,'type': self.shape_type}
        return dict_of_shape
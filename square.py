import shape
from logger_file import logger


class Square(shape.Shape):
    def __init__(self, shape_id, shape_type,side):
        cleaned_id,cleaned_side = self.validate_input_object(shape_id,side) 
        super().__init__(cleaned_id, shape_type)
        self.side = cleaned_side
        logger.info('success to create object ')  
    def get_area(self):
        """calculate square area
         taken : none
         return : square area  """
        square_area = self.side ** 2
        return square_area
    def get_perimeter(self):
        """calculate square perimeter
        taken : none
        return : square perimeter"""
        square_perimeter = self.side * 4
        return square_perimeter 
    def to_dict(self):
        """add side parameter to dict of a shape
         taken : none
         return : dict """
        data = super().to_dict()
        data['side'] = self.side
        return data
    def __str__(self) -> str:
        """show the object parameters"""
        
        perimeter = self.get_perimeter()
        area = self.get_area()
        return f'id:{self.shape_id}\ntype:{self.shape_type}\nside:{self.side}\narea:{area}\nperimeter:{perimeter}' 

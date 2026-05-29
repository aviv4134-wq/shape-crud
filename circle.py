import shape 
from logger_file import logger
class Circle(shape.Shape):
    PI = 3.14
    
    def __init__(self, shape_id, shape_type,radius):
        cleaned_id,cleaned_radius = self.validate_input_object(shape_id,radius) 
        super().__init__(cleaned_id, shape_type)
        self.radius = cleaned_radius
        logger.info('success to create object ')  
    
    def get_area(self):
        """calculate circle area
         taken : none
         return : circle area  """
        return Circle.PI * self.radius **2
    
    def get_perimeter(self):
        """calculate circle perimeter
        taken : none
        return : circle perimeter"""
        return Circle.PI * self.radius * 2
    
    def to_dict(self):
        """add side parameter to dict of a shape
         taken : none
         return : dict """
        data = super().to_dict()
        data['radius'] = self.radius
        return data
    

    def __str__(self) -> str:
        """show the object parameters"""
        perimeter = self.get_perimeter()
        area = self.get_area()
        return f'id:{self.shape_id}\ntype:{self.shape_type}\nradius:{self.radius}\narea:{area}\nperimeter:{perimeter}' 


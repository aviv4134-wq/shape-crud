import shape


class Rectangle(shape.Shape):
    
    def __init__(self, shape_id, shape_type,side):
        super().__init__(shape_id, shape_type)
        self.side = side    
    def get_area(self):
        """calculate rectangle area
         taken : none
         return : rectangle area  """
        rectangle_area = self.side ** 2
        return rectangle_area
    def get_perimeter(self):
        """calculate rectangle perimeter
        taken : none
        return : rectangle perimeter"""
        rectangle_perimeter = self.side * 4
        return rectangle_perimeter 
    def to_dict(self):
        pass

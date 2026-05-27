import shape

class Square(shape.Shape):
    def __init__(self, shape_id, shape_type,side):
        super().__init__(shape_id,shape_type)
        self.side = side
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
    
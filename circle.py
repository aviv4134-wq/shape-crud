import shape

class Circle(shape.Shape):
    PI = 3.14
    
    def __init__(self, shape_id, shape_type,radius):
        super().__init__(shape_id, shape_type)
        self.radius = radius
    
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
    
    #def __str__(self) -> str:
        Circle.get_perimeter(self)
        return self.shape_id,self.shape_type,self.radius 

c = Circle(6,'circle',5)
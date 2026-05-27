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
    

    def __str__(self) -> str:
        perimeter = Circle.get_perimeter(self)
        area = Circle.get_area(self)
        return f'id:{self.shape_id}\ntype:{self.shape_type}\nradius:{self.radius}\nperimeter:{perimeter}\narea:{area}' 

c = Circle(6,'circle',5)

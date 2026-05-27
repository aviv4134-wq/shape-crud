import shape

class Circle(shape.Shape):
    PI = 3.14
    
    def __init__(self, shape_id, shape_type,radius):
        super().__init__(shape_id, shape_type)
        self.radius = radius
    
    def get_area(self):
        return Circle.PI * self.radius **2
    
    def get_perimeter(self):
        return Circle.PI * self.radius * 2
    
    def to_dict(self):
        data = super().to_dict()
        data['radius'] = self.radius
        return data  